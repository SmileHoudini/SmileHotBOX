sysPath = r"C:\PythonLibs\HoudiniHotBox17.0"
LibPath =sysPath+"\\Uilib"
LibPath2 =sysPath+"\\lib"
WritePrefPath =  sysPath+"\\pref\\"
import sys
sys.path.append(sysPath)
sys.path.append(LibPath)
sys.path.append(LibPath2)
import math
import s_GetButton
import s_GetColor
import s_GetShape
import getWindowPose
import os

#readFile
houdiniHotPathIconPath = sysPath+"/Icon/"
nodeClass = "Sop"
s_button= s_GetButton.getButton(nodeClass)
fatherNumer = s_button.getFatherButtonNum()
PythonfilePath =LibPath2


color= s_GetColor.getColor()
shape= s_GetShape.getShape()
#Calculating angle
def getangle(a,b):
    lenA= math.sqrt(a[0]*a[0]+a[1]*a[1])
    lenB = math.sqrt(b[0] * b[0] + b[1] * b[1])
    A_B= a[0]*b[0] +a[1]*b[1]
    if(lenA*lenB !=0 ):
        arcC= A_B/(lenA*lenB)
        arcc=    math.acos(arcC)
        if a[1]>=0 and a[0]>0:
            return arcc*180/(math.pi)
        elif a[1]>=0 and a[0] < 0 :
            return arcc * 180 / (math.pi)

        elif a[0]<0 and a[1] < 0 :
            return 360 - arcc * 180 / (math.pi)
        elif a[0]>0 and a[1] <0:
            return 360- arcc * 180 / (math.pi)

def Hot7getLib2(lib2Path):

    a = os.listdir(lib2Path)
    index = 0
    for i in a:
        a[index] = i.split(".py")[0]
        index +=1

    new_a =[]

    for i in a:
        if i not in new_a:
            new_a.append(i)
    return  new_a
def Hot7getIconF(IconPath):
    a = os.listdir(IconPath)
    return  a

pythonFilelistL2 = Hot7getLib2(PythonfilePath)
IconFilelistL =Hot7getIconF(houdiniHotPathIconPath)

