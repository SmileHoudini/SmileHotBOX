import hou

class Cop_Path_S:
    def run(self):
    
        try:
            from PySide2 import QtCore, QtGui
            from PySide2 import QtWidgets
            
            clipboard = QtWidgets.QApplication.clipboard()
            mimeData = QtCore.QMimeData()
            
            nodes = hou.selectedNodes()
            path = nodes[0].path()
            
            mimeData.setText(path)
            
            clipboard.setMimeData(mimeData)
            
            print "The path: '"+str(path) + "' is now in clipboard !"
        except:
            pass
