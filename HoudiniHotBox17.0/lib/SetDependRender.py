import os
import sys

class SetDependRender():
    def __init__(self):
        self.ex =0      
    def run(self):
        
        
        sys.path.append(r"C:\Program Files\RedPack\pipeline\houdini\python_Lib2.7\subdepend")
	import mainUi
        
        reload(mainUi)
 