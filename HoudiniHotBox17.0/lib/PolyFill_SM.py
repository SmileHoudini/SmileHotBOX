import hou
kwargs ={}

class PolyFill_SM:
    def run(self):
        import soptoolutils

        soptoolutils.genericTool(kwargs, 'polyfill')