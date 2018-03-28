import hou
import math
import os

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys


class ReloadSense:
    def __init__(self):
        self.Root = ""
        self.xmlPath = ""
        self.isLoadXml = 0
        # cam
        self.nullNode = ""
        self.cameraNode = ""
        self.setKframePref()
        
        self.FPS = 24.0
        self.FStart = 1001
        self.FEnd = 1240
        self.With = 2048
        self.Hight = 1152
        self.GlobalSet = {}
        ##
        self.abcReferenceDict = {}
        self.manSenseNode = 0
        self.topNode = 0
        pass

    def setXmlPath(self, path):
        # Input xmlPath
        self.xmlPath = path

    def setKframePref(self):
        self.hou_keyframe = hou.Keyframe()
        self.hou_keyframe.setSlope(0)
        self.hou_keyframe.setInSlope(0)

        self.hou_keyframe.setAccel(1)
        self.hou_keyframe.setInAccel(1)
        self.hou_keyframe.interpretAccelAsRatio(False)
        self.hou_keyframe.setExpression("bezier()", hou.exprLanguage.Hscript)
        #self.hou_keyframe.setSlopeAuto(True)
        

    def realoadRoot(self):
        try:
            tree = ET.parse(self.xmlPath)
            self.Root = tree.getroot()
            self.isLoadXml = 1

        except:
            print "Reload Xml Error ! ,Please contact Lujun Chen."
            self.isLoadXml = 0

    def reloadMainSense(self):
        ## Success Reload Root.
        if self.isLoadXml == 1:
            # set Reference dict
            if hou.node("/obj/mainSense") is None:
                self.manSenseNode   = hou.node("/obj/").createNode("geo", "mainSense")
                self.setsNodes      =self.manSenseNode.createNode("merge", "Sets")
            # else:
            #     self.manSenseNode   = hou.node("/obj/mainSense")
            #     self.setsNodes      =hou.node("/obj/mainSense/Sets")
            self.realoadGReference()
            self.realoadGHierarchy()
            pass
        else:
            ## Error Rrload , return 0
            return 0
        pass

    def realoadGlobalSettings(self):
        self.GlobalSet = {'42': '6000fps', '24': '80fps', '25': '100fps', '26': '120fps', '27': '125fps', '20': '16fps',
                          '21': '20fps', '22': '40fps', '23': '75fps', '28': '150fps', '29': '200fps', '40': '2000fps',
                          '41': '3000fps', '1': 'hours', '3': 'seconds', '2': 'minutes', '5': '15fps',
                          '4': 'millseconds', '7': '25fps', '6': '24fps', '9': '48fps', '8': '30fps', '13': '3fps',
                          '12': '2fps', '11': '60fps', '10': '50fps', '39': '1500fps', '38': '1200fps', '15': '5fps',
                          '14': '4fps', '17': '8fps', '16': '6fps', '19': '12fps', '18': '10fps', '31': '250fps',
                          '30': '240fps', '37': '750fps', '36': '600fps', '35': '500fps', '34': '400fps',
                          '33': '375fps', '32': '300fps'}
        if self.isLoadXml == 1:
            for rootChild in self.Root:
                if rootChild.tag == "GlobalSettings":

                    for globalLableChild in rootChild:
                        if globalLableChild.tag == "Units":

                            time = globalLableChild.get('time')
                            try:
                                self.FPS = float(self.GlobalSet[time].split("f")[0])

                            except:
                                pass

                        if globalLableChild.tag == "TimeRange":
                            self.FStart = float(globalLableChild.get('start'))
                            self.FEnd = float(globalLableChild.get('end'))
                        if globalLableChild.tag == "CommonRenderSetting":
                            self.With = float(globalLableChild.get('width'))
                            self.Hight = float(globalLableChild.get('height'))

    def realoadGReference(self):
        if self.isLoadXml == 1:
            for rootChild in self.Root:
                if rootChild.tag == "Reference":
                    for file in rootChild:
                        value = file.get("filePath")
                        key = file.get("namespace")
                        self.abcReferenceDict[key] = value
        

    def realoadGHierarchy(self):

        if self.isLoadXml == 1:
            for rootChild in self.Root:
                if rootChild.tag == "Hierarchy":
                    # is  sets
                    for Sets in rootChild:
                        if Sets.get("name") == "Sets":
                            self.topNode = self.setsNodes
                            self.creatSenseLayer(Sets, self.topNode)
    
    def creatSenseLayer(self,Sets,topNode):
        for setChild in Sets:
            if setChild.get("isReferenceNode") == "False" and setChild.tag != "mesh":
                
