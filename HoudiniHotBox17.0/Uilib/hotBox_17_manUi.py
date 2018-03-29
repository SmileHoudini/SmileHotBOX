import os
#os.environ["SMILEHOTBOX"] =r"R:\filmServe\RnD\houdini\16\HoudiniHotBox17.0"
sysPath = os.getenv('SMILEHOTBOX')
#sysPath = r"C:\PythonLibs\HoudiniHotBox17.0"
#os.environ["SMILEHOTBOX"] =sysPath
LibPath =sysPath+r"/Uilib"
LibPath2 =sysPath+r"/lib"
import sys
sys.path.append(sysPath)
sys.path.append(LibPath)
sys.path.append(LibPath2)
import math
import s_GetButton
import s_GetColor
import s_GetShape
import getWindowPose
import s_GetHoudiniEnvenPath
import os
import hou
a=0
##append other python lib
s_houdiniEnvenPaths = s_GetHoudiniEnvenPath.readHoudiniEnv().read()
for s_childEnvPath in s_houdiniEnvenPaths:
    a= s_childEnvPath.split(" = ")[-1].split("\n")[0]
    sys.path.append(a)

#readFile
def selectClassButuonClass():
    a = hou.ui.curDesktop()
    pane = a.paneUnderCursor()
    currentTab = pane.currentTab()
    name = currentTab.type().name()
    return name

houdiniHotPathIconPath = sysPath+"/Icon/"

s_button= s_GetButton.getButton(selectClassButuonClass())
fatherNumer = s_button.getFatherButtonNum()

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



from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
#start ui
class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.line = []
        self.arrButtonPose =[]
        self.windowStartX       =0
        self.windowStartY       = 0
        self.windowXSize        = 1000
        self.windowYSize        = 1000
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
        self.cellCenterXY       =[self.windowStartX+0.5*self.windowXSize,self.windowStartY+0.5*self.windowYSize]
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


        #init ui
        self.initUI()


    def initUI(self):

        self.setGeometry(self.mousePose[0]-0.5*self.windowXSize, self.mousePose[1]-0.5*self.windowYSize,self.windowXSize, self.windowYSize)


        self.setWindowTitle('Pen styles')
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
    #Calculate the center position of each fan
    def getShapePos4 (self,shapeCenter,radio ):
        arrpos =[]
        arrpos.append(shapeCenter[0]-radio/2)
        arrpos.append(shapeCenter[1] - radio/2)
        arrpos.append(radio)
        arrpos.append(radio)
        return arrpos
    #Calculate the distance of each fan
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
        self.drawIconInside(event,qp)
        self.drawIconOutside(event,qp)
        self.drawTextInside(event,qp)
        self.drawTextOutside(event, qp)


        qp.end()
    def drawTextInside(self, event, qp):

        pen = QtGui.QPen(QtGui.QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2], 255), 30)

        qp.setPen(pen)

        insider = self.insideShapeRs[0]/2+ ( self.insideShapeRs[1]/2-self.insideShapeRs[0]/2)/2

        for i in range(self.fatherindex1):
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
        qp.setBrush(QtGui.QBrush(QtGui.QPixmap(houdiniHotPathIconPath+"ground1")))
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
        qp.setBrush(QtGui.QColor(self.insideColor[0], self.insideColor[1], self.insideColor[2],self.insideColor[3]))
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

        qp.setBrush(QtGui.QBrush(QtGui.QPixmap(houdiniHotPathIconPath + "ground1")))
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
        qp.setBrush(QtGui.QBrush(QtGui.QPixmap(houdiniHotPathIconPath+"ground1")))
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
        self.close()
        #self.runHoudiniPython()
        if self.lenMouse > self.insideShapeRs[1] / 2:
            self.runHoudiniPython()

    def mouseMoveEvent(self, en):
        #if self.isPressed:
        self.startPos =QtCore.QPoint(self.cellCenterXY[0],self.cellCenterXY[1])
        self.endPose = en.pos()

        self.line.append(self.startPos)
        self.line.append(self.endPose)
        self.line[1] =self.endPose

        self.update()

        self.line[-1] =self.endPose

    def runHoudiniPython(self):
        try:

            if  self.runPythonName != "":
            #try:
                lastNodeName = "import " + self.runPythonName
                runNodeName = "a ="+self.runPythonName+"."+self.runPythonName+"()"



                exec(lastNodeName)
                exec(runNodeName)
                a.run()

        except :
            raise


ex = Example()