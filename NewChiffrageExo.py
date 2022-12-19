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
tabWithScenarioAndCas=[]
tabWithNumscenario=[]
for row in sheet:
   if (row[2].value,row[3].value) not in tabWithScenarioAndCas :
      temptuple = (row[2].value,row[3].value)
      tabWithScenarioAndCas.append(temptuple)
   if row[2].value not in tabWithNumscenario :
      tabWithNumscenario.append(row[2].value)

tabWithScenarioAndCas.remove((None,None))
tabWithScenarioAndCas.remove(('Scenario', 'Cas de test'))
tabWithNumscenario.remove('Scenario')
tabWithNumscenario.remove((None))

sheetQuestion1 = book.create_sheet('Question_1')
sheetQuestion1.append(['Nombre de cas de test associé pour chaque scénario'])
sheetQuestion1.append(['Numéro de Scenario','Nombre de cas de test'])
for row in sheet:
   pass





print(tabWithScenarioAndCas)
print (tabWithNumscenario)


book.save('tempfile.xlsx')



""" Réfléchir a une méthode pour écrire directement sur une feuille en meme temps de prendre l'info"""

