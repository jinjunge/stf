# -*- encoding=utf8 -*-
__author__ = "keke"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

from airtest.core.api import using
using("hankCommon.air")
using("BasicOperation.air")
from hankCommon import HankTestingPilots
from BasicOperation import Guide
from BasicOperation import back
#游戏包名
connect_channel = "com.outfit7.mytalkinghank.anzhi"
#渠道名
mark_channel = "anzhi"

# operator = "Mobile"
# operator = "MIGUMobile"
operator = "Telecom"
# operator = "Unicom"

BillingPointPictures = "Double" #两倍
# BillingPointPictures = "Original" #本来

clear_app(connect_channel)
sleep(1.0)
start_app(connect_channel)
sleep(40.0)

if mark_channel == "anzhi":
    if exists(Template(r"tpl1537500526640.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.014, -0.364), resolution=(1080, 1920))):
        keyevent("back")
        sleep(5)
        keyevent("back")

hankTestPilot = HankTestingPilots()
#新手指南
hankTestPilot.hankGuide()

#新手礼包
hankTestPilot.HankGifts(mark_channel,operator,BillingPointPictures)
#198元\98元\40元
hankTestPilot.OneHundredNintyEightDiamond(mark_channel,operator,BillingPointPictures)
#18元
hankTestPilot.EighteenDiamond(mark_channel,operator,BillingPointPictures)
#8元
hankTestPilot.EightDiamond(mark_channel,operator,BillingPointPictures)
#3元
hankTestPilot.ThreeDiamond(mark_channel,operator,BillingPointPictures)
#退出游戏
exits = back()
exits.goback()















































