# -*- encoding=utf8 -*-
__author__ = "zx"

from airtest.core.api import *
auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

from airtest.core.api import using

using("BasicOperation.air")
using("MyTalkingTomPoolTestingPilot.air")

from BasicOperation import Guide
from BasicOperation import back
from MyTalkingTomPoolTestingPilot import TomPoolTestPilot

audit = "noAudit"
# audit = "isAudit"

# channel = "Mobile"
channel = "Telecom"
#channel = "Unicom"

if exists(Template(r"tpl1528333874352.png", record_pos=(0.378, -0.023), resolution=(1080, 1920))):
    touch(Template(r"tpl1528333888728.png", record_pos=(0.374, -0.021), resolution=(1080, 1920)))
    sleep(15)
if poco("com.outfit7.talkingtompool.bd:id/iv_banner_insert_close").wait(10):
    poco("com.outfit7.talkingtompool.bd:id/iv_banner_insert_close").click()

#首次安装，新手指南
def TalkingTomPoolGuide():
    TomPoolGuide = Guide()
    TomPoolGuide_run = TomPoolGuide.TalkingTomPoolGuide()
    TomPoolGuide_run
TalkingTomPoolGuide()

#新手礼包
def TomPoolGifts(channel,audit):
    TomPoolGifts = TomPoolTestPilot()
    TomPoolGifts_run = TomPoolGifts.TomPoolGifts(channel,audit)
    TomPoolGifts_run
TomPoolGifts(channel,audit)

#328元
def ThreeHundredTwentyEightCoin(channel):
    ThreeHundredTwentyEightCoin = TomPoolTestPilot()
    ThreeHundredTwentyEightCoin_run = ThreeHundredTwentyEightCoin.ThreeHundredTwentyEightCoin(channel)
    ThreeHundredTwentyEightCoin_run
ThreeHundredTwentyEightCoin(channel)

#128元
def OneHundredTwentyEightCoin(channel):
    OneHundredTwentyEightCoin = TomPoolTestPilot()
    OneHundredTwentyEightCoin_run = OneHundredTwentyEightCoin.OneHundredTwentyEightCoin(channel)
    OneHundredTwentyEightCoin_run
OneHundredTwentyEightCoin(channel)
    
#98元
def NintyEightCoin(channel):
    NintyEightCoin = TomPoolTestPilot()
    NintyEightCoin_run = NintyEightCoin.NintyEightCoin(channel)
    NintyEightCoin_run
NintyEightCoin(channel)

#30元
def ThirtyCoin(channel,audit):
    ThirtyCoin = TomPoolTestPilot()
    ThirtyCoin_run = ThirtyCoin.ThirtyCoin(channel,audit)
    ThirtyCoin_run
ThirtyCoin(channel,audit)

#12元
def TwelveCoin(channel,audit):
    TwelveCoin = TomPoolTestPilot()
    TwelveCoin_run = TwelveCoin.TwelveCoin(channel,audit)
    TwelveCoin_run
TwelveCoin(channel,audit)

#6元
def sixCoin(channel,audit):
    sixCoin = TomPoolTestPilot()
    sixCoin_run = sixCoin.sixCoin(channel,audit)
    sixCoin_run
sixCoin(channel,audit)

#50呀
def FiftyGiftBag(channel):
    FiftyGiftBag = TomPoolTestPilot()
    FiftyGiftBag_run = FiftyGiftBag.FiftyGiftBag(channel)
    FiftyGiftBag_run
FiftyGiftBag(channel)

#148元-2000
def OneHundredFourtyEightExchangeTwentyGiftBag(channel):
    OneHundredFourtyEightExchangeTwentyGiftBag = TomPoolTestPilot()
    OneHundredFourtyEightExchangeTwentyGiftBag_run = OneHundredFourtyEightExchangeTwentyGiftBag.OneHundredFourtyEightExchangeTwentyGiftBag(channel)
    OneHundredFourtyEightExchangeTwentyGiftBag_run
OneHundredFourtyEightExchangeTwentyGiftBag(channel)

#148元-20
def OneHundredFourtyEightExchangeTwoThousandGiftBag(channel):
    OneHundredFourtyEightExchangeTwoThousandGiftBag = TomPoolTestPilot()
    OneHundredFourtyEightExchangeTwoThousandGiftBag_run = OneHundredFourtyEightExchangeTwoThousandGiftBag.OneHundredFourtyEightExchangeTwoThousandGiftBag(channel)
    OneHundredFourtyEightExchangeTwoThousandGiftBag_run
OneHundredFourtyEightExchangeTwoThousandGiftBag(channel)

#20元
def TwentyGiftBag(channel,audit):
    TwentyGiftBag = TomPoolTestPilot()
    TwentyGiftBag_run = TwentyGiftBag.TwentyGiftBag(channel,audit)
    TwentyGiftBag_run
TwentyGiftBag(channel,audit)

#10元
def TenGiftBag(channel,audit):
    TenGiftBag = TomPoolTestPilot()
    TenGiftBag_run = TenGiftBag.TenGiftBag(channel,audit)
    TenGiftBag_run
TenGiftBag(channel,audit)

#退出游戏
def Exit():
    exit = back()
    exit_run = exit.goback()
    exit_run
Exit()






