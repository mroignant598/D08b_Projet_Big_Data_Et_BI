import sys
import pandas as pd  

# Initialisation des variables
data = []
current_codcde = None
current_ville = None
somme_quantite = 0
somme_timbrecde = 0

# Lecture des donnees depuis l'entree standard
for line in sys.stdin:
    # Extraction des champs a partir de la ligne d'entree
    codcde, ville, departement, datcde, timbrecde, qte = line.split(";")
    
    try:
        # Conversion des valeurs numeriques
        qte = float(qte)
        timbrecde = float(timbrecde)
    except ValueError:
        # Si une conversion echoue, on ignore la ligne
        continue
    
    # Si la commande actuelle est la meme que la precedente, on cumule les valeurs "qte" et "timbrecde"
    if current_codcde == codcde:
        somme_quantite += qte
        somme_timbrecde += timbrecde
        current_ville = ville
    else :
        # Si on change de commande, on stocke les valeurs precedentes et on reinitialise
        if current_codcde:
            data.append((current_codcde, current_ville, somme_quantite, somme_timbrecde))
        
        # Reinitialisation des valeurs pour la nouvelle commande
        current_codcde = codcde
        somme_quantite = qte
        somme_timbrecde = timbrecde
        current_ville = ville
 
# Ajout de la derniere commande traitee            
if current_codcde:
    data.append((current_codcde, current_ville, somme_quantite, somme_timbrecde))

# Creation d'un DataFrame a partir des donnees collectees
df = pd.DataFrame(data, columns=["codcde", "ville", "somme_quantite", "somme_timbrecde"])

# Tri du DataFrame sur la somme des quantites et la somme des timbres de commande
df_trie = df.sort_values(by=['somme_quantite', 'somme_timbrecde'], ascending=[False, False]).head(100)

# Exportation des résultats tries dans un fichier Excel
df_trie.to_excel("/datavolume1/Resultats_lot1.xlsx")