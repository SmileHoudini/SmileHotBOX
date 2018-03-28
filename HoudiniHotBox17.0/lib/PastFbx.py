import hou
class PastFbx:
    def __init__(self):
        pass
    def checkNode(self,node, name,temp1 =0):
        for childrenNode in node.parent().children():
            if childrenNode.name() == name:
                temp1 =childrenNode
        return temp1    
    
    def checkInput(self,qian,hou1,temp=0):
        if hou1.inputs() ==():
            pass
        else:    
            for node in hou1.inputs():
                if node == qian:
                    temp =hou1
                else:
                    temp =0
            return temp
    
        
    def creatNode(self,node,temp ):
        for mergeName  in temp:
            
            serachNode = self.checkNode(node, mergeName)
            
            if  serachNode :
                houNode  =  self.checkInput(node, serachNode )
                if  houNode ==0:
            
                    serachNode.setInput(100,node)
                    
                    node = serachNode
                else:
                    node = houNode 
                
            else:
                
                merge = node.createOutputNode("merge",mergeName)
                
                node = merge
    
    
    
    
    
    
    
    
    
    def run(self):
        plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)

        pos = plane.selectPosition()
        pos1 = pos
        node =  plane.currentNode()

        fl1=open('list.txt', 'r')
        a=  len( fl1.readlines())
        check = 0


        fl1.close()
        
    
        for index in range(a):
            pos[0] +=1
            
            try:
                null = node.createNode("object_merge")
               
            except:
                b = node.parent()
                null =b.createNode("object_merge")
              
                
            null.setPosition(pos)
            
            
            
            fl1=open('list.txt', 'r')
            
             
            path = fl1.readlines()[index][0:-1]
            
            allPath= path.split("++")
            
           
            null.parm("objpath1").set(allPath[0])
            
            null.parm("xformtype").set("local")
            
            attNode = null.createOutputNode("attribcreate")
            
            attNode.parm("name1").set("shop_materialpath")
            attNode.parm("type1").set("index")
            attNode.parm("string1").set("/shop/"+ allPath[-1])
            attNode.parm("class1").set("primitive")
            
            catchNode = attNode.createOutputNode("catche_tool_1.0.1")
            
            catchNode.bypass(1)
            
            currentNode =catchNode
            
            
            
            self.creatNode(currentNode,allPath[1:-1] )
            
            
            comping =int((index*1.0/(a-1))*100 )               
            
                  
                  
            
            
            fl1.close()
            print "CreatNode for " + null.name()+","+" Comping: " + str(comping)+"%"
            
            
        print  "\nCopy node success!!!!"
        
