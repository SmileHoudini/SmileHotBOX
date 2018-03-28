import hou
kwargs ={}
kwargs['bbox']= ""
class Torus_SM:
    def run(self):
        import toolutils
        import soptoolutils
        orad = 0.5
        irad = 0.25
        kwargs['bbox'] = hou.BoundingBox(-orad - irad, -irad, -orad - irad, orad + irad, irad, orad + irad)
        torus = soptoolutils.genericTool(kwargs, 'torus')
        torus.parm("type").set("poly")
        torus.parm("radx").set(orad)
        torus.parm("rady").set(irad)
