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
    UserResponse,
    quiz_flashcard,
)
from sqlalchemy import func
from faker import Faker
from more_data import questions_and_answers
import ipdb, random


fake = Faker()
session = Session()


session.query(User).delete()
session.query(Flashcard).delete()
session.query(Category).delete()
session.query(flashcard_categories).delete()
session.query(Quiz).delete()
session.query(QuizAttempt).delete()
session.query(UserResponse).delete()
session.query(quiz_flashcard).delete()
# generating user data
users = [
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
]
session.bulk_save_objects(users)
# session.commit()
users = session.query(User).all()
print(f"Created all users. {users}\n")

# testing user-flashcard relationship
for user in users:
    flashcard_count = random.randint(1, len(questions_and_answers))
    flashcard_library = random.sample(questions_and_answers, flashcard_count)
    print(f"\nThese are the cards for {user.username}:")

    for card in flashcard_library:
        print(f"Card Topic: {card['topic']}")
        card_category = session.query(Category).filter_by(name=card["topic"]).first()
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

        # ipdb.set_trace()
        session.add(new_flashcard)

    # testing quizzes
    user_flashcards = session.query(Flashcard).filter_by(user_id=user.id).all()
    quizzes_all = session.query(Quiz).all()

    for _ in range(3):
        quiz_name = fake.company()
        flashcard_library = random.sample(user_flashcards, 3)

        newQuiz = Quiz(title=quiz_name, user_id=user.id)
        for card in flashcard_library:
            newQuiz.flashcards.append(card)

        user.quizzes.append(newQuiz)

    # testing quiz attenpt
    user_quizzes = session.query(Quiz).filter_by(user_id=user.id).all()
    test_quiz = random.sample(user_quizzes, 1)

    for qZ in test_quiz:
        score = 0
        quiz_attempt = QuizAttempt(user_id=user.id, quiz_id=qZ.id)
        # ipdb.set_trace()

        for card in qZ.flashcards:
            available_answers = [
                f.answer
                for f in session.query(Flashcard).order_by(func.random()).limit(4).all()
            ]

            selected_answer = random.choice(available_answers)

            if selected_answer == card.answer:
                score += 1

            user_response = UserResponse(
                flashcard_id=card.id,
                selected_answer=selected_answer,
                is_correct=selected_answer == card.answer,
                quiz_attempt=quiz_attempt,
            )
        session.add(user_response)
    session.add(quiz_attempt)
# quiz_attempt = QuizAttempt(user_id=users[0].id, quiz_id=quiz.id)

# for flashcard in quiz.flashcards:
#     available_answers = [
#         f.answer
#         for f in session.query(Flashcard).order_by(func.random()).limit(4).all()
#     ]
#     if flashcard.answer not in available_answers:
#         available_answers.pop()
#         available_answers.append(flashcard.answer)
#     selected_answer = random.choice(available_answers)

#     user_response = UserResponse(
#         flashcard_id=flashcard.id,
#         selected_answer=selected_answer,
#         is_correct=selected_answer == flashcard.answer,
#         quiz_attempt=quiz_attempt,
#     )
#     session.add(user_response)

# session.add(quiz_attempt)
session.commit()
session.close()
