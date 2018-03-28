import hou
kwargs ={}

class PolyExtrude_SM:
    def run(self):
        import soptoolutils

        soptoolutils.customStateTool(kwargs, 'polyextrude::2.0')
