from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

db_file = 'sqlite:///C:\\Users\\Edijs\\Desktop\\Mokymai\\RenkuosiProgramuoti\\Python 13\\sqlite.db'

engine = create_engine(db_file)
Base = declarative_base()

class Cat(Base):
    __tablename__ = 'cat'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


Base.metadata.create_all(engine)
