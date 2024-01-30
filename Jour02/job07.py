import mysql.connector

class Salarie:
    def __init__(self, host, user, password, database):
        self.connexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connexion.cursor(buffered=True)
    
    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (nom, prenom, salaire, id_service))
        self.connexion.commit()

    # D'autres méthodes pour lire, mettre à jour, et supprimer des employés

    def __del__(self):
        self.cursor.close()
        self.connexion.close()
