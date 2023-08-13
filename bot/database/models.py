import sqlite3 as sql

def sql_init(): 
   global db, cursor
   with sql.connect('sneakerstore.db') as db:
      cursor = db.cursor()

      query = ("""
      CREATE TABLE IF NOT EXISTS product(
        name PRIMARY KEY,
        description TEXT,
        photo TEXT,
        price TEXT
      );  
      """)
      
      cursor.executescript(query)
      db.commit()

async def add_product(state):
   async with state.proxy() as data:
      cursor.execute('INSERT INTO product VALUES (?, ?, ?, ?)', tuple(data.values()))
      db.commit()

async def delete_product(name):
      cursor.execute("""DELETE from product where name = (?)""", (name,))
      db.commit()

def get_all()-> list:
    cursor.execute("SELECT * FROM PRODUCT")
    return cursor.fetchall()

def get()-> dict:
   cursor.execute("SELECT * FROM PRODUCT")
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
