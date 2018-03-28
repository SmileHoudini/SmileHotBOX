import hou
kwargs ={}
kwargs['bbox']= ""
class Box_SM:
    def run(self):
        import toolutils
        import soptoolutils

        kwargs['bbox'] = hou.BoundingBox(-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
        sphere = soptoolutils.genericTool(kwargs, 'box')
        sphere.parm("type").set("polymesh")
        sphere.parm("divrate1").set(2)
        sphere.parm("divrate2").set(2)
        sphere.parm("divrate3").set(2)
