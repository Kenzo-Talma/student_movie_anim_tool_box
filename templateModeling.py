import maya.cmds as cmds


def templateModeling_func():
    attribute = cmds.getAttr('MODELING' + ".template")

    if attribute == 0:
        cmds.setAttr('MODELING' + ".template", 1)
    else:
        cmds.setAttr('MODELING' + ".template", 0)
