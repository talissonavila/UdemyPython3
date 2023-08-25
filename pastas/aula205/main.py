import sqlite3

from pathlib import Path


ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL itself
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

sql_command = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES (:name, :weight)'
)
# cursor.executemany(
#     sql_command,
#     (
#         ('Luiz', 4), ('Otavio', 4)
#     )
# )

# cursor.execute(sql_command, {'name': 'Pedro', 'weight': 50.84})

# cursor.executemany(
#     sql_command,
#     (
#         {'name': 'Naruto', 'weight': 20},
#         {'name': 'Sasuke', 'weight': 21},
#         {'name': 'Sakura', 'weight': 15.15},
#     )
# )


if __name__ == '__main__':
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} where weight > "82"'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
