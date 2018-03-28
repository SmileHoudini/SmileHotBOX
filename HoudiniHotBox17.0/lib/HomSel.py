import hou
class HomSel:
    def __init__(self):
        pass

    def run(self):
        plane = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
        plane.curViewport().homeSelected()