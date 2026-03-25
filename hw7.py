import sqlite3

conn = sqlite3.connect('store.db')
cursor =conn.cursor()


cursor.execute(

    '''CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        name TEXT,
        price INTEGER,
        quantity INTEGER )
        ''')
conn.commit()

def create_products(name,price,quantity):
   cursor.execute(
        '''INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)''',
        (name, price, quantity)
    )

conn.commit()
print('Product added')


def read_products():
    cursor.execute('SELECT * FROM products')
    products =cursor.fetchall()

    for product in products:
        print(product)

def update_products(id,price):
    cursor.execute('''
    UPDATE  products SET price = ? WHERE id =?
''',
(price,id)
)
conn.commit()

def delete_product(id):
    cursor.execute('''
    DELETE FROM products WHERE id = ?
''', (id,)
)
conn.commit()

create_products("cola", 55, 100)
read_products()



