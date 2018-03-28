import hou
import shutil
import os
class ClearFile:
    def __init__(self):
        pass
        self.pathArr = []
        self.markPath = []
        self.severPath = []
    def getPathArr(self,rootNode):         
        if rootNode.children() and rootNode.isLockedHDA() == 0:
            for childNode in rootNode.children():
                NodeColor =  hou.Color(0,0,0)
                if childNode.type().name() == "catche_tool_1.0.1" and childNode.color() ==NodeColor:
                    tag =childNode.parm("trange").eval()
                    tempPath = ""
                    if tag == 0:
                        tempPath = childNode.parm("out_put_file0").eval()
                    else:    
                    
                        tempPath =childNode.parm("out_put_file1").eval()
                    str1= "/"
                    nameString = tempPath.split("/")[-1].split(".")[0]
                    tempPath = tempPath.split("/")[0:-1]
                    
                    tempPath = str1.join(tempPath)+"####"+nameString
                    
                    self.pathArr.append(tempPath)
                else:
                    self.getPathArr(childNode)
        else:
            pass
    def getmakPath(self,rootNode):
        self.getPathArr(rootNode)
        
        for pathString in self.pathArr:
            rootPath = pathString.split("####")[0]
            filePathName = pathString.split("####")[1]
            try:
                paths = os.listdir(rootPath)
                for path in paths:
                    if path.split(".")[0] == filePathName:
                        self.markPath.append(  (rootPath+"/"+path).split("sim")[-1])
            except:
                pass
    def deleteSimVPath(self):
        # deleteMainLayer
        
        verNames =[]
        for markPath in self.markPath:
            
            verNames.append( markPath.split("/")[1])
        verNames = list(set(verNames))
        
        
        
        simPrijectName  =self.pathArr[0].split("####")[0].split("sim")[0]
        simPrijectPath = simPrijectName+"sim"
        proVer = []
        try:
            pas = os.listdir(simPrijectPath)
            for path in pas:
                proVer.append(path)
        except:
            pass
        
        ret_list = list(set(verNames)^set(proVer)) 
        for vPath in ret_list:
            print "Delete folder :",simPrijectPath+"/"+vPath    
            shutil.rmtree(simPrijectPath+"/"+vPath,1)
        
            
    def getSimAllFilePath(self,path):
        if os.path.isdir(path):
            trees = os.listdir(path)
            for tree in trees:
                self.getSimAllFilePath(path+"/"+tree)
        elif   os.path.isfile(path):
        
            self.severPath.append( path.split(".")[0])
        else:
            pass
    def getsetArray(self):
        self.severPath  = list(set(self.severPath))
        self.severPathTemp = [] 
        for path in   self.severPath  :
            str1 = "/"
            allList = path.split("/")
            lastFileName =  allList[-1] 
            allList =allList[:-1]
            
            newPath = str1.join(allList)
            newPath =newPath+ "####"+ lastFileName
            self.severPathTemp.append(newPath)
        self.severPath = self.severPathTemp    
    
    def getDeletePath(self):
        temparr =[]
        temparr = self.severPath
        a= -1
        for sever in self.severPath:
            a+=1
            for catch in self.pathArr:
                if sever == catch:
                    temparr[a] =""
                    pass
                else:    
                    pass
                    
        retarr = ""        
        
        for finalPath in temparr:
            if finalPath != "":
                rootPath =  finalPath.split("####")[0]
                fileName = finalPath.split("####")[1]
                if  os.path.isdir(rootPath):
                    files = os.listdir(rootPath)
                    for file in files:
                        if file.split(".")[0] == fileName:
                            try:
                                os.remove(rootPath+"/"+file)
                                retarr = rootPath+"/"+fileName
                            except:
                                "delete error"
                    print "Delete file :",retarr                   
            
    def run(self):
        
        rootNode =hou.node("/obj/")
        self.getmakPath(rootNode)
        
        self.deleteSimVPath()
        
        
        
        
        simPrijectName  =self.pathArr[0].split("####")[0].split("sim")[0]
        simPrijectPath = simPrijectName+"sim"
        self.getSimAllFilePath(simPrijectPath)
        self.getsetArray()        
        
        
       
        self.getDeletePath()
        
            
        
        