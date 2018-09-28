# -*- encoding=utf8 -*-
__author__ = "zx"

from airtest.core.api import *
auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

from airtest.core.api import using

using("BasicOperation.air")
from BasicOperation import *

using("MyTalkingAngelTestingPilot.air")
from MyTalkingAngelTestingPilot import AngelTestPilot

# channel = "Mobile"
channel = "Telecom"
# channel = "Unicom"

#启动游戏
if exists(Template(r"tpl1527573475977.png", record_pos=(0.368, 0.156), resolution=(720, 1280))):
    touch(Template(r"tpl1527573475977.png", record_pos=(0.368, 0.156), resolution=(720, 1280)))
    sleep(40)

#首次安装，新手指南
angelGuide = Guide()
angelGuide.MyTalkingAngelaGuide()


AngelTestPilot= AngelTestPilot()
#新手礼包
AngelTestPilot.AngelGifts(channel)

#双倍赚币
AngelTestPilot.AngelDoubleCoin(channel)

#成堆钻石
AngelTestPilot.HeapDiamond(channel)

#袋装钻石
AngelTestPilot.BaggedDiamond(channel)

#盒装钻石
AngelTestPilot.BoxPackedDiamond(channel)
    
#小箱钻石
AngelTestPilot.SBoxAssemblyDiamond(channel)

#大箱钻石
AngelTestPilot.BBoxAssemblyDiamond(channel)

#衣橱
AngelTestPilot.Wardrobe(channel)

#退出游戏，返回主页面
AngelExit = back()
AngelExit.goback()
   














