#ui start
from PySide import QtGui, QtCore
#start ui
class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.line = []
        self.arrButtonPose =[]
        self.windowStartX       =0
        self.windowStartY       = 0
        self.windowXSize        = 1280
        self.windowYSize        = 700
        self.mousePose =[0,0]
        try:

            self.mousePose[0] = getWindowPose.getPose().x()
            self.mousePose[1] = getWindowPose.getPose().y()
        except:
            pass
        self.windowCenterPointx =self.windowStartX + self.windowXSize/2
        self.windowCenterPointY = self.windowStartY -self.windowYSize/2
        #color set and line set
        self.insideColor        = color.getInsideColor()
        self.lineColor          = color.getLineColor()
        self.lineWidth          = color.lineWidth()
        self.outsideColor       = color.getOitsideColor()
        self.selectColor        =color.getSelectColor()
        #shape:
        self.cellCenterXY       =[self.windowStartX+0.5*self.windowXSize+300,self.windowStartY+0.5*self.windowYSize+50]
        self.insideShapeRs      =shape.insideShapeRs()
        self.outsideShapeRs     =shape.outsideShapeRs()
        self.midsideShapeRs     = shape.midsideShapeRs()
        self.childangleRangeset =shape.childPerAngle()

        #countrl clickd
        self.inSelectIndexArr   =[]
        self.outSelectIndexArr  =[]
        self.mouseAngleArr      =[0]
        self.chindrenMouseAngleArr =[0]
        self.fatherindex        =6
        self.insideTextAngele =0
        #set in num
        self.fatherindex1       =fatherNumer
        self.childrenindex      =5
        self.childrenAngleRange =0

        self.childrenallIndexArr =[]
        self.lenMouse = 0
        self.fatherNameArr =[]
        self.fatherIconNameArr =[]
        self.childNmaeArr =[]
        self.childIconNmaeARR =[]
        self.runPythonName =""
        #text
        self.inSideTextSize =shape.inForntSize()
        self.outSideTextSize =shape.inForntSize()
        self.insedeTextColor =color.inForntColor()
        self.outSideTextColor =color.outForntColor()
        self.selectTextColor =color.selectForntColor()
        #icon
        self.insideIconOffSetY =10
        self.OutSideIconOffSetY =5
        self.inInitImageSize =[40,40]
        self.OutInitImageSize =[25,25]
        for i in  range(self.fatherindex1):
            # read file bt current inSelectIndexArr
            #if inSelectIndexArr[-1] :
                # read file name+"inSelectIndexArr[-1]"
                #append getnum

            self.childrenallIndexArr.append(s_button.getButton_indexInfo(i)[2])
        for i in  range(self.fatherindex1):
            # read file bt current inSelectIndexArr
            #['name', 'iconName', 6, [['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName']]]
            #if inSelectIndexArr[-1] :
                # read file name+"inSelectIndexArr[-1]"
                #append getnum

            self.fatherNameArr.append(s_button.getButton_indexInfo(i)[0])
            self.fatherIconNameArr.append(s_button.getButton_indexInfo(i)[1])
        #current start ui
        #father:
        self.readCurrentNameArr =[]
        self.currentIconClassName =""
        self.tempCurrentIconName ="None"
        self.fatherIconViewPath  ="None"

        #child:
        self.childrenCurrentImageArr =[]
        self.currentIconChildrenClassName =""

        #init ui
        self.initUI()

    def reloadFatherInfo(self):


        self.fatherNameArr =[]
        self.fatherIconNameArr=[]
        for i in  range(self.fatherindex1):
            # read file bt current inSelectIndexArr
            #['name', 'iconName', 6, [['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName']]]
            #if inSelectIndexArr[-1] :
                # read file name+"inSelectIndexArr[-1]"
                #append getnum

            self.fatherNameArr.append(s_button.getButton_indexInfo(i)[0])
            self.fatherIconNameArr.append(s_button.getButton_indexInfo(i)[1])
        self.update()

    def initUI(self):

        self.setGeometry(self.mousePose[0]-0.5*self.windowXSize, self.mousePose[1]-0.5*self.windowYSize,self.windowXSize, self.windowYSize)


        self.setWindowTitle('HoudiniHotBox17_Master')
        self.initUICount()
        #self.setWindowOpacity(1)
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()

    def initUICount(self):
        #init python filePath
        self.PyhonfileList = QtGui.QCompleter(pythonFilelistL2)
        self.FatherNameList = QtGui.QCompleter(self.fatherNameArr)
        self.IconFilelistLCom = QtGui.QCompleter(IconFilelistL)
        #father
        self.IconCurrentFilelistL =Hot7getIconF(houdiniHotPathIconPath + self.currentIconClassName)
        self.IconCurrentFilelistLCom =  QtGui.QCompleter(self.IconCurrentFilelistL)
        #children
        self.IconCurrentChildrenFilelistL =Hot7getIconF(houdiniHotPathIconPath + self.currentIconChildrenClassName)
        self.IconCurrentChildrenFilelistLCom =  QtGui.QCompleter(self.IconCurrentChildrenFilelistL)


        self.lineeditor_label1 = QtGui.QLabel(self)
        self.lineeditor_label1.setGeometry(QtCore.QRect(30,20,71,20))
        self.lineeditor_label1.setObjectName("lineeditor_label1")
        self.lineeditor_label1.setText("Node Class:")
        self.com = QtGui.QCompleter(["Sop","Object","Dop","Driver","Shop","Vop","default"])
        #allfilepath

        self.addItem1=QtGui.QComboBox(self)
        self.addItem1.setGeometry(QtCore.QRect(110,20,100,20))
        self.addItem1.setObjectName("addItem1")
        self.addItem1.addItem("Sop")
        self.addItem1.addItem("Object")
        self.addItem1.addItem("Dop")
        self.addItem1.addItem("Driver")
        self.addItem1.addItem("Shop")
        self.addItem1.addItem("Vop")
        self.addItem1.addItem("default")
        self.addItem1.setEditable(True)
        self.addItem1.setCompleter(self.com)
        self.addItem1.setEditText("Sop")



        ##########################################
        self.lineeditor_label3 = QtGui.QLabel(self)
        self.lineeditor_label3.setGeometry(QtCore.QRect(30,120,71, 16))
        self.lineeditor_label3.setObjectName("lineeditor_label2")
        templineeditor_label3Text =""
        try:
            templineeditor_label3Text =self.readCurrentNameArr[-1][1]
        except:
            pass
        self.lineeditor_label3.setText(templineeditor_label3Text)


        self.lineeditor_label4 = QtGui.QLabel(self)
        self.lineeditor_label4.setGeometry(QtCore.QRect(110,100,71, 16))
        self.lineeditor_label4.setObjectName("lineeditor_label2")
        self.lineeditor_label4.setText("NewName|")

        self.lineeditor_label5 = QtGui.QLabel(self)
        self.lineeditor_label5.setGeometry(QtCore.QRect(240,100,71, 16))
        self.lineeditor_label5.setObjectName("lineeditor_label2")
        self.lineeditor_label5.setText("Icon Class|")

        self.lineeditor_label6 = QtGui.QLabel(self)
        self.lineeditor_label6.setGeometry(QtCore.QRect(370,100,71, 16))
        self.lineeditor_label6.setObjectName("lineeditor_label2")
        self.lineeditor_label6.setText("Icon Name|")

        self.lineeditor_label7 = QtGui.QLabel(self)
        self.lineeditor_label7.setGeometry(QtCore.QRect(500,100,71, 16))
        self.lineeditor_label7.setObjectName("lineeditor_label2")
        self.lineeditor_label7.setText("Icon View|")


        self.hline = QtGui.QFrame(self)
        self.hline.setGeometry(QtCore.QRect(30, 150, 580, 16))
        self.hline.setFrameShape(QtGui.QFrame.HLine)
        self.hline.setFrameShadow(QtGui.QFrame.Sunken)
        self.hline.setObjectName("line")

        self.hline1 = QtGui.QFrame(self)
        self.hline1.setGeometry(QtCore.QRect(90, 110, 20, 100))
        self.hline1.setFrameShape(QtGui.QFrame.VLine)
        self.hline1.setFrameShadow(QtGui.QFrame.Sunken)
        self.hline1.setObjectName("line")

        self.hline2 = QtGui.QFrame(self)
        self.hline2.setGeometry(QtCore.QRect(220, 110, 20, 100))
        self.hline2.setFrameShape(QtGui.QFrame.VLine)
        self.hline2.setFrameShadow(QtGui.QFrame.Sunken)
        self.hline2.setObjectName("line")

        self.hline3 = QtGui.QFrame(self)
        self.hline3.setGeometry(QtCore.QRect(350, 110, 20, 100))
        self.hline3.setFrameShape(QtGui.QFrame.VLine)
        self.hline3.setFrameShadow(QtGui.QFrame.Sunken)
        self.hline3.setObjectName("line")

        self.hline4 = QtGui.QFrame(self)
        self.hline4.setGeometry(QtCore.QRect(480, 110, 20, 100))
        self.hline4.setFrameShape(QtGui.QFrame.VLine)
        self.hline4.setFrameShadow(QtGui.QFrame.Sunken)
        self.hline4.setObjectName("line")

        self.hline5 = QtGui.QFrame(self)
        self.hline5.setGeometry(QtCore.QRect(600, 0, 20, 581))
        self.hline5.setFrameShape(QtGui.QFrame.VLine)
        self.hline5.setFrameShadow(QtGui.QFrame.Sunken)
        self.hline5.setObjectName("line")


        ######################Init father Pathon Path
        self.addItem_Father=QtGui.QComboBox(self)
        self.addItem_Father.setGeometry(QtCore.QRect(110,120,110,20))
        self.addItem_Father.setObjectName("addItem1")
        self.addItem_Father.setEditable(True)
        self.addItem_Father.setCompleter(self.FatherNameList)
        self.additemFromNode(self.addItem_Father,self.fatherNameArr)
        self.addItem_Father.setEditText(self.fatherNameArr[0])

        self.addItem_FatherIcon=QtGui.QComboBox(self)
        self.addItem_FatherIcon.setGeometry(QtCore.QRect(240,120,110,20))
        self.addItem_FatherIcon.setObjectName("addItem2")
        self.addItem_FatherIcon.setEditable(True)
        self.addItem_FatherIcon.setCompleter(self.IconFilelistLCom)
        self.additemFromNode(self.addItem_FatherIcon,IconFilelistL)
        self.addItem_FatherIcon.setEditText("COMMON")
        self.addItem_FatherIcon.activated.connect(self.currentTextChange)

        self.addItem_FatherIconName=QtGui.QComboBox(self)
        self.addItem_FatherIconName.setGeometry(QtCore.QRect(370,120,110,20))
        self.addItem_FatherIconName.setObjectName("addItem3")
        self.addItem_FatherIconName.setEditable(True)
        self.addItem_FatherIconName.setCompleter(self.IconCurrentFilelistLCom)
        self.additemFromNode(self.addItem_FatherIconName,self.IconCurrentFilelistL)
        self.addItem_FatherIconName.setEditText("")
        self.addItem_FatherIconName.activated.connect(self.currentTextChange1)
        ##70
        ##################################################################################
        #child countrl Labe
        self.lineeditor_label3_children = QtGui.QLabel(self)
        self.lineeditor_label3_children.setGeometry(QtCore.QRect(30,180,71, 16))
        self.lineeditor_label3_children.setObjectName("lineeditor_label2_children")
        templineeditor_label3Text = self.runPythonName
        try:
            lineeditor_label3_children =self.readCurrentNameArr[-1][1]
        except:
            pass
        self.lineeditor_label3_children.setText(templineeditor_label3Text)
        # get python file current
        self.addItem_childrenNewName=QtGui.QComboBox(self)
        self.addItem_childrenNewName.setGeometry(QtCore.QRect(110,180,110,20))
        self.addItem_childrenNewName.setObjectName("addItem1_childrenNew")
        self.addItem_childrenNewName.setEditable(True)
        self.addItem_childrenNewName.setCompleter(self.PyhonfileList)
        self.additemFromNode(self.addItem_childrenNewName,pythonFilelistL2)
        self.addItem_childrenNewName.setEditText(pythonFilelistL2[0])

        # get Icon Class current
        self.addItem_childrenIconClass=QtGui.QComboBox(self)
        self.addItem_childrenIconClass.setGeometry(QtCore.QRect(240,180,110,20))
        self.addItem_childrenIconClass.setObjectName("addItem1_childrenIconClass")
        self.addItem_childrenIconClass.setEditable(True)
        self.addItem_childrenIconClass.setCompleter(self.IconFilelistLCom)
        self.additemFromNode(self.addItem_childrenIconClass,IconFilelistL)
        self.addItem_childrenIconClass.setEditText(pythonFilelistL2[0])
        self.addItem_childrenIconClass.activated.connect(self.currentChildrenTextChange)
        # set Icon name Current
        self.addItem_ChildrenIconName=QtGui.QComboBox(self)
        self.addItem_ChildrenIconName.setGeometry(QtCore.QRect(370,180,110,20))
        self.addItem_ChildrenIconName.setObjectName("addItem3_childrenIconName")
        self.addItem_ChildrenIconName.setEditable(True)
        self.addItem_ChildrenIconName.setCompleter(self.IconCurrentChildrenFilelistLCom)
        self.additemFromNode(self.addItem_ChildrenIconName,self.IconCurrentChildrenFilelistL)
        self.addItem_ChildrenIconName.setEditText("aa ")
        self.addItem_ChildrenIconName.activated.connect(self.currentChildrenTextChange1)


        ################################################## close windows and save
        self.saveAllSetHot7 =QtGui.QPushButton(self)
        self.saveAllSetHot7.setGeometry(QtCore.QRect(370,500,80,25))
        self.saveAllSetHot7.setText("Save All")
        self.saveAllSetHot7.clicked.connect(self.saveAllSet)

        self.closeSetHot7 =QtGui.QPushButton(self)
        self.closeSetHot7.setGeometry(QtCore.QRect(460,500,80,25))
        self.closeSetHot7.setText("Close")
        self.closeSetHot7.clicked.connect(self.closeWindow)



    #Calculate the center position of each fan

    def saveAllSet(self):
        self.reloadFatherInfo()

        #self.inSelectIndexArr   =[]
        #self.outSelectIndexArr  =[]

        fileDataPath =WritePrefPath +nodeClass+"\\button\\"+"button_"+str(self.inSelectIndexArr[-1]) +".data"
        f1 = open(fileDataPath,"r")
        tempArr = f1.readlines()
        f1.close()
        PythonName =self.addItem_childrenNewName.currentText()
        IconName =self.addItem_childrenIconClass.currentText() + "/"+ self.addItem_ChildrenIconName.currentText()
        fatherName =self.addItem_Father.currentText()
        fatherIconName =self.addItem_FatherIcon.currentText() +"/"+self.addItem_FatherIconName.currentText()
        f2= open(fileDataPath,"w")
        for i in tempArr:
            changeLine =i
            if i.split("=")[0] ==  "lab_"+str(self.outSelectIndexArr[-1]):
                changeLine = "lab_"+str(self.outSelectIndexArr[-1])+"="+PythonName+"="+IconName+"\n"
            if i.split("=")[0] == "fatherLab":
                changeLine ="fatherLab="+fatherName+"="+fatherIconName+"\n"
            print  changeLine
            f2.write(changeLine)
        f2.close()

        self.update()
    def closeWindow(self):
        self.close()

    def additemFromNode(self,node,lists):
        node.clear()
        for text in lists:
            node.addItem(text)
    #Calculate the distance of each fan
    def getShapePos4 (self,shapeCenter,radio ):
        arrpos =[]
        arrpos.append(shapeCenter[0]-radio/2)
        arrpos.append(shapeCenter[1] - radio/2)
        arrpos.append(radio)
        arrpos.append(radio)
        return arrpos

    ##When changing the automatic completion of classicon changes group
    def currentTextChange(self):
        self.currentIconClassName1 =self.addItem_FatherIcon.currentText()
        self.IconCurrentFilelistL =Hot7getIconF(houdiniHotPathIconPath + self.currentIconClassName1)
        self.IconCurrentFilelistLCom =  QtGui.QCompleter(self.IconCurrentFilelistL)
        self.addItem_FatherIconName.setCompleter(self.IconCurrentFilelistLCom)
        self.additemFromNode(self.addItem_FatherIconName,self.IconCurrentFilelistL)
        self.addItem_FatherIconName.setEditText(self.tempCurrentIconName)
    def currentTextChange1(self):
        self.fatherIconViewPath = houdiniHotPathIconPath +self.addItem_FatherIcon.currentText()+"/" +self.addItem_FatherIconName.currentText()
        self.update()
     ##When changing the automatic completion of classicon changes group
    def  currentChildrenTextChange(self):
        self.currentChildrenIconClassName1 =self.addItem_childrenIconClass.currentText()

        self.IconCurrentChildrenFilelistL =Hot7getIconF(houdiniHotPathIconPath + self.currentChildrenIconClassName1)
        self.IconCurrentChildrenFilelistLCom =  QtGui.QCompleter(self.IconCurrentChildrenFilelistL)
        self.addItem_ChildrenIconName.setCompleter(self.IconCurrentChildrenFilelistLCom)
        self.additemFromNode(self.addItem_ChildrenIconName,self.IconCurrentChildrenFilelistL)
        self.addItem_ChildrenIconName.setEditText( self.tempCurrentChildrenIconName )

    def currentChildrenTextChange1(self):
         self.ChildrenIconViewPath = houdiniHotPathIconPath +self.addItem_childrenIconClass.currentText()+"/" +self.addItem_ChildrenIconName.currentText()
         self.update()
    def updatawindow(self):
        templineeditor_label3Text =""
        currentfatherIconName =""


        try:
            templineeditor_label3Text =self.readCurrentNameArr[-1][1]
            iconIndex = self.readCurrentNameArr[-1][0]
            currentfatherIconName =  self.fatherIconNameArr[iconIndex]
        except:
            pass
        #select inside
        self.lineeditor_label3.setText(templineeditor_label3Text)
        self.addItem_Father.setEditText(templineeditor_label3Text)
        self.addItem_FatherIcon.setEditText(currentfatherIconName.split("/")[0])
        self.currentIconClassName = currentfatherIconName.split("/")[0]

        #select outside
        self.lineeditor_label3_children.setText(self.runPythonName)
        self.addItem_childrenNewName.setEditText(self.runPythonName)

        try:

            self.IconCurrentFilelistL =Hot7getIconF(houdiniHotPathIconPath + self.currentIconClassName)
            self.IconCurrentFilelistLCom =  QtGui.QCompleter(self.IconCurrentFilelistL)
            self.addItem_FatherIconName.setCompleter(self.IconCurrentFilelistLCom)
            self.additemFromNode(self.addItem_FatherIconName,self.IconCurrentFilelistL)
            self.addItem_FatherIconName.setEditText(currentfatherIconName.split("/")[1])
            self.tempCurrentIconName =currentfatherIconName.split("/")[1]
        except:
            self.addItem_FatherIconName.setEditText("None")
        #set selectIconClass and Png Name
        self.addItem_childrenIconPath = "OBJ/switcher"
        try:
            self.addItem_childrenIconPath =self.childrenCurrentImageArr[self.outSelectIndexArr[-1]]
        except:
            pass
        #set Out Select Class
        self.addItem_childrenIconClass.setEditText(self.addItem_childrenIconPath.split("/")[0])
        self.currentIconChildrenClassName =self.addItem_childrenIconPath.split("/")[0]

        ##set out select iCON Name
        try:

            self.IconCurrentChildrenFilelistL =Hot7getIconF(houdiniHotPathIconPath + self.currentIconChildrenClassName)
            self.IconCurrentChildrenFilelistLCom =  QtGui.QCompleter(self.IconCurrentChildrenFilelistL)
            self.addItem_ChildrenIconName.setCompleter(self.IconCurrentChildrenFilelistLCom)
            self.additemFromNode(self.addItem_ChildrenIconName,self.IconCurrentChildrenFilelistL)
            self.addItem_ChildrenIconName.setEditText(self.addItem_childrenIconPath.split("/")[1])
            self.tempCurrentChildrenIconName =self.addItem_childrenIconPath.split("/")[1]
        except:
            self.addItem_ChildrenIconName.setEditText("None")
        ##setcurrentIcon
        self.fatherIconViewPath = houdiniHotPathIconPath +self.addItem_FatherIcon.currentText()+"/" +self.addItem_FatherIconName.currentText()
        self.ChildrenIconViewPath =houdiniHotPathIconPath +self.addItem_childrenIconClass.currentText()+"/" +self.addItem_ChildrenIconName.currentText()
        self.update()
    def drawIconFather(self,enent,qp):
        qp = QtGui.QPainter(self)

        qp.translate(510,120)
        qp.scale(0.5,0.5)
        image = QtGui.QImage(self.fatherIconViewPath)

        qp.drawImage(0,0,image)

    def drawIconChildren(self,enent,qp):
        try:
            qp = QtGui.QPainter(self)

            qp.translate(510,160)
            qp.scale(0.5,0.5)
            image = QtGui.QImage(self.ChildrenIconViewPath)
            qp.drawImage(0,0,image)
        except:
            pass
    def getDissMousetoShapeCenter(self,cellCenter,mousePose):
        newVector = [cellCenter[0]-mousePose[0],cellCenter[1]-mousePose[1]]
        lendiss = QtGui.QVector2D.length( QtGui.QVector2D(newVector[0],newVector[1]))
        return  lendiss
    def paintEvent(self, event):
        qp = QtGui.QPainter()

        qp.begin(self)
        self.drawLines1(event, qp)
        self.ellipsePathIn(event,qp)


        self.ellipsePathOut(event,qp)

        self.clickellipsePathIn(event,qp)

        self.clickellipsePathOut(event, qp)
        self.drawLines(event, qp)
        self.drawLines1(event, qp)
        self.ellipsePathmid(event,qp)


        self.ellipsePathIn1(event, qp)
        self.update()
        self.drawIconInside(event,qp)
        self.drawIconOutside(event,qp)
        self.drawTextInside(event,qp)
        self.drawTextOutside(event, qp)
        self.drawIconFather(event,qp)
        self.drawIconChildren(event,qp)

        qp.end()
    def drawTextInside(self, event, qp):

        pen = QtGui.QPen(QtGui.QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2], 255), 30)

        qp.setPen(pen)

        insider = self.insideShapeRs[0]/2+ ( self.insideShapeRs[1]/2-self.insideShapeRs[0]/2)/2
        index= -1
        for i in range(self.fatherindex1):
            index +=1
            qp.setPen(QtGui.QColor( self.insedeTextColor[0],  self.insedeTextColor[1],  self.insedeTextColor[2]))
            text = self.fatherNameArr[i]
            textLen = len(text)

            textSize = self.inSideTextSize
            qp.translate(self.cellCenterXY[0],self.cellCenterXY[1])
            injiange = 360/self.fatherindex1
            inx = insider*math.cos(math.radians(i*injiange+ injiange/2))
            iny =insider*math.sin(math.radians(i*injiange+ injiange/2))

            qp.setFont(QtGui.QFont("Decorative", textSize))

            qp.translate(inx,-iny)

            qp.drawText(-1* ((textLen*textSize/2 +((textLen+1)/4)*textSize ))/2,textSize/2+self.insideIconOffSetY ,text)
            try:
                if self.inSelectIndexArr[-1] == i :

                    qp.setPen(QtGui.QColor(self.selectTextColor[0], self.selectTextColor[1], self.selectTextColor[2]))
                    qp.drawText(-1 * ((textLen * textSize / 2 + ((textLen + 1) / 4) * textSize)) / 2, textSize / 2+self.insideIconOffSetY, text)
                    nameIndex =[index,text]

                    self.readCurrentNameArr.append(nameIndex)

            except:
                pass
            #qp.drawText(0,0, text)
            qp.resetTransform()
    def drawIconInside(self, event, qp):

        insider = self.insideShapeRs[0]/2+ ( self.insideShapeRs[1]/2-self.insideShapeRs[0]/2)/2
        initImageSize = [ self.inInitImageSize[0], self.inInitImageSize[1]]
        for i in range(self.fatherindex1):
            text = self.fatherNameArr[i]
            textLen = len(text)
            textSize = self.inSideTextSize

            image = QtGui.QImage(houdiniHotPathIconPath+"OBJ/switcher")
            try:
                if QtGui.QImage(houdiniHotPathIconPath+self.fatherIconNameArr[i]).size().width():
                    image = QtGui.QImage(houdiniHotPathIconPath+self.fatherIconNameArr[i])
            except:
                pass
            size =image.size()

            scaleImagex =initImageSize[0]*1.0/ size.width()
            scaleImagey = initImageSize[1]*1.0/size.height()


            qp.translate(self.cellCenterXY[0],self.cellCenterXY[1])
            injiange = 360/self.fatherindex1
            inx = insider*math.cos(math.radians(i*injiange+ injiange/2))
            iny =insider*math.sin(math.radians(i*injiange+ injiange/2))

            qp.translate(inx,-iny)
            qp.scale(scaleImagex,scaleImagey)
            #qp.drawImage(-1* ((textLen*textSize/2 +((textLen+1)/4)*textSize ))/2, -50-textSize,image)
            qp.setRenderHint(QtGui.QPainter().Antialiasing,True)
            qp.drawImage(-0.5*initImageSize[0],-1.0*initImageSize[1],image)

            qp.resetTransform()

    def drawTextOutside(self, event, qp):

        pen = QtGui.QPen(QtGui.QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2], 255), 30)

        qp.setPen(pen)

        insider = self.outsideShapeRs[0] / 2 + (self.outsideShapeRs[1] / 2 - self.outsideShapeRs[0] / 2) / 2

        startAngle = (self.insideTextAngele - (self.childrenindex * self.childrenAngleRange) * 1.0 / 2)%360
        self.childNmaeArr =[]
        for i in  range(self.childrenindex):
            # read file bt current inSelectIndexArr
            #['name', 'iconName', 6, [['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName']]]
            #if inSelectIndexArr[-1] :
                # read file name+"inSelectIndexArr[-1]"
                #append getnum
            try:
                self.childNmaeArr.append(s_button.getButton_indexInfo(self.inSelectIndexArr[-1])[3][i])
            except:
                pass

        for i in range(self.childrenindex):
            qp.setPen(QtGui.QColor(self.outSideTextColor[0], self.outSideTextColor[1], self.outSideTextColor[2]))
            text= ""
            try:
                text = self.childNmaeArr[i][0]
            except:
                pass
            textLen = len(text)

            textSize = self.outSideTextSize
            qp.translate(self.cellCenterXY[0],self.cellCenterXY[1])
            injiange = self.childrenAngleRange
            angle =((startAngle +injiange*i)+injiange/2)%360
            inx = insider * math.cos(math.radians(angle))
            iny = insider * math.sin(math.radians(angle))

            qp.setFont(QtGui.QFont("Decorative", textSize))

            qp.translate(inx, -iny)

            qp.drawText(-1 * ((textLen * textSize / 2 + ((textLen + 1) / 4) * textSize)) / 2, textSize / 2+self.OutSideIconOffSetY, text)
            try:
                if self.outSelectIndexArr[-1] == i  and  self.lenMouse >self.insideShapeRs[1]/2 :
                    qp.setPen(QtGui.QColor(self.selectTextColor[0], self.selectTextColor[1], self.selectTextColor[2]))
                    qp.drawText(-1 * ((textLen * textSize / 2 + ((textLen + 1) / 4) * textSize)) / 2, textSize / 2+self.OutSideIconOffSetY,
                                text)
                    self.runPythonName=text

            except:
                pass
            # qp.drawText(0,0, text)
            qp.resetTransform()
    def drawIconOutside(self, event, qp):
        initImageSize = [self.OutInitImageSize[0],self.OutInitImageSize[1]]


        insider = self.outsideShapeRs[0] / 2 + (self.outsideShapeRs[1] / 2 - self.outsideShapeRs[0] / 2) / 2

        startAngle = (self.insideTextAngele - (self.childrenindex * self.childrenAngleRange) * 1.0 / 2)%360
        self.childNmaeArr =[]
        self.childIconNmaeArr =[]
        for i in  range(self.childrenindex):
            # read file bt current inSelectIndexArr
            #['name', 'iconName', 6, [['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName'], ['name', 'iconName']]]
            #if inSelectIndexArr[-1] :
                # read file name+"inSelectIndexArr[-1]"
                #append getnum
            try:
                self.childNmaeArr.append(s_button.getButton_indexInfo(self.inSelectIndexArr[-1])[3][i])
            except:
                pass
        self.childrenCurrentImageArr =[]
        for i in range(self.childrenindex):
            qp.setPen(QtGui.QColor(20, 34, 3))
            text= ""

            imagePath ="OBJ/switcher"
            try:
                text = self.childNmaeArr[i][0]
                if QtGui.QImage(houdiniHotPathIconPath+self.childNmaeArr[i][1]):
                    imagePath =  self.childNmaeArr[i][1]
            except:
                #check install icon
                return 0
            textLen = len(text)
            textSize = self.outSideTextSize
            image =QtGui.QImage(houdiniHotPathIconPath+imagePath)

            self.childrenCurrentImageArr.append(imagePath)
            size =image.size()
            scaleImagex =initImageSize[0]*1.0/ size.width()
            scaleImagey = initImageSize[1]*1.0/size.height()

            qp.translate(self.cellCenterXY[0],self.cellCenterXY[1])
            injiange = self.childrenAngleRange
            angle =((startAngle +injiange*i)+injiange/2)%360
            inx = insider * math.cos(math.radians(angle))
            iny = insider * math.sin(math.radians(angle))
            qp.translate(inx, -iny)
            qp.scale(scaleImagex,scaleImagey)
            qp.drawImage(-0.5* size.width(),-1.0*size.height(),image)

            qp.resetTransform()

    def ellipsePathIn (self,event,qp):
        path = QtGui.QPainterPath()
        inellPose = self.getShapePos4(self.cellCenterXY, self.insideShapeRs[0])
        outellPose = self.getShapePos4(self.cellCenterXY, self.insideShapeRs[1])

        #QBrush(QPixmap("images/brick.png")
        #QtGui.QColor( self.insideColor[0], self.insideColor[1],self.insideColor[2])
        qp.setBrush(QtGui.QBrush(QtGui.QPixmap(houdiniHotPathIconPath+"ground")))
        index = self.fatherindex1
        self.fatherindex= self.fatherindex1
        fenge = 1
        perA= 360/index

        for i in range(index):

            startAngle = perA*i+fenge
            endAngle   = perA-fenge
            #in inside
            path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
            path.arcTo(inellPose[0]-20,inellPose[1],inellPose[2]+40,inellPose[3],startAngle,endAngle)
            #out inside
            path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
            path.arcTo(outellPose[0],outellPose[1],outellPose[2],outellPose[3],startAngle,endAngle)

            path.setFillRule(QtCore.Qt.OddEvenFill)

        qp.drawPath(path)
    def ellipsePathIn1 (self,event,qp):
        path = QtGui.QPainterPath()
        inellPose = self.getShapePos4(self.cellCenterXY, self.insideShapeRs[0])
        outellPose = self.getShapePos4(self.cellCenterXY, self.insideShapeRs[1])

        #QBrush(QPixmap("images/brick.png")
        #QtGui.QColor( self.insideColor[0], self.insideColor[1],self.insideColor[2])
        qp.setBrush(QtGui.QColor(self.insideColor[0], self.insideColor[1], self.insideColor[2],50))
        index = 2
        self.fatherindex= self.fatherindex1
        fenge = 0
        perA= 360/index

        for i in range(index):

            startAngle = perA*i+fenge
            endAngle   = perA-fenge
            #in inside
            path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
            path.arcTo(inellPose[0]-20,inellPose[1],inellPose[2]+40,inellPose[3],startAngle,endAngle)


            path.setFillRule(QtCore.Qt.OddEvenFill)

        qp.drawPath(path)

    def clickellipsePathIn (self,event,qp):
        path = QtGui.QPainterPath()
        inellPose = self.getShapePos4(self.cellCenterXY, self.insideShapeRs[0])
        outellPose = self.getShapePos4(self.cellCenterXY, self.insideShapeRs[1])


        qp.setBrush(QtGui.QColor(self.selectColor[0], self.selectColor[1], self.selectColor[2],200))
        index = self.fatherindex
        fenge = 1
        perA= 360/index
        posmouthx=0
        posmouthy = 0
        try:
            posmouthx =self.line[-1].x()-self.cellCenterXY[0]
            posmouthy = self.cellCenterXY[1] -self.line[-1].y()

        except:

            pass
        pos =[posmouthx,posmouthy]
        bpos = [1,0]
        mouthAngle =getangle(pos,bpos )

        lenMouse = self.getDissMousetoShapeCenter(pos,[0,0])
        self.lenMouse =lenMouse
        if(lenMouse < self.insideShapeRs[1]/2):
            self.mouseAngleArr.append(mouthAngle)


        for i in range(self.fatherindex):
            if self.mouseAngleArr[-1]>i*perA and self.mouseAngleArr[-1]<(i+1)*perA :
                startAngle = perA*i+fenge
                endAngle   = perA-fenge
                #in inside
                #path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
                #path.arcTo(inellPose[0]-20,inellPose[1],inellPose[2]+40,inellPose[3],startAngle,endAngle)
                #out inside
                path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
                path.arcTo(outellPose[0],outellPose[1],outellPose[2],outellPose[3],startAngle,endAngle)

                path.setFillRule(QtCore.Qt.OddEvenFill)
                self.inSelectIndexArr.append(i)

        qp.drawPath(path)
    #bianyuan start
    def ellipsePathmid (self,event,qp):
        path = QtGui.QPainterPath()
        inellPose = self.getShapePos4(self.cellCenterXY, self.midsideShapeRs[0])
        outellPose = self.getShapePos4(self.cellCenterXY, self.midsideShapeRs[1])


        qp.setBrush(QtGui.QColor( self.insideColor[0], self.insideColor[1],self.insideColor[2]))
        index = 1
        fenge = 0
        perA= 360/index
        self.fatherindex =index
        for i in range(1):

            startAngle = perA*i+fenge
            endAngle   = perA-fenge
            #in inside
            path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
            path.arcTo(inellPose[0],inellPose[1],inellPose[2],inellPose[3],startAngle,endAngle)
            #out inside
            path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
            path.arcTo(outellPose[0],outellPose[1],outellPose[2],outellPose[3],startAngle,endAngle)

            path.setFillRule(QtCore.Qt.OddEvenFill)

        qp.drawPath(path)
    #bianyuan end
    def ellipsePathOut (self,event,qp):
        path = QtGui.QPainterPath()
        inellPose = self.getShapePos4(self.cellCenterXY, self.outsideShapeRs[0])
        outellPose = self.getShapePos4(self.cellCenterXY, self.outsideShapeRs[1])
        qp.setBrush(QtGui.QBrush(QtGui.QPixmap(houdiniHotPathIconPath+"ground")))
        index =5
        try:
            index =self.childrenallIndexArr[self.inSelectIndexArr[-1]]
        except:
            pass
        self.childrenindex = index
        fenge = 0.5
        perA = self.childangleRangeset

        self.childrenAngleRange =perA
        fatherAngle =0
        if self.mouseAngleArr[-1]:
            fatherAngle =(math.ceil( self.mouseAngleArr[-1]/(360/ self.fatherindex))-0.5)*(360/ self.fatherindex)
        self.insideTextAngele =fatherAngle
        startAngle = fatherAngle -(index*perA)*1.0/2
        try:
            if self.inSelectIndexArr[-1]>-1:
                for a in range(index):
                    endAngle =perA
                    path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
                    path.arcTo(inellPose[0], inellPose[1], inellPose[2], inellPose[3], startAngle+fenge, endAngle-fenge)
                    # out inside
                    path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
                    path.arcTo(outellPose[0], outellPose[1], outellPose[2], outellPose[3], startAngle+fenge, endAngle-fenge)

                    path.setFillRule(QtCore.Qt.OddEvenFill)
                    startAngle+=perA



                qp.drawPath(path)
        except:
            pass

    def clickellipsePathOut (self,event,qp):
        path = QtGui.QPainterPath()
        inellPose = self.getShapePos4(self.cellCenterXY, self.outsideShapeRs[0])
        outellPose = self.getShapePos4(self.cellCenterXY, self.outsideShapeRs[1])

        qp.setBrush(QtGui.QColor(self.selectColor[0], self.selectColor[1], self.selectColor[2],200))
        index = self.childrenindex
        fenge = 2
        perA =  self.childrenAngleRange
        posmouthx = 0
        posmouthy = 0
        try:
            posmouthx = self.line[-1].x() - self.cellCenterXY[0]
            posmouthy = self.cellCenterXY[1] - self.line[-1].y()

        except:
            pass
        pos = [posmouthx, posmouthy]
        bpos = [1, 0]
        mouthAngle = getangle(pos, bpos)

        lenMouse = self.getDissMousetoShapeCenter(pos, [0, 0])

        if (lenMouse > self.insideShapeRs[1] / 2):
            try:
                self.chindrenMouseAngleArr.append(int(mouthAngle))
            except:
                pass
        fatherAngle = 0
        if self.mouseAngleArr[-1]:
            fatherAngle =(math.ceil( self.mouseAngleArr[-1]/(360/ self.fatherindex))-0.5)*(360/ self.fatherindex)
        startAngle =( fatherAngle - (index * perA) * 1.0 / 2) %360
        tempStartAngle =( fatherAngle - (index * perA) * 1.0 / 2) %360
        tempLastStartAngle = ((fatherAngle - (index * perA) * 1.0 / 2) % 360)*(index-1)%360
        if (lenMouse > self.insideShapeRs[1] / 2):
            for i in range(self.childrenindex):

                if self.chindrenMouseAngleArr[-1] >startAngle and self.chindrenMouseAngleArr[-1] < startAngle+ perA:

                    endAngle = perA
                    # in inside
                    path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
                    path.arcTo(inellPose[0], inellPose[1], inellPose[2], inellPose[3], startAngle, endAngle)
                    # out inside
                    path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
                    path.arcTo(outellPose[0], outellPose[1], outellPose[2], outellPose[3], startAngle, endAngle)

                    path.setFillRule(QtCore.Qt.OddEvenFill)
                    self.outSelectIndexArr.append(i)
                else:
                    try:
                        if i ==  self.outSelectIndexArr[-1]  :
                            endAngle = perA
                            # in inside
                            path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
                            path.arcTo(inellPose[0], inellPose[1], inellPose[2], inellPose[3], startAngle, endAngle)
                            # out inside
                            path.moveTo(self.cellCenterXY[0], self.cellCenterXY[1])
                            path.arcTo(outellPose[0], outellPose[1], outellPose[2], outellPose[3], startAngle, endAngle)

                            path.setFillRule(QtCore.Qt.OddEvenFill)
                    except:
                        pass
                #over select angle


                startAngle = (startAngle+perA)%360

            qp.drawPath(path)

    def drawLines(self,event, qp):
        pen = QtGui.QPen(QtGui.QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2], 255),self.lineWidth)
        qp.setPen(pen)
        index = len(self.line)
        for i in range( index):
            qp.drawLine(self.line[0],self.line[-1])
            #qp.drawLine(self.line[1],self.line[-1])
    def drawLines1(self,event, qp):
        pen = QtGui.QPen(QtGui.QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2], 255),0.0001)
        qp.setPen(pen)
    def drawLines2(self,event, qp):
        pen = QtGui.QPen(QtGui.QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2], 255),0.0001)
        qp.setPen(pen)
    def mousePressEvent(self, en):
        self.isPressed = 1
        self.startPos =QtCore.QPoint(250,250)
        self.endPose = en.pos()

    def mouseReleaseEvent(self, en):
        self.isPressed = 0
        #self.runHoudiniPython()
        #self.close()



    def mouseMoveEvent(self, en):
        #if self.isPressed:
        self.startPos =QtCore.QPoint(self.cellCenterXY[0],self.cellCenterXY[1])
        self.endPose = en.pos()

        self.line.append(self.startPos)
        self.line.append(self.endPose)
        self.line[1] =self.endPose

        self.update()

        self.line[-1] =self.endPose
        self.updatawindow()

    def runHoudiniPython(self):
        try:

            if  self.runPythonName != "":
            #try:
                lastNodeName = "import " + self.runPythonName
                runNodeName = "a ="+self.runPythonName+"."+self.runPythonName+"()"



                exec(lastNodeName)
                exec(runNodeName)
                a.run()

        except:
            pass
class H7WindSet():
    def run(self):

        ex = Example()


a= H7WindSet()
a.run()