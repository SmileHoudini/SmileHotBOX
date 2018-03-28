import hou
kwargs ={}
kwargs['bbox']= ""
class Path_SM:
    def run(self):
        import objecttoolutils

        objecttoolutils.customStateTool(kwargs, 'path')
