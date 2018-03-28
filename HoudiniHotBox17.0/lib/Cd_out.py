import hou
class Cd_out:
    def __init__(self):
        self.pane=hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        try:
            self.node= hou.selectedNodes()[0]
        except:
            self.node= self.pane.currentNode()
        
        fl=open('material.txt', 'w')
        
        
        fl.write(self.node.path())
        fl.close()
   
    def run(self):
            
        self.pane.cd("/out")