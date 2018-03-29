import os

class getButton:
    def __init__(self,className):
        self.classNmae1 =className
        self.s_path = os.getenv('SMILEHOTBOX')+r"/pref"
        self.prefPath = self.s_path+r"/"+self.classNmae1+r"/button/"
        self.fatherBPath = self.prefPath+"fatherButtonNum.dat"
        self.fatherButtonNum =5
        self.setFatherButtonNum()

    def setFatherButtonNum(self):
        f1= open(self.fatherBPath,"r" )
        self.fatherButtonNum =int ( f1.readlines()[0].split("=")[1])
        f1.close()
    # fatherall
    def getFatherButtonNum(self):
        return self.fatherButtonNum
    #index is father total numb 
    def getButton_indexInfo(self,index):

        indexStr= str(index)
        button_indexPath =  self.prefPath +"button_"+indexStr+".data"
        f1= open(button_indexPath,"r" )
        fileString = f1.readlines()
        fatherLab=fileString[0].split("=")[1]
        fatherLabIconName=fileString[0].split("=")[2].split("\n")[0]
        childNumber =int(fileString[1].split("=")[1])
        labarr=[]
        for i in range(childNumber):
            arr =[]
            name= fileString[i+2].split("=")[1].split("\n")[0]
            icon =fileString[i+2].split("=")[2].split("\n")[0]
            arr =[name,icon]

            labarr.append(arr)

        arryData =[fatherLab,fatherLabIconName,childNumber,labarr]
        f1.close()
        return arryData

#b= getButton("Sop")
#print  b.getFatherButtonNum()
#for i in range(b.getFatherButtonNum()):

    #print b.getButton_indexInfo(i)

