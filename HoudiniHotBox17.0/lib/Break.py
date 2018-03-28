import hou
color = hou.Color()
color.setRGB((0.9,0.45,0))

color1 = hou.Color()
color1.setRGB((0.9,0,0))

color2 = hou.Color()
color2.setRGB((0.45,0,0.9))

color3 = hou.Color()
color3.setRGB((0,0.4,0))
class Break:
    def __init__(self):
        pass

    def run(self):
        
        selectNodes = hou.selectedNodes()
        for node in selectNodes:
            posx = node.position()[0]
            posy = node.position()[1]
             
            vorNode = node.createOutputNode('voronoifracture')
            vorNode.setPosition([posx,posy-3])
            isoNode = node.createOutputNode('isooffset')
            isoNode.parm('samplediv').set(50)
            
            isoNode.setPosition([posx+1,posy-1])
            sctterNode = isoNode.createOutputNode('scatter')
            sctterNode.parm('npts').set(100)
            sctterNode.parm('relaxpoints').set(0)
            sctterNode.parm('randomizeorder').set(0)
            sctterNode.parm('useemergencylimit').set(0)
            vorNode.setInput(1,sctterNode,0)
            
            node.setSelected(0)
    
