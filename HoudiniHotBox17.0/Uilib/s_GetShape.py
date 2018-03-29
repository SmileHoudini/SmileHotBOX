import os

class getShape:
    def __init__(self):
        self.classNmae1 ="publicCountrl"
        self.s_path = os.getenv('SMILEHOTBOX')+r"/pref"
        self.prefPath = self.s_path+r"/"+self.classNmae1+r"/shape/"
        self.fatherBPath = self.prefPath+"shape.dat"
        self.sourceString = ""
        self.setString()
    def setString(self):
        f1= open(self.fatherBPath,"r" )
        self.sourceString = f1.readlines()
        f1.close()
    def insideShapeRs(self):
        color = self.sourceString[0].split("=")[1].split("\n")[0].split(",")
        color1 =[]
        for i in color:
            color1.append(int(i))
        return color1
    def outsideShapeRs(self):
        color = self.sourceString[1].split("=")[1].split("\n")[0].split(",")
        color1 =[]
        for i in color:
            color1.append(int(i))
        return color1
    def midsideShapeRs(self):
        color = self.sourceString[2].split("=")[1].split("\n")[0].split(",")
        color1 =[]
        for i in color:
            color1.append(int(i))
        return color1
    def inForntSize(self):
        color = int(self.sourceString[3].split("=")[1].split("\n")[0])
        return color
    def outForntSize(self):
        color = int(self.sourceString[4].split("=")[1].split("\n")[0])
        return color
    def childPerAngle(self):
        color = int(self.sourceString[5].split("=")[1].split("\n")[0])
        return color


