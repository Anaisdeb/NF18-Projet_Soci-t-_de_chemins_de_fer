# Modèle logique de données

> Note : dans les classes où aucune précision n'est apportée sur la nullité ou non des attributs, tous sont considérés par défaut comme `NOT NULL`. Les transformations non triviales sont justifiées dans la note de clarification.

## Classes fondamentales

```
Gare(#nom:string, #ville:string, adresse:string, horaire:heure)
Ligne(#code:int, nom:string)
Hotel(#adresse:string, ville:string, nom:string, nb_etoiles:int)
Taxi(#numero:int, ville:string, marque:string, tarif:int, tel:int)
Transport(#numero:int, ville:string, compagnie:string, type:{bus,velo,tramway})
```

## Classes issues d'héritages
```
Voyageur(#id:integer, nom : string, prenom:string, adresse: string, num_tel:integer[10], num_carte:integer, statut:{voyageur|grandVoyageur|grandVoyageurPlus}, regulier : boolean)
avec (id, nom, prenom, adresse, num_tel) NOT NULL, num_carte UNIQUE, (num_carte NOT NULL AND statut NOT NULL AND regulier) XOR (NOT regulier)
```
Redondance apportée par l'introduction du booléen `regulier` pour discriminer les classes filles, mais plus sympa pour la manipulation de données par la suite.

```
Train(#num:int, placemax:const int, classe1:const bool, vitessemax:const int, type:{RER|TER|TGV}, code_ligne=>ligne)
avec (type=RER AND placemax=place_max_RER AND classe1=false AND vitessemax=vitsse_max_RER) XOR (type=TER AND placemax=place_max_TER AND classe1=true AND vitessemax=vitesse_max_TER) XOR (type=TGV AND placemax=place_max_TGV AND classe1=true AND vitessemax=vitesse_max_TGV)
```
On suppose que `vitesse_max_TER`, `place_max_TER`, etc. sont des constantes définies en mémoire.

```
RegulierC(#id:int,lundi:bool,...,dimanche:bool)
ExceptionnelC(#id:int,ajout:bool,jour_debut:date,jour_fin:date)
avec jour_debut<=jour_fin
```
Classes issues de `Calendrier`.

## Classes issues d'associations
```
Horaire(#id:int, arrivee:heure, depart:heure, train=>Train, rang_arret=>Arret, code_ligne=>Arret, regulierC=>RegulierC)
Arret(#rang:int, #code_ligne=>Ligne, nom_gare=>Gare, ville=>Gare)
Trajet(#place:int, #id=>Billet, horaire_depart=>Horaire.id, horaire_arrivee=>Horaire.id) 
Billet(#id:int, gare_depart:string, depart:heure, gare_arrivee:string, arrivee:heure, assurance:bool, prix:int)
Propose_taxi(#num_taxi=>Taxi, #id_billet=>Reservation, #id_voyageur=>Reservation)
Propose_hotel(#adresse=>Hotel, #id_billet=>Reservation, #id_voyageur=>Reservation)
Propose_transport(#numero=>Transport, #id_billet=>Reservation, #id_voyageur=>Reservation)
Reservation(#id_billet=>Billet, #id_voyageur=>Voyageur, paiement:{espece,CB,cheque})
ExceptionnelC_Horaire(#horaire=>Horaire.id, exceptionnelC=>ExceptionnelC)
```

## Contraintes complexes portant sur l'ensemble du modèle
```
/*Les horaires de départ et d'arrivée associés à un trajet doivent être issus du même train.*/
R1 = Jointure(Trajet,Horaire ; Trajet.horaire_depart=Horaire.id)
R2 = Jointure(R1, Horaire ; R1.Horaire_arrivee=Horaire.id and R1.train!=Horaire.train)
IF R2!={} THEN "ERROR"

/*Un train ne s'arrête que sur des arrêts qui se situent sur la ligne sur laquelle il circule.*/
R1 = Jointure(Horaire, Train, Horaire.train=Train.num)
R2 = Restriction(R1, R1.CodeArret!=R1.code_ligne)
IF R2!={} THEN "ERROR"
```
