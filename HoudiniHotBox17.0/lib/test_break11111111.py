import hou 
class test_break11111111 : 
    def run(self):  
        InstallSelectNode = list( hou.selectedNodes())[0]  
        s_plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        s_pos = s_plane.selectPosition()
        s_parent_node =s_plane.pwd() 
        ##Strat creat SopNodegeo4__null2
        SopNodegeo4__null2=s_parent_node.createNode('null')
        ##End creat SopNodegeo4__null2
        
        ##Strat creat SopNodegeo4__scatter1
        SopNodegeo4__scatter1=s_parent_node.createNode('scatter::2.0')
        ##End creat SopNodegeo4__scatter1
        
        ##Strat creat SopNodegeo4__voronoifracture1
        SopNodegeo4__voronoifracture1=s_parent_node.createNode('voronoifracture')
        ##End creat SopNodegeo4__voronoifracture1
        
        ##Strat creat SopNodegeo4__pointwrangle1
        SopNodegeo4__pointwrangle1=s_parent_node.createNode('attribwrangle')
        ##End creat SopNodegeo4__pointwrangle1
        
        ##Strat creat SopNodegeo4__null1
        SopNodegeo4__null1=s_parent_node.createNode('null')
        ##End creat SopNodegeo4__null1
        
        ##Strat connect SopNodegeo4__null1
        ##End connect SopNodegeo4__null1
        
        ##Strat connect SopNodegeo4__null1
        SopNodegeo4__scatter1.setInput(0,SopNodegeo4__null2,0)
        ##End connect SopNodegeo4__null1
        
        ##Strat connect SopNodegeo4__null1
        SopNodegeo4__voronoifracture1.setInput(0,SopNodegeo4__null2,0)
        SopNodegeo4__voronoifracture1.setInput(1,SopNodegeo4__scatter1,0)
        SopNodegeo4__voronoifracture1.parm('depthnoisescaleramp2pos').set(1.0)
        SopNodegeo4__voronoifracture1.parm('depthnoisescaleramp2value').set(1.0)
        ##End connect SopNodegeo4__null1
        
        ##Strat connect SopNodegeo4__null1
        SopNodegeo4__pointwrangle1.setInput(0,SopNodegeo4__voronoifracture1,0)
        SopNodegeo4__pointwrangle1.parm('snippet').set('@Cd.r = 0.5;')
        ##End connect SopNodegeo4__null1
        
        ##Strat connect SopNodegeo4__null1
        SopNodegeo4__null1.setInput(0,SopNodegeo4__pointwrangle1,0)
        ##End connect SopNodegeo4__null1
        
        SopNodegeo4__null2.setDisplayFlag(True)
        s_pos[1]-=1
        SopNodegeo4__null2.setPosition(s_pos)
        s_pos[1]-=1
        SopNodegeo4__scatter1.setPosition(s_pos)
        s_pos[1]-=1
        SopNodegeo4__voronoifracture1.setPosition(s_pos)
        s_pos[1]-=1
        SopNodegeo4__pointwrangle1.setPosition(s_pos)
        s_pos[1]-=1
        SopNodegeo4__null1.setPosition(s_pos)
        try:  
            SopNodegeo4__null2.setInput(0,InstallSelectNode, 0)  
        except:  
            pass  
