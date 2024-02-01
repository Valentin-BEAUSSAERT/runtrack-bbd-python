
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

class ProductDatabase:
    def __init__(self, host, user, passwd, database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                database=self.database
            )
            return self.connection
        except Error as err:
            messagebox.showerror("Erreur", f"Une erreur s'est produite: {err}")
            return None

    def fetch_products(self):
        conn = self.connect()
        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM product")
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            return rows
        else:
            return []

    def add_product(self, name, description, price, quantity, category):
        conn = self.connect()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO product (name, description, price, quantity, category) VALUES (%s, %s, %s, %s, %s)"
                values = (name, description, price, quantity, category)
                cursor.execute(query, values)
                conn.commit()
                return True
            except Error as err:
                messagebox.showerror("Erreur", f"Une erreur s'est produite lors de l'ajout: {err}")
                return False
            finally:
                if conn.is_connected():
                    cursor.close()
                    conn.close()


    def delete_product(self, product_id):
        conn = self.connect()
        if conn is not None:
            cursor = conn.cursor()
            query = "DELETE FROM product WHERE id = %s"
            cursor.execute(query, (product_id,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else:
            return False

    def update_product(self, product_id, name, description, price, quantity, category):
        conn = self.connect()
        if conn is not None:
            cursor = conn.cursor()
            query = """
            UPDATE product
            SET name = %s, description = %s, price = %s, quantity = %s, category = %s
            WHERE id = %s
            """
            values = (name, description, price, quantity, category, product_id)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else:
            return False

