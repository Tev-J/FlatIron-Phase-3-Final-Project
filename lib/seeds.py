#!/usr/bin/env python3

from models import Session, User, Flashcard, Category, Base, engine, Quiz
from faker import Faker
from more_data import questions_and_answers, networking_fundamentals_topics
import ipdb

fake = Faker()

# with engine.connect() as conn:
#     conn.execute("DROP TABLE flashcard")

session = Session()


session.query(User).delete()
session.query(Flashcard).delete()


# if engine.dialect.has_table(engine, "flashcard"):
#     session.query(Flashcard).delete()

# generating user data
users = [
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
]
session.bulk_save_objects(users)


# testin flashcards
flashcards = []
for item in questions_and_answers:
    flashcard_inst = Flashcard(question=item["question"], answer=item["answer"])
    flashcards.append(flashcard_inst)


session.bulk_save_objects(flashcards)


# testing categories
categories = []
for topic in networking_fundamentals_topics:
    category_inst = Category(name=topic)
    categories.append(category_inst)

session.bulk_save_objects(categories)

# testing quiz
quiz = [
    Quiz(title=fake.job()),
    Quiz(title=fake.job()),
    Quiz(title=fake.job()),
    Quiz(title=fake.job()),
    Quiz(title=fake.job()),
]
# ipdb.set_trace()
session.bulk_save_objects(quiz)

session.commit()
session.close()
