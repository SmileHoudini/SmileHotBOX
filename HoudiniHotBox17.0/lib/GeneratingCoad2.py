def AsCoadMainOfNode(f,nodes):
    checkParentCreat =0
    secondParent =0
    InstallNodeName = ""
    for child in nodes:
          
        a= child.asCode()
        aSp =a.split("\n")
        #check first parent can be creat
        if checkParentCreat  == 0:
            clearLine = 0
            for i in aSp:
                i+= "\n"
                checkParent ="    hou_parent = hou.node"
                checkChild ="    hou_node = hou.node"
                checkMove = "hou_node.move"
                
                if  clearLine ==0 :
                    try:
                        checkDefParm2 = i.split("\n")[0].split(" ")[-2]
                        
                    except:
                        checkDefParm2 ="None"
                    
                    ###eval def parm
                    try:
                        if  i.split("\n")[0].split(" ")[-2] =="parm":
                            checkDefParm1 = child.parm( i.split(" ")[-3].split("/")[-1]).isAtDefault()
                    except:
                        pass
                    #####    checkParent
                    if i[0:len(checkParent)] == checkParent:
                       
                        f.write("    hou_parent = s_parent_node\n")
                    elif i[0:len(checkChild)] == checkChild:
                        f.write("    pass\n")
                    elif i[0:len(checkMove)] == checkMove:
                        f.write("hou_node.move(s_pos)\n")    
                    
                    #clearParm
                    elif checkDefParm2 =="parm" and checkDefParm1 == 1:
                        clearLine = 7
                    elif checkDefParm2 == "parm" :
                        clearLine = 3
                    # #clearParm end
                    else:
                        
                        if i == "\n":
                            pass
                        else:    
                            f.write(i)
                checkParentCreat +=1
                 
                
                if clearLine>0:
                    clearLine -=1
            f.write("s_pos[1]-=1\n")     
            f.write("fatherConectNode_"+child.name()+ " = hou_node\n")
            InstallNodeName ="fatherConectNode_"+child.name()
            f.write("\n")
            f.write("#write +++++++++++"+ child.name()+" end\n")
            f.write("\n\n\n")
            
            
            
        elif checkParentCreat >0 :
            clearLine = 0
            for i in aSp:
                i+= "\n"
                checkParent ="    hou_parent = hou.node"
                checkChild ="    hou_node = hou.node"
                checkMove = "hou_node.move"
                checkInput ="    hou_node.setInput"
                checkConnectNode = "hou_node = hou_parent.node"
                if  clearLine ==0 :
                    try:
                        checkDefParm2 = i.split("\n")[0].split(" ")[-2]
                    except:
                        checkDefParm2 ="None"
                    ###eval def parm
                    try:
                        if  i.split("\n")[0].split(" ")[-2] =="parm":
                            checkDefParm1 = child.parm( i.split(" ")[-3].split("/")[-1]).isAtDefault()       
                    except:
                        pass    
                    #####  checkParent    
                    if i[0:len(checkParent)] == checkParent :
                        
                        f.write("    hou_parent = s_parent_node\n")
                    
                        
                    elif i[0:len(checkChild)] == checkChild:
                        f.write("    pass\n")
                    elif i[0:len(checkMove)] == checkMove:
                        
                        f.write("hou_node.move(s_pos)\n") 
                    elif i[0:len(checkConnectNode)] == checkConnectNode:
                        f.write("\n")
                        
                    elif i[0:len(checkInput)] == checkInput:
                        f.write("    pass\n")
                        arryi = i.split(",")
                        childIndexName = arryi[1].split("node")[-1][2:-2]
                        f.write(arryi[0][4:]+","+"fatherConectNode_"+childIndexName+","+arryi[2])
                    
                    #clearParm
                    elif checkDefParm2 =="parm" and checkDefParm1 == 1:
                        clearLine = 7
                    elif checkDefParm2 == "parm" :
                        clearLine = 3
                    # #clearParm end
                    
                    else:
                        if i == "\n":
                            pass
                        else:    
                            f.write(i)
                if clearLine>0:
                    clearLine -=1
            f.write("s_pos[1]-=1\n")
            
            f.write("fatherConectNode_"+child.name()+ " = hou_node\n")
            f.write("\n")
            f.write("#write +++++++++++"+ child.name()+" end\n")
            f.write("\n\n\n")    
        if child.type().name() == "attribvop":
                childNodes= child.children()
                vopFatherConnectName = "fatherConectNode_"+ child.name()
                for vopNode in childNodes:
                    vopNodeName ="vopNode"+vopNode.name()
                    vopTypeName = vopNode.type().name()
                    f.write( vopNodeName+"="+vopFatherConnectName+".createNode("+"'"+vopTypeName+"'"+")\n")
                    
                for vopNode in childNodes:
                    vopNodeName ="vopNode"+vopNode.name()
                    vopTypeName = vopNode.type().name()    
                    for vopParm in list(vopNode.parms()):
                        if vopParm.isAtDefault() ==1:
                            pass
                        else:
                            vopParmValue = vopParm.eval() 
                            vopParmName =  vopParm.name()
                            if isinstance(vopParmValue, str):
                                f.write( vopNodeName+".parm("+"'"+ vopParmName+"'"+")"+".set("+"'" +str(vopParmValue)+"'"+")\n")
                            else:
                                f.write( vopNodeName+".parm("+"'"+ vopParmName+"'"+")"+".set("+str(vopParmValue)+")\n")
                
                
                for vopNode in childNodes:
                    vopNodeName ="vopNode"+vopNode.name()
                    vopTypeName = vopNode.type().name()
                    for con in list(vopNode.inputConnections()):
                        inpuIndex =   con.inputIndex()
                        inputNode =  con.inputNode()
                        outputIndex = con.outputIndex()
                        f.write( vopNodeName+".setInput("+str(inpuIndex)+","+"vopNode"+inputNode.name()+","+str(outputIndex)+")\n")   


    return InstallNodeName                    
                        
                        
class GeneratingCode2:
    def run(self):
        nodes = list(hou.selectedNodes())
        serachName = hou.ui.readInput('Innput Python Script name',buttons=['Ok','Cancle'])[1]
        ascoadName =serachName
        ascoadPath = r"C:\PythonLibs\HoudiniHotBox17.0\lib" +"\\"+ ascoadName+".py"
        f=open(ascoadPath,"w")
        
        f.write("s_plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)\n")
        f.write("s_pos = s_plane.selectPosition()\n")
        
        f.write("s_parent_node =s_plane.pwd() \n")
        InstallNodeName = AsCoadMainOfNode(f,nodes)
        f.close()
        f=open(ascoadPath,"r")
        sourcePy=f.readlines()
        f.close()
        f=open(ascoadPath,"w")
        f.write("import hou \n")
        f.write("class "+ascoadName+" :" +" \n")
        f.write("    def run(self):  \n")
        f.write("        InstallSelectNode = list( hou.selectedNodes())[0]  \n")
        
        for line in list( sourcePy):
            lineNew = "        "+line
            f.write(lineNew)
             
        f.write("        try:  \n")
        f.write("            "+InstallNodeName+".setInput(0,InstallSelectNode, 0)"+"  \n")
        f.write("        except:  \n")
        f.write("            pass  \n")
        f.close()
        