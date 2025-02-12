# D08b_Projet_Big_Data_Et_BI
D08b_Projet_Big_Data_Et_BI

A partir du fichier nettoyage.py, les données de dataw_fro3 sont nettoyées en :
	- retirant les accents
	- remplaçant les valeurs nul par 0
	- supprimant les lignes dupliquées
	- standardisant les formats de date
	- extrayant les numéros de département
Un nouveau fichier CSV est généré (data.csv et data_100.csv)

Dans les différents dossiers lots se trouvent les scripts à exécuter pour répondre aux différents lots.
Pour le lot 1, il faut lancer le job.sh sur hbase comme pour le lot 2.
L'introduction sur happybase pour le lot 3 se fait via le job.sh en suivant le mapper et le reducer. Pour la suite du lot 3, il faut exécuter les fichiers "code_lot3_1.py", "code_lot3_2.py" et "code_lot3_3.py" permettant de fournir les fichiers demandés aux formats csv, pdf et excel.
Les résultats du Lot 4 se trouve dans le fichier Power BI.


Consignes :

LOT 1 :
1. Filtrer les données selon les critères suivants :
	• Entre 2006 et 2010,
	• Avec uniquement les départements : 53, 61 et 28
2. A partir du point 1 : Ressortir dans un tableau des 100 meilleures commandes avec la ville, la somme des quantités des articles et la valeur de « timbrecde »
	La notion de meilleure commande :
		(1) La somme des quantités la plus grande
		(2) Le plus grand nombre de « timbrecde »
3. Exporter le résultat dans un fichier Excel.

LOT 2 :
1. Filtrer les données selon les critères suivants :
	• Entre 2011 et 2016
	• Avec uniquement les départements : 22, 49 et 53
2. A partir du point 1 : Ressortir de façon aléatoire de 5% des 100 meilleures commandes avec la ville, la somme des quantités des articles sans « timbrecli » (le timbrecli non renseigné ou à 0)
+ Moyenne des quantités de chaque commande
Avoir un PDF avec un graphe (PIE) (secteur par Ville)

LOT 3 :
1. Mettre en place une base NoSQL HBASE pour stocker le contenu du fichier CSV
2. Interroger la base de données NoSQL HBASE avec des scripts python.
	· La meilleure commande de Nantes de l’année 2020.
	· Le nombre total de commandes effectuées entre 2010 et 2015, réparties par année
	· Le nom, le prénom, le nombre de commande et la somme des quantités d’objets du client qui a eu le plus de frais de timbrecde.
3. Créer un programme python (avec Panda) pour créer des graphes en pdf et des tableaux Excel et csv devotre importation dans HBase : 
	 Question 2 partie 1 du lot 3 en csv 
	 Question 2 partie 2 du lot 3 en barplot matplotib exporté en pdf 
	 Question 2 partie 3 du lot 3 en excel

LOT 4 :
Mettre en oeuvre des dashboards PowerBI récupérant les données depuis HBase.
	· Pour répondre au Lot 1 et Lot 2 au niveau des résultats avec les graphes
	· Vous avez carte blanche pour créer d’autres graphes, d’autres types de requêtes.
	· Mise en place d’un Dashboard interactif




Rappel de lancement Hadoop :
./start_docker_digi.sh
./lance_srv_slaves.sh
./bash_hadoop_master.sh

./start-hadoop.sh
start-hbase.sh
./service_hbase_thrift.sh
./hbase_odbc_rest.sh