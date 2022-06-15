import sqlite3
import random

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()
cursor.execute('''create table IF NOT EXISTS cat(
  id integer primary key AUTOINCREMENT,
  name text,
  age integer
);''')

# for i in range(10):
#     random_age = random.randint(1, 60)
#     cursor.execute(f"""insert into cat(name, age) values('Cat{i}', {random_age})""")
#     connection.commit()

for row in cursor.execute('select * from cat;'):
    # print(row)
    print(row[1])
