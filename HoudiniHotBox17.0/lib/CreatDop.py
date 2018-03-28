import hou
class CreatDop:
    def __init__(self):
    
        self.plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        
        self.pos = self.plane.selectPosition()
        self.pos1 = self.pos
        self.node = self.plane.currentNode()
        
        try:
            self.dopNode =self.node.createNode("dopnet")
               
        except:
            self.a = self.node.parent()
            self.dopNode =self.a.createNode("dopnet")
    
    def run(self):
        self.dopNode.setPosition(self.pos)  
        self.dopNode.setName("dopNode_rbd")
        
        
        for node in  self.dopNode.children():
            if node.name() == "output":
                mergeNode =node.createInputNode(0,"gravity").createInputNode(0,"bulletrbdsolver").createInputNode(0,"merge")
                mergeNode.setName("mergeRbd")
    
