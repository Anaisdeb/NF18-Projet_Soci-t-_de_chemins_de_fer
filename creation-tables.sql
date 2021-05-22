DROP TYPE IF EXISTS type_de_transport CASCADE;
DROP TYPE IF EXISTS type_de_statut CASCADE;
DROP TYPE IF EXISTS type_de_train CASCADE;
DROP TYPE IF EXISTS type_de_paiement CASCADE;
DROP TABLE IF EXISTS Trajet CASCADE;
DROP TABLE IF EXISTS ExceptionnelC_Horaire CASCADE;
DROP TABLE IF EXISTS Horaire CASCADE;
DROP TABLE IF EXISTS Train CASCADE;
DROP TABLE IF EXISTS Arret CASCADE;
DROP TABLE IF EXISTS Gare CASCADE;
DROP TABLE IF EXISTS Ligne CASCADE;
DROP TABLE IF EXISTS Propose_taxi CASCADE;
DROP TABLE IF EXISTS Propose_hotel CASCADE;
DROP TABLE IF EXISTS Propose_transport CASCADE;
DROP TABLE IF EXISTS Taxi CASCADE;
DROP TABLE IF EXISTS Hotel CASCADE;
DROP TABLE IF EXISTS Transport CASCADE;
DROP TABLE IF EXISTS Reservation CASCADE;
DROP TABLE IF EXISTS Voyageur CASCADE;
DROP TABLE IF EXISTS RegulierC CASCADE;
DROP TABLE IF EXISTS ExceptionnelC CASCADE;
DROP TABLE IF EXISTS Billet CASCADE;


CREATE TABLE Gare
(
    nom VARCHAR NOT NULL,
    ville VARCHAR NOT NULL,
    adresse VARCHAR NOT NULL,
    horaire VARCHAR NOT NULL,
    PRIMARY KEY (nom, ville)
);

CREATE TABLE Ligne (
    code INTEGER PRIMARY KEY,
    nom VARCHAR NOT NULL
);

CREATE TABLE Hotel (
    adresse VARCHAR PRIMARY KEY,
    ville VARCHAR NOT NULL,
    nom VARCHAR NOT NULL,
    nb_etoiles INTEGER NOT NULL
);

CREATE TABLE Taxi (
    numero INTEGER PRIMARY KEY,
    ville VARCHAR NOT NULL,
    marque VARCHAR NOT NULL,
    tarif INT NOT NULL,
    tel INTEGER NOT NULL                          
);

CREATE TYPE type_de_transport AS ENUM('bus','velo','tramway');

CREATE TABLE Transport (
    numero INTEGER PRIMARY KEY,
    ville VARCHAR NOT NULL,
    compagnie VARCHAR NOT NULL,
    tarif INTEGER NOT NULL,
    type type_de_transport NOT NULL         
);

CREATE TYPE type_de_statut AS ENUM('voyageur','grandVoyageur','grandVoyageurPlus');

CREATE TABLE Voyageur (
    id SERIAL PRIMARY KEY,
    nom VARCHAR NOT NULL,
    prenom VARCHAR NOT NULL,
    adresse VARCHAR NOT NULL,
    num_tel VARCHAR(10) NOT NULL,
    num_carte VARCHAR(16) UNIQUE,
    statut type_de_statut,
    regulier BOOLEAN NOT NULL,
    CHECK(NOT(regulier AND (num_carte IS NULL OR statut IS NULL))),
    CHECK(NOT(NOT regulier AND (num_carte IS NOT NULL OR statut IS NOT NULL)))
);

CREATE TYPE type_de_train AS ENUM('RER','TER','TGV');

CREATE TABLE Train(
    num INTEGER PRIMARY KEY, 
    placemax INTEGER NOT NULL,
    classe1 BOOLEAN NOT NULL,
    vitessemax INTEGER NOT NULL,
    type type_de_train NOT NULL,
    code_ligne INTEGER NOT NULL REFERENCES Ligne(code),
    CHECK((type='RER' AND NOT classe1 AND placemax=250 AND vitessemax=90) OR (type='TER' AND classe1 AND placemax=300 AND vitessemax=200) OR (type='TGV' AND classe1 AND placemax=350 AND vitessemax=400))
);

