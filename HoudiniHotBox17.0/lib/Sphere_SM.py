import hou
kwargs ={}
kwargs['bbox']= ""
class Sphere_SM:
    def run(self):
        import toolutils
        import soptoolutils
        rad = 0.5
        kwargs['bbox'] = hou.BoundingBox(-rad, -rad, -rad, rad, rad, rad)
        sphere = soptoolutils.genericTool(kwargs, 'sphere')
        sphere.parm("type").set("polymesh")
        sphere.parm("radx").set(rad)
        sphere.parm("rady").set(rad)
        sphere.parm("radz").set(rad)
