import hou
import os
class RenderPath:
    def __init__(self):
        self.node_sel = hou.selectedNodes()
    def set_parm(self):
        for node in self.node_sel:
          
            
            if node.parm('ver') not in node.parms():
                add_parm = hou.StringParmTemplate('ver', 'Version', 1, ('v001',))

                parm_group = node.parmTemplateGroup()
                parm_group.insertBefore('vm_picture', add_parm)
                node.setParmTemplateGroup(parm_group)
            change_file = node.setParms(
                    {"vm_picture": "$HIP/render" + '''/$OS/`chs("ver")`/$HIPNAME.$OS.$F4.exr'''})
                
                          
    def get_path_y(self):
        path_x = hou.hipFile.path()
        path_x = path_x.split("CG")[0]
        pathArr = path_x.split("/")
        pathArr[0] = "W:"
        pathArr[-1] = "Zup_renders/Effects/Elements" 
        str1 = "/"
        path = str1.join(pathArr)
        return path
                    
                        
    def run(self):
        self.set_parm()