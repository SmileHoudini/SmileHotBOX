import hou
kwargs ={}
kwargs['type']= ""
class DrawCurce_SM:
    def run(self):
        import stroketoolutils

        kwargs['type'] = "curve"
        stroketoolutils.strokeSource(kwargs)
