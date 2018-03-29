import time
timeStart = time.time()

import os
import math
scriptPath =r"C:\PythonLibs\HoudiniHotBox17.0\ScriptUi"
def writeBat(divide):
    hipFile = hou.hipFile.path()
    renderNode = list(hou.selectedNodes())[0]
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
    once= math.ceil(totalFrame/divide)
    sourceString2 =[]
    fileName2 = scriptPath+r"/"+"run.bat"
    for i in range(divide):
        perStart = (i*once)+start
        perEnd = perStart+once-1
        if perEnd> end:
            perEnd =end
        if end-perEnd< once/2:
            perEnd =end    
        print  perStart ,"  ",perEnd
        version = hou.applicationVersion()
        fileName =  scriptPath+r"/"+"renderList"+str(i)+".bat"
        runPath = str(version[0])+"."+str(version[1])+"."+str(version[2])
        sourceString =''' r"C:/Program Files/Side Effects Software/Houdini '''+runPath+'''r/bin/hython2.7.exe" r"C:/Program Files/Side Effects Software/Houdini '''+runPath+'''r/bin/hrender.py" -e -f ''' +  str(perStart) +" "+ str(perEnd) +" -d " +renderPath+" "+hipFile +" && exit [/b] [ExitCode]"
        fl=open(fileName, 'w')
        fl.write(sourceString )
        fl.write("\n")      
        fl.close()
        sourceString2.append("start "+ scriptPath+r"/"+"renderList"+str(i)+".bat" )
        if(perEnd ==end):
            break
    fl=open(fileName2, 'w')
    for source in sourceString2:
        fl.write(source)
        fl.write("\n") 
    fl.close()
def runBat():
    a= r"C:\render\run.bat"
    a = os.path.sep.join(a.split(r'/'))
    os.system(a)
def run1():
    strNumber = hou.ui.readInput('Devide catch number',buttons=['Ok','Cancle'])[1]
    intNumber =1;
    try:
        intNumber = int(strNumber)
        if intNumber >10:
            print "warning: Request number is too large, may affect the performance of the machine, it is recommended within 10"
        if intNumber >30:
            intNumber =30
            print "warning: Too many requests have been changed to 30 "
        elif  intNumber<=0:
            intNumber =5
            print "Bad request has been changed to 5"
    except:
        print "it's not int number,ex:1 or 5!"
        return
    divide =intNumber
    writeBat(divide)
    runBat()



################################################################
class ClassRender:
    def run(self):
        run1()

		
        
    
