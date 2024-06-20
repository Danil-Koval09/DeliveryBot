import sqlite3


def create_users_tables():
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    telegram_id BIGINT NOT NULL UNIQUE,
    phone TEXT
    );
    ''')

# create_users_tables()

def create_cart_table():
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carts(
    cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(user_id),
    total_price DECIMAL(12,2) DEFAULT 0,
    total_products INTEGER DEFAULT 0
    );
    ''')

# create_cart_table()

def create_cart_products_table():
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cart_products(
    cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(50) NOT NULL,
    quantity INTEGER NOT NULL,
    final_price DECIMAL(12,2) NOT NULL,
    cart_id INTEGER REFERENCES carts(card_id),
    UNIQUE(product_name,cart_id)
    );
    ''')

# create_cart_products_table()

def create_categories_table():
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name VARCHAR(30) NOT NULL UNIQUE
    );
    ''')

# create_categories_table()

def insert_categories():
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO categories(category_name) VALUES
    ('Лаваш'),
    ('Донары'),
    ('Бургеры'),
    ('Хот-доги'),
    ('Напитки'),
    ('Соусы')
    ''')
    database.commit()
    database.close()

# insert_categories()

def create_products_table():
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(30) NOT NULL UNIQUE,
    price DECIMAL(12,2) NOT NULL,
    description VARCHAR(200),
    image TEXT,
    category_id INTEGER NOT NULL,
    
    FOREIGN KEY(category_id) REFERENCES categories(category_id)
    );
    ''')

# create_products_table()

def insert_products_table():
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO products(category_id, product_name, price, description, image) VALUES
    (1, 'Лаваш говяжий', 28000, 'Мясо , огурчики, чипсы, помидоры, соус' , 'media/lavash/lavash_1.jpg'),
    (1, 'Лаваш куриный', 26000, 'Мясо куриное , огурчики, чипсы, помидоры, соус' , 'media/lavash/lavash_2.jpg'),
    (1, 'Лаваш говяжий с сыром', 30000, 'Мясо , огурчики, чипсы, помидоры , сыр, соус' , 'media/lavash/lavash_3.jpg'),
    (2, 'Донер классический в лаваше', 25000, 'Мясо , лаваш, огурцы, помидоры , салат, соус' , 'media/kebab/kebab_1.jpg'),
    (2, 'Донер халапеньо в лаваше', 27000, 'Мясо , лаваш, огурцы, помидоры , салат, халапеньо, соус' , 'media/kebab/kebab_2.jpg'),
    (2, 'Донер вегетарианский в лаваше', 20000, 'Лаваш, огурцы, помидоры , салат, соус' , 'media/kebab/kebab_3.jpg'),
    (3, 'Гамбургер', 25000, 'Булочка, говядина, огурцы, помидоры , салат, соус' , 'media/burger/burger_1.jpg'),
    (3, 'Чикенбургер', 23000, 'Булочка, курица, огурцы, помидоры , салат, соус' , 'media/burger/burger_2.jpg'),
    (3, 'Черный бургер', 27000, 'Булочка черная, говядина, огурцы, помидоры , салат, соус' , 'media/burger/burger_3.jpg'),
    (4, 'Французский Хот-Дог', 20000, 'Булочка , сосиська, соус' , 'media/hot-dog/hot_dog_1.jpg'),
    (4, 'Баварский Хот-Дог', 22000, 'Булочка , боварская сосиська, салат, соус' , 'media/hot-dog/hot_dog_2.jpg'),
    (4, 'Американский Хот-Дог ', 15000, 'Булочка , сосиська, бекон, салат, соус' , 'media/hot-dog/hot_dog_3.jpg'),
    (5, 'Coca-Cola 0,5', 10000, '' , 'media/water/water_1.jpg'),
    (5, 'Fanta 0,5', 10000, '' , 'media/water/water_2.jpg'),
    (5, 'Sprite 0,5', 10000, '' , 'media/water/water_3.jpg'),
    (6, 'Сырный соус', 4000, '' , 'media/soup/soup_1.jpg'),
    (6, 'Чесночный соус', 4000, '' , 'media/soup/soup_2.jpg'),
    (6, 'Барбекю соус', 4000, '' , 'media/soup/soup_3.jpg')
    ''')
    database.commit()
    database.close()

# insert_products_table()

def first_select_user(cha_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE telegram_id = ?
    ''', (cha_id,))
    user = cursor.fetchone()
    database.close()

    return user

def first_register_user(cha_id, full_name):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO users(telegram_id, full_name) VALUES(?,?)
    ''' , (cha_id,full_name))
    database.commit()
    database.close()

# Данная функция нужна для сохранения телефона
def update_user_to_finish_register(chat_id,phone):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
        UPDATE users
        SET phone = ?
        WHERE telegram_id = ?
    ''', (phone,chat_id))
    database.commit()
    database.close()

