import sys
import happybase

# Configurer la connexion a  HBase
connection = happybase.Connection('127.0.0.1', 9090)
connection.open()

# Nom de la table HBase
hbase_table_name = 'data_digicheese'

# Supprimer la table HBase si elle existe déja
try:
    connection.disable_table(hbase_table_name)
    connection.delete_table(hbase_table_name)
except Exception:
    pass

# Creer une table HBase avec des column families
data = {
    'client': dict(),
    'commande': dict()
}
connection.create_table(hbase_table_name, data)
table = connection.table(hbase_table_name)

# Boucler sur les données
for index, line in enumerate(sys.stdin):
    nomcli, prenomcli, codcde, ville, datcde, annee, timbrecde, qte, codcli, departement, timbrecli, codobj, libobj, cpcli = line.split(';')
    index = str(index).encode()
    data = {
            b'client:nom': nomcli.encode(),
            b'client:prenom': prenomcli.encode(),
            b'client:ville': ville.encode(),
            b'client:departement': departement.encode(),
            b'client:codcli': codcli.encode(),
            b'commande:code': codcde.encode(),
            b'commande:quantite': qte.encode(),
            b'commande:date' : datcde.encode(),
            b'commande:annee' : annee.encode(),
            b'commande:timbrecde' : timbrecde.encode(),
            b'commande:timbrecli' : timbrecli.encode(),
            b'commande:codobj' : codobj.encode(),
            b'commande:libobj' : libobj.encode()
        }

    # Inserer les données dans HBase
    table.put(index, data)

connection.close()
~