#                #creat setsnode and creat xform and key
                mergeName = setChild.get("name")
                xformNode = topNode.createInputNode(1000,"xform","xform:"+mergeName)
                mergeNode = xformNode.createInputNode(0,"merge",mergeName)
                xformName = mergeName
                ##set xform                
                self.sexGroupXform(xformNode,xformName)
                ## set xform end!
                self.topNode =mergeNode
                
                self.creatSenseLayer(setChild, self.topNode)

                pass
            elif setChild.get("isReferenceNode") == "True" and setChild.tag != "mesh":
                mergeName = setChild.get("name")

                # creat setsnode and creat xform and key

                xformNode = topNode.createInputNode(1000,"xform","xform:"+mergeName)
                mergeNode = xformNode.createInputNode(0,"merge",mergeName)
                xformName = mergeName
                ##set xform
                self.sexGroupXform(xformNode,xformName)
                ## set xform end!


                self.topNode = mergeNode
                self.creatSenseLayer(setChild, self.topNode)


            ################################################################# is mesh
            elif setChild.get("isReferenceNode") == "True" and setChild.tag == "mesh":
                abcName = setChild.get("name")

                # creat setsnode and creat xform and key

                alembicNode = topNode.createInputNode(1000, "alembic", abcName)
                self.topNode = alembicNode

                ##setAbc parm
                filePathLast = abcName.split(":")[-1]
                filePathKey = abcName.split(":")[0]
                #setAbc filePath
                alembicNode.parm("fileName").set(self.abcReferenceDict[filePathKey])

                selectPath = self.getAbcSelectionObjPath(alembicNode,"")
                alembicNode.parm("objectPath").set(selectPath)
                
                # creat setsnode and creat xform
    def sexGroupXform(self,xformNode,xformName):        
        for rootChild in self.Root:
            if rootChild.tag == "Sets":
                # is  sets
                for set in rootChild:
                    if set.get("name").split("|")[-1] == xformName:
                        
                        self.sexGroupXformKey(set,xformNode)
                        
                    #if Set.get("name") == "Sets":
    def setKLoop(self,node,key,parmXml,indexXml,parmNode):        
        
        if key.tag == parmXml and parmXml!= "rotate":
            node.parm(parmNode).set(float(key.get(indexXml)))
        elif key.tag == parmXml and parmXml  == "rotate" :
            node.parm(parmNode).set(float(key.get(indexXml))*(180.0 / math.pi))
    
    def setKLoopAnim(self,node,key,ParmXml,parm):
        if key.get("name") == ParmXml:
            for Frame in key:                
                time = (float(Frame.get("time"))-1) / self.FPS
                value = float(Frame.get("value"))
                #inTanget = math.tan((math.pi/180)*float(Frame.get("inTangent")))
                #outTangent = math.tan((math.pi/180)*float(Frame.get("outTangent")))
                
                #inWeight = (float(Frame.get("inWeight"))*1.0)/(math.cos(float(Frame.get("inTangent"))*math.pi/180))
                #outWeight =(float(Frame.get("outWeight"))*1.0)/(math.cos(float(Frame.get("outTangent"))*math.pi/180))
                
                #self.hou_keyframe.setSlope(outTangent)
                #self.hou_keyframe.setInSlope(inTanget)

                #self.hou_keyframe.setAccel(outWeight)
                #self.hou_keyframe.setInAccel(inWeight)
                
                
                NodeParm = node.parm(parm)
                self.hou_keyframe.setTime(time)
                self.hou_keyframe.setValue(value)
                NodeParm.setKeyframe(self.hou_keyframe)
                
    def setKLoopAnimRot(self,node,key,ParmXml,parm):
        if key.get("name") == ParmXml:
            for Frame in key:                
                time = (float(Frame.get("time"))-1) / self.FPS
                value = float(Frame.get("value"))* (180.0 / math.pi)
                NodeParm = node.parm(parm)
                self.hou_keyframe.setTime(time)
                
