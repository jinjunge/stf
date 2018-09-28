# -*- encoding=utf8 -*-
__author__ = "zx"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from airtest.core.api import using

using("BasicOperation.air")
from BasicOperation import *

using("MyTalkingTomTestingPilot.air")
from MyTalkingTomTestingPilot import TomTestPilot

poco = AndroidUiautomationPoco(force_restart=False)

audit = "noAudit"
# audit = "isAudit"

# channel = "Mobile"
channel = "Telecom"
# channel = "Unicom"
#启动游戏
def Startgame():
    if exists(Template(r"tpl1528423786702.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, 0.253), resolution=(1080, 1920))):
        touch(Template(r"tpl1528423809962.png", record_pos=(-0.001, 0.259), resolution=(1080, 1920)))
        sleep(30)

    # if poco("com.outfit7.talkingtom.bd:id/iv_banner_insert_close").wait(10):
    #     poco("com.outfit7.talkingtom.bd:id/iv_banner_insert_close").click()

#启动游戏
Startgame()

#新手指南
tomGuide = Guide()
tomGuide.MyTalkingTomGuide()

#10元礼包
tomGifts = Gifts()
tomGifts.MyTalkingTomGifts(channel,audit)

TomTestPilot = TomTestPilot()
#双倍赚币-10元
TomTestPilot.TomDoubleCoin(channel,audit)

#5元钻石
TomTestPilot.FiveDiamond(channel,audit)

#70
TomTestPilot.SeventyDiamond(channel,audit)

#190
TomTestPilot.HundredNinetyDiamond(channel,audit)

#1590
TomTestPilot.ThousandFiveHundeedNinetyDiamond(channel)

#6250
TomTestPilot.SixthousandTwoHundredFiftyDiamond(channel)

#成人眼药水
TomTestPilot.AdultEyedrops(channel,audit)

#婴儿眼药水
TomTestPilot.BabyEyedrops(channel,audit)

#水手制服
TomTestPilot.SailorUniforms(channel,audit)

#退出游戏
exit = back()
exit.goback()
