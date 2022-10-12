# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from fileExercise import factoriel,approxEpsilone
from solverSudokuMe import *
from SortFile import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi')  # Press Ctrl+F8 to toggle the breakpoint.

    #print(approxEpsilone(90))
    #listNumber = [-1,2,4,3,9,6,-1,-1,-1]
    #puzzle = solverPuzzle(listNumber)
    #print(puzzle)

    pathFrom = r"C:\Users\cobcouli\Downloads"
    pathTo = r"C:\Users\cobcouli\coulibayFolder"
    copyingFilebyYear(pathFrom,pathTo)
    #filelist = listOfFile(pathFrom)
    #print(getMetaDataOfListFile(pathFrom,filelist))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/







