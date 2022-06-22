from ddl import Cat, db_file
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(db_file)
session = sessionmaker(bind=engine)

john = Cat('John', 12)
mike = Cat('Mike', 34)

# Create (insert rows)
with session.begin() as _session:
    _session.add(john)
    _session.add(mike)

# Retrieve (select)
with session.begin() as _session:
    print('Query 1:', _session.query(Cat).statement)
    data = [row.name for row in _session.query(Cat).all()]
    print(data)
    #for user in _session.query(Cat).filter_by(name='Mike'):
    #    print(user)
    print('Query 2:', _session.query(Cat.id, Cat.age).statement)
    data0 = [row.age for row in _session.query(Cat.id, Cat.age).all()]
    print(data0)
    print('Query 3:', _session.query(Cat.name).filter_by(id=4).statement)

# Update
with session.begin() as _session:
    for kitty in _session.query(Cat).all():
        kitty.age = kitty.age + 1
    _session.commit()

# Delete
with session.begin() as _session:
    for kitty in _session.query(Cat).all():
        _session.delete(kitty)
