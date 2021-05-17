#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime as dt

def exception(conn) :
    cur = conn.cursor()
    
    #affichage du calendrier exceptionnel
    print()
    print("Voici le calendrier exceptionnel : ")
    print("id | ajout | debut | fin")
    print("-------------------")
    
    sql = "SELECT * FROM exceptionnelc"
    cur.execute(sql)
    res = cur.fetchall()

    for raw in res:
        print (raw[0], raw[1], raw[2], raw[3])
    
    print("-------------------")
    print()
        
    #insert ou delete ?
    delete = input("Voulez-vous retirer un élément du calendrier exceptionnel ? oui ou non ? : ")
    
    #requête
    if delete == "oui":
        #id ?
        idi = int(input("Quel est l'id ? : "))
        #suppression de la référence dans horaire sur le calendrier exceptionnel
        sql = "DELETE FROM exceptionnelc_horaire WHERE id_horaire='%s'" % (idi)
        cur.execute(sql)
        conn.commit()
        #suppression du calendrier exceptionnel
        sql = "DELETE FROM exceptionnelc WHERE id='%s'" % (idi)
        cur.execute(sql)
        conn.commit()

    else :
        #valeurs ?
        ajout = input("Est-ce un ajout dans le calendrier ? true or false ? : ")
        
        jour_debut = input("Entrez la date de début au format YYYY-MM-DD : ")
        year, month, day = map(int, jour_debut.split('-'))
        jour_debut = dt.datetime(year, month, day)
        formatted_date1 = jour_debut.strftime('%Y-%m-%d %H:%M:%S')
        
        jour_fin = input("Entrez la date de début au format YYYY-MM-DD : ")
        year, month, day = map(int, jour_fin.split('-'))
        jour_fin= dt.datetime(year, month, day)
        formatted_date2= jour_fin.strftime('%Y-%m-%d %H:%M:%S')

        sql = ("INSERT INTO exceptionnelc (ajout,jour_debut,jour_fin) VALUES ('%s', '%s', '%s');" % (ajout, formatted_date1, formatted_date2))
        cur.execute(sql)
        conn.commit()