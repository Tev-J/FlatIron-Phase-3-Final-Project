#!/usr/bin/env python3

from models import Session, User, Flashcard, Category, Base, engine
from faker import Faker
from more_data import questions_and_answers, networking_fundamentals_topics
import ipdb, random


fake = Faker()

# with engine.connect() as conn:
#     conn.execute("DROP TABLE flashcard")
session = Session()
# session.rollback()
# session.close()

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)


session.query(User).delete()
session.query(Flashcard).delete()
# # Reset primary key sequence for the users and flashcards tables
# session.execute('DELETE FROM sqlite_sequence WHERE name="user"')
# session.execute('DELETE FROM sqlite_sequence WHERE name="flashcard"')


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
users = session.query(User).all()
# generating user data
# generating user data


...

# testin flashcards
# flashcards = []
# for item in questions_and_answers:
#     flashcard_inst = Flashcard(question=item["question"], answer=item["answer"])
#     flashcards.append(flashcard_inst)


# session.bulk_save_objects(flashcards)

# testing user-flashcard relationship
for user in users:
    print(user.username)
    flashcard_count = random.randint(1, len(questions_and_answers))
    flashcard_library = random.sample(questions_and_answers, flashcard_count)
    # print(f"\nThese are the cards for {user.username}:")
    for card in flashcard_library:
        ipdb.set_trace()
        new_flashcard = Flashcard(question=card["question"], answer=card["answer"])
        user.flashcards.append(new_flashcard)

        # new_category = Category()

        session.add(new_flashcard)


categories = []
for topic in networking_fundamentals_topics:
    category_inst = Category(name=topic)
    categories.append(category_inst)

session.bulk_save_objects(categories)


session.commit()
session.close()
