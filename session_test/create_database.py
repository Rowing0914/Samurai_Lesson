import sqlite3
from contextlib import closing

dbname = 'db1.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    # executeメソッドでSQL文を実行する
    create_table = '''create table users (id int, name varchar(64),
                      age int, gender varchar(32))'''
    c.execute(create_table)

    create_table = '''create table user_master (username varchar(64), password varchar(64))'''
    c.execute(create_table)

    insert_sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
    users = [
        (2, 'Shota', 54, 'male'),
        (3, 'Nana', 40, 'female'),
        (4, 'Tooru', 78, 'male'),
        (5, 'Saki', 31, 'female')
    ]
    c.executemany(insert_sql, users)
    conn.commit()

    insert_sql = 'insert into user_master (username, password) values (?,?)'
    users = [
        ('Shota','aaa'),
        ('john','bbb'),
    ]
    c.executemany(insert_sql, users)
    conn.commit()

    select_sql = 'select * from users'
    for row in c.execute(select_sql):
        print(row)

    select_sql = 'select * from user_master'
    for row in c.execute(select_sql):
        print(row)