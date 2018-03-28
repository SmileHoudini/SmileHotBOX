###############################################################################################################
import hou
import subprocess
class closeMulitRop:
    def run(self):
        f1 = open(r"C:\render\kill.bat" ,"r")
        source = list(f1.readlines())
        for a in source:
            pid =str(a.split("\n")[0])
            cmd = "taskkill /pid " + pid + " -t -f"
            proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    universal_newlines=True, shell=1)
        f1.close()


import time

timeStart = time.time()
import hou
from PySide2 import QtCore, QtGui, QtUiTools
from PySide2 import QtWidgets
import os, time

renderNode = list(hou.selectedNodes())[0]


def evalSopPath(renderNode):
    if renderNode.type().name() == "rop_geometry":
        renderPath = renderNode.path()

    elif renderNode.type().name() == "opengl":
        renderPath = renderNode.path()

    elif renderNode.type().name() == "filecache":
        renderNode.allowEditingOfContents()
        renderNode = hou.node(renderNode.path() + "/render")

    elif renderNode.type().name() == "catche_tool_1.0.1":
        renderNode = hou.node(renderNode.path() + "/render")

    else:
        pass
    return renderNode


def evaltotalFrame(renderNode):
    renderPath = 0
    start = 0
    end = 0
    if renderNode.type().name() == "rop_geometry":
        renderPath = renderNode.path()
        start = renderNode.parm("f1").eval()
        end = renderNode.parm("f2").eval()
    elif renderNode.type().name() == "opengl":
        renderPath = renderNode.path()
        start = renderNode.parm("f1").eval()
        end = renderNode.parm("f2").eval()

    elif renderNode.type().name() == "filecache":
        renderNode.allowEditingOfContents()
        renderNode = hou.node(renderNode.path() + "/render")
        renderPath = renderNode.path()
        start = renderNode.parm("f1").eval()
        end = renderNode.parm("f2").eval()
    elif renderNode.type().name() == "catche_tool_1.0.1":
        renderNode = hou.node(renderNode.path() + "/render")
        renderPath = renderNode.path()
        start = renderNode.parm("f1").eval()
        end = renderNode.parm("f2").eval()
    else:
        print "Is not IO node ex:rop_geometry,filecache,catche_tool_1.0.1"
        return
    totalFrame = (end - start)
   
    return totalFrame+1


wordDir = os.getenv('SMILEHOTBOX') + "//ScriptUi//"


class Backend(QtCore.QThread):
    update_date = QtCore.Signal()

    def __init__(self, parent=None):
        super(Backend, self).__init__(parent)
        self.swich = 1
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose, 1)

    def run(self):
        while self.swich:
            data = QtCore.QDateTime.currentDateTime()
            self.update_date.emit()
            time.sleep(0.5)


class CharPickerTutorial(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CharPickerTutorial, self).__init__(parent)
        # ui Loader
        self.allFrame =0
        self.compingNum = 0
        self.tsInit = 0
        self.compingFrame = 0
        self.loader = QtUiTools.QUiLoader()
        self.ui = self.loader.load(wordDir + 'a.ui')
        self.ui.setWindowTitle('MulitProceRop: ' + renderNode.type().name())
        self.progressBar = self.ui.findChild(QtWidgets.QWidget, 'progressBar')
        self.progressBar.setProperty("value", 0)
        self.buttonCancle = self.ui.findChild(QtWidgets.QPushButton, 'pushButtonCancle')
        self.label_2 = self.ui.findChild(QtWidgets.QLabel, 'label_2')
        self.buttonCancle.clicked.connect(self.closeWindow)
        self.b = Backend()
        self.b.update_date.connect(self.setProgressB)
        self.b.start()
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose,1)
        
        
        self.ui.show()
        
        
        
    
        
        
    def getRenderingIndex(self):
        dir = r"C:\render"
        listFile = os.listdir(dir)
        index = 0
        listNum = 0
        for i in listFile:
            
            if i.split("dex")[0] == "in":
                listNum +=1
                textdir = dir + "\\" + i
                a = 0
                while (a < 1):
                    try:
                        with open(textdir, 'r') as f:
                            index += int(f.readlines()[0])
                            a += 1
                    except:
                        pass
        return index

    def setProgressB(self):
        a=0
        try:


     
            self.allFrame = evaltotalFrame(renderNode)
            self.compingFrame = self.getRenderingIndex()
            
            if self.compingFrame >self.allFrame:
                self.compingFrame = evaltotalFrame(renderNode)
            
            self.compingNum  = (self.compingFrame * 1.0) / (self.allFrame  * 1.0 )* 100
             
            self.progressBar.setProperty("value", self.compingNum )
            
           
        except:
            pass

        timeend = time.time()
        ts1 = self.tsInit
        
        if int(self.compingNum) < 100:
            ts1 = int(timeend - timeStart)
            self.tsInit =ts1
        
        tm = 0
        th = 0
        ts = ts1 % 60
        tm = (ts1 / 60) % 60
        th = (ts1 / 3600) % 60
        if ts < 10:
            ts = "0" + str(ts)
        else:
            ts = str(ts)
        if tm < 10:
            tm = "0" + str(tm)
        else:
            tm = str(tm)
        if th < 10:
            th = "0" + str(th)
        else:
            th = str(th)
        try:
            texString = "Render time:  " + th + ":" + tm + ":" + ts + "       Complated Frame:" + str(int(self.compingFrame))

            self.label_2.setText(texString)
        except:
            pass
        

    def closeWindow(self):
        a = closeMulitRop()
        a.run()
        #self.b.close()
        self.ui.close()        
        
        
        
        
        


showWindowsMuti = CharPickerTutorial()