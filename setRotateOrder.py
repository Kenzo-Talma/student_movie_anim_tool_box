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


class setRotateOrderWin(QtWidgets.QDialog):

    def __init__(self, parent=mayaMainWindow()):
        super(setRotateOrderWin, self).__init__(parent)
        self.setWindowTitle(" set rotate order")
        self.setMinimumWidth(200)
        # self.setMinimumHeight(500)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.createWidget()
        self.createLayout()

        self.rotateOrder = 0
        self.rotateNames = ['xyz', 'yzx', 'zxy', 'xzy', 'yxz', 'zyx']

    # def functions

    def defineOrder(self):
        self.rotateOrder = int(self.orderSlider.value())
        #print(self.rotateOrder)
        self.setRotateOrderButton.setText(self.rotateNames[self.rotateOrder])

    def setRotateOrder(self):
        ctrlList = cmds.ls(sl=True)
        #print(self.rotateOrder)

        for ctrl in ctrlList:
            cmds.setAttr(ctrl + '.rotateOrder', self.rotateOrder)

    # widgets

    def createWidget(self):
        self.setRotateOrderButton = QtWidgets.QPushButton('xyz')
        self.setRotateOrderButton.clicked.connect(self.setRotateOrder)

        self.orderSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.orderSlider.setMinimum(0)
        self.orderSlider.setMaximum(5)
        self.orderSlider.setSingleStep(1)
        self.orderSlider.sliderMoved.connect(self.defineOrder)

        # layout

    def createLayout(self):
        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(self.setRotateOrderButton)
        mainLayout.addWidget(self.orderSlider)


"""d = setRotateOrderWin()
d.show()
"""