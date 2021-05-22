#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def nouvelle_gare(conn) :
    cur = conn.cursor()
    
    #zone horaire (GMT)
    print()
    sql="SET TIMEZONE='GMT'"
    cur.execute(sql)
    sql="SHOW TIMEZONE"
    cur.execute(sql)
    raw = cur.fetchone()
    print("  TimeZone")
    print("------------")
    print("    %s" % (raw[0]))

    #affichage des gares
    print("Voici les gares : ")
    print("| nom | ville | adresse | horaire")
    print("-----------------------------------------------------------------------------")

    sql = "SELECT * FROM gare"
    cur.execute(sql)
    res = cur.fetchall()

    for raw in res:
        print ("| %s | %s | %s | %s |" % (raw[0], raw[1], raw[2], raw[3]))

    print("-----------------------------------------------------------------------------")
    print()
    
    print("CREER UNE GARE :")
    #nom ?
    nom = (input("Quelle est le nom de la gare ? : "))
    #ville?
    ville = (input("Quel est le nom de la ville ? : "))
    #adresse?
    adresse = (input("Quelle est l'adresse de la gare ? : "))
    #horaire?
    horaire = input("Quelle est la zone horaire de la gare (GMT) ? : ")
    #ajout de la ligne
    sql = "INSERT INTO gare (nom, ville, adresse, horaire) VALUES (%s, %s, %s, %s);"
    cur.execute(sql, (nom, ville, adresse, horaire))
    conn.commit()