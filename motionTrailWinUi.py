import sys
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as mui
from PySide2 import QtGui, QtCore, QtWidgets
import shiboken2
import importlib


def mayaMainWindow():
    mainWindowPtr = mui.MQtUtil.mainWindow()
    if sys.version_info.major >= 3:
        return (shiboken2.wrapInstance(int(mainWindowPtr), QtWidgets.QWidget))
    else:
        return (shiboken2.wrapInstance(long(mainWindowPtr), QtWidgets.QWidget))


class MotionTrailWin(QtWidgets.QDialog):

    def __init__(self, parent=mayaMainWindow()):
        super(MotionTrailWin, self).__init__(parent)
        self.setWindowTitle("easy motion trail")
        self.setMinimumWidth(200)
        # self.setMinimumHeight(500)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.createWidget()
        self.createLayout()

        self.selectedControl = None

    # def UI functions

    def selectControl_func(self):
        controlLst = cmds.ls(sl=True)
        slLen = len(controlLst)
        # print(slLen)

        if slLen > 0:
            self.selectedControl = controlLst
        else:
            self.selectedControl = None

    def diplaySelectedName_func(self):
        control = self.selectedControl

        if control == None:
            self.diplaySelectedNameLabel.setText("select control")
        else:
            self.diplaySelectedNameLabel.setText(str(control))



    # def functions

    def createMotionTrail_func(self):
        control = self.selectedControl

        currentSel = cmds.ls(sl=True)

        cmds.select(clear=True)

        for ctrl in control:
            cmds.select(ctrl)
            mel.eval('snapshot  -motionTrail 1  -increment 1 -startTime `playbackOptions -query -min` -endTime `playbackOptions -query -max`;')

        cmds.select(currentSel)

    def deleteMotionTrail_func(self):
        motionTraiList = cmds.ls(type='motionTrailShape')

        for moTr in motionTraiList:
            par = cmds.listRelatives(moTr, p=True, c=False, ap=False)
            cmds.delete(par)


    # widgets

    def createWidget(self):
        self.selectControlButton = QtWidgets.QPushButton("select control")
        self.selectControlButton.clicked.connect(self.selectControl_func)
        self.selectControlButton.clicked.connect(self.diplaySelectedName_func)

        self.diplaySelectedNameLabel = QtWidgets.QLabel("select control")

        self.createMotionTrailButton = QtWidgets.QPushButton("create motion trail")
        self.createMotionTrailButton.clicked.connect(self.createMotionTrail_func)

        self.deleteMotionTrailButton = QtWidgets.QPushButton("delete motion trail")
        self.deleteMotionTrailButton.clicked.connect(self.deleteMotionTrail_func)

    # layout

    def createLayout(self):
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(self.selectControlButton)
        mainLayout.addWidget(self.diplaySelectedNameLabel)
        mainLayout.addWidget(self.createMotionTrailButton)
        mainLayout.addWidget(self.deleteMotionTrailButton)

'''d = MotionTrailWin()
d.show()'''