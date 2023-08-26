import pymysql
import dotenv
import os


TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
)

with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # Esse comando limpa a tabela inteira
    connection.commit()

    with connection.cursor() as cursor:
        results = cursor.execute(
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUE ("Luiz", 25) '
        )
        print(f'Resultados = {results}')
    connection.commit()
