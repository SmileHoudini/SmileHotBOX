import hou

class FlipBookMultRnder:
    def MakeFlipBook(self):
        strNumberarr = hou.ui.readInput('Input FlipBookName', buttons=['Ok', 'Cancle'])
        strNumber = strNumberarr[1]
        if strNumberarr[0] ==1 :
            return 0
        if  strNumber == "":
            return 0
        
        plane = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
        vie = plane.curViewport()
        camPath = vie.camera().path()
        camName = vie.camera().name()
        outNode = hou.node("/out/")
        opglNode  = outNode.createNode("opengl")
        opglNode.setName("FlipBook_"+strNumber,1)
        opglNode.parm("camera").set(camPath)
        opglNode.parm('trange').set("normal")
        opglNode.parm("f1").setExpression("$FSTART")
        opglNode.parm("f2").setExpression("$FEND")
        
        picPath = "$HIP/FlipBook/"+camName+"/"+"$OS/$HIPNAME.$OS.$F4.exr"
        opglNode.parm("picture").set(picPath)
        plane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
        plane.cd("/out/")
        opglNode.setSelected(1)
        plane.homeToSelection()
	return 1	
    def run(self):
           	
        afl= self.MakeFlipBook()
	if afl == 0:
	    pass
	else:
            import MutRopUI
	    selectM = MutRopUI.MutROP()
	    checkOpen = selectM.run()
	    if checkOpen ==1:
	
	        import MutRopUI2
	        reload (MutRopUI2)
        