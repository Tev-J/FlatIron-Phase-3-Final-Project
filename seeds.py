from .session import Session
from faker import Faker
fake = Faker()
from .user import User

session = Session()

users = [
    User(username=fake.user_name(), email=fake.ascii_safe_email(), password=fake.uuid4()),
    User(username=fake.user_name(), email=fake.ascii_safe_email(), password=fake.uuid4()),
    User(username=fake.user_name(), email=fake.ascii_safe_email(), password=fake.uuid4()),
    User(username=fake.user_name(), email=fake.ascii_safe_email(), password=fake.uuid4()),
    
]
session.bulk_save_objects(users)