#                inTanget = math.tan((math.pi/180)*float(Frame.get("inTangent")))
#                outTangent = math.tan((math.pi/180)*float(Frame.get("outTangent")))
#                
#                inWeight = (float(Frame.get("inWeight"))*1.0)/(math.cos(float(Frame.get("inTangent"))*math.pi/180))
#                outWeight =(float(Frame.get("outWeight"))*1.0)/(math.cos(float(Frame.get("outTangent"))*math.pi/180))
#                
#                self.hou_keyframe.setSlope(outTangent)
#                self.hou_keyframe.setInSlope(inTanget)
#
#                self.hou_keyframe.setAccel(outWeight)
#                self.hou_keyframe.setInAccel(inWeight)
                
                
                self.hou_keyframe.setValue(value) 
                NodeParm.setKeyframe(self.hou_keyframe)             
    
    def sexGroupXformKey(self,set,node):
        for key in set:
            self.setKLoop(node,key,"rotatePivot","x","px")
            self.setKLoop(node,key,"rotatePivot","y","py")
            self.setKLoop(node,key,"rotatePivot","z","pz")
            
            self.setKLoop(node,key,"translate","x","tx")
            self.setKLoop(node,key,"translate","y","ty")
            self.setKLoop(node,key,"translate","z","tz")
            
            self.setKLoop(node,key,"rotate","x","rx")
            self.setKLoop(node,key,"rotate","y","ry")
            self.setKLoop(node,key,"rotate","z","rz")
            
            self.setKLoop(node,key,"scale","x","sx")
            self.setKLoop(node,key,"scale","y","sy")
            self.setKLoop(node,key,"scale","z","sz")
        for key in set.findall("anim"):

            self.setKLoopAnim(node,key,"translateX","tx")
            self.setKLoopAnim(node,key,"translateY","ty")
            self.setKLoopAnim(node,key,"translateZ","tz")

            self.setKLoopAnim(node,key,"scaleX","sx")
            self.setKLoopAnim(node,key,"scaleX","sy")
            self.setKLoopAnim(node,key,"scaleX","sz")

            self.setKLoopAnimRot(node,key,"rotateX","rx")
            self.setKLoopAnimRot(node,key,"rotateY","ry")
            self.setKLoopAnimRot(node,key,"rotateZ","rz")
            c = hou.Color(1.0,0,0)
            node.setColor(c)
            
            
                    
    ##/main/geoGrp/Fountain_Mid_009/Fountain_Mid_009Shape
    def getAbcSelectionObjPath(self,abcNode,path):
        nameArr = abcNode.name().split(":")
        if nameArr[0] != "xform":
            path=("/"+nameArr[-1]+path)
        topNode = abcNode.outputs()[0]
        
        if nameArr[-1] == "main" :
            return path        
        return self.getAbcSelectionObjPath(topNode,path) 
        
    
    def setGlobalSettings(self):
        hou.setFps(self.FPS)
        start_frame = self.FStart
        end_frame = self.FEnd

        setGobalFrangeExpr = 'tset `(%d-1)/$FPS` `%d/$FPS`' % (start_frame, end_frame)
        hou.hscript(setGobalFrangeExpr)
        hou.playbar.setPlaybackRange(start_frame, end_frame)
        self.cameraNode.parm("resx").set(self.With)
        self.cameraNode.parm("resy").set(self.Hight)

    def realoadMainCamera(self):
        if self.isLoadXml == 1:
            for rootChild in self.Root:

                if rootChild.tag == "Cameras":

                    for cam in rootChild:

                        CameraPathArr = cam.get("name").split("|")
                        # ['', 'Cameras', 'trk_cam']

                        
                        # creat camera nodes
                        self.nullNode, self.cameraNode = self.creatCamNodes(CameraPathArr)

                        # read anim
                        for anim in cam.findall("anim"):
                            # anim _____ {'isReferenceNode': 'False', 'name': 'rotateX'}
                            
                            self.setCamKey(anim)

                        # read imagePlane
                        for imagePlane in cam.findall("imagePlane"):
                            # imagePlane _____ {'imageName': 'R:/filmServe/1015_JA_MBBN/VFX/rawPlates/SC0045/VFX_0045_4600/CL_v01/2048x1152_JPG/MBB_VFX00454600_CLv01_V001.1001.jpg', 'name': 'trk_camShape->imagePlaneShape1', 'useFrameExtension': 'True'}
                            imagePath = imagePlane.get("imageName").split(".")
                            imagePath[-2] = "$F4"
                            str1 = "."
                            imagePath = str1.join(imagePath)
                            
                            self.cameraNode.parm("vm_background").set(imagePath)
                        rotatePivot = cam.find("rotatePivot")
                        self.cameraNode.parm("px").set(float(rotatePivot.get("x")))
                        self.cameraNode.parm("py").set(float(rotatePivot.get("y")))
                        self.cameraNode.parm("pz").set(float(rotatePivot.get("z")))
                        
                        
                        for attr in cam.findall("attr"):
                            if attr.get("long") =="horizontalFilmAperture" :
                                ape = float(attr.get("value"))* 25.400173
                                expr = str(ape) +"*min(1, (ch(resx)/ch(resy)*ch(aspect))/1.500000)"
                                self.cameraNode.parm("aperture").setExpression(expr,hou.exprLanguage.Hscript)
                            if attr.get("long") =="focalLength" :
                                focalLength = float(attr.get("value"))
                                
                                self.cameraNode.parm("focal").set(focalLength)
                            
                            if attr.get("long") =="nearClipPlane" :
                                nearClipPlane = float(attr.get("value"))
                                
                                self.cameraNode.parm("near").set(nearClipPlane)
                                
                            if attr.get("long") =="farClipPlane" :
                                farClipPlane = float(attr.get("value"))
                                
                                self.cameraNode.parm("far").set(farClipPlane)       
                                
                        ## Success Reload Root.

        else:
            ## Error Rrload , return 0
            return 0

    ######################   realoadMainCamera Api
    def creatCamNodes(self, CameraPathArr):
        objNode = hou.node("/obj/")
        if hou.node("/obj/mainCamera/Cameras") is None:
            mainCamera = objNode.createNode("subnet", "mainCamera")
            nullNode = mainCamera.createNode("null", "Cameras")
            cameraNode = nullNode.createOutputNode("cam", CameraPathArr[2])
            nullNode.setInput(0, mainCamera.indirectInputs()[0])
        else:
            mainCamera = hou.node("/obj/mainCamera/")
            nullNode = hou.node("/obj/mainCamera/Cameras/")
            cameraNode = hou.node("/obj/mainCamera/" + CameraPathArr[2])
        return nullNode, cameraNode

    # setCamKeyforLoop
    def setCamKeyforLoop(self, anim, Node, itemString, parmString):
        if anim.get("name") == itemString:
            for key in anim:
                time = (float(key.get("time"))-1) / self.FPS
                value = float(key.get("value"))
                parm = Node.parm(parmString)
