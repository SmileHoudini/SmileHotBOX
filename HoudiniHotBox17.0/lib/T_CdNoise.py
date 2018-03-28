import hou
class T_CdNoise:	
    def __init__(self):
        self.noise =5 			
    def run(self):
        node =list( hou.selectedNodes())[0]
        vopNode = node.createOutputNode("attribvop")
        a= vopNode.children()[0]
        b= vopNode.children()[1]
       
        noiseNode =  vopNode.createNode("turbnoise")
        noiseNode.setInput(1,a,0)
        b.setInput(3,noiseNode,0)
        noiseNode.moveToGoodPosition()
        vopNode.setDisplayFlag(1)
        vopNode.setRenderFlag(1)
        vopNode.setTemplateFlag(1)
        node.setTemplateFlag(0)
 