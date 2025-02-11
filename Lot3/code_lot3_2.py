import happybase
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Connection a HBase
connection = happybase.Connection('localhost', port=9090)
table = connection.table('data_digicheese')

# Scanner la table
scanner = table.scan()

# Dictionnaire pour stocker les commandes uniques.
commandes_uniques = {}

for key, data in scanner:
    # Recuperer les colonnes codcde et datcde
    commande_id = data.get(b'commande:code', b'').decode()
    annee = int(data.get(b'commande:annee'))

    # Verifier que les deux informations existent
    if not commande_id or not annee:
        continue

    if 2010 <= annee <= 2015:
        # Regrouper par code commande : on ne conserve qu'une seule entree par commande
        if commande_id not in commandes_uniques:
            commandes_uniques[commande_id] = annee

connection.close()

# Compter le nombre de commandes par annee
commandes_par_annee = {}

for annee in commandes_uniques.values():
    commandes_par_annee[annee] = commandes_par_annee.get(annee, 0) + 1

# Affichage du resultat
print("Nombre total de commandes effectuees entre 2010 et 2015 (uniques, regroupees par 'codcde'):")
for annee in range(2010, 2016):
    print("Annee {} : {} commandes".format(annee, commandes_par_annee.get(annee, 0)))

# Création du barplot
plt.figure(figsize=(8, 5))
plt.bar(commandes_par_annee.keys(), commandes_par_annee.values(), color='skyblue')

# Ajout des labels et titre
plt.xlabel("Année")
plt.ylabel("Nombre de commandes")
plt.title("Nombre total de commandes uniques entre 2010 et 2015")
plt.xticks(list(commandes_par_annee.keys()))

plt.savefig('/datavolume1/commandes_2010_2015.pdf')

