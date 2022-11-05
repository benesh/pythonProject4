import openpyxl as op
from chiffrage_file_with_xlrd import getcolumn

path = r"C:\Users\cobcouli\OneDrive - Capgemini\Documents\Python_ressources\Feuille de calcul dans Exercice python_Jouer_avec_des_donnees.xlsx"


def run():
    book  = op.load_workbook(path)
    sheet = book['Gestion_des_Rapporteurs']
    print(sheet)

def getNumberOfCase(file,NameColum):
    #get the colum of lettre or position
    pass

def getColumPosition(column,sheet):
    row = sheet[1]
    for cell in row:
        if cell == column:
            return cell.column

def nbreCasaasocieAuscenario(sheet,colunmScenario,columnCasdeTest):
    pass

