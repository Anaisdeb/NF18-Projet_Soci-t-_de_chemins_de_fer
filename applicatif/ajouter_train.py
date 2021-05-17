#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:15:23 2021

@author: nf18p109
"""

import psycopg2

def ajout(connexion) :
    cur = connexion.cursor()
    sql = "SELECT * FROM ligne"
    cur.execute(sql)
    row = cur.fetchone()
    while row:
        print()
        #traitement de la ligne
        print(". Code : {} | Nom : {} |".format(row[0], row[1])) 
        #passer à la ligne suivante
        row = cur.fetchone()

    ligne=None
    while ligne == None :
        try :
            print()
            j=int(input("Sur quelle ligne voulez-vous ajouter votre train ? "))
            sql = "SELECT * FROM ligne WHERE ligne.code=%s"
            cur.execute(sql, (j,))
            ligne = cur.fetchone()
            print(ligne)
        except psycopg2.DataError as e:
                print("Cette ligne n'existe pas")
                print("Message système :", e)
                connexion.rollback()
        

    
    erreur = 1
    while erreur :
        type_t=input("Quel est le type de votre train ? (TER, TGV, RER)")
        numero=int(input("Quel est le numéro de votre train"))
        if type_t=='TER':
            try:
                sql="INSERT INTO Train VALUES (%s, 300, true, 200, 'TER', %s)" #faire la gestion d'erreur si la clé existe déjà
                cur.execute(sql, (numero, ligne[0]))
                connexion.commit()
                erreur=0
            except psycopg2.IntegrityError as e:
                print("Il existe déjà un train avec ce numéro")
                print("Message système :", e)
                erreur=1
                connexion.rollback()
                
        if type_t=='RER':
            try :
                sql="INSERT INTO Train VALUES (%s, 250, false, 90, 'RER', %s)"
                cur.execute(sql, (numero, ligne[0]))
                connexion.commit()
                erreur=0
            except psycopg2.IntegrityError as e:
                print("Il existe déjà un train avec ce numéro")
                print("Message système :", e)
                erreur=1
                connexion.rollback()
                
        if type_t=='TGV':
            try :
                sql="INSERT INTO Train VALUES (%s, 350, true, 400, 'TGV', %s)"
                cur.execute(sql, (numero, ligne[0]))
                connexion.commit()
                erreur=0
            except psycopg2.IntegrityError as e:
                print("Il existe déjà un train avec ce numéro")
                print("Message système :", e)
                erreur=1
                connexion.rollback()
        if  type_t!='RER' and type_t!='TGV' and type_t!='TER':
            print("Le type n'est pas valide")
            erreur=1

    
    
    #Choix du calendrier régulier du train
    l=bool(input("Voulez-vous que le train circule le lundi ? (True/False) "))
    m=bool(input("Voulez-vous que le train circule le mardi ? (True/False) "))
    me=bool(input("Voulez-vous que le train circule le mercredi ? (True/False) "))
    j=bool(input("Voulez-vous que le train circule le jeudi ? (True/False) "))
    v=bool(input("Voulez-vous que le train circule le vendredi ? (True/False) "))
    s=bool(input("Voulez-vous que le train circule le samedi ? (True/False) "))
    d=bool(input("Voulez-vous que le train circule le dimanche ? (True/False) "))
    
        
    
    
    try:
        sql = "INSERT INTO regulierC(lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id" #récupérer l'id du clendrier crée
        cur.execute(sql, (l, m, me, j, v, s, d))
        reg = cur.fetchone()
        connexion.commit()
    except psycopg2.DataError as e:
        print("Veuillez entrer True ou False")
        print("Message système :", e)
        connexion.rollback()
        
        
        
    
    
    j=-1
    while j!=0 :
        sql="SELECT * FROM arret WHERE arret.code_ligne=%s"
        cur.execute(sql, (ligne[0],))
        row = cur.fetchone()
        i=1
        print()
        print("O. Quitter")
        while row:
            print()
            #traitement de la ligne
            print(i, end='') #mettre sur la même ligne
            print(". Gare : {} | Ville : {} |".format(row[2], row[3])) 
            i=i+1
            #passer à la ligne suivante
            row = cur.fetchone()

        while j<0 or j>i:
            print()
            j=int(input("Dans quelle gare votre train doit-il faire un arrêt ? (tapez 0 pour quitter)"))
        if j==0:
            break
        sql="SELECT * FROM arret WHERE arret.code_ligne=%s"
        cur.execute(sql, (ligne[0],))
        row = cur.fetchone()
        for k in range(j-1):
            row = cur.fetchone()
        arret=row
        print(row)
        j=-1
        arrivee=input("Donnez l'heure d'arrivée du train (format HH:MM:SS)")
        depart=input("Donnez l'heure de départ du train (format HH:MM:SS)")
        try:
            sql = "INSERT INTO Horaire(arrivee,depart,train,rang,code_ligne,regulierC) VALUES (%s,%s, %s, %s, %s, %s);" 
            cur.execute(sql, (arrivee, depart, numero, arret[0], ligne[0], reg))
            connexion.commit()
        except psycopg2.DataError as e:
            print("Veuillez entrer un horaire valide")
            print("Message système :", e)
            connexion.rollback()    
            
   