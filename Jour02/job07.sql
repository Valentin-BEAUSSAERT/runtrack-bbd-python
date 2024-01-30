CREATE DATABASE IF NOT EXISTS MaNouvelleBase;

USE MaNouvelleBase;

CREATE TABLE IF NOT EXISTS employe (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255),
  prenom VARCHAR(255),
  salaire DECIMAL(10, 2),
  id_service INT
);


INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
('Dupont', 'Jean', 3200.00, 1),
('Martin', 'Alice', 3500.00, 2);


SELECT * FROM employe WHERE salaire > 3000.00;


CREATE TABLE IF NOT EXISTS service (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255)
);


INSERT INTO service (nom) VALUES
('Informatique'),
('Ressources Humaines');

SELECT e.nom, e.prenom, s.nom AS service
FROM employe e
JOIN service s ON e.id_service = s.id;
