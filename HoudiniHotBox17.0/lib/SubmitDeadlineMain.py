import sys
from PySide import QtGui, QtCore
import os
import shutil
import hou

# Choose Machine
list_Machine_7 = "node201,node202,node203,node204,node205,node206,node207,node208,node209,node210,node211,node212"
list_Machine_8 = "node13,node16,node17,node19,node20,node21,node212,node214,node215,node218,node22,node224,node225,node226,node23,node27"

# Choose Deadline path
DeadlinePath_7 = '"C:/Program Files/Thinkbox/Deadline7/bin/deadlinecommand.exe" '
DeadlinePath_8 = '"C:/Program Files/Thinkbox/Deadline8/bin/deadlinecommand.exe" '

node = hou.selectedNodes()[0]
Job_Name_ = hou.hipFile.basename()
Houdini_File_ = hou.hipFile.path()
Render_Node_ = node.path()

RFStart = hou.hscriptStringExpression("$RFSTART")
RFEnd = hou.hscriptStringExpression("$RFEND")
Frame_List_ = RFStart + "-" + RFEnd


class mainWindow(QtGui.QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.DeadlinePath = DeadlinePath_7

        self.setWindowTitle("Submit Houdini Job to Deadline")

        self.label_jobName = QtGui.QLabel("Job Name", self)
        self.lineEdite_jobName = QtGui.QLineEdit(Job_Name_, self)

        self.label_Priority = QtGui.QLabel("Priority", self)
        self.lineEdite_Priority = QtGui.QLineEdit("50", self)

        self.label_MachineList = QtGui.QLabel("Machine List", self)
        self.lineEdite_MachineList = QtGui.QLineEdit(list_Machine_7, self)

        self.label_HoudiniFile = QtGui.QLabel("Houdini File", self)
        self.lineEdite_HoudiniFile = QtGui.QLineEdit(Houdini_File_, self)

        self.label_RenderNode = QtGui.QLabel("Render Node", self)
        self.lineEdite_RenderNode = QtGui.QLineEdit(Render_Node_, self)

        self.label_FrameList = QtGui.QLabel("Frame List", self)
        self.lineEdite_FrameList = QtGui.QLineEdit(Frame_List_, self)

        self.label_ChunkSize = QtGui.QLabel("ChunkSize", self)
        self.lineEdite_ChunkSize = QtGui.QLineEdit("1", self)
        
        self.label_Version = QtGui.QLabel("Version", self)
        self.lineEdite_Version = QtGui.QLineEdit("15", self)
        # add Button
        self.btn_Submit = QtGui.QPushButton("Submit", self)
        self.btn_Cancel = QtGui.QPushButton("Cancel", self)
        self.btn_Cancel.clicked.connect(self.closeWindow)
        self.btn_Submit.clicked.connect(self.A)

        self.CBox = QtGui.QComboBox(self)
        self.CBox.addItem("Deadline7")
        self.CBox.addItem("Deadline8")
        self.CBox.activated.connect(self.SelectDeadline)

        self.spacerItem = QtGui.QSpacerItem(39, 20)

        Layout = QtGui.QGridLayout()
        HBLayout = QtGui.QHBoxLayout()
        HBLayout.addStretch(1)
        VBLayout = QtGui.QVBoxLayout()
        VBLayout.addStretch(1)
        Layout.addWidget(self.label_jobName, 1, 0)
        Layout.addWidget(self.lineEdite_jobName, 1, 1)
        Layout.addWidget(self.label_Priority, 2, 0)
        Layout.addWidget(self.lineEdite_Priority, 2, 1)
        Layout.addWidget(self.label_MachineList, 3, 0)
        Layout.addWidget(self.lineEdite_MachineList, 3, 1)
        Layout.addWidget(self.label_HoudiniFile, 4, 0)
        Layout.addWidget(self.lineEdite_HoudiniFile, 4, 1)
        Layout.addWidget(self.label_RenderNode, 5, 0)
        Layout.addWidget(self.lineEdite_RenderNode, 5, 1)
        Layout.addWidget(self.label_FrameList, 6, 0)
        Layout.addWidget(self.lineEdite_FrameList, 6, 1)
        Layout.addWidget(self.label_ChunkSize, 7, 0)
        Layout.addWidget(self.lineEdite_ChunkSize, 7, 1)
        Layout.addWidget(self.label_Version, 8, 0)
        Layout.addWidget(self.lineEdite_Version, 8, 1)
        HBLayout.addWidget(self.CBox)
        HBLayout.addItem(self.spacerItem)
        HBLayout.addWidget(self.btn_Submit)
        HBLayout.addWidget(self.btn_Cancel)

        VBLayout.addLayout(Layout)
        VBLayout.addLayout(HBLayout)
        self.setLayout(VBLayout)

        self.resize(380, 150)
        self.move(self.getMPos())

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        palette1 = QtGui.QPalette()
        palette1.setColor(self.backgroundRole(), QtGui.QColor(60, 60, 60))
        palette1.setColor(self.foregroundRole(), QtGui.QColor(200, 200, 200))
        self.setPalette(palette1)

    def SelectDeadline(self):
        Source = self.CBox.currentText()
        if Source == "Deadline7":
            self.lineEdite_MachineList.setText(list_Machine_7)
            self.DeadlinePath = DeadlinePath_7
        if Source == "Deadline8":
            self.lineEdite_MachineList.setText(list_Machine_8)
            self.DeadlinePath = DeadlinePath_8

    def A(self):
        JobName = self.lineEdite_jobName.text()
        Priority = self.lineEdite_Priority.text()
        MachineList = self.lineEdite_MachineList.text()
        HoudiniFile = self.lineEdite_HoudiniFile.text()
        RenderNode = self.lineEdite_RenderNode.text()
        FrameList = self.lineEdite_FrameList.text()
        ChunkSize = self.lineEdite_ChunkSize.text()
        Version = self.lineEdite_Version.text()

        try:
            os.listdir("C:/Temp_DeadlineSubmit")
            pass
        except:
            os.mkdir("C:/Temp_DeadlineSubmit")

        file_jobInfo = open("C:/Temp_DeadlineSubmit/houdini_job_info.job", "w")
        file_pluginInfo = open("C:/Temp_DeadlineSubmit/houdini_plugin_info.job", "w")
        file_submit = open("C:/Temp_DeadlineSubmit/houdini_submit.bat", "w")

        # write information
        w_jobInfo = ["Plugin=Houdini\n",
                     "Name=" + JobName + "\n",
                     "Priority=" + Priority + "\n",
                     "Whitelist=" + MachineList + "\n",
                     "Frames=" + FrameList + "\n"
                     "ChunkSize="+ChunkSize]
        w_pluginInfo = ["SceneFile=" + HoudiniFile + "\n",
                        "OutputDriver=" + RenderNode + "\n",
                        "Version=" + Version]

        w_submit = [self.DeadlinePath,
                    "C:/Temp_DeadlineSubmit/houdini_job_info.job ",
                    "C:/Temp_DeadlineSubmit/houdini_plugin_info.job"]

        file_jobInfo.writelines(w_jobInfo)
        file_jobInfo.close()
        file_pluginInfo.writelines(w_pluginInfo)
        file_pluginInfo.close()
        file_submit.writelines(w_submit)
        file_submit.close()

        os.system("C:/Temp_DeadlineSubmit/houdini_submit.bat")
        shutil.rmtree("C:/Temp_DeadlineSubmit")

    def closeWindow(self):
        self.close()

    # Get mouse position
    def getMPos(self):
        a = QtGui.QApplication.desktop()
        b = a.cursor()
        MPos = b.pos()
        return MPos


# app = QtGui.QApplication(sys.argv)
window = mainWindow()
window.show()
# app.exec_()