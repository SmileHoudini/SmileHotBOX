import hou
import os
import subprocess
class OpenInNk:
    def __init__(self):
        self.nkfilePath     = ""
        self.nkfondPath     =""  
        self.startFrame     = 1
        self.endFrame       = 240
        self.camSize        = "2048 1152"
        self.nodeStartPos   = -7
        self.nodeEndPos     = -105
        self.picPathArry    = []
        self.sourceRoot = ""
        dataPath = os.getenv('SMILEHOTBOX')+"\\data\\nukstart.data"
        self.nkdataStart = dataPath
        self.setInit()
    
    def setInit(self):
        selectNodes = hou.selectedNodes()
        
        #set self.nkfilePath
        houdiniFileFilePath = hou.hipFile.path()
        nukFileArr =  houdiniFileFilePath.split("/")
        houdiniHipFileName = nukFileArr[-1]
        nukFileArr[-1] ="prevComp" 
        str1 ="/"
        self.nkfilePath = str1.join(nukFileArr)+"/"+houdiniHipFileName[:-3]+"nk"
        #creat Nuke Path
        nkFondPath = str1.join( self.nkfilePath.split("/")[:-1])
        
        try:
            os.mkdir(nkFondPath)
        except:
            pass
        self.nkfondPath =  nkFondPath   
        #set self.startFrame & self.endFrame 
        try:
            self.startFrame = list(selectNodes)[0].parm("f1").eval() 
            self.endFrame  = list(selectNodes)[0].parm("f2").eval()
            
            #set cam size 
            camPath  =  list(selectNodes)[0].parm("camera").eval()
            camNode =   hou.node(camPath)
            revx =      camNode.parm("resx").eval()
            revy =      camNode.parm("resy").eval()
            self.camSize = '"'+str(revx)+" " +  str(revy)+'"'
            
            #set self.picPathArry
            for renderNode in  list(selectNodes):
                sourcePicPath =  renderNode.parm("vm_picture").eval()
                sourcePicPathArry =  sourcePicPath.split(".")
                sourcePicPathArry[-2] ="####"
                str2= "."
                picPath =  str2.join(sourcePicPathArry)
                self.picPathArry.append(picPath)
            
            # self.sourceRoot   
            with open(self.nkdataStart,"r") as f :
                self.sourceRoot =  f.read()
            
        except:
            pass
        
    def readSource(self):
        with open(self.nkdataStart,"r") as f :
            source =  f.readlines()
            return source
    def setRootData(self):
        name = "name "+self.nkfilePath +"\n"
        source =""

        source+="\nRoot {\n"
        source +="inputs 0\n"
        source +=name
        source +="first_frame "+str(self.startFrame)+"\n"
        source +="last_frame "+str(self.endFrame)+"\n"
        source +="lock_range true\n"
        source +=" }\n"
        return source
    def setReadData(self,filePath):
        source = ""
        file = "file "+filePath+"\n"
        format = "format "+'' +"\n"

        source +="Read {\n"
        source +="inputs 0\n"
        source +=file
        #source +=format
        source += "first " + str(self.startFrame) + "\n"
        source += "last " + str(self.endFrame) + "\n"
        source += "origfirst " + str(self.startFrame) + "\n"
        source += "origlast " + str(self.endFrame) + "\n"
        source +="origset true"+ "\n"
        source +="name Read1"+ "\n"
        source +="xpos -7"+"\n"
        source +="ypos -105"+"\n"
        source +="}" +"\n"
        return source
    
    def runNk( self,newNukePath,nkExePath,nkPythonPaht):    
        #write nkbat
        homePath =hou.homeHoudiniDirectory()
        fnkbat=open(homePath+"/"+"nkbat.bat","w")
        fnkbat.write('"')
        fnkbat.write(nkPythonPaht+'" '+homePath+"/"+"nkstart.py")
        fnkbat.close()  
        #rwitr  nkstart.py
        nkstart=open(homePath+"/"+ "nkstart.py","w")
        nkstart.write("import subprocess\n")
        
        cmd = [nkExePath,"--nukex", newNukePath]
        nkstart.write("cmd = ")
        nkstart.write(str(cmd))
        nkstart.write("\n")
        nkstart.write("subprocess.Popen(cmd ,stdout=subprocess.PIPE,shell=0)")
        
        nkstart.close()       
        
        
    
    
    
    def run(self):
        copySouse = ""
        newNukePath =""
        writeSource = self.sourceRoot + self.setRootData()
        for path in self.picPathArry:
            writeSource+= self.setReadData(path)
        allFiles =  os.listdir(self.nkfondPath)
        allFilesTemp = [] 
        newNukePath =self.nkfilePath
        if allFiles == []:
            with open(self.nkfilePath,"w") as f :
                f.write(writeSource)
        
        else:
            for a in     allFiles:
                if a[-1] =="~":
                    pass
                else:
                    allFilesTemp.append(a)
            
            allFiles = allFilesTemp
            newNukePath = self.nkfondPath  + "/" + allFiles[-1]
            with open(newNukePath) as f:
                copySouce = f.read()
        
        
            writeSource =  copySouce
           
            for path in self.picPathArry:
                writeSource+= self.setReadData(path)
            
            with open(newNukePath,"w") as f :    
                f.write(writeSource)
            
            #run nuk
        nkExePath = r"C:\Program Files\Nuke10.5v2\Nuke10.5.exe"
        nkPythonPath = r"C:\Program Files\Nuke10.5v2\python.exe"
        self.runNk( newNukePath,nkExePath,nkPythonPath)        
        nkBatPath= hou.homeHoudiniDirectory() + "/nkbat.bat"        
        bat_py = os.path.normcase(nkBatPath)
        os.popen('explorer.exe {0}'.format(bat_py))
        
        print     "final",newNukePath