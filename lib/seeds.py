#!/usr/bin/env python3

from models import Session, User, Flashcard, Base, engine
from faker import Faker
import ipdb

fake = Faker()

# with engine.connect() as conn:
#     conn.execute("DROP TABLE flashcard")

session = Session()


session.query(User).delete()
session.query(Flashcard).delete()


# if engine.dialect.has_table(engine, "flashcard"):
#     session.query(Flashcard).delete()


users = [
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
]
session.bulk_save_objects(users)
# print(users)

from more_data import questions_and_answers


flashcards = []
for item in questions_and_answers:
    flashcard_inst = Flashcard(question=item["question"], answer=item["answer"])
    flashcards.append(flashcard_inst)

# print(flashcards)

# ipdb.set_trace()
session.bulk_save_objects(flashcards)


# ipdb.set_trace()

session.commit()
session.close()
