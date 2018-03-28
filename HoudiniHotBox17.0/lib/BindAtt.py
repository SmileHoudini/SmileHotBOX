import hou
class BindAtt:
    def __init__(self):
        pass

    def run(self):
        plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        if plane.pwd().type().name() == "attribvop" :
            
            vopNode = plane.pwd()
            geo = vopNode.geometry()
            atts = ""
            if vopNode.parm("bindclass").eval() == 2:
                atts = list(geo.pointAttribs())
            else:
                atts = list(geo.primAttribs())
            attsName = []
            temp = atts
            for iNode in temp:
                if iNode.name() == "P" or iNode.name() == "v" or iNode.name() == "N"  or iNode.name() == "force" or iNode.name() == "Cd" or iNode.name() == "life" or iNode.name() == "age" or iNode.name() == "uv" or iNode.name() == "id":
                   atts.remove(iNode) 
            [attsName.append(i.name()+"@"+str(i.size())+i.dataType().name()[0].lower()) for i in atts] 
            
            checks = hou.ui.selectFromList(attsName)
            for check in list(checks):
                
                nameString = attsName[check]
                parmSelect = atts[check]
                
                Atttype =  parmSelect.dataType().name()
                attSize = parmSelect.size()
                bindNode = vopNode.createNode("bind")
               
                print nameString
                if nameString.split("@")[1] == "1f":
                    bindNode.parm("parmtype").set(0)
                
                if nameString.split("@")[1] == "2f":
                    bindNode.parm("parmtype").set(5) 
                
                if nameString.split("@")[1] == "3f":
                    bindNode.parm("parmtype").set(6)
                    
                if nameString.split("@")[1] == "1i":
                    bindNode.parm("parmtype").set(1)
                    
                if nameString.split("@")[1] == "1s":
                    bindNode.parm("parmtype").set(15)
                if nameString.split("@")[1] == "4f":
                    bindNode.parm("parmtype").set(11)    
                    
                    
                pos = plane.selectPosition()
                bindNode.setPosition(pos)
                bindNode.parm("parmname").set(parmSelect.name())
                bindNode.setName("In_"+parmSelect.name())
                bindOutNode = bindNode.createOutputNode("bind")
                bindOutNode.parm("useasparmdefiner").set(1)    
                bindOutNode.parm("exportparm").set(2)
                bindOutNode.setInput(0,bindNode,0)
                bindOutNode.parm("parmname").set(parmSelect.name())
                bindOutNode.parm("overridetype").set(1)
                bindOutNode.setName("Out_"+parmSelect.name())
                
        if plane.pwd().type().name() == "popvop" :
            
            vopNode = plane.pwd()
            geo = vopNode.parent().geometry()
            atts = ""
            
            atts = list(geo.pointAttribs())
            attsName = []
            temp = atts
            for iNode in temp:
                if iNode.name() == "P" or iNode.name() == "v" or iNode.name() == "N"  or iNode.name() == "force" or iNode.name() == "Cd" or iNode.name() == "life" or iNode.name() == "age" or iNode.name() == "uv" or iNode.name() == "id":
                   atts.remove(iNode) 
            [attsName.append(i.name()+"@"+str(i.size())+i.dataType().name()[0].lower()) for i in atts] 
            
            checks = hou.ui.selectFromList(attsName)
            for check in list(checks):
                
                nameString = attsName[check]
                parmSelect = atts[check]
                
                Atttype =  parmSelect.dataType().name()
                attSize = parmSelect.size()
                bindNode = vopNode.createNode("bind")
               
                print nameString
                if nameString.split("@")[1] == "1f":
                    bindNode.parm("parmtype").set(0)
                
                if nameString.split("@")[1] == "2f":
                    bindNode.parm("parmtype").set(5) 
                
                if nameString.split("@")[1] == "3f":
                    bindNode.parm("parmtype").set(6)
                    
                if nameString.split("@")[1] == "1i":
                    bindNode.parm("parmtype").set(1)
                    
                if nameString.split("@")[1] == "1s":
                    bindNode.parm("parmtype").set(15)
                if nameString.split("@")[1] == "4f":
                    bindNode.parm("parmtype").set(11)    
                    
                    
                pos = plane.selectPosition()
                bindNode.setPosition(pos)
                bindNode.parm("parmname").set(parmSelect.name())
                bindNode.setName("In_"+parmSelect.name())
                bindOutNode = bindNode.createOutputNode("bind")
                bindOutNode.parm("useasparmdefiner").set(1)    
                bindOutNode.parm("exportparm").set(2)
                bindOutNode.setInput(0,bindNode,0)
                bindOutNode.parm("parmname").set(parmSelect.name())
                bindOutNode.parm("overridetype").set(1)
                bindOutNode.setName("Out_"+parmSelect.name()) 