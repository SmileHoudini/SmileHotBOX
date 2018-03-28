import hou
import os
class openMantraPicread:
    def run(self):
        node = hou.selectedNodes()[0]
        PathParm = node.parm("vm_picture").eval()
        PathParm =PathParm.split(".")[0:-2]
        PathParm.append("$F4.exr")
        path = ""
        for i in PathParm:
            path+=i
            path+="."
	try:
            os.mkdir(r"c:\openpic")
        except:
            pass
        f1 = open(r"C:\openpic\mplay.bat","w")
        
        
        path =r'"C:\Program Files\Side Effects Software\Houdini '+hou.applicationVersionString()+r'\bin\mplay.exe" ' + path[0:-1] +" && exit [/b] [ExitCode]"
        
        f1.write("@echo off \n")
        f1.write(path)
        f1.close

import subprocess
class OpenPicMainTest:
    def run(self):
        a=   openMantraPicread()
        a.run()
        subprocess.Popen("cmd.exe /c" + "c:\\openpic\\mplay.bat && exit")