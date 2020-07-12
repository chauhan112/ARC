from IPython.display import Markdown
from MarkdownToolsDB import MarkdownToolsDB
from Path import Path
from ListDB import ListDB
import os
from Utils import Utils, DescribeUtils
class Data:
    def __init__(self, path):
        self.projectPath = path
        self.trainFiles = Path.filesWithExtension("json", Path.joinPath(self.projectPath, "training"))
        self.testFiles = Path.filesWithExtension("json", Path.joinPath(self.projectPath, "test"))
        self.evaFiles = Path.filesWithExtension("json", Path.joinPath(self.projectPath, "evaluation"))
        
    def training(self, number = 10, random = False):
        if(random):
            return Utils.randomNrOfFiles(self.trainFiles, number)
        return self.trainFiles[:number]       
    
    def test(self, number = 10, random = False):
        if(random):
            return Utils.randomNrOfFiles(self.testFiles, number)
        return self.testFiles[:number]  
    
    def evaluation(self, number = 10, random = False):
        if(random):
            return Utils.randomNrOfFiles(self.evaFiles, number)
        return self.evaFiles[:number]  
    
    def describe(self):
        proto = "## <font face='comic sans ms' color ='SeaGreen'>{}</font>\n"
        # ARC project
        st = proto.format("ARC project")
        proto = "#" + proto
        # files
        st += proto.format("files:")
        st += DescribeUtils.getList() + "\n"*2
        # datasets
        st += proto.format("datasets:")
        st += DescribeUtils.dataSet()
        return Markdown(st)

    def plot(self, datas):
        if(type(datas) is not list):
            datas = [datas]
        for task in datas:
            Utils.plot_task(task)
        
    def getAllFiles(self):
        return self.trainFiles + self.testFiles + self.evaFiles