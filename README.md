# Projet NF18

## Fonctionnement général

L'objectif du projet est de mettre en pratique les principes de conception, de développement et d'interrogation de base de données vus en cours sur un exemple concret significatif.

Les étudiants travailleront dans des groupes de 4. Ils seront corrigés et notés par l'intervenant de TD. Les sujets seront consultables sur le site.

Les livrables seront déposés sur le gitlab de l'utc, en s'assurant bien que l'intervenant de TD a (au moins) les droits de lecture sur les fichiers du dépôt.

## Livrables

Les livrables suivant seront à fournir tout au long du projet :

- note de clarification : fichier texte complétant le sujet en éclaircissant les points posant questions.

- MCD UML : la modélisation logique des données se fera en UML. A titre indicatif, elle pourra comporter autour d'une douzaine de classes et d'une vingtaine d'associations. L'héritage sera mobilisé autant que possible, ainsi que les contraintes de modélisation avancées une foiscelles-ci étudiées en cours.

- MLD relationnel

- étude de normalisation : fichier texte décrivant pour un sous-ensemble de classes cohérents la liste des dépendances fonctionnelles et l'analyse justifiant le niveau de normalisation fonctionnelle du schéma relationnel.

- fichiers de création et d'interrogation de la base de données: fichiers SQL permettant de créer la base de données, insérer un nombre de données suffisant (autour d'une dizaine par classe), de réaliser les interrogations demandées dans le sujet, et de supprimer la base de données. Pour faciliter leur utilisation, ils peuvent être constitués de quatre fichiers différents (par exemple nommésTABLE.SQL, DATA.SQL, INTERROGATION.SQL et DELETE.SQL) et respectivement réalisant la création des tables, l'insertion des données, l'interrogation de requêtes et la suppression de la BdD. Ces fichiers utiliseront le SGBD postgresql, et devront absolument compiler correctement.

- des fichiers applicatifs de la BdD, permettant le sous-ensemble de tâches défini dans le sujet (typiquement l'insertion, la modification ou la suppression de certains éléments de la BdD, l'affichage de son contenu, et la réalisation des interrogations demandées). Le langage de l'application proposé est le python, vu en cours. Vous pouvez proposer un autre langage à votre intervenant de TD (par exemple php), qui n'a aucune obligation de l'accepter.

- une version modifée des livrables sera demandée en fin de semestre pour les statuts étudiants, avec des contraintes de modélisation avancées et du non-relationnel.

## Calendrier pour les étudiants (NF18)

Le projet se déroulera en deux phases : une première phase de 5 semaines pendant la période en entreprise des apprentis, et une seconde phase de deux semaines en fin de semestre.

Phase 1 : BdD relationnelle

- semaine 7 : rendu de la note de clarification et du MCD v1

- semaine 8 : rendu du MCD v2 et du MLD

- semaine 9 : rendu SQL

- semaine 10 : rendu Applicatif python

- semaine 11 : correction et rendu final de la phase 1

Phase 2 : BdD non-relationnelle

- semaine 14 et 15 : adaptation de la BdD en nosql (postgresql/Json ou MongoDB)

## Calendrier pour les apprentis (AI23)

Les apprentis auront à commencer la conception hors des séances de TD. La partie SQL et applicative pourra être réalisée pendant les deux dernières séances. Le choix leur ai donné de travailler sur une BdD relationnelle ou non-relationnelle.

hors séance pendant la semaine 12 : note de clarification et MCD v1

hors séance pendant la semaine 13 : MCD v2 et MLD

semaine 14 : SQL

semaine 15 : Applicatif python
