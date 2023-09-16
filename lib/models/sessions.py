from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///lib/db/data.db")
Session = sessionmaker(bind=engine)


