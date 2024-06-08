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


class PlageAnimMainWin(QtWidgets.QDialog):

    def __init__(self, parent=mayaMainWindow()):
        super(PlageAnimMainWin, self).__init__(parent)
        self.setWindowTitle("l'anim a la plage")
        self.setMinimumWidth(200)
        # self.setMinimumHeight(500)
        self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)

        self.createWidget()
        self.createLayout()

    # def functions

    def runTweenMachineButton_func(self):
        from student_movie_anim_tool_box import startTweenMachine
        startTweenMachine.tweenMachine.start()

    def runAnimBotButton_func(self):
        from student_movie_anim_tool_box import startAnimBot

        importlib.reload(startAnimBot)

        startAnimBot.startAnimBot_func()

    def runtemplateModeling_func(self):
        from student_movie_anim_tool_box import templateModeling

        importlib.reload(templateModeling)

        templateModeling.templateModeling_func()

    def runUnlockModeling_func(self):
        from student_movie_anim_tool_box import unlockModeling

        importlib.reload(unlockModeling)

        unlockModeling.unlockModeling_func()

    def runtemplateProps_func(self):
        from student_movie_anim_tool_box import templateProps

        importlib.reload(templateProps)

        templateProps.templateProps_func()

    def runDefaultRotateOrderButton_func(self):
        from student_movie_anim_tool_box import defaultRotateOrder

        importlib.reload(defaultRotateOrder)

        defaultRotateOrder.setDefaultRotateOrder()

    def runRotateOrderButton_func(self):
        from student_movie_anim_tool_box import setRotateOrder

        importlib.reload(setRotateOrder)

        setRotateOrderWin = setRotateOrder.setRotateOrderWin()
        setRotateOrderWin.show()

    def runCreateParentMarkerButton_func(self):
        from student_movie_anim_tool_box import createParentMarker

        importlib.reload(createParentMarker)

        createParentMarkerWin = createParentMarker.ParentMarkerWin()
        createParentMarkerWin.show()

    def runMotionTrailWinButton_func(self):
        from student_movie_anim_tool_box import motionTrailWinUi

        importlib.reload(motionTrailWinUi)

        TrailWin = motionTrailWinUi.MotionTrailWin()
        TrailWin.show()

    # widgets

    def createWidget(self):

        self.runTweenMachineButton = QtWidgets.QPushButton("Tween Machine")
        self.runTweenMachineButton.clicked.connect(self.runTweenMachineButton_func)

        self.runAnimBotButton = QtWidgets.QPushButton("start animBot")
        self.runAnimBotButton.clicked.connect(self.runAnimBotButton_func)

        self.runUnlockModelingButton = QtWidgets.QPushButton("unlock MODELING")
        self.runUnlockModelingButton.clicked.connect(self.runUnlockModeling_func)

        self.runtemplateModelingButton = QtWidgets.QPushButton("template MODELING")
        self.runtemplateModelingButton.clicked.connect(self.runtemplateModeling_func)

        self.runtemplatePropsButton = QtWidgets.QPushButton("template PROPS")
        self.runtemplatePropsButton.clicked.connect(self.runtemplateProps_func)

        self.runDefaultRotateOrderButton = QtWidgets.QPushButton("set default rotate order")
        self.runDefaultRotateOrderButton.clicked.connect(self.runDefaultRotateOrderButton_func)

        self.runRotateOrderButton = QtWidgets.QPushButton("set rotate order")
        self.runRotateOrderButton.clicked.connect(self.runRotateOrderButton_func)

        self.runCreateParentMarkerButton = QtWidgets.QPushButton("create parent marker")
        self.runCreateParentMarkerButton.clicked.connect(self.runCreateParentMarkerButton_func)

        self.runMotionTrailWinButton = QtWidgets.QPushButton("motion trail tool")
        self.runMotionTrailWinButton.clicked.connect(self.runMotionTrailWinButton_func)

    # layout

    def createLayout(self):

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(self.runTweenMachineButton)
        mainLayout.addWidget(self.runAnimBotButton)
        mainLayout.addWidget(self.runtemplateModelingButton)
        mainLayout.addWidget(self.runUnlockModelingButton)
        mainLayout.addWidget(self.runtemplatePropsButton)
        mainLayout.addWidget(self.runDefaultRotateOrderButton)
        mainLayout.addWidget(self.runRotateOrderButton)
        mainLayout.addWidget(self.runCreateParentMarkerButton)
        mainLayout.addWidget(self.runMotionTrailWinButton)

# test ui
"""d = PlageAnimMainWin()
d.show()"""
