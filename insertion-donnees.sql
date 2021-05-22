INSERT INTO Gare VALUES ('Gare de Compiègne', 'Creil', '7 rue de la Paix', 'UTC + 12');
INSERT INTO Gare VALUES('Gare Saint-Lussier', 'Le Havre', '107 rue de la jointure', 'UTC+12');
INSERT INTO Gare VALUES('Gare Oise-Europe', 'Beauvais', '18 avenue de la clé primaire', 'UTC+12');
INSERT INTO Gare VALUES('Gare d''Amiens', 'Amiens', '47 Place Alphonse Fiquet', 'UTC+12');
INSERT INTO Gare VALUES('Gare de Lyon', 'Paris', 'Place Louis Armand', 'UTC+12');
INSERT INTO Gare VALUES('Gare du Nord', 'Paris', '112 rue de Maubeuge', 'UTC+12');
INSERT INTO Gare VALUES('Gare Saint-Lazare', 'Paris', '13 rue d''Amsterdam', 'UTC+12');
INSERT INTO Gare VALUES('Gare Saint-Roch', 'Montpellier', 'Place Auguste Gibert', 'UTC+12');

INSERT INTO Ligne VALUES(12, 'Ligne de Compi');
INSERT INTO Ligne VALUES(24, 'Ligne d''Amiens');
INSERT INTO Ligne VALUES(3, 'TER Hauts-de-France');
INSERT INTO Ligne VALUES(5, 'Transilien H');
INSERT INTO Ligne VALUES(2, 'RER D');
INSERT INTO Ligne VALUES(7, 'RER A');

INSERT INTO Hotel VALUES('12 rue de la Villette', 'Creil', 'Ibis budget', 2);
INSERT INTO Hotel VALUES('70 Avenue de Huy', 'Le Havre', 'Campanile', 3);
INSERT INTO Hotel VALUES('Avenue des Champs-Elysées','Paris','Ritz',5);

INSERT INTO Taxi VALUES (206318, 'Amiens', 'tesla', 50, 0678903617);
INSERT INTO Taxi VALUES (567895, 'Beauvais', 'ferrari', 48, 0634568903);
INSERT INTO Taxi VALUES (18523, 'Paris', 'BMW', 53, 0624568903);

INSERT INTO Transport VALUES (3, 'Compiègne', 'Ville de Compiegne', 4, 'bus');
INSERT INTO Transport VALUES (2, 'Creil',  'Vélotic', 5, 'velo');
INSERT INTO Transport VALUES (5, 'Paris',  'RATPx', 2, 'tramway');

INSERT INTO Voyageur(nom,prenom,adresse,num_tel,regulier) VALUES('Jean','AIMARE','5 avenue Foch Paris','066666666', false );
INSERT INTO Voyageur(nom,prenom,adresse,num_tel,num_carte,statut,regulier) VALUES('Michel','DUCHEMIN-DE-FER', '18 bouvelard de la Brioche Albertville', '0612563409', '392XF5687BN097V','grandVoyageurPlus',true);

INSERT INTO Train VALUES (212, 300, true, 200, 'TER', 12);
INSERT INTO Train VALUES (147, 350, true, 400, 'TGV', 24);
INSERT INTO Train VALUES (156, 250, false, 90, 'RER', 12);
INSERT INTO Train VALUES (18, 350, true, 400, 'TGV', 24);
INSERT INTO Train VALUES (37, 250, false, 90, 'RER', 12);



INSERT INTO RegulierC(lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche) VALUES (false,true,false,true,false,false,false);
INSERT INTO RegulierC(lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche) VALUES (true,true,true,true,true,true,false);
INSERT INTO RegulierC(lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche) VALUES (true,true,false,true,false,false,false);

INSERT INTO ExceptionnelC(ajout,jour_debut,jour_fin) VALUES (true, '2021-10-23', '2021-11-04');

INSERT INTO Arret VALUES(2,12,'Gare de Compiègne','Creil');
INSERT INTO Arret VALUES(7,12,'Gare Oise-Europe','Beauvais');
INSERT INTO Arret VALUES(9,24,'Gare d''Amiens','Amiens');
INSERT INTO Arret VALUES(1,3,'Gare d''Amiens','Amiens');
INSERT INTO Arret VALUES(2,3,'Gare de Compiègne','Creil');
INSERT INTO Arret VALUES(3,3,'Gare Oise-Europe','Beauvais');
INSERT INTO Arret VALUES(4,3,'Gare du Nord','Paris');
INSERT INTO Arret VALUES(5,3,'Gare de Lyon','Paris');
INSERT INTO Arret VALUES(1,12,'Gare d''Amiens','Amiens');
INSERT INTO Arret VALUES(3,12,'Gare Oise-Europe','Beauvais');
INSERT INTO Arret VALUES(4,12,'Gare du Nord','Paris');
INSERT INTO Arret VALUES(5,12,'Gare de Lyon','Paris');
INSERT INTO Arret VALUES(1,24,'Gare d''Amiens', 'Amiens');
INSERT INTO Arret VALUES(7,24,'Gare de Lyon', 'Paris');

INSERT INTO Horaire(arrivee,depart,train,rang,code_ligne,regulierC) VALUES ('03:07:00','03:11:00', 212, 1, 12,1);
INSERT INTO Horaire(arrivee,depart,train,rang,code_ligne,regulierC) VALUES ('11:00:00','11:03:00', 212, 7, 12,1);
INSERT INTO Horaire(arrivee,depart,train,rang,code_ligne,regulierC) VALUES ('15:15:00','15:18:00', 156, 1, 12,2);
INSERT INTO Horaire(arrivee,depart,train,rang,code_ligne,regulierC) VALUES ('07:00:00','07:03:00', 212, 1, 12,2);
INSERT INTO Horaire(arrivee,depart,train,rang,code_ligne,regulierC) VALUES ('07:32:00','07:35:00', 212, 2, 12,2);
INSERT INTO Horaire(arrivee,depart,train,rang,code_ligne,regulierC) VALUES ('07:48:00','07:53:00', 212, 3, 12,2);
INSERT INTO Horaire(arrivee,depart,train,rang,code_ligne,regulierC) VALUES ('08:14:00','08:17:00', 212, 4, 12,2);
INSERT INTO Horaire(arrivee,depart,train,rang,code_ligne,regulierC) VALUES ('08:24:00','08:27:00', 212, 5, 12,2);
INSERT INTO Horaire(arrivee,depart,train,rang,code_ligne,regulierC) VALUES ('09:00:00','09:03:00', 147, 1, 24,2);
INSERT INTO Horaire(arrivee,depart,train,rang,code_ligne,regulierC) VALUES ('10:45:00','10:48:00', 147, 7, 24,2);

INSERT INTO Billet VALUES(1, 'Gare de Compiègne','07:09:00','Gare Oise-Europe','11:00:00',true,1); 
INSERT INTO Billet VALUES(2, 'Gare d''Amiens','18:50:00','Gare Oise-Europe','11:00:00',false,1);

INSERT INTO Trajet VALUES(1,58,1,2);
INSERT INTO Trajet VALUES(1,102,9,10);

INSERT INTO Reservation VALUES(1, 1, 'CB');

INSERT INTO ExceptionnelC_Horaire VALUES(1, 1);
