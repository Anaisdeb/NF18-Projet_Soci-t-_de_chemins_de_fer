#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def nouvelle_ligne(conn) :
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
    
    #arret ou ligne ou gare ?
    element = input("Quel élément souhaitez-vous créer/supprimer ? (arret ou ligne ou gare) : ")
    
    if element == "arret":
        delete = input("Voulez-vous supprimer un arret ? (oui ou non) : ")
        #requête
        if delete == "oui":
            #rang ?
            rang = int(input("Quel est le rang ? : "))
            #code ligne ?
            code_ligne= int(input("Quel est le code de la ligne ? : "))
            #suppression de l'horaire associé à l'arret
            sql = "DELETE FROM horaire WHERE rang='%s' AND code_ligne='%s'" % (rang, code_ligne)
            cur.execute(sql)
            conn.commit() 
            #suppression de l'arret
            sql = "DELETE FROM arret WHERE rang='%s' AND code_ligne='%s'" % (rang, code_ligne)
            cur.execute(sql)
            conn.commit()    
        else :
            #rang ?
            rang = int(input("Quel est le rang ? : "))
            #code ligne ?
            code_ligne = int(input("Quel est le code de la ligne ? : "))
            #nom gare?
            nom_gare = (input("Quel est le nom de la gare ? : "))
            #ville?
            ville = (input("Quel est la ville ? : "))
            #ajout de l'arret
            sql = ("INSERT INTO arret (rang, code_ligne, nom_gare, ville) VALUES ('%s', '%s', '%s', '%s');" % (rang, code_ligne, nom_gare, ville))
            cur.execute(sql)
            conn.commit()
            
    elif element == "ligne":
        print("CREER UNE LIGNE :")
        #code ?
        code = int(input("Quelle est le code de la ligne ? : "))
        #nom?
        nom = (input("Quel est le nom de la ligne ? : "))
        #ajout de la ligne
        sql = ("INSERT INTO ligne (code, nom) VALUES ('%s', '%s');" % (code, nom))
        cur.execute(sql)
        conn.commit()
        
    else : #element == "gare"
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
        sql = ("INSERT INTO gare (nom, ville, adresse, horaire) VALUES ('%s', '%s', '%s', '%s');" % (nom, ville, adresse, horaire))
        cur.execute(sql)
        conn.commit()