#                inTanget = math.tan((math.pi/180)*float(key.get("inTangent")))
#                outTangent = math.tan((math.pi/180)*float(key.get("outTangent")))
#                
#                inWeight = (float(key.get("inWeight"))*1.0)/(math.cos(float(key.get("inTangent"))*math.pi/180))
#                outWeight =(float(key.get("outWeight"))*1.0)/(math.cos(float(key.get("outTangent"))*math.pi/180))
#                
#                self.hou_keyframe.setSlope(outTangent)
#                self.hou_keyframe.setInSlope(inTanget)
#
#                self.hou_keyframe.setAccel(outWeight)
#                self.hou_keyframe.setInAccel(inWeight)
                self.hou_keyframe.setTime(time)
                self.hou_keyframe.setValue(value)
                parm.setKeyframe(self.hou_keyframe)

    def setCamKeyforLoopRoot(self, anim, Node, itemString, parmString):
        if anim.get("name") == itemString:
            for key in anim:
                time = (float(key.get("time"))-1) / self.FPS
                value = float(key.get("value")) * (180.0 / math.pi)
                
                parm = Node.parm(parmString)
#                inTanget = math.tan((math.pi/180)*float(key.get("inTangent")))
#                outTangent = math.tan((math.pi/180)*float(key.get("outTangent")))
#                
#                inWeight = (float(key.get("inWeight"))*1.0)/(math.cos(float(key.get("inTangent"))*math.pi/180))
#                outWeight =(float(key.get("outWeight"))*1.0)/(math.cos(float(key.get("outTangent"))*math.pi/180))
#                
#                self.hou_keyframe.setSlope(outTangent)
#                self.hou_keyframe.setInSlope(inTanget)
#
#                self.hou_keyframe.setAccel(outWeight)
#                self.hou_keyframe.setInAccel(inWeight)
                self.hou_keyframe.setTime(time)
                self.hou_keyframe.setValue(value)
                parm.setKeyframe(self.hou_keyframe)

    def setCamKey(self, anim):
        if anim.get("isReferenceNode") == "False":
            # set rot xyz
            self.setCamKeyforLoopRoot(anim, self.cameraNode, "rotateX", "rx")
            self.setCamKeyforLoopRoot(anim, self.cameraNode, "rotateY", "ry")
            self.setCamKeyforLoopRoot(anim, self.cameraNode, "rotateZ", "rz")
            self.setCamKeyforLoop(anim, self.nullNode, "scaleX", "sx")
            self.setCamKeyforLoop(anim, self.nullNode, "scaleY", "sy")
            self.setCamKeyforLoop(anim, self.nullNode, "scaleZ", "sz")
            self.setCamKeyforLoop(anim, self.cameraNode, "translateX", "tx")
            self.setCamKeyforLoop(anim, self.cameraNode, "translateY", "ty")
            self.setCamKeyforLoop(anim, self.cameraNode, "translateZ", "tz")
            try:

                self.setCamKeyforLoop(anim, self.cameraNode, "visibility", "display")
                self.setCamKeyforLoop(anim, self.cameraNode, "focalLength", "focal")
                self.setCamKeyforLoop(anim, self.cameraNode, "fStop", "fstop")
                self.setCamKeyforLoop(anim, self.cameraNode, "focusDistance", "focus")



            except:
                pass

    def run(self):
        ## Run main start
        # init rootPath
        houdiniHipFilePath1 = hou.hipFile
        xmlPath1 = houdiniHipFilePath1.path().split("/CG/")[0]+r"/CG/Animation/Publish"
        for path1 in  os.listdir(xmlPath1):
            if path1.split(".")[-1] =="xml":
                dissmessageKey = hou.ui.displayMessage("Please select the type of import or reload", buttons=("Sense", "Camera","all","Cancel"))
                if dissmessageKey == 3:
                    pass
                else:
                
                    path1 =xmlPath1+"/"+ path1
                    self.setXmlPath(path1)
                    self.realoadRoot()
                    if dissmessageKey == 0:
                    
                        if hou.node("/obj/mainSense/"):
                            
                            hou.node("/obj/mainSense/").destroy()
                        self.reloadMainSense()
                    elif dissmessageKey == 1:
                        if hou.node("/obj/mainCamera/"):
                            #destroy camNode
                            hou.node("/obj/mainCamera/").destroy()
                            self.realoadGlobalSettings()
                            self.realoadMainCamera()
                            self.setGlobalSettings()
                    else:
                        
                        if hou.node("/obj/mainSense/"):
                            
                            hou.node("/obj/mainSense/").destroy()
                        if hou.node("/obj/mainCamera/"):
                            #destroy camNode
                            hou.node("/obj/mainCamera/").destroy()
                            
                        self.realoadGlobalSettings()
                        self.realoadMainCamera()
                        self.setGlobalSettings()
                        self.reloadMainSense()    
                            

