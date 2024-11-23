import sqlite3

connection = sqlite3.connect('module_14_4.db')


def initiate_db():
    with connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Products(id INTEGER PRIMARY KEY,'
                       'title TEXT NOT NULL,'
                       'description TEXT,'
                       'price INTEGER NOT NULL,'
                       'pics BLOB)')

        #cursor.execute('DELETE FROM Products')  # удалим старые записи
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(*) FROM Products')
        if cursor.fetchone()[0] == 0:
            # заполним таблицу
            for i in range(1, 5):
                try:
                    with open(f'pic{i}.png', 'rb') as pic:
                        cursor.execute('INSERT INTO Products(title, description, price, pics) VALUES(?,?,?,?)',
                                       (f'Продукт{i}', f'Описание{i}', i * 100, pic.read()))
                except Exception as err:
                    print(err)
        connection.commit()


def get_all_products():
    result = []
    with connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Products')

        result = cursor.fetchall()

    return result


if __name__ == '__main__':
    initiate_db()
    for i in get_all_products():
        print(i[4])