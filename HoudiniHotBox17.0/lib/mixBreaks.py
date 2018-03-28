import hou
color = hou.Color()
color.setRGB((0.9,0.45,0))

color1 = hou.Color()
color1.setRGB((0.9,0,0))

color2 = hou.Color()
color2.setRGB((0.45,0,0.9))

color3 = hou.Color()
color3.setRGB((0,0.4,0))

class mixBreaks:

    def run(self):
        serachName = hou.ui.readInput('Innput constraint name',buttons=['Ok','Cancle'])[1]
        selectNodes = hou.selectedNodes()
        for node in selectNodes:
            posx = node.position()[0]
            posy = node.position()[1]
             
            MixBreak = node.createOutputNode('Mix_break')
            MixBreak.setPosition([posx,posy-2])
            MixBreakConstraint = MixBreak.createOutputNode('mix_break_constraint')
            #mix_break_constraint1.parm('samplediv').set(50)
            
            MixBreakConstraint.setPosition([posx+1,posy-3])
            Assemble = MixBreak.createOutputNode('assemble')
            Assemble.parm('newname').set(0)
            Assemble.parm('pack_geo').set(1)
            Assemble.setPosition([posx-1,posy-3])
            #sctterNode.parm('randomizeorder').set(0)
            #sctterNode.parm('useemergencylimit').set(0)
            #vorNode.setInput(1,sctterNode,0)
            catchToolNode = Assemble.createOutputNode('catche_tool_1.0.1')
            catchToolNode1 = MixBreakConstraint.createOutputNode('catche_tool_1.0.1')
            catchToolNode.createOutputNode('null').setName('Out_pack_'+serachName)
            catchToolNode1.createOutputNode('null').setName('Out_glue_'+serachName)
            catchToolNode.setColor(color1)
            catchToolNode.setSelected(1)
            catchToolNode1.setColor(color1)
            catchToolNode1.setSelected(1)
            node.setSelected(0)
            
            
