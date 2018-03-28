import hou
class SelPoints:
    def __init__(self):
        pass

    def run(self):
        plane = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
        plane.setSelectionMode(hou.selectionMode.Geometry)
        plane.setCurrentState("select")
        plane.setPickGeometryType(hou.geometryType.Points)