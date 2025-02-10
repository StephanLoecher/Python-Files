from typing import Iterable

def saveFile(path, data: str):
    saveFile = open(path, "w+")
    try:
        saveFile.write(data)
        saveFile.close()
    except:
        saveFile.close()

def saveLinesToFile(path, data: Iterable[str]):
    saveFile = open(path, "w+")
    try:
        saveFile.writelines(data)
        saveFile.close()
    except:
        saveFile.close()

def readFile(path):
    saveFile = open(path, "r")
    try:
        textFromFile = saveFile.read()
        saveFile.close()
        return textFromFile
    except:
        saveFile.close()

def readLinesFromFile(path):
    saveFile = open(path, "r")
    try:
        textFromFile = saveFile.readlines()
        saveFile.close()
        return textFromFile
    except:
        saveFile.close()

