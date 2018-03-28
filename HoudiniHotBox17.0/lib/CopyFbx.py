import hou
class CopyFbx:
    def __init__(self):
        self.fbxNodes =list(hou.selectedNodes())

#############################

        self.path = []

        self.serackNode = []

        self.temp = []
    def serach(self,node):
       
        
       
        try:
            catNode = node.inputs()[0]
            self.temp.append( catNode.name())
            self.serach(catNode)
            a=1
        except:
            pass
         
        return self.temp 
      
    
    
    #######################################
    def serach_node(self,node):
        
        if node.children():
            for childrenNode in node.children():
                
                if childrenNode.children() == ():
                    if childrenNode.type().name() == 'file' or childrenNode.type().name() == 'alembic':
                       
                        
                        
                        nodePath = childrenNode.path()
                        
                        self.path.append(nodePath)
                        self.serackNode.append(childrenNode)
                else:
                    self.serach_node(childrenNode)
                   
                            
    def run(self):                
     
        fl=open('list.txt', 'w')
        
        
        for fbxNode in self.fbxNodes:
            self.serach_node(fbxNode)
            
            
            nodepaths = self.path
            
            comp = 0
            allcomp = len(self.serackNode)
            
            for node in self.serackNode:
                comp +=1
                
                
                self.temp = []
                zu = self.serach(node.parent())
                self.path = node.path()
                
                path1= ""
                for cengji in zu:
                    path1+=("++"+cengji)
                
                    
                
                meterialPath = "++"+node.parent().parm("shop_materialpath").eval().split("/")[-1]
                allPath = self.path +path1+meterialPath
                fl.write(allPath)
                fl.write("\n")
                comping = comp*1.0/allcomp
                print "CurrentNode name is:"+ node.name()+ " Comping: " + str( int(comping*100)) +"%"
                
        fl.close()    
        
        print  "\nCopy node success!!!!"







       