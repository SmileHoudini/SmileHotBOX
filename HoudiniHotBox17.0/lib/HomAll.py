import hou
class HomAll:
    def __init__(self):
        pass

    def run(self):
        plane = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
        plane.curViewport().frameAll()