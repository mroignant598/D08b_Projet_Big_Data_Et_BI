import happybase
import pandas as pd 

# Configurer la connexion à HBase
connection = happybase.Connection('127.0.0.1', 9090) 
connection.open()

# Nom de la table HBase
hbase_table_name = 'data_digicheese'

# Création des variables 
nantes_commande = []
current_codcde = None
somme_qte = 0
somme_timbrecde = 0

# Connexion a la table
table = connection.table(hbase_table_name)

# Tri selon l'annee 2020, introduction des valeurs "current_codcde", "somme_qte" et "somme_timbre" dans une liste "nantes_commandes" 
for key, data in table.scan(filter = "SingleColumnValueFilter('client', 'ville', =, 'substring:Nantes')"):
    commande_date = data.get(b'commande:date', b'0000-00-00').decode()
    if commande_date[:4] == "2020":
        commande_id = data.get(b'commande:code', b'').decode()
        qte_cde = float(data.get(b'commande:quantite', b'0.0').decode())
        timbrecde_cde = float(data.get(b'commande:timbrecde', b'0.0').decode())

        # Si la commande actuelle est la meme que la precedente, on cumule les valeurs
        if current_codcde == commande_id:
            somme_qte += qte_cde
            somme_timbrecde += timbrecde_cde
        else :
            # Si on change de commande, on stocke les valeurs precedentes et on reinitialise
            if current_codcde:    
                nantes_commande.append((current_codcde, somme_qte, somme_timbrecde))
            
            # Reinitialisation des valeurs pour la nouvelle commande    
            current_codcde = commande_id
            somme_timbrecde = timbrecde_cde
            somme_qte = qte_cde

# Ajout de la derniere commande traitee            
if current_codcde:    
    nantes_commande.append((current_codcde, somme_qte, somme_timbrecde))

# Creation d'un DataFrame a partir des donnees collectees    
df_nantes = pd.DataFrame(nantes_commande, columns=["ID_commande", "Somme_quantite", "Somme_timbrecde"])

# Tri du DataFrame sur la somme des quantites et la somme des timbrecde par commande
df_nantes_tri = df_nantes.sort_values(by=['Somme_quantite', 'Somme_timbrecde'], ascending=[False, False]).head(1)

# Export du fichier au format csv
df_nantes_tri.to_csv('/datavolume1/meilleure_commande_Nantes_en_2000.csv', index=False)

# Fermeture de la connexion                
connection.close()


