#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:09:11 2021

@author: nf18p109
"""

def detail(connexion) :
    cur = connexion.cursor()
    sql = "SELECT * FROM gare"
    cur.execute(sql)
    row = cur.fetchone()
    if row == None :
        print("Il n'y a pas de gare dans votre BDD ")
    else :
        i=0
        while row:
            print()
            #traitement de la ligne
            print(i, end='') #mettre sur la même ligne
            print(". Nom : {} | Ville : {} | Adresse : {} | Fuseau horaire : {}".format(row[0], row[1], row[2], row[3])) #à revoir vérifier que toutes les opérations s'affichent correctement (ajout acolade finale)
            i=i+1
            #passer à la ligne suivante
            row = cur.fetchone()
        j=-1
        while j<0 or j>i:
            print()
            j=int(input("Veuillez choisir une gare "))
        #on cherche les trains passant pas cette gare, ainsi que les services disponibles
        cur.execute(sql)
        row = cur.fetchone()
        for k in range(j):
            row = cur.fetchone()
        tab=row
        print(row)
        #On cherche les hôtels
        sql = "SELECT * FROM Hotel WHERE Hotel.ville=%s"
        cur.execute(sql, (tab[1],))
        row = cur.fetchone()
        if row :
            print()
            print()
            print("Hôtels disponibles :")
            print()
            while row :
                print()
                print("Adresse : {} | Ville : {} | Nom : {} | Nombre d'étoiles :{} ".format(row[0], row[1], row[2], row[3]))
                row = cur.fetchone()

         # On cherche les taxis
        sql = "SELECT * FROM Taxi WHERE Taxi.ville=%s"
        cur.execute(sql, (tab[1],))
        row = cur.fetchone()
        if row:
            print()
            print()
            print("Taxis disponibles :")
            print()
            while row:
                print()
                print("Numéro : {} | Ville : {} | Marque : {} | Tarif {} euros |  Téléphone : {}".format(row[0], row[1], row[2], row[3], row[4]))
                row = cur.fetchone()

        # On cherche les transports
        sql = "SELECT * FROM Transport WHERE Transport.ville=%s"
        cur.execute(sql, (tab[1],))
        row = cur.fetchone()
        if row:
            print()
            print()
            print("Transports disponibles :")
            print()
            while row:
                print()
                print("Numéro : {} | Ville : {} | Compagnie : {} | Tarif {} euros |  Type : {}".format(row[0], row[1], row[2], row[3], row[4]))
                row = cur.fetchone()

        #On cherche les lignes passant par cette gare
        sql = "SELECT * FROM ligne l, arret a, train t, horaire h WHERE a.ville=%s AND l.code=a.code_ligne AND a.nom_gare=%s AND t.code_ligne=a.code_ligne AND h.code_ligne=a.code_ligne AND h.rang=a.rang AND h.train=t.num"
        cur.execute(sql, (tab[1], tab[0]))
        row = cur.fetchone()
        if row:
            print()
            print()
            print()
            while row:
                print("Ligne :")
                print()
                print("Code : {} | Nom : {} | Rang de l'arrêt : {} ".format(row[0], row[1], row[2]))
                print("Trains :")
                print("Numéro : {} | Type: {} | Horaire d'arrivée : {} | Horaire de départ {}".format(row[6], row[10], row[14], row[13]))
                row = cur.fetchone()

        print()
