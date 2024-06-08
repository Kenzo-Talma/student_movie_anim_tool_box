import sys
import maya.cmds as cmds
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


class MirrorPoseWin(QtWidgets.QDialog):

    def __init__(self, parent=mayaMainWindow()):
        super(MirrorPoseWin, self).__init__(parent)
        self.setWindowTitle("le rig a la plage")
        self.setMinimumWidth(200)
        # self.setMinimumHeight(500)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.createWidget()
        self.createLayout()

        self.mirrorSide = None
        self.mirrorInv = None


    def mirrorPose(self):
        mirrorSide = self.mirrorSide

        mirrorInv = self.mirrorInv

        controlList = cmds.ls(sl=True)

        for control in controlList:
            controlInv = None
            if '_' + mirrorSide in control :
                controlInv = control.replace('_' + mirrorSide, '_' + mirrorInv)
            elif mirrorSide + '_' in controlList:
                controlInv = control.replace(mirrorSide + '_', mirrorInv + '_')

            ctRot = cmds.xform(control, ro=True, q=True, os=True)
            ctRotInv = cmds.xform(controlInv, ro=True, q=True, os=True)

            ctTrans = cmds.xform(control, t=True, q=True, os=True)
            ctTransInv = cmds.xform(controlInv, t=True, q=True, os=True)

            cmds.xform(controlInv, ro=ctRot, os=True, a=True)
            cmds.xform(control, ro=ctRotInv, os=True, a=True)

            cmds.xform(controlInv, t=ctTrans, os=True, a=True)
            cmds.xform(control, t=ctTransInv, os=True, a=True)

    def leftButton_func(self):
        self.mirrorSide = 'L'
        self.mirrorInv = 'R'

    def rightButton_func(self):
        self.mirrorSide = 'R'
        self.mirrorInv = 'L'

    def createWidget(self):

        self.leftButton = QtWidgets.QPushButton("L")
        self.leftButton.clicked.connect(self.leftButton_func)
        self.leftButton.clicked.connect(self.mirrorPose)

        self.rightButton = QtWidgets.QPushButton("R")
        self.rightButton.clicked.connect(self.rightButton_func)
        self.rightButton.clicked.connect(self.mirrorPose)

    def createLayout(self):
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(self.leftButtonButton)
        mainLayout.addWidget(self.rightButtonButton)
