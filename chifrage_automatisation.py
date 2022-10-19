import xlrd as xl
import openpyxl as op
import pandas as pd



def chiffrage():
    path = r"C:\Users\cobcouli\OneDrive - Capgemini\Documents\Python_ressources\Feuille de calcul dans Exercice python_Jouer_avec_des_donnees.xlsx"
    pathe = r"C:\Users\cobcouli\OneDrive - Capgemini\Documents\Python_ressources\Feuille de calcul dans Exercice python_Jouer_avec_des_donnees.xlsx"
    df = pd.read_excel (path)

    #Pour chaque numero de scenario, donne le nombre de cas de test associé
    """ grouping the scenarios """
    scenario = df.groupby('Scenario')
    scenarioSorted = scenario.nunique()

    for scena, restscena in scenario:
        print(scena)
        print(nombre_de_row(restscena))
        print("############################")
        print(restscena)











def nombre_de_row(df):
    return df.shape

