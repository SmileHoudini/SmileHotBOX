import hou
class Cd_Material:
    def __init__(self):
        self.pane=hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        self.node= hou.selectedNodes()[0]
        fl=open('material.txt', 'w')
        fl.write(self.node.path())
        fl.close() 
        
    
    
    def run(self):
        if self.node.type().name() == "material" and self.node.parm("shop_materialpath1").eval() == "":
            
            
            self.pane.cd("/shop")
        elif self.node.type().name() == "material" and self.node.parm("shop_materialpath1").eval() != "":
            try:
                mNode = hou.node(self.node.parm("shop_materialpath1").eval())
                
                mNode.allowEditingOfContents()
                self.pane.cd(mNode.path())
                
            
            except:
                self.pane.cd("/shop")
                
                
        if self.node.type().name() == "geo" and self.node.parm("shop_materialpath").eval() == "":
            
            
            self.pane.cd("/shop")
        elif self.node.type().name() == "geo" and self.node.parm("shop_materialpath").eval() != "":
            try:
                mNode = hou.node(self.node.parm("shop_materialpath").eval())
                
                mNode.allowEditingOfContents()
                self.pane.cd(mNode.path())
                
            
            except:
                self.pane.cd("/shop")                
                
a= Cd_Material()
a.run()