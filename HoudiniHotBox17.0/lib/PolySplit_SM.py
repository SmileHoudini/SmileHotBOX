import hou
kwargs ={}

class PolySplit_SM:
    def run(self):
        import soptoolutils

        soptoolutils.customStateTool(kwargs, 'polysplit::2.0')