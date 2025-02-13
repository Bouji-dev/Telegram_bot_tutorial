import sqlite3

connection = sqlite3.Connection('user.db')
cursor = connection.cursor()

create_tabel_query = """
    CREATE TABLE IF NOT EXISTS users(
        id integer primary key,
        first_name text,
        last_name text,
        phone_number text
    );
"""
cursor.execute(create_tabel_query)
connection.commit()
connection.close()


sample_data_query = """
    INSERT INTO users (id, first_name, last_name, phone_number)
    VALUES (?, ?, ?, ?)
"""
sample_data = [(3432, 'Behnam', 'Sh', '09120000000'),
            (12344235, 'Angela', 'Sh', '09120000000'),
            (223, 'Bouji', 'Sh', '0912300000007')]

with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    cursor.executemany(sample_data_query, sample_data)


fetch_data_query = """
    SELECT id, first_name, last_name, phone_number FROM users
"""
rows = []
with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    cursor.execute(fetch_data_query)
    rows = cursor.fetchall()


########################################################