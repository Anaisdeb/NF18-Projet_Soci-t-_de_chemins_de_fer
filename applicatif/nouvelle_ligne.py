#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def nouvelle_ligne(conn) :
    cur = conn.cursor()
    
    #affichage des lignes
    print("Voici les lignes : ")
    print("| code | nom")
    print("-----------------------------")

    sql = "SELECT * FROM ligne"
    cur.execute(sql)
    res = cur.fetchall()

    for raw in res:
        print ("| %s | %s |" % (raw[0], raw[1]))

    print("-----------------------------")
    print()
    
    print("CREER UNE LIGNE :")
    #code ?
    code = int(input("Quelle est le code de la ligne ? : "))
    #nom?
    nom = (input("Quel est le nom de la ligne ? : "))
    #ajout de la ligne
    sql = "INSERT INTO ligne (code, nom) VALUES (%s, %s);"
    cur.execute(sql,(code, nom))
    conn.commit()
    
    #affichage des gares
    sql = "SELECT * FROM gare"
    cur.execute(sql)
    res = cur.fetchall()

    for raw in res:
        print ("| %s | %s | %s | %s |" % (raw[0], raw[1], raw[2], raw[3]))

    print("-----------------------------------------------------------------------------")
    print()
    
    while(not res):
        print("Aucune gare à proposer. Veuillez créer des gares.\n")
        
    print("Voici les gares : ")
    print("---------------------")
    for i in range(len(res)):
        print(i+1," - ",res[i][0])
    print("---------------------")
    
    nb_arrets = int(input("Combien d'arrets sont sur cette ligne ? : "))
    for j in range (nb_arrets):
        print("rang", j, ":")
        #nom gare?
        gare = (int(input("Quel est le numero de la gare ? : ")))
        #ajout de l'arret
        sql = "INSERT INTO arret (rang, code_ligne, nom_gare, ville) VALUES (%s, %s, %s, %s);"
        cur.execute(sql, (j, code, res[gare-1][0], res[gare-1][1]))
        conn.commit()