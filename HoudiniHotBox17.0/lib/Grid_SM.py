import hou
kwargs ={}
kwargs['bbox']= ""
class Grid_SM:
    def run(self):
        import toolutils
        import soptoolutils

        size = 4.0
        kwargs['bbox'] = hou.BoundingBox(-size / 2.0, 0, -size / 2.0, size / 2.0, 0, size / 2.0)
        grid = soptoolutils.genericTool(kwargs, 'grid')
        grid.parm("sizex").set(size)
        grid.parm("sizey").set(size)

