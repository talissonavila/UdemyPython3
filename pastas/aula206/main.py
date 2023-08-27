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
    cursorclass=pymysql.cursors.DictCursor,
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

    # Execute with tuple
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ("Luiz", 20)
        result = cursor.execute(sql, data)

        print(f'Comando sql = {sql}. Data = {data}')
        print(f'Resultados = {result}')
    connection.commit()

    # Execute command with dict
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = {
            "age": 27,
            "name": "Otavio",
        }
        result = cursor.execute(sql, data2)

        print(f'\nComando sql = {sql}. Data = {data2}')
        print(f'Resultados = {result}')
    connection.commit()

    # Execute many with tuple of dicts
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"age": 40, "name": "Beatrice", },
            {"age": 3, "name": "Maria", },
            {"name": "Paul", "age": 34, },
            {"age": 9, "name": "Nina", },
        )
        result = cursor.executemany(sql, data3)

        print(f'\nComando sql = {sql}. Data = {data3}')
        print(f'Resultados = {result}')
    connection.commit()

    # Execute many with tuple of tuples
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 10),
            ("Cortana", 6),
        )
        result = cursor.executemany(sql, data4)

        print(f'\nComando sql = {sql}. Data = {data4}')
        print(f'Resultados = {result}')
    connection.commit()

    # Read with select command
    with connection.cursor() as cursor:
        # input_lower_id = input(f'Digit the lower id: ')
        # input_bigger_id = input(f'Digit the bigger id: ')

        input_lower_id = 2
        input_bigger_id = 3
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (input_lower_id, input_bigger_id))

        print(f'\nComando sql  = {cursor.mogrify(sql, (input_lower_id, input_bigger_id))}')
        select_all = cursor.fetchall()
        print(f'Resultado = {select_all}\n')

        for row_ in select_all:
            print(f'Linha = {row_}')
        print()

    # Delete sql command
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = 5'
        )
        cursor.execute(sql)
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        for row_ in cursor.fetchall():
            print(row_)
        print()

    # Update sql command
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id = %s'
        )
        cursor.execute(sql, ("Magela", 89, 7))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        for row_ in cursor.fetchall():
            print(row_['nome'])
    connection.commit()
