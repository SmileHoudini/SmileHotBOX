import os
class ImportFbx:
    def __init__(self):
       
        hipFilePath =hou.hipFile.path()
        sp= hipFilePath.split("/")
        
        
        self.fbxFilePath1 ="X:"+"/"+sp[1]+"/"+sp[2]+"/"+sp[3]+"/"+"mm"
        self.allFilePath = os.listdir(self.fbxFilePath1)
        allFbxPath =[]
        for file in self.allFilePath:
            if file.split(".")[-1] =="fbx" or file.split(".")[-1] =="abc":
                allFbxPath.append(file.split(".")[0])
        allFbxPath.sort()
        
        self.check=0
        try:
            
            self.fbxFilePath = self.fbxFilePath1 +"/"+allFbxPath[-1]+".abc"
            self.lastName =allFbxPath[-1]
            
            for a in self.allFilePath:
               
                
                if a ==self.fbxFilePath.split("/mm/")[-1]:
                    
                    self.check=1
            if self.check==1:
                pass
            else:
                node =hou.node("/obj/sasdsdsdssssssss")
                node.setName("sas")
                    
        except:
            pass
            self.fbxFilePath = self.fbxFilePath1 +"/"+allFbxPath[-1]+".fbx"
            self.check=2
    def run(self):
        if self.check ==1:
            node = hou.node('/obj/')
            abcNode = node.createNode("alembicarchive")
            abcNode.parm("fileName").set(self.fbxFilePath)
            
            abcNode.setName(self.lastName+"_index_0",1)
            abcNode.parm("buildHierarchy").pressButton()
            
            
        else:
            
            hou.hipFile.importFBX(self.fbxFilePath)