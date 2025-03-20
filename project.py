# Importation des bibliothèques nécessaires
import pandas as pd
import os
python -m venv env
# Obtenir le chemin du répertoire actuel
current_directory = os.getcwd()  # Répertoire de travail actuel
nom_fichier = "p2-arbres-fr.csv"  # Nom du fichier
chemin_fichier = os.path.join(current_directory, nom_fichier)  # Correction de "ccurrent_directory"

# Vérifier si le fichier existe avant de le charger
if os.path.exists(chemin_fichier):
    # Charger les données depuis un fichier CSV avec le séparateur ";"
    df = pd.read_csv(chemin_fichier, sep=";")

    # Afficher des informations générales sur le DataFrame
    print("Informations sur la structure du DataFrame :")
    df.info()  # Affiche le nombre de colonnes, de lignes et les types de données

    # Afficher les premières lignes du DataFrame pour un aperçu
    print("\nAperçu des premières lignes du DataFrame :")
    print(df.head())  # Affiche les 5 premières lignes par défaut

    # Vérification des types de données de chaque colonne
    print("\nTypes de données des colonnes :")
    print(df.dtypes)  # Donne les types de données pour chaque colonne

    # Analyse des valeurs manquantes
    print("\nAnalyse des valeurs manquantes :")

    # Calculer le nombre de valeurs manquantes par colonne
    valeurs_manquantes = df.isnull().sum()
    print("\nNombre de valeurs manquantes par colonne :")
    print(valeurs_manquantes)

    # Calculer le pourcentage de valeurs manquantes par colonne
    pourcentage_manquantes = (df.isnull().sum() / len(df)) * 100
    print("\nPourcentage de valeurs manquantes par colonne :")
    print(pourcentage_manquantes)

    # Identifier les lignes contenant des valeurs manquantes
    lignes_manquantes = df[df.isnull().any(axis=1)]
    print("\nLignes contenant des valeurs manquantes :")
    print(lignes_manquantes)

    # Identifier les colonnes avec des valeurs manquantes
    colonnes_manquantes = df.columns[df.isnull().any()]
    print("\nColonnes avec des valeurs manquantes :")
    print(colonnes_manquantes)
else:
    print(f"Erreur : le fichier '{nom_fichier}' est introuvable dans le répertoire actuel.")

