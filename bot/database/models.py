import sqlite3 as sql


class DataBase:
    def __init__(self):
        with sql.connect('sneakerstore.db') as self.db:
            self.cursor = self.db.cursor()

            self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
          name PRIMARY KEY,
          description TEXT,
          photo TEXT,
          price TEXT
        );  
        """)

            self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
          user_id INTEGER PRIMARY KEY,
          products TEXT
        );  
        """)
            self.db.commit()
    
    async def close_con(self):
        await self.db.close()
        

    """------------------------------GET REQUESTS------------------------------"""
    def get_user_data(self, id):
        return self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (id,)).fetchall()

    def get_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def get_products_details(self):
        self.cursor.execute("SELECT * FROM products")
        data = self.cursor.fetchall()

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


    """------------------------------POST REQUESTS------------------------------"""
    async def add_product_to_cart(self, id, product_name):
        if self.get_user_data(id)[0][1] != None:
            products_in_cart = self.get_user_data(id)[0][1]
        else:
            products_in_cart = ''
        self.cursor.execute("UPDATE users SET products = ? WHERE user_id = ?",
                            (f'{products_in_cart + product_name},', id))
        self.db.commit()

    async def add_product_to_assortment(self, state):
        async with state.proxy() as data:
            self.cursor.execute(
                "INSERT INTO products VALUES (?, ?, ?, ?)", tuple(data.values()))
            self.db.commit()

    async def create_user(self, id):
        self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (id,))
        self.db.commit()


    """------------------------------DELETE REQUESTS------------------------------"""
    async def delete_product(self, name):
        self.cursor.execute("DELETE FROM products WHERE NAME = (?)", (name,))
        self.db.commit()

    async def clear_cart(self, id):
        self.cursor.execute(
            "UPDATE users SET products = ? WHERE user_id = ?", (None, id))
        self.db.commit()

    