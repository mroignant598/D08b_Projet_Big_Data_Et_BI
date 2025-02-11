import sys
import csv
import datetime

csv_reader = csv.reader(sys.stdin)
next(csv_reader)

# lecture des donnees depuis le fichier CSV et selection des differentes colonnes
for word in csv_reader :
    codcde = word[6]
    ville = word[5]
    datcde = word[7]
    qte = word[15]
    timbrecli = word[8]
    departement = word[25]
    points = word[20]
    
    # extraction de l'annee      
    try:
        annee = datetime.datetime.strptime(datcde, "%Y-%m-%d").year
    except ValueError:
        continue

    # transformation de la donnee points en float    
    points = float(points)

    # tri pour n'avoir que les donnees entre 2011 et 2016 ainsi que les commandes ayant des points superieurs a 0 pour eviter tous les goodies offerts
    if 2011 <= annee <= 2016 and points >= 0:
        # tri sur les departements 22, 49 et 53 pour les commandes ayant un timbrecli egal a 0
        if departement in ['22', '49', '53'] and timbrecli == '0.0':
            print("%s;%s;%s;%s;%s;%s;%s" % (codcde, ville, departement, datcde, timbrecli, qte, points)) 
        
