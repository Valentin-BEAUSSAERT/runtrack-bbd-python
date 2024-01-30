-- Insertion des données dans la table etage
INSERT INTO etage (nom, numero, superficie) VALUES ('RDC', 0, 500);
INSERT INTO etage (nom, numero, superficie) VALUES ('R+1', 1, 500);

-- Insertion des données dans la table salle
INSERT INTO salle (nom, id_etage, capacite) VALUES ('Lounge', 1, 100);
INSERT INTO salle (nom, id_etage, capacite) VALUES ('Studio Son', 1, 5);
INSERT INTO salle (nom, id_etage, capacite) VALUES ('Broadcasting', 2, 50);
INSERT INTO salle (nom, id_etage, capacite) VALUES ('Bocal Peda', 2, 4);
INSERT INTO salle (nom, id_etage, capacite) VALUES ('Coworking', 2, 80);
INSERT INTO salle (nom, id_etage, capacite) VALUES ('Studio Video', 2, 5);
