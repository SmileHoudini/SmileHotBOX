import os
import sys

class Open_Master():
    def __init__(self):
        self.ex =0      
    def run(self):
        global hotBoxManUiCountrlShow            
        #os.popen(sysPath +"\\hotBox_17_manUi_countrl.exe")
        import hotBox_17_manUi_countrl
        
        reload(hotBox_17_manUi_countrl)
        hotBoxManUiCountrlShow = hotBox_17_manUi_countrl.Example()