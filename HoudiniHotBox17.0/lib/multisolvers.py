import hou

class multisolvers:
    def __init__(self):
        a=1
    
    def addgeosover(self):
        selectNode =  hou.selectedNodes()[0]
        outNode = selectNode.outputs()[0]
        inputNode = selectNode.inputs()[0]
        mNode =  outNode.createInputNode(0,"multisolver")
        mNode.setInput(0,inputNode)
        
        mNode.setInput(1,selectNode)
        nullNode = selectNode.createInputNode(0,"null")
        nullNode.destroy()
        mNode.createInputNode(2,"rbd_sencond_cut")
    
    def addgluesover(self):
    
        selectNode =  hou.selectedNodes()[0]
        selectNode.createInputNode(2,"glue_deleteBy_SOPatt")
    
    
    def addpinsover(self):
        selectNode =  hou.selectedNodes()[0]        
        selectNode.createInputNode(2,"constraint_pin_sover")
        
        
        
    def run(self):
        selectNode =  hou.selectedNodes()[0]
        if  selectNode.type().name() ==   "bulletrbdsolver" :
            
            self.addgeosover()
        else:
            if selectNode.inputs()[1].type().name() == "glueconrel":
               self.addgluesover()
               
            else :
                selectNode.inputs()[1].type().name() == "hardconrel"
            
                self.addpinsover()
           