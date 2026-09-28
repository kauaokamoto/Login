import json
import os


FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(FOLDER, "dataFile.json")


def loadFile():
    if os.path.exists(FILE): 
        with open(FILE,"r",encoding="utf-8") as f:
            return json.load(f)

    initialData = [ {"num": 0, "name": ["kaua", "kauã"], "cara": "sigma", "senha": "2010"}]
    saveFile(initialData)
    return initialData

def saveFile(newArray):
    with open(FILE,"w",encoding="utf-8") as f:
        json.dump(newArray,f,indent=4,ensure_ascii=False)

nameArray = loadFile()
        