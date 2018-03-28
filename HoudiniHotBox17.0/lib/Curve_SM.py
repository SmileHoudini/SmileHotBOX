import hou
kwargs ={}
kwargs['bbox']= ""
class Curve_SM:
    def run(self):
        import toolutils
        import soptoolutils
        activepane = toolutils.activePane(kwargs)
        if activepane.type() == hou.paneTabType.SceneViewer:
            # Get the current context.
            sceneviewer = toolutils.sceneViewer()
            # Create a SOP container.
            container = soptoolutils.createSopNodeContainer(sceneviewer, "curve_object1")
            # Create the curve.
            newnode = soptoolutils.createSopNodeGenerator(container, "curve", None)
            # Turn on the highlight flag so we see the SOPs selected output.
            newnode.setHighlightFlag(True)
            if sceneviewer.isCreateInContext():
                newnode.setCurrent(True, True)
                sceneviewer.enterCurrentNodeState()
                toolutils.homeToSelectionNetworkEditorsFor(newnode)
            else:
                container.setCurrent(True, True)
                toolutils.homeToSelectionNetworkEditorsFor(container)
                activepane.setPwd(container.parent())
                activepane.setCurrentState("objcurve")
        elif activepane.type() == hou.paneTabType.NetworkEditor:
            soptoolutils.genericTool(kwargs, "curve")
        else:
            raise hou.Error("Can't run the tool in the selected pane.")
