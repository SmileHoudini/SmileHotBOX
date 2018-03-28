import hou
class Copy_Node:    
    def copy1(self):   
        nodes = hou.selectedNodes()        
        fl=open('list.txt', 'w')
        for node in nodes:        
            nodepath = node.path()            
            fl.write(nodepath )
            fl.write("\n")        
        fl.close()    
    def past1(self):
        plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        pos = plane.selectPosition()
        pos1 = pos
        node =  plane.pwd()     
        fl1=open('list.txt', 'r')
        a=  len( fl1.readlines())
        fl1.close()
        writeNodeName = ""
        if node.path() == "/obj":
            writeNodeName = hou.ui.readInput('Innput GeoNode Name: ',buttons=['Ok','Cancle'])[1]
        for index in range(a):            
            try:
                
                
                fl1=open('list.txt', 'r')             
                path = fl1.readlines()[index][0:-1]
                fl1.close()
                
                if hou.node(path).type().name() == "catche_tool_1.0.1":
                    null = node.createNode("file")
                    catchNode = hou.node(path)
                    rangeTagNum = catchNode.parm("trange").eval()
                    CathPath =""
                    if rangeTagNum ==0:
                        CathPath =  catchNode.parm("out_put_file0").eval()
                    else:
                        CathPath = catchNode.parm("out_put_file1").eval()
                        
                        tempPath =  CathPath.split(".")
                        
                        tempPath[-3] = "$F4"
                        str1 = "."
                        CathPath =str1.join(tempPath)
                        
                    null.parm("file").set(CathPath)
                else:    
                    null = node.createNode("object_merge")
                    
                    null.parm("objpath1").set(path)
                null.setPosition(pos)                
                color = hou.Color()
                color.setRGB((0.45,0,0.9))
                try:
                    null.setName("Merge_"+path.split("/")[-1],1)
                    null.setColor(color)
                except:
                    pass
                
                pos[0] +=3
            except:
                geoNode = node.createNode("geo",writeNodeName)
                geoNode.children()[0].destroy()
                null= geoNode.createNode("object_merge")                 
                geoNode.setPosition(pos)      
                fl1=open('list.txt', 'r')             
                path = fl1.readlines()[index][0:-1]
                null.parm("objpath1").set(path)
                color = hou.Color()
                color.setRGB((0.45,0,0.9))
                try:
                    null.setName("Merge_"+path.split("/")[-1],1)
                    null.setColor(color)
                except:
                    pass
                fl1.close()
                pos[0] +=3
                
    def run(self):
        nodes = hou.selectedNodes()
        
        if len(nodes)>0:
            self.copy1()
        else:
            self.past1()