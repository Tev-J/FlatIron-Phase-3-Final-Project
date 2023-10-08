#!/usr/bin/env python3

from models import (
    Session,
    User,
    Flashcard,
    Category,
    flashcard_categories,
    Base,
    engine,
    Quiz,
    QuizAttempt,
    QuizResponse,
    quiz_flashcard,
)
from sqlalchemy import func
from faker import Faker
from more_data import questions_and_answers
import random


fake = Faker()

# Clearing existing data
with Session() as session:
    session.query(User).delete()
    session.query(Flashcard).delete()
    session.query(Category).delete()
    session.query(flashcard_categories).delete()
    session.query(Quiz).delete()
    session.query(QuizAttempt).delete()
    session.query(QuizResponse).delete()
    session.query(quiz_flashcard).delete()
    session.commit()

# Seeding the data
with Session() as session:
    # generating user data
    users = [
        User(username=fake.user_name(), password=fake.uuid4()),
        User(username=fake.user_name(), password=fake.uuid4()),
        User(username=fake.user_name(), password=fake.uuid4()),
        User(username=fake.user_name(), password=fake.uuid4()),
    ]
    session.bulk_save_objects(users)
    users = session.query(User).all()
    print(f"Created all users. {users}\n")

    # testing user-flashcard relationship
    for user in users:
        flashcard_count = random.randint(1, len(questions_and_answers))
        flashcard_library = random.sample(questions_and_answers, flashcard_count)
        print(f"\nThese are the cards for {user.username}:")

        for card in flashcard_library:
            print(f"Card Topic: {card['topic']}")
            card_category = (
                session.query(Category).filter_by(name=card["topic"]).first()
            )
            if card_category is None:
                card_category = Category(name=card["topic"])
                session.add(card_category)
                session.flush()
                print(f"New Category: {card_category.name}")
            else:
                print(f"Existing category ID: {card_category.id}")

            print(f"Creating flashcard for {user.username}\n")
            new_flashcard = Flashcard(
                question=card["question"], answer=card["answer"], user_id=user.id
            )

            new_flashcard.categories.append(card_category)
            user.flashcards.append(new_flashcard)
            session.add(new_flashcard)

        # testing quizzes
        user_flashcards = session.query(Flashcard).filter_by(user_id=user.id).all()

        for _ in range(3):
            quiz_name = fake.company()
            flashcard_samples = random.sample(user_flashcards, 3)

            new_quiz = Quiz(title=quiz_name, user_id=user.id)
            for card in flashcard_samples:
                new_quiz.flashcards.append(card)

            user.quizzes.append(new_quiz)

        # testing quiz attempt
        for quiz in user.quizzes:
            quiz_attempt = QuizAttempt(user_id=user.id, quiz_id=quiz.id)
            session.add(quiz_attempt)

            for card in quiz.flashcards:
                available_answers = [
                    f.answer
                    for f in session.query(Flashcard)
                    .order_by(func.random())
                    .limit(4)
                    .all()
                ]
                selected_answer = random.choice(available_answers)
                user_response = QuizResponse(
                    flashcard_id=card.id,
                    selected_answer=selected_answer,
                    is_correct=(selected_answer == card.answer),
                    quiz_attempt=quiz_attempt,
                )
                session.add(user_response)

            quiz_attempt.calculate_score()

    session.commit()
