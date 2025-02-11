import happybase
import pandas as pd 

# Configurer la connexion à HBase
connection = happybase.Connection('127.0.0.1', 9090) 
connection.open()

# Nom de la table HBase
hbase_table_name = 'data_digicheese'

# Initialisation des variables
commande_client = []
current_codcde = None
somme_qte = 0
somme_timbrecde = 0
nombre_commande = 0
current_nom = None
current_prenom = None
current_codcli = None

# Connexion a la table
table = connection.table(hbase_table_name)

for key, data in table.scan():
    # Extraction des valeurs des colonnes de HBase
    nom = data.get(b'client:nom', b'').decode()
    prenom = data.get(b'client:prenom', b'').decode()
    commande_id = data.get(b'commande:code', b'').decode()
    qte_cde = float(data.get(b'commande:quantite', b'0.0').decode())
    timbrecde_cde = float(data.get(b'commande:timbrecde', b'0.0').decode())
    code_cli = data.get(b'client:codcli', b'').decode()
    
    # Si la commande actuelle est la meme que la precedente, on cumule les valeurs
    if current_codcde == commande_id:
        somme_qte += qte_cde
        somme_timbrecde += timbrecde_cde
        current_nom = nom
        current_prenom = prenom
        nombre_commande += 1 
        current_codcli = code_cli
    else :
        # Si on change de commande, on stocke les valeurs precedentes et on reinitialise
        if current_codcde:    
            commande_client.append((current_codcli, current_nom, current_prenom, nombre_commande, somme_qte, somme_timbrecde))

        # Reinitialisation des valeurs pour la nouvelle commande 
        current_codcde = commande_id
        somme_qte = qte_cde
        somme_timbrecde = timbrecde_cde
        current_nom = nom
        current_prenom = prenom
        nombre_commande = 1 
        current_codcli = code_cli
            
# Ajout de la derniere commande traitee 
if current_codcde:    
    commande_client.append((current_codcli, current_nom, current_prenom, nombre_commande, somme_qte, somme_timbrecde))

# Creation d'un DataFrame a partir des donnees collectees
df = pd.DataFrame(commande_client, columns=["ID_client", "Nom", "Prenom", "Nombre_commande", "Somme_quantite", "Somme_timbrecde"])

# Agreger les données par ID_client
df_grouped = df.groupby(by=["ID_client", "Nom", "Prenom"]).agg(
    {"Nombre_commande": "sum", "Somme_quantite": "sum", "Somme_timbrecde": "sum"}
).reset_index()

# Trier par la colonne "Somme_timbrecde" et afficher le top 1 client
df_top_client = df_grouped.sort_values(by="Somme_timbrecde", ascending=False).head(1)

# Export du fichier au format excel
df.to_excel('/datavolume1/commande_client.xlsx')
df_grouped.to_excel('/datavolume1/classemenet_clients.xlsx')
df_top_client.to_excel('/datavolume1/meilleur_client.xlsx')


# Fermeture de la connexion 
connection.close()