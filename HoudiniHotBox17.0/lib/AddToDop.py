import hou
selNodes =list( hou.selectedNodes())
class AddToDop:
    def __init__(self):
        pass
    def checkPrmType(self,node):
        geo = node.geometry()
        pr = geo.prims()[0]
        typeName = pr.type().name()
        
        if typeName == "Polygon":
            constraintName =pr.attribValue("constraint_name")
            if constraintName == "glue":
                return 1
            else:
                return 2
            
        else:
            if typeName == "PackedPrim" or typeName =="PackedFragment":
                return 0
    
    def addRBD(self,node,selNode):
        path = "../../"+selNode.name()
        rbdpackobjectNode = node.createInputNode(100,"rbdpackedobject")
        rbdpackobjectNode.parm("soppath").set(path)
        
    def addGlue(self,node,selNode):
        path = "../../"+selNode.name()
        inputNode = node.inputs()[0]
        
        constraintNode =  node.createInputNode(0,"constraintnetwork")
        constraintNode.setInput(0,inputNode,0)
        glueNode = constraintNode.createInputNode(1,"glueconrel")
        glueNode.parm("dataname").set("glue")
        constraintNode.parm("soppath").set(path)
        
    def addPin(self,node,selNode):
    
        path = "../../"+selNode.name()
        inputNode = node.inputs()[0]
        
        constraintNode =  node.createInputNode(0,"constraintnetwork")
        constraintNode.setInput(0,inputNode,0)
        pinNode = constraintNode.createInputNode(1,"hardconrel")
        pinNode.parm("dataname").set("pin")
        pinNode.parm("restlength").set(0)
        constraintNode.parm("soppath").set(path)
        constraintNode.parm("usetransform").set(1)
        constraintNode.parm("reloadfromsops").deleteAllKeyframes()
        constraintNode.parm("reloadfromsops").setExpression("$FF==$RFSTART")
        
                
    def run(self):
        selNodes =list( hou.selectedNodes())
        for selNode in selNodes:
            for dopNode in selNodes[0].parent().children():
                if dopNode.name() == "dopNode_rbd":
                     for node in  dopNode.children():
                        if node.name() == "output" and self.checkPrmType(selNode) == 1:
                            self.addGlue(node,selNode)
                        if node.name() == "output" and self.checkPrmType(selNode) == 2:
                            self.addPin(node,selNode)    
                        if node.name() == "mergeRbd" and self.checkPrmType(selNode) == 0:
                            self.addRBD(node,selNode)    
    
