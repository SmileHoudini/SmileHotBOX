import hou
kwargs ={}

class PolyBridge_SM:
    def run(self):
        import soptoolutils

        soptoolutils.customStateTool(kwargs, 'polybridge')