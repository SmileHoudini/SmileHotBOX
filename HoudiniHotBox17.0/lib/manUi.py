import sys
import math
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

from PySide import QtGui, QtCore
class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.line = []
        self.arrButtonPose =[]
        self.windowStartX       =2900
        self.windowStartY       = 100
        self.windowXSize        = 1920
        self.windowYSize        = 1080
        self.windowCenterPointx =self.windowStartX + self.windowXSize/2
        self.windowCenterPointY = self.windowStartY -self.windowYSize/2
        #color set and line set
        self.insideColor        = [60,60,60]
        self.lineColor          = [210,210,210]
        self.lineWidth          = 3
        self.outsideColor       =[70,70,70]
        self.selectColor        =[174,166,157]
        #shape:
        self.cellCenterXY       =[500,500]
        self.insideShapeRs      =[100,300]
        self.outsideShapeRs     =[330,450]
        self.midsideShapeRs     = [300, 310]

        #countrl clickd
        self.inSelectIndexArr   =[]
        self.outSelectIndexArr  =[]
        self.mouseAngleArr      =[0]
        self.chindrenMouseAngleArr =[0]
        self.fatherindex        =6
        self.insideTextAngele =0
        #set in num
        self.fatherindex1       =6
        self.childrenindex      =5
        self.childrenAngleRange =0
        self.childrenallIndexArr =[]
        self.lenMouse = 0
        for i in  range(self.fatherindex1):
            # read file bt current inSelectIndexArr
            #if inSelectIndexArr[-1] :
                # read file name+"inSelectIndexArr[-1]"
                #append getnum
            self.childrenallIndexArr.append(i+5)


        #init ui
        self.initUI()
    def initUI(self):

        self.setGeometry(self.windowStartX, self.windowStartY,self.windowXSize, self.windowYSize)


        self.setWindowTitle('Pen styles')
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
    def getShapePos4 (self,shapeCenter,radio ):
        arrpos =[]
        arrpos.append(shapeCenter[0]-radio/2)
        arrpos.append(shapeCenter[1] - radio/2)
        arrpos.append(radio)
        arrpos.append(radio)
        return arrpos

    def getDissMousetoShapeCenter(self,cellCenter,mousePose):
        newVector = [cellCenter[0]-mousePose[0],cellCenter[1]-mousePose[1]]
        lendiss = QtGui.QVector2D.length( QtGui.QVector2D(newVector[0],newVector[1]))
        return  lendiss
    def paintEvent(self, event):
        qp = QtGui.QPainter()

        qp.begin(self)
        self.drawLines1(event, qp)
        self.ellipsePathIn(event,qp)

        self.drawLines2(event, qp)
        self.ellipsePathOut(event,qp)
        self.drawLines1(event, qp)
        self.clickellipsePathIn(event,qp)

        self.clickellipsePathOut(event, qp)
        self.drawLines(event, qp)
        self.drawLines2(event, qp)
        self.ellipsePathmid(event,qp)


        self.ellipsePathIn1(event, qp)
        self.drawTextInside(event,qp)
        self.drawTextOutside(event, qp)


        qp.end()
    def drawTextInside(self, event, qp):

        pen = QtGui.QPen(QtGui.QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2], 255), 30)

        qp.setPen(pen)

        insider = self.insideShapeRs[0]/2+ ( self.insideShapeRs[1]/2-self.insideShapeRs[0]/2)/2

        for i in range(self.fatherindex1):
            qp.setPen(QtGui.QColor(20, 34, 3))
            text = "Mode"+"::"+str(i)
            textLen = len(text)

            textSize = 10
            qp.translate(500,500)
            injiange = 360/self.fatherindex1
            inx = insider*math.cos(math.radians(i*injiange+ injiange/2))
            iny =insider*math.sin(math.radians(i*injiange+ injiange/2))

            qp.setFont(QtGui.QFont("Decorative", textSize))

            qp.translate(inx,-iny)

            qp.drawText(-1* ((textLen*textSize/2 +((textLen+1)/4)*textSize ))/2,textSize/2 ,text)
            try:
                if self.inSelectIndexArr[-1] == i :
                    qp.setPen(QtGui.QColor(200, 240, 30))
                    qp.drawText(-1 * ((textLen * textSize / 2 + ((textLen + 1) / 4) * textSize)) / 2, textSize / 2, text)

            except:
                pass
            #qp.drawText(0,0, text)
            qp.resetTransform()

    def drawTextOutside(self, event, qp):

        pen = QtGui.QPen(QtGui.QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2], 255), 30)

        qp.setPen(pen)

        insider = self.outsideShapeRs[0] / 2 + (self.outsideShapeRs[1] / 2 - self.outsideShapeRs[0] / 2) / 2

        startAngle = (self.insideTextAngele - (self.childrenindex * self.childrenAngleRange) * 1.0 / 2)%360

        for i in range(self.childrenindex):
            qp.setPen(QtGui.QColor(20, 34, 3))
            text = "SopFun"+"::"+str(i)
            textLen = len(text)

            textSize = 8
            qp.translate(500, 500)
            injiange = self.childrenAngleRange
            angle =((startAngle +injiange*i)+injiange/2)%360
            inx = insider * math.cos(math.radians(angle))
            iny = insider * math.sin(math.radians(angle))

            qp.setFont(QtGui.QFont("Decorative", textSize))

            qp.translate(inx, -iny)

            qp.drawText(-1 * ((textLen * textSize / 2 + ((textLen + 1) / 4) * textSize)) / 2, textSize / 2, text)
            try:
                if self.outSelectIndexArr[-1] == i  and  self.lenMouse >self.insideShapeRs[1]/2 :
                    qp.setPen(QtGui.QColor(200, 240, 30))
                    qp.drawText(-1 * ((textLen * textSize / 2 + ((textLen + 1) / 4) * textSize)) / 2, textSize / 2,
                                text)

            except:
                pass
            # qp.drawText(0,0, text)
            qp.resetTransform()


    def ellipsePathIn (self,event,qp):
        path = QtGui.QPainterPath()
        inellPose = self.getShapePos4(self.cellCenterXY, self.insideShapeRs[0])
        outellPose = self.getShapePos4(self.cellCenterXY, self.insideShapeRs[1])

        #QBrush(QPixmap("images/brick.png")
        #QtGui.QColor( self.insideColor[0], self.insideColor[1],self.insideColor[2])
        qp.setBrush(QtGui.QBrush(QtGui.QPixmap("D:/y.png")))
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
        qp.setBrush(QtGui.QBrush(QtGui.QPixmap("D:/y.png")))
        index =5
        try:
            index =self.childrenallIndexArr[self.inSelectIndexArr[-1]]
        except:
            pass
        self.childrenindex = index
        fenge = 0.5
        perA =20

        self.childrenAngleRange =20
        fatherAngle =0
        if self.mouseAngleArr[-1]:
            fatherAngle =(math.ceil( self.mouseAngleArr[-1]/(360/ self.fatherindex))-0.5)*(360/ self.fatherindex)
        self.insideTextAngele =fatherAngle
        startAngle = fatherAngle -(index*perA)*1.0/2

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

    def clickellipsePathOut (self,event,qp):
        path = QtGui.QPainterPath()
        inellPose = self.getShapePos4(self.cellCenterXY, self.outsideShapeRs[0])
        outellPose = self.getShapePos4(self.cellCenterXY, self.outsideShapeRs[1])

        qp.setBrush(QtGui.QColor(self.selectColor[0], self.selectColor[1], self.selectColor[2],200))
        index = self.childrenindex
        fenge = 2
        perA = 20
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
        pen = QtGui.QPen(QtGui.QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2], 255),0.001)
        qp.setPen(pen)
    def drawLines2(self,event, qp):
        pen = QtGui.QPen(QtGui.QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2], 255),0.1)
        qp.setPen(pen)
    def mousePressEvent(self, en):
        self.isPressed = 1
        self.startPos =QtCore.QPoint(250,250)
        self.endPose = en.pos()

    def mouseReleaseEvent(self, en):
        self.isPressed = 0
        self.runHoudiniPython()
        self.close()

    def mouseMoveEvent(self, en):
        #if self.isPressed:
        self.startPos =QtCore.QPoint(500,500)
        self.endPose = en.pos()

        self.line.append(self.startPos)
        self.line.append(self.endPose)
        self.line[1] =self.endPose

        self.update()

        self.line[-1] =self.endPose

    def runHoudiniPython(self):
        try:
            print self.inSelectIndexArr[-1]
            print self.outSelectIndexArr[-1]
        except:
            pass
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()