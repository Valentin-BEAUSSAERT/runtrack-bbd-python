import sqlite3

# Créer la base de données zoo et se connecter à elle
conn = sqlite3.connect('zoo.db')
cursor = conn.cursor()

# Créer la table "animal"
cursor.execute('''CREATE TABLE IF NOT EXISTS animal (
                id INTEGER PRIMARY KEY,
                nom TEXT,
                race TEXT,
                type_cage_id INTEGER,
                date_naissance DATE,
                pays_origine TEXT)''')

# Créer la table "cage"
cursor.execute('''CREATE TABLE IF NOT EXISTS cage (
                id INTEGER PRIMARY KEY,
                superficie REAL,
                capacite_max INTEGER)''')

# Fermer la connexion à la base de données
conn.close()

def ajouter_animal(nom, race, type_cage_id, date_naissance, pays_origine):
    conn = sqlite3.connect('zoo.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO animal (nom, race, type_cage_id, date_naissance, pays_origine)
                    VALUES (?, ?, ?, ?, ?)''', (nom, race, type_cage_id, date_naissance, pays_origine))
    conn.commit()
    conn.close()

def supprimer_animal(animal_id):
    conn = sqlite3.connect('zoo.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM animal WHERE id = ?', (animal_id,))
    conn.commit()
    conn.close()

def modifier_animal(animal_id, nom, race, type_cage_id, date_naissance, pays_origine):
    conn = sqlite3.connect('zoo.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE animal
                    SET nom = ?, race = ?, type_cage_id = ?, date_naissance = ?, pays_origine = ?
                    WHERE id = ?''', (nom, race, type_cage_id, date_naissance, pays_origine, animal_id))
    conn.commit()
    conn.close()

def afficher_animaux():
    conn = sqlite3.connect('zoo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM animal')
    animaux = cursor.fetchall()
    conn.close()
    return animaux

def calculer_superficie_totale():
    conn = sqlite3.connect('zoo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(superficie) FROM cage')
    superficie_totale = cursor.fetchone()[0]
    conn.close()
    return superficie_totale
