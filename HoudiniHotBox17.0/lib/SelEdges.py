import hou
class SelEdges:
    def __init__(self):
        pass

    def run(self):
        plane = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
        plane.setCurrentState("select")
        plane.setPickGeometryType(hou.geometryType.Edges)