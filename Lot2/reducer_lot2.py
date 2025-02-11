import sys
import pandas as pd  
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Initialisation des variables
data = []
current_codcde = None
current_ville = None
somme_quantite = 0
count = 1

# Lecture des donnees depuis l'entree standard
for line in sys.stdin:
    # Extraction des champs a partir de la ligne d'entree
    codcde, ville, departement, datcde, timbrecli, qte, points = line.split(";")
    
    try:
        # Conversion de la quantite en nombre flottant
        qte = float(qte)
        
    except ValueError:
        # Si une conversion echoue, on ignore la ligne
        continue
    
    # Si la commande actuelle est la meme que la precedente, on cumule les valeurs
    if current_codcde == codcde:
        somme_quantite += qte
        count += 1
        current_ville = ville
    else :
        # Si on change de commande, on stocke les valeurs precedentes et on reinitialise
        if current_codcde:
            data.append((current_codcde, current_ville, somme_quantite, somme_quantite/count))
        
        # Reinitialisation des valeurs pour la nouvelle commande
        current_codcde = codcde
        somme_quantite = qte
        count = 1
        current_ville = ville
            
# Ajout de la derniere commande traitee
if current_codcde:
    data.append((current_codcde, current_ville, somme_quantite, somme_quantite/count))

# Creation d'un DataFrame a partir des donnees collectees
df = pd.DataFrame(data, columns=["codcde", "ville", "somme_quantite", "moyenne"])

# Tri du DataFrame sur la somme des quantites et la moyenne des quantites par commande
df_trie = df.sort_values(by=['somme_quantite', 'moyenne'], ascending=[False, False]).head(100)

# Sélection aleatoire de 5 commandes parmi les 100 meilleures
df_top5 = df.sample(n=5)

# Creation d'un diagramme circulaire (pie chart) pour representer ces 5 commandes
plt.figure()
plt.pie(df_top5['somme_quantite'], labels=df_top5['ville'], autopct='%1.1f%%', startangle=140)
plt.title("Top 5 aléatoire des 100 meilleures commandes")

# creation d'un fichier PDF contenant le graphique
with PdfPages('/datavolume1/Top5_aleatoire.pdf') as pdf :
    pdf.savefig() # Sauvegarde du graphique dans le fichier PDF


