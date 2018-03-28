

#Merge all the selected nodes. 
#Please set the hotkey as 'm', just like NUKE.  Monci 201608 QQ287707452

import hou
class Merge:

    def run(self):
        try:
            nodes = hou.selectedNodes()
            
            if len(nodes)!=0:
                pane=hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
                pos = pane.selectPosition()
            
            merge = nodes[0].parent().createNode('merge')
            merge.setPosition(pos)
            merge.setRenderFlag(1)
            merge.setDisplayFlag(1)
            
            for i in range(len(nodes)):
                nodes[i].setSelected(0)
                merge.setInput(i,nodes[i])
        except:
            pass
            
            
a= Merge()
a.run()