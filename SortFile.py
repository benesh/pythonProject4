import os
from datetime import datetime
from shutil import copy,Error


def copyingFilebyYear(pathFrom, pathTo):
    # lister lES fichier dans un dossier
    listfile = listOfFile(pathFrom)
    # List of tuple of tab,stat
    listTupleMetadataFile = getMetaDataOfListFile(pathFrom, listfile)
    # liste des differente mois des fichiers de manière unique
    listOfMouthUnique = uniqueValues(listeOfMouth(listTupleMetadataFile))
    #creating folder from listOFMounth
    createFolders(pathTo, listOfMouthUnique)
    for elem in listTupleMetadataFile:
        copyfile(makePath(pathFrom,elem[0]),makePath(pathTo,elem[1].month))



def copyfile(pathTo,destination):
    try:
        copy(pathTo,destination)
    except OSError as err:
        print(err)


def makePath(pathPrincipal,suffix):
    return pathPrincipal + "\\" + str(suffix)


def createFolders(parentFolder, folders):
    for folder in folders:
        try :
            os.makedirs( makePath(parentFolder,folder))
        except OSError as err:
            print(err)

def listOfFile(path):
    return os.listdir(path)


def listeOfMouth(tupleOfMetaData):
    listOfMouth = []
    for elem in tupleOfMetaData:
        listOfMouth.append(elem[1].month)
    return listOfMouth


def uniqueValues(listOfMouth):
    listUniqueValues = []
    for elem in listOfMouth:
        if elem not in listUniqueValues:
            listUniqueValues.append(elem)
    return listUniqueValues


def getMetaDataOfListFile(path, listFiles):
    tupleOfMetaData = []
    for file in listFiles:
        tempTuple = (file, getMetaDataTime(path, file))
        tupleOfMetaData.append(tempTuple)
    return tupleOfMetaData


def getMetaDataTime(path, file):
    # make an asbulute path for the file
    completePath = makePath(path, file)
    return datetime.fromtimestamp(os.stat(completePath).st_mtime)