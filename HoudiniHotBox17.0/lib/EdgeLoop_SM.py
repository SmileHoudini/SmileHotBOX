import hou
kwargs ={}

class EdgeLoop_SM:
    def run(self):
        import soptoolutils

        soptoolutils.customStateTool(kwargs, 'edgeloop')