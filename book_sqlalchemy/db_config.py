# For configuration and class code
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Base class for the table
Base = declarative_base()

# Create the class Book and extend it from the base class
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    title = Column(String(45), nullable=False)
    author = Column(String(45), nullable=False)
    genres = Column(String(45))

    def __repr__(self):
        return "<Book(title='{0}', author='{1}', genres='{2}')>".format(
            self.title, self.author, self.genres)

# Configure engine for the database (dialect and driver)
engine = create_engine('mysql+pymysql://mauri:280490mg@localhost:3306/flask_test', echo=True)
Base.metadata.create_all(engine)

# Create a session for the database
Session = sessionmaker(bind=engine)
session = Session()