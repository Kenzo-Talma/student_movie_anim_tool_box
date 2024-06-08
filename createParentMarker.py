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


class ParentMarkerWin(QtWidgets.QDialog):

    def __init__(self, parent=mayaMainWindow()):
        super(ParentMarkerWin, self).__init__(parent)
        self.setWindowTitle("marker tool")
        self.setMinimumWidth(200)
        # self.setMinimumHeight(500)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.createWidget()
        self.createLayout()

        self.parentObj = None

    # def UI functions

    def selectParent_func(self):
        parentLst = cmds.ls(sl=True)
        slLen = len(parentLst)


        if slLen == 1:
            self.parentObj =parentLst[0]
        else:
            self.parentObj = None

    def diplayParentName_func(self):
        parentObj = self.parentObj

        if parentObj == None:
            self.parentDisplayLabel.setText("select parent")
        else:
            self.parentDisplayLabel.setText(str(parentObj))



    # def functions

    def createPositionLocator_func(self):
        parentobj = self.parentObj

        if parentobj == None :
            print('select parent')
        else:
            cmds.select(clear=True)
            pos = cmds.xform(parentobj, q=True, t=True, ws=True)
            rot = cmds.xform(parentobj, q=True, ro=True, ws=True)

            posLoc = cmds.spaceLocator(n=parentobj + '_positionLoc')
            cmds.xform(posLoc, t=pos, ws=True)
            cmds.xform(posLoc, ro=rot, ws=True)

    def createParentMarker_func(self):
        parentObj = self.parentObj
        pos = None
        rot = None
        if parentObj == None :
            print('select parent')
        else:
            posLoc = parentObj + '_positionLoc'
            if cmds.objExists(posLoc):
                pos = cmds.xform(posLoc, q=True, t=True, ws=True)
                rot = cmds.xform(posLoc, q=True, ro=True, ws=True)
                cmds.delete(posLoc)
            else:
                pos = cmds.xform(parentObj, q=True, t=True, ws=True)
                rot = cmds.xform(parentObj, q=True, ro=True, ws=True)

            cmds.select(clear=True)

            parentMarker = cmds.spaceLocator(n=parentObj + '_parentMarker')[0]
            cmds.setAttr(parentMarker + '.localScaleX', 5)
            cmds.setAttr(parentMarker + '.localScaleY', 5)
            cmds.setAttr(parentMarker + '.localScaleZ', 5)

            offset = cmds.group(parentMarker, n=parentMarker + '_offset')
            grp = cmds.group(offset, n=parentMarker + '_grp')

            markerShere = cmds.sphere(n=parentMarker + 'Sphere')[0]
            cmds.setAttr(markerShere + ".overrideEnabled", 1)
            cmds.setAttr(markerShere + ".overrideDisplayType", 2)

            cmds.parent(markerShere, parentMarker)


            cmds.xform(grp, t=pos, ws=True)
            cmds.xform(grp, ro=rot, ws=True)

            cmds.parentConstraint(parentObj, grp, mo=True)


    # widgets

    def createWidget(self):
        self.selectParentButton = QtWidgets.QPushButton("select parent")
        self.selectParentButton.clicked.connect(self.selectParent_func)
        self.selectParentButton.clicked.connect(self.diplayParentName_func)

        self.parentDisplayLabel = QtWidgets.QLabel("select parent")

        self.createPositionLocator = QtWidgets.QPushButton("create temporary locator")
        self.createPositionLocator.clicked.connect(self.createPositionLocator_func)

        self.createParentMarkerButton = QtWidgets.QPushButton("create parent marker")
        self.createParentMarkerButton.clicked.connect(self.createParentMarker_func)

    # layout

    def createLayout(self):
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(self.selectParentButton)
        mainLayout.addWidget(self.parentDisplayLabel)
        mainLayout.addWidget(self.createPositionLocator)
        mainLayout.addWidget(self.createParentMarkerButton)