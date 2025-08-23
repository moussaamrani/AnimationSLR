import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données
data = pd.read_csv('CORPUS-Final.csv')

# Récupération de la colonne "Venue Type"
target = data["Venue Type"]

# Comptage des types de publication
NbConf = sum("CONF" in str(t).upper() for t in target)
NbWSHOP = sum("WSHOP" in str(t).upper() for t in target)
NbJOUR = sum("JOUR" in str(t).upper() for t in target)

# Vérification des valeurs
print(f"Conférences : {NbConf}")
print(f"Workshops : {NbWSHOP}")
print(f"Journaux : {NbJOUR}")

# Calcul des pourcentages
TotalPub = NbConf + NbWSHOP + NbJOUR
rateCONF = NbConf / TotalPub * 100
rateWSHOP = NbWSHOP / TotalPub * 100
rateJOUR = NbJOUR / TotalPub * 100

# Vérification des taux
print(rateCONF, rateWSHOP, rateJOUR)
print("Somme des pourcentages :", rateCONF + rateWSHOP + rateJOUR)

# Préparation des données pour le graphique
Tasks = [rateCONF, rateWSHOP, rateJOUR]
my_labels = ['Conference', 'Workshop', 'Journal']
my_colors = ['#ea8b3e', '#8b3eea', '#ffcc00']
my_explode = (0, 0, 0)

# Création du graphique
plt.figure(figsize=(6, 6))  # Taille uniforme
plt.pie(
    Tasks,
    labels=my_labels,
    textprops={'fontsize': 18},
    autopct='%1.1f%%',
    startangle=180,
    colors=my_colors,
    explode=my_explode,
    wedgeprops={"edgecolor": "black", 'linewidth': 1.7}
)

# Supprimer le titre et rendre les proportions égales
plt.title('')
plt.axis('equal')

# Sauvegarde du PDF sans marges blanches
plt.savefig(
    "Distribution-over-venue-type.pdf",
    dpi=600,
    bbox_inches='tight',  # Supprime les marges blanches
    pad_inches=0          # Élimine les espaces résiduels
)

plt.show()