def insert_to_cart(cha_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO carts(user_id) VALUES
    (
    (SELECT user_id FROM users WHERE telegram_id = ?)
    );
    ''', (cha_id,))
    database.commit()
    database.close()


def get_all_categories():
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM categories;
    ''')
    categories = cursor.fetchall()
    database.close()
    return categories


def get_products_by_category_id(category_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_id, product_name FROM products
    WHERE category_id = ?
    ''', (category_id,))
    products = cursor.fetchall()
    database.close()
    return products

def get_proguct_detail(product_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM products
    WHERE product_id = ?
    ''', (product_id,))
    product = cursor.fetchone()
    database.close()
    return product

# Функция для получения id карточки пользователя
def get_user_cart_id(chat_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT cart_id FROM carts
    WHERE user_id = (
        SELECT user_id FROM users WHERE telegram_id = ?
    )
    ''', (chat_id,))
    cart_id = cursor.fetchone()[0]
    database.close()
    return cart_id


# Функция для получения количества продукта в корзине по id карточки пользователя
def get_quantity(cart_id, product):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT quantity FROM cart_products
    WHERE cart_id = ? and product_name = ?
    ''', (cart_id, product))
    quantity = cursor.fetchone()[0]
    database.close()
    return quantity

# Функция которая добавляет и изменяет кол-во продуктов в корзине
def insert_or_update_cart_product(cart_id, product_name, quantity, final_price):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    try:
        cursor.execute('''
        INSERT INTO cart_products(cart_id, product_name, quantity, final_price)
        VALUES(?,?,?,?)
        ''', (cart_id, product_name, quantity, final_price))
        database.commit()
        return True
    except:
        cursor.execute('''
        UPDATE cart_products
        SET quantity = ?,
        final_price = ?
        WHERE product_name = ? AND cart_id = ?
        ''',(quantity, final_price, product_name, cart_id))
        database.commit()
        return False
    finally:
        database.close()


def update_total_product_total_price(cart_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    UPDATE carts
    SET total_products = (
    SELECT SUM(quantity) FROM cart_products 
    WHERE cart_id = :cart_id
    ),
    total_price = (
    SELECT SUM(final_price) FROM cart_products 
    WHERE cart_id = :cart_id
    )
    WHERE cart_id = :cart_id
    ''', {'cart_id' : cart_id})
    database.commit()
    database.close()


def get_cart_products(cart_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_name , quantity, final_price
    FROM cart_products
    WHERE cart_id = ? 
    ''', (cart_id,))
    cart_products = cursor.fetchall()
    database.close()
    return cart_products

def get_total_products_price(cart_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT total_products , total_price FROM carts WHERE cart_id = ?
    ''',(cart_id,))
    total_products , total_price = cursor.fetchone()
    database.close()
    return total_products,total_price

def get_cart_products_for_delete(cart_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT cart_product_id , product_name FROM
    cart_products
    WHERE cart_id = ? 
    ''', (cart_id,))
    cart_products = cursor.fetchall()
    database.close()
    return cart_products

def delete_cart_product_from(cart_product_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM cart_products WHERE cart_product_id = ? 
    ''', (cart_product_id,))
    database.commit()
    database.close()


def drop_cart_products_default(cart_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM cart_products WHERE cart_id = ? 
    ''', (cart_id,))
    database.commit()
    database.close()


def order_total_price():
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders_total_price(
    orders_total_price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER REFERENCES carts(cart_id),
    total_price DECIMAL(12, 2) DEFAULT 0,
    total_products INTEGER DEFAULT 0,
    time_now TEXT,
    new_data TEXT
    );
    ''')

def order():
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
    orders_id INTEGER PRIMARY KEY AUTOINCREMENT,
    orders_total_price_id INTEGER REFERENCES orders_total_price(orders_total_price_id),
    product_name VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL,
    final_price DECIMAL(12, 2) NOT NULL
    );
    ''')

# order_total_price()
# order()

def save_order_total(cart_id , total_products, total_price, time_now, new_date):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO orders_total_price(cart_id , total_products, total_price, time_now, new_data)
    VALUES(?,?,?,?,?)
    ''',(cart_id , total_products, total_price, time_now, new_date))

    database.commit()
    database.close()

def orders_total_price_id(cart_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT orders_total_price_id FROM orders_total_price
    WHERE cart_id = ?
    ''', (cart_id,))
    order_total_id = cursor.fetchall()[-1][0]
    database.close()
    return order_total_id

def save_order(order_total_id, product_name, quantity, final_price):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO orders(orders_total_price_id, product_name, quantity, final_price)
    VALUES (?,?,?,?)
    ''', (order_total_id, product_name, quantity, final_price))
    database.commit()
    database.close()


def get_orders_total_price(cart_id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM orders_total_price
    WHERE cart_id = ?
    ''',(cart_id,))
    order_total_price = cursor.fetchall()
    database.close()
    return order_total_price

def get_detail_product(id):
    database = sqlite3.connect('Shop.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_name, quantity, final_price FROM orders
    WHERE orders_total_price_id = ?
    ''', (id,))
    detail_product = cursor.fetchall()
    database.close()
    return detail_product
