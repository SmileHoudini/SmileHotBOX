import hou
kwargs ={}
kwargs['bbox']= ""
class Circle_SM:
    def run(self):
        import toolutils
        import soptoolutils

        kwargs['bbox'] = hou.BoundingBox(-1.0, -1., -.0, 1.0, 1., .0)
        sphere = soptoolutils.genericTool(kwargs, 'circle')
        sphere.parm("type").set("poly")

