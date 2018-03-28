import os
import math
import time
import hou
import signal
import shutil
import subprocess

timeStart = time.time()
try:
    os.mkdir(r"C:\render")
except:
    pass
scriptPath = r"C:\render"
pa = r'C://render//renderList0.bat'
renderNode = 0

class MutROP:
    def __init__(self):
        # clear file
        self._allFrame =0
        self.dialog = " "
        try:
            shutil.rmtree(r"C:\render")
            os.mkdir(r"C:\render")
        except:
            pass
    def clearFile(self):
        # clear file
        self.dialog = " "
        try:
            shutil.rmtree(r"C:\render")
            os.mkdir(r"C:\render")
        except:
            pass
    def writeBat(self, divide,_node):
        hipFile = hou.hipFile.path()
        perpythonscript ="import MoutRopPref\nreload(MoutRopPref)\nMoutRopPref.MoutRopPref()"

        renderNode =_node 
        renderPath = 0
        start = 0
        end = 0
        if renderNode.type().name() == "rop_geometry":
            renderPath = renderNode.path()

            renderNode.parm("postframe").set(perpythonscript)
            renderNode.parm("lpostframe").set("python")

            start = renderNode.parm("f1").eval()
            end = renderNode.parm("f2").eval()


        elif renderNode.type().name() == "opengl":
            renderPath = renderNode.path()

            renderNode.parm("postframe").set(perpythonscript)
            renderNode.parm("lpostframe").set("python")

            start = renderNode.parm("f1").eval()
            end = renderNode.parm("f2").eval()


        elif renderNode.type().name() == "filecache":
            renderNode.allowEditingOfContents()
            renderNode = hou.node(renderNode.path() + "/render")

            renderNode.parm("postframe").set(perpythonscript)
            renderNode.parm("lpostframe").set("python")

            renderPath = renderNode.path()

            start = renderNode.parm("f1").eval()

            end = renderNode.parm("f2").eval()

        elif renderNode.type().name() == "catche_tool_1.0.1":
            renderNode = hou.node(renderNode.path() + "/render")

            renderPath = renderNode.path()
            renderNode.parm("postframe").set(perpythonscript)
            renderNode.parm("lpostframe").set("python")

            start = renderNode.parm("f1").eval()
            end = renderNode.parm("f2").eval()

        else:
            print "Is not IO node ex:rop_geometry,filecache,catche_tool_1.0.1"
            return

        totalFrame = (end - start)

        once = math.ceil(totalFrame / divide)

        sourceString2 = []
        fileName2 = scriptPath + "\\" + "run.bat"
        for i in range(divide):
            perStart = (i * once) + start

            perEnd = perStart + once - 1
            if perEnd > end:
                perEnd = end
            if end - perEnd < once / 2:
                perEnd = end
            #print  perStart, "  ", perEnd
            fileName = scriptPath + "\\" + "renderList" + str(i) + ".bat"
            sourceString = ''' "C:\\Program Files\\Side Effects Software\\Houdini 16.0.504.20\\bin\\hython2.7.exe" "C:\\Program Files\\Side Effects Software\\Houdini 16.0.504.20\\bin\\hrender.py" -e -f ''' + str(
                perStart) + " " + str(perEnd) + " -d " + renderPath + " " + hipFile + " && exit [/b] [ExitCode]"

            fl = open(fileName, 'w')

            fl.write(sourceString)
            fl.write("\n")
            fl.close()

            sourceString2.append(scriptPath + "\\" + "renderList" + str(i) + ".bat")
            if (perEnd == end):
                break

        fl = open(fileName2, 'w')
        for source in sourceString2:
            fl.write(source)
            fl.write("\n")

        fl.close()
        self._allFrame = totalFrame
        
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
    
    
    def runBat(self,node):

        a = r"C:\render\run.bat"
        # a = os.path.sep.join(a.split(r'/'))
        f = open(a, "r")
        sourceing = list(f.readlines())
        
        f.close()
        f2 = open(r"C:\render\kill.bat", "w");
        hou.hipFile.save()
        for batsource in sourceing:
            proc = subprocess.Popen(batsource, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    universal_newlines=True, shell=1)
            pid = proc.pid
            f2.write(str(pid) + "\n")
            # os.kill(pid, signal.SIGSEGV)
        f2.close()
        # sleep program
        _a=1
        while(_a):
            
            if (self.getRenderingIndex()) >= self._allFrame+1 :
                _a=0
                print "Current Node ",node.name(),"@","Current Frame ", self.getRenderingIndex(),"/",self._allFrame+1
                print node.name()," end..........................."
                
            else:    
                
                
                print "Current Node ",node.name(),"@","Current Frame ", self.getRenderingIndex(),"/",self._allFrame+1
                
            time.sleep(0.5)
        #clear file
        self.clearFile()
    def run(self):
        global showWindowsMuti
        strNumberarr = hou.ui.readInput('Devide catch number', buttons=['Ok', 'Cancle'])
        strNumber = strNumberarr[1]
        if strNumberarr[0] ==1 :
            return 0
        if  strNumber == "":
            return 0
            
        intNumber = 1
        try:
            intNumber = int(strNumber)
            if intNumber > 10:
                print "warning: Request number is too large, may affect the performance of the machine, it is recommended within 10"
            if intNumber > 30:
                intNumber = 30
                print "warning: Too many requests have been changed to 30 "
            elif intNumber <= 0:
                intNumber = 5
                print "Bad request has been changed to 5"
        except:
            print "it's not int number,ex:1 or 5!"

            return

        divide = intNumber
        
        nodes =  list(hou.selectedNodes())
        for node in nodes:
            print "\n\n"
            print node.name()," start!!!!!!!!!!!!"
            
            self.writeBat(divide,node)
            self.runBat(node)
            renderNode = node
            
        return 1

        
        
