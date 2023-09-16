#!/usr/bin/env python3

from ..models import Session, User
from faker import Faker

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
import ipdb

ipdb.set_trace()
