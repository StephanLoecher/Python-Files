import os
from typing import Iterable

path = os.path.join("./save.txt")

def saveFile(data: str):
    try:
        saveFile = open(path, "a+")
        saveFile.write(data)
        saveFile.close()
    except:
        saveFile.close()

def saveLinesToFile(data: Iterable[str]):
    try:
        saveFile = open(path, "a+")
        saveFile.writelines(data)
        saveFile.close()
    except:
        saveFile.close()

def readFile():
    try:
        saveFile = open(path, "r")
        textFromFile = saveFile.read()
        saveFile.close()
        return textFromFile
    except:
        saveFile.close()

def readLinesFromFile():
    try:
        saveFile = open(path, "r")
        textFromFile = saveFile.readlines()
        saveFile.close()
        return textFromFile
    except:
        saveFile.close()

