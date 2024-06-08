import maya.cmds as cmds

def setDefaultRotateOrder():
    ctrlList = ['chara_guy_rig_main:FKShoulder_R',
                'chara_guy_rig_main:FKElbow_R',
                'chara_guy_rig_main:FKWrist1_R',
                'chara_guy_rig_main:IKArm_L',
                'chara_guy_rig_main:IKLeg_L',
                'chara_guy_rig_main:IKLeg_R',
                'chara_guy_rig_main:IKArm_R',
                'chara_guy_rig_main:FKShoulder_L',
                'chara_guy_rig_main:FKElbow_L',
                'chara_guy_rig_main:FKWrist1_L',
                'chara_guy_rig_main:FKHip_R',
                'chara_guy_rig_main:FKHip_L',
                'chara_guy_rig_main:FKKnee_L',
                'chara_guy_rig_main:FKKnee_R',
                'chara_guy_rig_main:FKAnkle_L',
                'chara_guy_rig_main:FKAnkle_R']

    lst = cmds.ls(sl=True)
    print(lst)
    if len(lst):
        roList = lst
    else:
        roList = ctrlList

    for ob in roList:
        cmds.setAttr(ob + '.rotateOrder', 3)
