import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connexion à la base de données MySQL réussie")
    except Error as err:
        print(f"Erreur: '{err}'")
    return connection

def execute_query(connection, query, args=None):
    cursor = connection.cursor()
    try:
        if args:
            cursor.execute(query, args)
        else:
            cursor.execute(query)
        connection.commit()
        print("Requête réussie")
    except Error as err:
        print(f"Erreur: '{err}'")


def add_product(connection, name, description, price, quantity, id_category):
    query = """
    INSERT INTO product (name, description, price, quantity, id_category) 
    VALUES (%s, %s, %s, %s, %s);
    """
    args = (name, description, price, quantity, id_category)
    execute_query(connection, query, args)

def delete_product(connection, product_id):
    query = "DELETE FROM product WHERE id = %s;"
    args = (product_id,)
    execute_query(connection, query, args)


def update_product(connection, product_id, name=None, description=None, price=None, quantity=None):
    args = []
    query = "UPDATE product SET "
    if name:
        query += "name = %s, "
        args.append(name)
    if description:
        query += "description = %s, "
        args.append(description)
    if price:
        query += "price = %s, "
        args.append(price)
    if quantity:
        query += "quantity = %s, "
        args.append(quantity)
    query = query.rstrip(', ')
    query += " WHERE id = %s;"
    args.append(product_id)
    execute_query(connection, query, tuple(args))


# Exemple de connexion à la base de données
connection = create_server_connection("localhost", "root", "SQL12345", "store")

# Exemple d'ajout d'un produit
add_product(connection, "Nouveau Produit", "Description du nouveau produit", 100, 10, 1)

# Exemple de suppression d'un produit
delete_product(connection, 1)

# Exemple de mise à jour d'un produit
update_product(connection, 2, price=150, quantity=20)
