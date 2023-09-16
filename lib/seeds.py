#!/usr/bin/env python3

from models import Session, User, Flashcard
from faker import Faker
import ipdb

fake = Faker()


session = Session()

users = [
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
    User(username=fake.user_name(), password=fake.uuid4()),
]
session.bulk_save_objects(users)
print(users)

from more_data import questions_and_answers


flashcards = []
for item in questions_and_answers:
    flashcard = Flashcard(question=item["question"], answer=item["answer"])
    flashcards.append(flashcard)

print(flashcards)


ipdb.set_trace()
