import os

class getColor:
    def __init__(self):
        self.classNmae1 ="publicCountrl"
        self.s_path = os.getenv('SMILEHOTBOX')+r"/pref"
        self.prefPath = self.s_path +r"/"+self.classNmae1+r"/color/"
        self.fatherBPath = self.prefPath+"color.dat"
        self.sourceString = ""
        self.setString()
    def setString(self):
        f1= open(self.fatherBPath,"r" )
        self.sourceString = f1.readlines()
        f1.close()
    def getLineColor(self):
        color = self.sourceString[0].split("=")[1].split("\n")[0].split(",")
        color1 =[]
        for i in color:
            color1.append(int(i))
        return color1
    def getSelectColor(self):
        color = self.sourceString[1].split("=")[1].split("\n")[0].split(",")
        color1 =[]
        for i in color:
            color1.append(int(i))
        return color1
    def getInsideColor(self):
        color = self.sourceString[2].split("=")[1].split("\n")[0].split(",")
        color1 =[]
        for i in color:
            color1.append(int(i))
        return color1
    def getOitsideColor(self):
        color = self.sourceString[3].split("=")[1].split("\n")[0].split(",")
        color1 =[]
        for i in color:
            color1.append(int(i))
        return color1
    def lineWidth(self):
        color = int(self.sourceString[4].split("=")[1].split("\n")[0])
        return color

    def inForntColor(self):
        color = self.sourceString[5].split("=")[1].split("\n")[0].split(",")
        color1 =[]
        for i in color:
            color1.append(int(i))
        return color1
    def outForntColor(self):
        color = self.sourceString[6].split("=")[1].split("\n")[0].split(",")
        color1 =[]
        for i in color:
            color1.append(int(i))
        return color1

    def selectForntColor(self):
        color = self.sourceString[7].split("=")[1].split("\n")[0].split(",")
        color1 =[]
        for i in color:
            color1.append(int(i))
        return color1
#a=getColor()
#print  a.getLineColor(),a.getLineColor(),a.getInsideColor(),a.lineWidth()