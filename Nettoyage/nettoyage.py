import unicodedata
import pandas as pd 

def remove_accents(text):
    if isinstance(text, str) :
        return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')

df = pd.read_csv("dataw_fro03.csv")

# Suppression des accents
for col in df.columns:
    if df[col].dtype == 'object' :
        df[col] = df[col].apply(remove_accents)

# Remplace les valeurs nul par 0
df.fillna(0, inplace = True)

# Suppression des lignes dupliquées
df.drop_duplicates(inplace=True)

# Standardisation du format des dates 
df['datcde'] = pd.to_datetime(df['datcde'], errors='coerce')

# Extraction des numéros de département
df['departement'] = df['cpcli'].astype(str).str[:2]

# Génération nouveau CSV
df.to_csv("data.csv", index=False, encoding='utf-8')

