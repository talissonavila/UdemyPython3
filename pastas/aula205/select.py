import sqlite3

from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# cursor.execute(
#     f'SELECT * FROM {TABLE_NAME} LIMIT 5'
# )

cursor.execute(
     f'SELECT * FROM {TABLE_NAME} WHERE id = "6"'
)
row_ = cursor.fetchone()
print(f'Id 6 is {row_}')


# for row in cursor.fetchall():
#     _id, name, weight = row
#     print(_id, name, weight)

cursor.close()
connection.close()
