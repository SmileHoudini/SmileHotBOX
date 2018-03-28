import os
import sys

class OpCGTeamWork():
    def __init__(self):
        self.ex =0      
    def run(self):
        global CGt
        #os.popen(sysPath +"\\hotBox_17_manUi_countrl.exe")
        sys.path.append(r"C:\Program Files\RedPack\pipeline\houdini\python_Lib2.7\CGTmW\publish_CGTm")
	import openUI
        
        reload(openUI)
        #CGt= openUI.open_publish()
	#CGt.publish_UI()
	#CGt.show() 