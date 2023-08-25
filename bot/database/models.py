import sqlite3 as sql

def sql_init(): 
   global db, cursor
   with sql.connect('sneakerstore.db') as db:
      cursor = db.cursor()

      cursor.execute("""
      CREATE TABLE IF NOT EXISTS products(
        name PRIMARY KEY,
        description TEXT,
        photo TEXT,
        price TEXT
      );  
      """)

      cursor.execute("""
      CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        products TEXT
      );  
      """)
      
      db.commit()

async def add_product(state):
   async with state.proxy() as data:
      cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)", tuple(data.values()))
      db.commit()

async def delete_product(name):
      cursor.execute("DELETE from products where name = (?)", (name,))
      db.commit()

async def add_user(id):
    cursor.execute("INSERT INTO users (user_id) VALUES (?)", (id,))
    db.commit()

def get_user_data(id):
    return cursor.execute("SELECT * FROM users WHERE user_id = ?", (id,)).fetchall()

async def add_product_to_cart(id, product_name):
    if get_user_data(id)[0][1]!= None:
      products_in_cart = get_user_data(id)[0][1]
    else:
        products_in_cart = ''
    cursor.execute("UPDATE users SET products = ? WHERE user_id = ?", (f'{products_in_cart + product_name},', id))
    db.commit()

async def clear_cart(id):
    cursor.execute("UPDATE users SET products = ? WHERE user_id = ?", (None, id))
    db.commit()

def get_all():
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def get():
   cursor.execute("SELECT * FROM products")
   data = cursor.fetchall()
   
   keys = ('name', 'description', 'photo', 'price')
   name = []
   description = []
   photo = []
   price = []
   for i in data:
      name.append(i[0])
      description.append(i[1])
      photo.append(i[2])
      price.append(i[3])
   all_data = [name, description, photo, price]
   product_data = dict(zip(keys, all_data))
   return product_data
