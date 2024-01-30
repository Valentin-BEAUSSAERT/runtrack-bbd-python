import mysql.connector

# Connexion à la base de données
try:
    connexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='SQL12345',
        database='LaPlateforme'
    )
    cursor = connexion.cursor()

    # Requête SQL pour récupérer les noms et capacités des salles
    query = "SELECT nom, capacite FROM salle"
    cursor.execute(query)

    # Récupération des résultats
    resultats = cursor.fetchall()
    for (nom, capacite) in resultats:
        print(f"('{nom}', {capacite})")

except mysql.connector.Error as err:
    print("Erreur lors de la connexion à la base de données:", err)

finally:
    if connexion.is_connected():
        cursor.close()
        connexion.close()
