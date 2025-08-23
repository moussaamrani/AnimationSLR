import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données
data = pd.read_csv('CORPUS-Final.csv')

# Récupération de la colonne "Orientation"
target = data["Orientation"]

# Comptage des catégories
Nboffline = sum("INDUS" in str(t).upper() for t in target)
Nbonline = sum("ACA" in str(t).upper() for t in target)

# Calcul des pourcentages
TotalPub = Nboffline + Nbonline
rateoffline = Nboffline / TotalPub * 100
rateonline = Nbonline / TotalPub * 100

# Préparer les données pour le graphique
ratioDist = [rateonline, rateoffline]
my_labels = ['Academic', 'Industrial']
my_colors = ['lightblue', 'silver']
my_explode = (0, 0)

# Création du graphique
plt.figure(figsize=(6, 6))  # Ajuste la taille globale
plt.pie(
    ratioDist,
    labels=my_labels,
    textprops={'fontsize': 25},
    autopct='%1.1f%%',
    startangle=180,
    colors=my_colors,
    explode=my_explode,
    wedgeprops={"edgecolor": "black", 'linewidth': 1.7}
)

# Pas de titre, proportions égales
plt.title('')
plt.axis('equal')

# Sauvegarde du PDF sans marges blanches
plt.savefig(
    "Distribution-over-Orientation.pdf",
    dpi=600,
    bbox_inches='tight',  # Supprime les marges blanches
    pad_inches=0          # Élimine l'espace résiduel
)

plt.show()
