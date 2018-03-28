import hou
class T_PosNose:
    def run(self):
        node =list( hou.selectedNodes())[0]
        vopNode = node.createOutputNode("attribvop")
        
        
        a= vopNode.children()[0]
        b= vopNode.children()[1]
       
        noiseNode =  vopNode.createNode("turbnoise")
        noiseNode.parm("signature").set("v")
        addNode  = vopNode.createNode("add")
        
        
        noiseNode.setInput(1,a,0)
        addNode.setInput(0,a,0)
        
        b.setInput(0,addNode,0)
        addNode.setInput(1,noiseNode,0)
        
        
        noiseNode.moveToGoodPosition()
        addNode.moveToGoodPosition()
        vopNode.setDisplayFlag(1)
        vopNode.setRenderFlag(1)
        vopNode.setTemplateFlag(1)
        node.setTemplateFlag(0)
        pane=hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        pane.cd(vopNode.path())