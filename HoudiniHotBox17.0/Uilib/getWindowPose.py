import sys

from PySide2 import QtCore
from PySide2 import QtWidgets

def getPose():
    
    a = QtWidgets.QApplication.desktop()
    b= a.cursor()
    c= b.pos()
    return c

