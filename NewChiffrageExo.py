""" ce code à pour but de faire les stats sur l'excell avec une nouvelle approche
  - donc la première approche est d'écrire directement les résultats dans l'excell
  et ne pas conservé dans une varibale """

import openpyxl as op
from chiffrage_file_with_xlrd import getcolumn

path = r"C:\Users\cobcouli\OneDrive - Capgemini\Documents\Python_ressources\Feuille de calcul dans Exercice python_Jouer_avec_des_donnees.xlsx"

book = op.load_workbook(path)
sheet = book['Gestion_des_Rapporteurs']
print(sheet)
"""delete the empty rows """

"""1) for each scenario get the number of case it have"""
tabtuple=[]
tabscenarioUnique=[]
for row in sheet:
   if (row[2].value,row[3].value) not in tabtuple :
      temptuple = (row[2].value,row[3].value)
      tabtuple.append(temptuple)
   if row[2].value not in tabscenarioUnique :
      tabscenarioUnique.append(row[2].value)

for tuple in tabtuple :
   if tuple[0]:
      pass

print(tabtuple)


def countTupleIndex1(tab1tuple):
   for item in tab1tuple:
      pass


