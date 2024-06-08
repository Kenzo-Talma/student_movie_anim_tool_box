import maya.cmds as cmds


def templateProps_func():
    obList = cmds.listRelatives('RIGGING', children=True)

    for ob in obList:
        if 'props' in ob:
            attribute = cmds.getAttr(ob + ".template")

            if attribute == 0:
                cmds.setAttr(ob + ".template", 1)
            else:
                cmds.setAttr(ob + ".template", 0)