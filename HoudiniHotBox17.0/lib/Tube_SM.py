import hou
kwargs ={}
kwargs['bbox']= ""
class Tube_SM:
    def run(self):
        import toolutils
        import soptoolutils
        rad = 0.5
        height = 1.0
        kwargs['bbox'] = hou.BoundingBox(-rad, -height / 2., -rad, rad, height / 2., rad)
        tube = soptoolutils.genericTool(kwargs, 'tube')
        tube.parm("type").set("poly")
        tube.parm("radscale").set(rad)
        tube.parm("height").set(height)
