#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import psycopg2
from détail_gare import *
from afficher_billets import *
from inscrire_voyageur import *
from database_config import *
import chercher_trajet
import statistiques
import reserver_billet
from exception import *
from nouvelle_ligne import *
import ajouter_train

connexion = psycopg2.connect(
    "host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD)
)

d = 0
while d != 10:
    print("1. Afficher les billets")
    print("2. Inscrire un voyageur")
    print("3. Chercher un trajet et acheter un billet")
    print("4. Détails d'une gare")
    print("5. Créer une nouvelle ligne")
    print("6. Ajouter un train")
    print("7. Statistiques")
    print("8. Exception")
    print("9. Quitter")
    d = int(input("Veuillez choisir une option "))
    if d == 1:
        try:
            afficher_billet(connexion)
        except psycopg2.IntegrityError as e:
            connexion.rollback()
            print("message système :", e)
    if d == 2:
        try:
            inscrire_voyageur(connexion)
        except psycopg2.IntegrityError as e:
            connexion.rollback()
            print("message système :", e)
    if d == 3:
        try:
            chercher_trajet.recherche_trajet(connexion)
        except psycopg2.IntegrityError as e:
            connexion.rollback()
            print("message système :", e)
    if d == 4:
        try:
            detail(connexion)
        except psycopg2.IntegrityError as e:
            connexion.rollback()
            print("message système :", e)
    if d == 5:
        try:
            nouvelle_ligne(connexion)
        except psycopg2.IntegrityError as e:
            connexion.rollback()
            print("message système :", e)
    if d == 6:
        try:
            ajouter_train.ajout(connexion)
        except psycopg2.IntegrityError as e:
            connexion.rollback()
            print("message système :", e)
    if d == 7:
        try:
            statistiques.choix(connexion)
        except psycopg2.IntegrityError as e:
            connexion.rollback()
            print("message système :", e)
    if d == 8:
        try:
            exception(connexion)
        except psycopg2.IntegrityError as e:
            connexion.rollback()
            print("message système :", e)
    if d == 9:
        print("--- Fin du programme ---")
        connexion.close()
        exit()