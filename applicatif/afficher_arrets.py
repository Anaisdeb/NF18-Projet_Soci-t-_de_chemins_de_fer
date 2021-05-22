#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def afficher_arrets(conn) :
    cur = conn.cursor()
    
    #affichage des arrêts
    print()
    print("Voici les arrets : ")
    print("| rang | ligne | gare | ville")
    print("----------------------------------------")

    sql = "SELECT * FROM arret"
    cur.execute(sql)
    res = cur.fetchall()

    for raw in res:
        print ("| %s | %s | %s | %s |" % (raw[0], raw[1], raw[2], raw[3]))

    print("----------------------------------------")
    print()
