import hou
kwargs ={}

class PolyBevel_SM:
    def run(self):
        import soptoolutils

        soptoolutils.customStateTool(kwargs, 'polybevel::2.0')