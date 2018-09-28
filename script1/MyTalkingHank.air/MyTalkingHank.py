# -*- encoding=utf8 -*-
__author__ = "zx"

from airtest.core.api import *
auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

from airtest.core.api import using

using("BasicOperation.air")
using("MyTalkingHankTestingPilot.air")
from BasicOperation import *
from MyTalkingHankTestingPilot import HankTestingPilots

# channel = "Mobile"
# channel = "Telecom"
channel = "Unicom"

if exists(Template(r"tpl1527566292694.png", record_pos=(0.0, 0.264), resolution=(1080, 1920))):
    touch(Template(r"tpl1527566292694.png", record_pos=(0.0, 0.264), resolution=(1080, 1920)))
    sleep(25)
poco = AndroidUiautomationPoco(force_restart=False)
if poco("com.outfit7.talkingtompool.bd:id/iv_banner_insert_close").wait(10):
    poco("com.outfit7.talkingtompool.bd:id/iv_banner_insert_close").click()

#首次安装，新手指南
def hankGuide():
    hankGuide = Guide()
    Guide_run = hankGuide.MyTalkingHankGuide()
    Guide_run
# hankGuide()

#新手礼包
def HankGifts(channel):
    HankGifts = HankTestingPilots()
    HankGifts_run = HankGifts.HankGifts(channel)
    HankGifts_run
# HankGifts(channel)
    
#198元
def OneHundredNintyEightDiamond(channel):
    OneHundredNintyEightDiamond = HankTestingPilots()
    OneHundredNintyEightDiamond_run = OneHundredNintyEightDiamond.OneHundredNintyEightDiamond(channel)
    OneHundredNintyEightDiamond_run
OneHundredNintyEightDiamond(channel)

#98元
def NintyEightDimond(channel):
    NintyEightDimond = HankTestingPilots()
    NintyEightDimond_run = NintyEightDimond.NintyEightDimond(channel)
    NintyEightDimond_run
# NintyEightDimond(channel)

#40元
def fourtyDiamond(channel):
    fourtyDiamond = HankTestingPilots()
    fourtyDiamond_run = fourtyDiamond.fourtyDiamond(channel)
    fourtyDiamond_run
# fourtyDiamond(channel)

#18元
def EighteenDiamond(channel):
    EighteenDiamond = HankTestingPilots()
    EighteenDiamond_run = EighteenDiamond.EighteenDiamond(channel)
    EighteenDiamond_run
# EighteenDiamond(channel)

#8元
def EightDiamond(channel):
    EightDiamond = HankTestingPilots()
    EightDiamond_run = EightDiamond.EightDiamond(channel)
    EightDiamond_run
EightDiamond(channel)

#3元
def ThreeDiamond(channel):
    ThreeDiamond = HankTestingPilots()
    ThreeDiamond_run = ThreeDiamond.ThreeDiamond(channel)
    ThreeDiamond_run
ThreeDiamond(channel)

#退出游戏
def Exit():
    exits = back()
    exits_run = exits.goback()
    exits_run
Exit()



































