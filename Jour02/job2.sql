-- Création de la table etage
CREATE TABLE IF NOT EXISTS etage (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(255),
  numero INT,
  superficie INT
);

-- Création de la table salle
CREATE TABLE IF NOT EXISTS salle (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(255),
  id_etage INT,
  capacite INT,
  FOREIGN KEY (id_etage) REFERENCES etage(id)
);
