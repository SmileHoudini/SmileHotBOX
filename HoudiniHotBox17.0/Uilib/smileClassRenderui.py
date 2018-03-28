###############################################################################################################
import time
timeStart = time.time()
import hou
from PySide import QtCore, QtGui,QtUiTools
import os,time
renderNode = list(hou.selectedNodes())[0]
def evalSopPath(renderNode):
    if renderNode.type().name() == "rop_geometry":
        renderPath = renderNode.path()
    
    elif renderNode.type().name() == "filecache":
        renderNode.allowEditingOfContents()
        renderNode =hou.node( renderNode.path()+"/render")
           
    elif renderNode.type().name() == "catche_tool_1.0.1":
        renderNode =hou.node( renderNode.path()+"/render")
    
    else:
        pass
    return  renderNode  
def evaltotalFrame(renderNode):
    renderPath=0
    start =0
    end =0
    if renderNode.type().name() == "rop_geometry":
        renderPath = renderNode.path()
        start = renderNode.parm("f1").eval()
        end = renderNode.parm("f2").eval()
    elif renderNode.type().name() == "filecache":
        renderNode.allowEditingOfContents()
        renderNode =hou.node( renderNode.path()+"/render")
        renderPath = renderNode.path()
        start = renderNode.parm("f1").eval()
        end = renderNode.parm("f2").eval()
    elif renderNode.type().name() == "catche_tool_1.0.1":
        renderNode =hou.node( renderNode.path()+"/render")
        renderPath = renderNode.path()
        start = renderNode.parm("f1").eval()
        end = renderNode.parm("f2").eval()
    else:
        print "Is not IO node ex:rop_geometry,filecache,catche_tool_1.0.1"
        return 
    totalFrame =(end-start)
    return totalFrame
import os
wordDir = os.getenv('SMILEHOTBOX')+"\\ScriptUi"
class Backend(QtCore.QThread):
    update_date= QtCore.Signal()
    def __init__(self,parent=None):
        super(Backend, self).__init__(parent)
        self.swich =1
    def run(self):
        while self.swich:
            data = QtCore.QDateTime.currentDateTime()
            self.update_date.emit()
            time.sleep(0.5)

class CharPickerTutorial(QtGui.QWidget):
    def __init__(self, parent=None):
        super(CharPickerTutorial, self).__init__(parent)
        # ui Loader
        self.loader = QtUiTools.QUiLoader()
        self.ui = self.loader.load(wordDir + 'a.ui')
        self.ui.setWindowTitle('MulitProceRop')
        self.progressBar = self.ui.findChild(QtGui.QWidget, 'progressBar')
        self.progressBar.setProperty("value", 0)
        self.buttonCancle =  self.ui.findChild(QtGui.QPushButton, 'pushButtonCancle')
        self.label_2 =  self.ui.findChild(QtGui.QLabel, 'label_2')
        self.buttonCancle.clicked.connect(self.closeWindow)
        self.b = Backend()
        self.b.update_date.connect(self.setProgressB)
        self.b.start()
        self.ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ui.show()
     
    def setProgressB(self):
        try:
            allPath= evalSopPath(renderNode).parm("sopoutput").eval().split(".bgeo")[0].split(".")[0]
            fileName= evalSopPath(renderNode).parm("sopoutput").eval().split(".bgeo.")[0].split("/")[-1].split(".")[0:-1]
            serachPath= allPath.split("/")[0:-1]
            str0 = "\\";
            str1 = ".";
            fileName =str1.join( fileName );
            path= str0.join( serachPath );
            path = os.listdir(path)
            cont=0
            for p in path:
                p=p.split(".bgeo.")[0].split(".")[0:-1]
                p= str1.join( p);
                if fileName ==p:
                    cont +=1
            a= cont*1.0/ evaltotalFrame(renderNode)*1.0*100      
            self.progressBar.setProperty("value", a)
        except:
            pass
        timeend = time.time()
        ts1 =int(timeend-timeStart)
        tm=0
        th=0
        ts= ts1%60
        tm=(ts1/60)%60
        th= (ts1/3600)%60
        if ts <10: 
            ts= "0"+str(ts)
        else:
            ts = str(ts)
        if tm <10: 
            tm= "0"+str(tm)
        else:
            tm = str(tm)
        if th <10: 
            th= "0"+str(th)
        else:
            th = str(th)
        try:    
            texString = "Render time:  "+th+":"+tm+":"+ts+"       Complate :"+str(a)+"%"
            self.label_2.setText(texString)
        except:
            pass
            
        
        
        
    def closeWindow(self):
        self.b.swich=0
        self.ui.close()
        

dialog =CharPickerTutorial()

