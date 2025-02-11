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
    nomcli = word[2]
    prenomcli = word[3]
    cpcli = word[4]
    codcli = word[0]
    departement = word[25]
    timbrecli = word[8]
    codobj = word[14]
    libobj = word[17]
    
    # extraction de l'annee 
    try:
        annee = datetime.datetime.strptime(datcde, "%Y-%m-%d").year
    except ValueError:
        continue
    
    print("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (nomcli, prenomcli, codcde, ville, datcde, annee, timbrecde, qte, codcli, departement, timbrecli, codobj, libobj, cpcli)) 
        
