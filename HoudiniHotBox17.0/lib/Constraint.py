import hou
class Constraint:
    def run(self):
        selectNodes =  hou.selectedNodes()
        temp = 0
        posx = 0
        for node in selectNodes:
            
            posx+=node.position()[0]
        
        
        posMiddle1 = posx/len(selectNodes)    
        posMiddle2 = selectNodes[0].position()[1]
        
        
        
        
        
        for node in selectNodes:
            temp +=1
            
            
            global mergeNode 
            
            
            if temp <=1:
                mergeNode = node.createOutputNode("merge")
            
            else:
                mergeNode.setInput(100,node)
                
        mergeNode.setPosition([posMiddle1,posMiddle2-2])
        
        
        mergeNode.createOutputNode("Constraint_generator").createOutputNode("null")
