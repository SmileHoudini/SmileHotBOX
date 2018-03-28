import hou
class Cd_Object:
    def __init__(self):
        self.pane=hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        
    
    
    
    def run(self):
        f1 = open('material.txt', 'r')
        a=   f1.readlines()[0]
        a=hou.node(a).parent().path()
        
        f1.close()
        self.pane.cd(a)