import mysql.connector

# Informations de connexion à la base de données
host = "localhost"
user = "root"
password = "SQL12345"
database_name = "LaPlateforme"

# Création de la connexion à la base de données
try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database_name
    )

    # Création d'un curseur pour exécuter des requêtes
    cursor = conn.cursor()

    # Requête SQL pour récupérer les informations des étudiants
    query = "SELECT * FROM etudiant"  # Remplacez 'etudiants' par le nom réel de la table si différent

    # Exécution de la requête
    cursor.execute(query)

    # Récupération des résultats
    etudiants = cursor.fetchall()

    # Affichage des résultats
    for etudiant in etudiants:
        print(etudiant)

except mysql.connector.Error as error:
    print(f"Une erreur s'est produite: {error}")

finally:
    # Fermeture du curseur et de la connexion
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("La connexion MySQL est fermée")