CREATE TABLE RegulierC(
    id SERIAL PRIMARY KEY,
    lundi BOOLEAN NOT NULL,
    mardi BOOLEAN NOT NULL,
    mercredi BOOLEAN NOT NULL,
    jeudi BOOLEAN NOT NULL,
    vendredi BOOLEAN NOT NULL,
    samedi BOOLEAN NOT NULL,
    dimanche BOOLEAN NOT NULL
);

CREATE TABLE ExceptionnelC(
    id SERIAL PRIMARY KEY,
    ajout BOOLEAN NOT NULL,
    jour_debut DATE NOT NULL,
    jour_fin DATE NOT NULL,
    CHECK (jour_debut <= jour_fin),
    UNIQUE (ajout, jour_debut, jour_fin)
);

CREATE TABLE Arret(
    rang INTEGER,
    code_ligne INTEGER,
    nom_gare VARCHAR NOT NULL,
    ville VARCHAR NOT NULL,
    PRIMARY KEY(rang, code_ligne),
    FOREIGN KEY (code_ligne) REFERENCES Ligne (code),
    FOREIGN KEY (nom_gare, ville) REFERENCES Gare(nom, ville )
);

CREATE TABLE Horaire(
    id SERIAL PRIMARY KEY,
    depart TIME NOT NULL,
    arrivee TIME NOT NULL,
    train INTEGER NOT NULL REFERENCES Train(num),
    rang INTEGER NOT NULL,
    code_ligne INTEGER NOT NULL,
    regulierC INTEGER NOT NULL REFERENCES RegulierC(id),
    FOREIGN KEY(rang, code_ligne) REFERENCES Arret(rang, code_ligne)
);

CREATE TABLE Billet (
    id SERIAL PRIMARY KEY,
    gare_depart VARCHAR NOT NULL,
    depart TIME NOT NULL,
    gare_arrivee VARCHAR NOT NULL,
    arrivee TIME NOT NULL,
    assurance BOOLEAN NOT NULL,
    prix INTEGER NOT NULL
);

CREATE TABLE Trajet(
    id INTEGER NOT NULL,
    place INTEGER NOT NULL,
    horaire_depart INTEGER NOT NULL,
    horaire_arrivee INTEGER NOT NULL,
    PRIMARY KEY(place, id),
    FOREIGN KEY (id) REFERENCES Billet(id),
    FOREIGN KEY (horaire_depart) REFERENCES Horaire(id),
    FOREIGN KEY (horaire_arrivee) REFERENCES Horaire(id)
);

CREATE TYPE type_de_paiement AS ENUM('espece','CB','cheque');

CREATE TABLE Reservation(
    id_billet INTEGER,
    id_voyageur INTEGER,
    paiement type_de_paiement NOT NULL,
    PRIMARY KEY(id_billet, id_voyageur)
);

CREATE TABLE Propose_taxi (
    num_taxi INTEGER,
    id_billet INTEGER,
    id_voyageur INTEGER,
    PRIMARY KEY (num_taxi, id_billet, id_voyageur),
    FOREIGN KEY (num_taxi) REFERENCES Taxi(numero),
    FOREIGN KEY (id_billet, id_voyageur) REFERENCES Reservation(id_billet, id_voyageur)
);

CREATE TABLE Propose_hotel(
    adresse VARCHAR,
    id_billet INTEGER,
    id_voyageur INTEGER,
    PRIMARY KEY(adresse, id_billet, id_voyageur),
    FOREIGN KEY (adresse) REFERENCES Hotel(adresse),
    FOREIGN KEY (id_billet, id_voyageur) REFERENCES Reservation(id_billet, id_voyageur)
);

CREATE TABLE Propose_transport (
    numero INTEGER,
    id_billet INTEGER,
    id_voyageur INTEGER,
    PRIMARY KEY (numero, id_billet, id_voyageur),
    FOREIGN KEY (numero) REFERENCES Transport(numero),
    FOREIGN KEY (id_billet, id_voyageur) REFERENCES Reservation(id_billet, id_voyageur)
);

CREATE TABLE ExceptionnelC_Horaire(
    id_horaire INTEGER,
    exceptionnelC INTEGER,
    PRIMARY KEY(id_horaire, exceptionnelC),
    FOREIGN KEY (id_horaire) REFERENCES Horaire(id),
    FOREIGN KEY (exceptionnelC) REFERENCES ExceptionnelC(id)
);