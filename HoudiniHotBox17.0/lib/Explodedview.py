import hou
class Explodedview:
    def __init__(self):
        self._xformArr = []
        self._mergeNode_ = []
        self.xformArr_ =[]
        self.tempArr =[]
        self.keyParmNameArr =["tx","ty","tz","sx","sy","sz","rx","ry","rz","px","py","pz"] 
        self.manSensePath = r"/obj/mainSense/"
        pass
    
    def clearNode(self,objNode,nweMergeNode):
        a=1
                
        xformNode = objNode.outputs()[0]
        if xformNode.type().name() != "merge":
        
            xformNode.setInput(0,nweMergeNode)
            #deleteXformNode
            while(a):
                if xformNode.type().name() == "xform":
                    nextNode = xformNode.outputs()[0]
                    #delete
                    xformNode.destroy()
                    xformNode = nextNode
                else:
                    a=0
        else:
            xformNode.setInput(1000,nweMergeNode)
        objNode.destroy()         
    def serachOutPuts(self,node):
        if node.outputs()[0].type().name() !="merge":
            manSenseXformNode= hou.node( self.manSensePath+ node.outputs()[0].name().split(":::")[1])
            self.tempArr.append(manSenseXformNode)   
            newNode = node.outputs()[0]
            self.serachOutPuts(newNode)
        else:
            return
    def setXformValueFun(self,currentNode,refenceNode,str):
        currentNode.parm(str).setExpression("ch("+'"'+refenceNode.path()+"/"+str+'"'+")",hou.exprLanguage.Hscript)
#        if refenceNode.parm(str).isAtDefault() == 0:
#            if refenceNode.parm(str).keyframes():
#                #currentNode.parm(str).setExpression("ch("+'"'+refenceNode.path()+"/"+str+'"'+")",hou.exprLanguage.Hscript)
#            else:
#                #currentNode.parm(str).set(refenceNode.parm(str).eval())
#        else:
#            pass
        
    def setXformValue(self,currentNode,refenceNode):
        #secColor
        currentNode.setColor(refenceNode.color())
        for  parm in self.keyParmNameArr:
        
            self.setXformValueFun(currentNode,refenceNode,parm)
    
   #head Node 
    def headeNodes(self,hidNode):
        for node in list(hidNode.inputs()):
            xformNode = node.inputs()[0]
                
            a=1
            while(a):
                try:
                    if xformNode.inputs()[0]:
                        nextNode = xformNode.inputs()[0]
                        xformNode.hide(1)
                        xformNode = nextNode
                    else:
                        xformNode.hide(1)
                        a=0
                except:
                    xformNode.hide(1)
                    a=0
    def istopNode(self,node):
        insideNode = hou.node( node.parm("objpath1").eval())
        index = 1
        result =0
        while(index):
            if len( insideNode.inputs())<2 and len( insideNode.inputs()) !=0:
                
                nextNode = insideNode.inputs()[0]   
                insideNode = nextNode
            elif len( insideNode.inputs()) ==0:
               result =1 
               index  =0
            else:
               result =0
               index  =0
               
        return result  
                    
    def creatNode(self,node):
        nodePosition = node.position()
        nodeName     = self._mergeNode_.name()
        self._xformArr.reverse()
        
        if node.outputs():
            if self.istopNode(node) ==0:
                ## add merge out Node in self._xformArr
                self.tempArr =[]
                self.serachOutPuts(node)
                for mainSenseNodeChildren in self.tempArr:
                    self._xformArr.append(mainSenseNodeChildren)
                
               
                ## add merge out Node in self._xformArr  end
                nweMergeNode =  node.parent().createNode("merge",nodeName)
                nweMergeNode.setPosition(nodePosition)
                index = -1
                for inPutMgrge in list( self._mergeNode_.inputs()):
                    inObjNode = nweMergeNode.createInputNode(1000,"object_merge",inPutMgrge.name())
                    inObjNode.parm("objpath1").set(inPutMgrge.path())
                    
                    startOutPutNode = inObjNode
                    
                    for CreatXform in self._xformArr:
                        xformNode = startOutPutNode.createOutputNode("xform","S:::"+CreatXform.name()+":::S")   
                        #setvalue start
                        
                        self.setXformValue(xformNode,CreatXform)
                        pass
                        #setvalue end
                        startOutPutNode = xformNode
                    #conect sets
                    index +=1
                    nweMergeNode.setInput(index,startOutPutNode)
                    
                ##hide node start
                    
                self.headeNodes(nweMergeNode)
                ##hide node end
                 #conect last node
                self.clearNode(node,nweMergeNode)
            else:
                print "Is Topest Node!"
                
                
        else:
            nweMergeNode =  node.parent().createNode("merge",nodeName)
            nweMergeNode.setPosition(nodePosition)
            index = -1
            for inPutMgrge in list( self._mergeNode_.inputs()):
                inObjNode = nweMergeNode.createInputNode(1000,"object_merge",inPutMgrge.name())
                inObjNode.parm("objpath1").set(inPutMgrge.path())
                
                startOutPutNode = inObjNode
                
                for CreatXform in self._xformArr:
                    xformNode = startOutPutNode.createOutputNode("xform","S:::"+CreatXform.name()+":::S")   
                    #setvalue start
                    self.setXformValue(xformNode,CreatXform)
                    #setvalue end
                    startOutPutNode = xformNode
                #conect sets
                index +=1
                nweMergeNode.setInput(index,startOutPutNode)   
    
    def recoad_xformArr(self,_XformNode):    
        if _XformNode.type().name() == "xform":
            self._xformArr.append(_XformNode)
            nextNode = _XformNode.inputs()[0]
            self.recoad_xformArr(nextNode)
            
        elif _XformNode.type().name() == "merge" and len(_XformNode.inputs()) == 1:
            nextNode = _XformNode.inputs()[0]
            self.recoad_xformArr(nextNode)
        else:
            self._mergeNode_ = _XformNode
            
            
             
                 
    def findCurrentRootTree(self,node):
        if node.type().name() == "merge":
            #stratWork
            _node = hou.node( node.parm("objpath").eval())
            #find _mergeNode  and recoad _mergeNode outPut Transform
            
        else:#node is xform
            _node = hou.node( node.parm("objpath1").eval())
            #find _mergeNode  and recoad _mergeNode outPut Transform
            
            
            #init self._xformArr
            self._xformArr = []
            self._mergeNode_ = []
            exMergeNode = self.recoad_xformArr(_node)
           
            # creat inputNode
            self.creatNode(node)    
    
    def run(self):
        selectNodes = list(hou.selectedNodes())
        
        for node in selectNodes:
            
            if node.type().name() =="xform":
                a= 1    
                while(a):
                    
                    if node.type().name() == "xform":
                        nextNode = node.inputs()[0]
                   
                    
                        node = nextNode
                    else:
                        
                        a=0
                    
                self.findCurrentRootTree(node)      
            else:    
                self.findCurrentRootTree(node)            
