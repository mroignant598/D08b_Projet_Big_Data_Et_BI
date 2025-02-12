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
    timbrecde = word[9]
    qte = word[15]
    departement = word[25]
    
    # extraction de l'annee    
    try:
        annee = datetime.datetime.strptime(datcde, "%Y-%m-%d").year
    except ValueError:
        continue
    
       
    if 2006 <= annee <= 2010:
        if departement in ['28', '53', '61']:
            print("%s;%s;%s;%s;%s;%s" % (codcde, ville, departement, datcde, timbrecde, qte)) 
        
