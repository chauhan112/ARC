import random
from MarkdownToolsDB import MarkdownToolsDB
from Path import Path
from ListDB import ListDB
import os
import json
from visualization.Plot import Plot
class Utils:
    def plot(file):
        if(type(file) == str):
            file = Utils.read(file)
        Plot(file)

    def read(filePath):
        with open(filePath, 'r') as f:
            task = json.load(f)
        return task
    def randomNrOfFiles(files, no):
        return [random.choice(files) for i in range(no)]

class DescribeUtils:
    def files(ext, paths = [r"..\..\..\5. may\activities\Abstract and reasoning", '.']):
        files = []
        for p in paths:
            files += ListDB.filterOutResult([".ipynb_checkpoints"],Path.filesWithExtension(ext, p))
        return files

    def getList(*toList):
        if(len(toList) == 0):
            toList = ['ipynb', 'py', 'html']
        p = MarkdownToolsDB.list2htmlOrderedList
        k = p(toList, False)
        for ext in toList:
            k = k.replace(f"<li>{ext}</li>", f"<li>{ext} files:{p(Path.basename(DescribeUtils.files(ext)))}</li>")
        return k
    
    def dataSet(path = r"..\..\..\5. may\activities\Abstract and reasoning\abstraction-and-reasoning-challenge"):
        vals = ['evaluation', 'test', 'training']
        valStr = [k + " : " + str(len(os.listdir(Path.joinPath(path, k)))) for k in vals]
        return MarkdownToolsDB.list2htmlOrderedList(valStr)
    
    def getAllScriptFiles(paths = [r"..\..\..\5. may\activities\Abstract and reasoning", '.']):
        k = ['ipynb', 'py', 'html']
        files = []
        for ext in k:
            files += DescribeUtils.files(ext, paths)
        return files