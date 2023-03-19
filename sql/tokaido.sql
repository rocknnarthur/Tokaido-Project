--
-- Création de la base de données :
--

DROP DATABASE IF EXISTS Tokaido;

CREATE DATABASE Tokaido CHARACTER SET 'utf8';

USE Tokaido;

--
-- Création des tables :
--

CREATE TABLE Joueur (
	jou_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	jou_nom VARCHAR(30) NOT NULL,
	jou_prenom VARCHAR(30) NOT NULL,
    jou_pseudo VARCHAR(20) NOT NULL,
	jou_creation DATE,
	jou_login VARCHAR(20) NOT NULL,
	jou_password VARCHAR(30) NOT NULL,
	PRIMARY KEY (jou_id)
)
ENGINE=INNODB;


CREATE TABLE Statistiques (
	sta_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	sta_win INT,
    sta_lose INT,
	PRIMARY KEY (sta_id),
    CONSTRAINT fk_sta_id FOREIGN KEY (sta_id) REFERENCES Joueur(jou_id)
)
ENGINE=INNODB;

--
-- Insertion de valeurs dans les tables :
--

INSERT INTO Joueur
VALUES	(1, 'CHEVREL', 'Arthur', 'Art333', '2023-03-15', 'rocknnarthur', 'raclette123!');


INSERT INTO Statistiques
VALUES	(1, 0, 0);

-- 
-- Requêtes :
--

SELECT *
VALUES	(1, 0, 0);