import maya.cmds as cmds


def unlockModeling_func():
    attribute = cmds.getAttr('MODELING' + ".overrideDisplayType")

    if attribute == 0:
        if cmds.objExists('MODELING'):
            cmds.setAttr("MODELING.overrideEnabled", 1)
            cmds.setAttr("MODELING.overrideDisplayType", 2)

        if cmds.objExists('ANIMATION'):
            cmds.setAttr("ANIMATION.overrideEnabled", 1)
            cmds.setAttr("ANIMATION.overrideDisplayType", 2)
    else:
        if cmds.objExists('MODELING'):
            cmds.setAttr("MODELING.overrideDisplayType", 0)

        if cmds.objExists('ANIMATION'):
            cmds.setAttr("ANIMATION.overrideDisplayType", 0)
