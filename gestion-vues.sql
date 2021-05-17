CREATE VIEW verifLigne (code_ligne) AS
SELECT COUNT(Horaire.code_ligne)
FROM Horaire
JOIN Train ON Horaire.train = Train.num
WHERE Horaire.code_ligne <> Train.code_ligne;
/*Permet de vérifier qu'un train ne s'arrête que sur des arrêts qui se situent sur la ligne sur laquelle il circule      */

CREATE VIEW verifTrain (train) AS
SELECT COUNT(H1.train)
FROM Trajet, Horaire H1, Horaire H2
WHERE Trajet.horaire_depart=H1.id AND Trajet.horaire_arrivee=H2.id AND H1.train<>H2.train;
/*Permet de vérifier que l'horaire de départ d'un trajet et son horaire d'arrivée ont le même train*/