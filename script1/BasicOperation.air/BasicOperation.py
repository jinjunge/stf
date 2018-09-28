# -*- encoding=utf8 -*-

__author__ = "zx"

from airtest.core.api import *
auto_setup(__file__)
from airtest.core.api import using
using("MyTalkingAngelTestingPilot.air")
using("MyTalkingTomTestingPilot.air")
using("MyTalkingTomPoolTestingPilot.air")
using("MyTalkingHankTestingPilot.air")

from MyTalkingAngelTestingPilot import AngelTestPilot
from MyTalkingTomTestingPilot import TomTestPilot
from MyTalkingTomPoolTestingPilot import TomPoolTestPilot
from MyTalkingHankTestingPilot import HankTestingPilots

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)



def photo1_TalkingTomPoolGuide():
    wait(Template(r"tpl1531302603133.png", record_pos=(0.025, -0.014), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636607018.png", record_pos=(0.001, 0.104), resolution=(1920, 1080)),duration=3,times=2)
    wait(Template(r"tpl1529636641774.png", record_pos=(-0.001, 0.179), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636651121.png", record_pos=(-0.003, 0.181), resolution=(1920, 1080)))
    wait(Template(r"tpl1529636664050.png", record_pos=(0.001, -0.02), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636672469.png", record_pos=(0.215, -0.001), resolution=(1920, 1080)))
    sleep(28)
    wait(Template(r"tpl1529636718487.png", record_pos=(0.432, 0.217), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636729393.png", record_pos=(0.433, 0.218), resolution=(1920, 1080)))
    sleep(5)

    swipe((1433.3,528.5),(1695.0,528.5))
    sleep(10)

    swipe((1418.3,527.5),(1691.0,510.5))
    sleep(8)

    swipe((1086.4,172.4),(1086.4,993.0))
    sleep(8)

    swipe((1505.1,485.5),(1744.0,719.2))
    sleep(5)
    swipe((1128,806),(1457.1,870.2))
    sleep(28)

    touch((930,204))
    sleep(5)
    touch(Template(r"tpl1529637728345.png", record_pos=(0.061, 0.215), resolution=(1920, 1080)))
    sleep(5)
    touch(Template(r"tpl1529637745216.png", record_pos=(0.223, 0.203), resolution=(1920, 1080)))
    sleep(25)

def photo2_TalkingTomPoolGuide():
    wait(Template(r"tpl1531360137146.png", record_pos=(-0.016, -0.013), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636607018.png", record_pos=(0.001, 0.104), resolution=(1920, 1080)),duration=3,times=2)
    wait(Template(r"tpl1529636641774.png", record_pos=(-0.001, 0.179), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636651121.png", record_pos=(-0.003, 0.181), resolution=(1920, 1080)))
    wait(Template(r"tpl1529636664050.png", record_pos=(0.001, -0.02), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636672469.png", record_pos=(0.215, -0.001), resolution=(1920, 1080)))
    sleep(28)
    wait(Template(r"tpl1529636718487.png", record_pos=(0.432, 0.217), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636729393.png", record_pos=(0.433, 0.218), resolution=(1920, 1080)))
    sleep(5)

    swipe((1433.3,528.5),(1695.0,528.5))
    sleep(10)

    swipe((1418.3,527.5),(1691.0,510.5))
    sleep(8)

    swipe((1086.4,172.4),(1086.4,993.0))
    sleep(8)

    swipe((1505.1,485.5),(1744.0,719.2))
    sleep(5)
    swipe((1128,806),(1457.1,870.2))
    sleep(28)

    touch((930,204))
    sleep(5)
    touch(Template(r"tpl1529637728345.png", record_pos=(0.061, 0.215), resolution=(1920, 1080)))
    sleep(5)
    touch(Template(r"tpl1529637745216.png", record_pos=(0.223, 0.203), resolution=(1920, 1080)))
    sleep(25)

def photo3_TalkingTomPoolGuide():
    wait(Template(r"tpl1531364913497.png", record_pos=(-0.007, -0.014), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636607018.png", record_pos=(0.001, 0.104), resolution=(1920, 1080)),duration=3,times=2)
    wait(Template(r"tpl1529636641774.png", record_pos=(-0.001, 0.179), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636651121.png", record_pos=(-0.003, 0.181), resolution=(1920, 1080)))
    wait(Template(r"tpl1529636664050.png", record_pos=(0.001, -0.02), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636672469.png", record_pos=(0.215, -0.001), resolution=(1920, 1080)))
    sleep(28)
    wait(Template(r"tpl1529636718487.png", record_pos=(0.432, 0.217), resolution=(1920, 1080)))
    touch(Template(r"tpl1529636729393.png", record_pos=(0.433, 0.218), resolution=(1920, 1080)))
    sleep(5)

    swipe((1433.3,528.5),(1695.0,528.5))
    sleep(10)

    swipe((1418.3,527.5),(1691.0,510.5))
    sleep(8)

    swipe((1086.4,172.4),(1086.4,993.0))
    sleep(8)

    swipe((1505.1,485.5),(1744.0,719.2))
    sleep(5)
    swipe((1128,806),(1457.1,870.2))
    sleep(28)

    touch((930,204))
    sleep(5)
    touch(Template(r"tpl1529637728345.png", record_pos=(0.061, 0.215), resolution=(1920, 1080)))
    sleep(5)
    touch(Template(r"tpl1529637745216.png", record_pos=(0.223, 0.203), resolution=(1920, 1080)))
    sleep(25)

#首次安装，使用指南
class Guide(object):
    
    def MyTalkingTomGuide(self):
        if exists(Template(r"tpl1528421013765.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, -0.035), resolution=(1080, 1920))):
            wait(Template(r"tpl1528421048887.png", record_pos=(-0.005, 0.205), resolution=(1080, 1920)),20)
            touch(Template(r"tpl1528421070811.png", record_pos=(0.001, 0.209), resolution=(1080, 1920)))  
            sleep(10)
            touch(Template(r"tpl1528421070811.png", record_pos=(0.001, 0.209), resolution=(1080, 1920)))
            sleep(5)
            touch(Template(r"tpl1528421143716.png", record_pos=(-0.005, 0.399), resolution=(1080, 1920)))
            sleep(3)
        if exists(Template(r"tpl1528421166679.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.01, -0.072), resolution=(1080, 1920))):
            touch(Template(r"tpl1528421192728.png", record_pos=(0.333, -0.02), resolution=(1080, 1920)))
            sleep(5)
        if exists(Template(r"tpl1528421249213.png", record_pos=(0.358, -0.827), resolution=(1080, 1920))):
            touch(Template(r"tpl1528421249213.png", record_pos=(0.358, -0.827), resolution=(1080, 1920)))
        sleep(5)
        if exists(Template(r"tpl1528421296692.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.009, -0.035), resolution=(1080, 1920))):
            touch(Template(r"tpl1528421311594.png", record_pos=(0.433, -0.831), resolution=(1080, 1920)))
            sleep(5)
        if exists(Template(r"tpl1533197145625.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.007, -0.033), resolution=(1080, 1920))):
            # touch(Template(r"tpl1533197163426.png", record_pos=(0.429, -0.819), resolution=(1080, 1920)))
            keyevent("back")
            sleep(5)
        if exists(Template(r"tpl1533197199021.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.0, 0.497), resolution=(1080, 1920))):
            touch(Template(r"tpl1535439201173.png", record_pos=(0.396, -0.799), resolution=(720, 1280)))
            # touch((973.0,117.9))
            sleep(5)

    def MyTalkingHankGuide(self):
        if exists(Template(r"tpl1528794807132.png", threshold=0.65, target_pos=5, rgb=False, record_pos=(0.006, -0.033), resolution=(720, 1280))):   
            touch(Template(r"tpl1528794944318.png", record_pos=(0.0, 0.329), resolution=(720, 1280)),duration=3,times=2)
            sleep(5)
            touch(Template(r"tpl1528794967575.png", threshold=0.65, target_pos=5, rgb=False, record_pos=(-0.004, 0.636), resolution=(720, 1280)))
            sleep(3)        
            if exists(Template(r"tpl1528794989026.png", threshold=0.65, target_pos=5, rgb=False, record_pos=(0.014, -0.013), resolution=(720, 1280))):
                touch(Template(r"tpl1528795011999.png", record_pos=(0.304, -0.019), resolution=(720, 1280)))
                sleep(18)
            if exists(Template(r"tpl1528796264806.png", threshold=0.65, target_pos=5, rgb=False, record_pos=(0.004, -0.021), resolution=(720, 1280))):
                touch(Template(r"tpl1528796280135.png", record_pos=(0.417, -0.825), resolution=(720, 1280)))
                sleep(3)
            if exists(Template(r"tpl1528795098333.png", threshold=0.65, target_pos=5, rgb=False, record_pos=(0.169, 0.121), resolution=(720, 1280))):
                touch(Template(r"tpl1528795123939.png", record_pos=(0.064, -0.117), resolution=(720, 1280)))
                sleep(15)
            # if exists(Template(r"tpl1528855226781.png", threshold=0.6499999999999998, target_pos=5, rgb=False, record_pos=(-0.38, 0.773), resolution=(1080, 1920))):
            if exists(Template(r"tpl1537497617909.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(-0.372, 0.782), resolution=(1080, 1920))):
            # touch(Template(r"tpl1528857483975.png", record_pos=(0.031, 0.397), resolution=(1080, 1920)),duration=3,times=2)
                swipe((555,1450),(555,1150))
                sleep(10)
            if exists(Template(r"tpl1528855528866.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.192, 0.764), resolution=(1080, 1920))):
                touch(Template(r"tpl1528795320279.png", record_pos=(-0.194, 0.782), resolution=(720, 1280)))
                sleep(3)
                touch(Template(r"tpl1528795354931.png", record_pos=(0.029, 0.208), resolution=(720, 1280)))
                sleep(10)
            if exists(Template(r"tpl1528855565619.png", threshold=0.9000000000000004, target_pos=5, rgb=False, record_pos=(-0.005, 0.763), resolution=(1080, 1920))):
                touch(Template(r"tpl1528795399843.png", record_pos=(-0.007, 0.782), resolution=(720, 1280)))
                sleep(20)
            if exists(Template(r"tpl1528855601771.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.185, 0.769), resolution=(1080, 1920))):
                touch(Template(r"tpl1528795454052.png", record_pos=(0.183, 0.782), resolution=(720, 1280)))
                sleep(3)
                wait(Template(r"tpl1528795474101.png", record_pos=(0.111, -0.429), resolution=(720, 1280)))
                touch(Template(r"tpl1528795488911.png", record_pos=(0.037, -0.474), resolution=(720, 1280)))
                sleep(10)
                wait(Template(r"tpl1528795515076.png", record_pos=(0.119, -0.442), resolution=(720, 1280)))
                touch(Template(r"tpl1528795523243.png", record_pos=(0.047, -0.481), resolution=(720, 1280)))
                sleep(18)
            if exists(Template(r"tpl1528795570874.png", threshold=0.8500000000000002, target_pos=5, rgb=False, record_pos=(0.375, 0.726), resolution=(720, 1280))):
                touch(Template(r"tpl1528795570874.png", record_pos=(0.375, 0.726), resolution=(720, 1280)))
                sleep(10)
                wait(Template(r"tpl1528795592358.png", record_pos=(0.178, 0.36), resolution=(720, 1280)))
                #touch(Template(r"tpl1528795602044.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.182, 0.358), resolution=(720, 1280)))
                touch(Template(r"tpl1528859892109.png", record_pos=(0.155, 0.369), resolution=(1080, 1920)))
                sleep(20)
                wait(Template(r"tpl1528795638380.png", record_pos=(0.175, 0.439), resolution=(720, 1280)))
                touch(Template(r"tpl1528795652170.png", record_pos=(0.161, 0.407), resolution=(720, 1280)))
                sleep(10)
                wait(Template(r"tpl1528795688656.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.343, -0.486), resolution=(720, 1280)))
                touch(Template(r"tpl1528795702246.png", record_pos=(-0.335, -0.487), resolution=(720, 1280)))
                sleep(10)
                wait(Template(r"tpl1528795722489.png", record_pos=(-0.192, 0.774), resolution=(720, 1280)))
                touch(Template(r"tpl1528795729388.png", record_pos=(-0.193, 0.782), resolution=(720, 1280)))
                sleep(10)
                touch(Template(r"tpl1528795751202.png", record_pos=(-0.393, 0.239), resolution=(720, 1280)))
                sleep(3)
                touch(Template(r"tpl1528795774663.png", record_pos=(-0.304, -0.397), resolution=(720, 1280)))
                sleep(3)
                touch(Template(r"tpl1528795751202.png", record_pos=(-0.393, 0.239), resolution=(720, 1280)))
                sleep(3)
                touch(Template(r"tpl1528795809864.png", record_pos=(-0.014, -0.399), resolution=(720, 1280)))
                sleep(3)
                wait(Template(r"tpl1528795826716.png", record_pos=(-0.003, 0.776), resolution=(720, 1280)))
                touch(Template(r"tpl1528795833751.png", record_pos=(-0.004, 0.772), resolution=(720, 1280)))
                sleep(10)
                touch(Template(r"tpl1528795862688.png", record_pos=(0.2, 0.438), resolution=(720, 1280)))
                sleep(10)
                wait(Template(r"tpl1528795879671.png", record_pos=(0.369, 0.722), resolution=(720, 1280)))
                touch(Template(r"tpl1528795887770.png", record_pos=(0.36, 0.728), resolution=(720, 1280)))
                sleep(10)
                wait(Template(r"tpl1528795910689.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.181, 0.354), resolution=(720, 1280)))
                touch(Template(r"tpl1528795910689.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.181, 0.354), resolution=(720, 1280)))
                sleep(3)
                wait(Template(r"tpl1528795948300.png", record_pos=(-0.001, 0.239), resolution=(720, 1280)))
                touch(Template(r"tpl1528805630917.png", record_pos=(0.006, -0.022), resolution=(1080, 1920)))
                sleep(3)
                wait(Template(r"tpl1528795991406.png", record_pos=(0.006, 0.651), resolution=(720, 1280)))
                touch(Template(r"tpl1528796000215.png", record_pos=(0.001, 0.65), resolution=(720, 1280)))
                sleep(10)
                wait(Template(r"tpl1528795879671.png", record_pos=(0.369, 0.722), resolution=(720, 1280)))
                touch(Template(r"tpl1528795887770.png", record_pos=(0.36, 0.728), resolution=(720, 1280)))
                sleep(10)
                wait(Template(r"tpl1528796055229.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.41, 0.546), resolution=(720, 1280)))
                touch(Template(r"tpl1528796233239.png", record_pos=(-0.415, 0.55), resolution=(720, 1280)))
                sleep(5)
        if exists(Template(r"tpl1528796264806.png", threshold=0.65, target_pos=5, rgb=False, record_pos=(0.004, -0.021), resolution=(720, 1280))):
            touch(Template(r"tpl1528796280135.png", record_pos=(0.417, -0.825), resolution=(720, 1280)))
            sleep(3)
        sleep(5)

    def MyTalkingAngelaGuide(self):
        if exists(Template(r"tpl1527646290378.png", record_pos=(0.02, -0.004), resolution=(1080, 1920))):
            # wait(Template(r"tpl1527648452875.png", record_pos=(0.0, 0.207), resolution=(1080, 1920)),20)
            # touch(Template(r"tpl1527648469364.png", record_pos=(-0.009, 0.217), resolution=(1080, 1920)))   
            # sleep(10)
            touch(Template(r"tpl1535462984111.png", record_pos=(-0.006, 0.216), resolution=(1080, 1920)),duration=0.01,times=3)
            sleep(3)
            touch(Template(r"tpl1527647150560.png", record_pos=(-0.009, 0.393), resolution=(1080, 1920)))
            sleep(3)
        if exists(Template(r"tpl1527647168075.png", record_pos=(-0.002, -0.024), resolution=(1080, 1920))):
            touch(Template(r"tpl1527647176176.png", record_pos=(0.308, -0.011), resolution=(1080, 1920)))
            sleep(5)
        if exists(Template(r"tpl1527647218489.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.011, -0.119), resolution=(1080, 1920))):
            touch(Template(r"tpl1527647226513.png", record_pos=(-0.352, -0.807), resolution=(1080, 1920)))
            sleep(5)
        if exists(Template(r"tpl1533196421069.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(-0.006, 0.483), resolution=(1080, 1920))):
            touch((961.0,112.9))
            sleep(3)
            
    def TalkingTomPoolGuide(self):
        if exists(Template(r"tpl1531302603133.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.025, -0.014), resolution=(1920, 1080))):
            
            photo1_TalkingTomPoolGuide()
        
        elif exists(Template(r"tpl1531360137146.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.016, -0.013), resolution=(1920, 1080))):
            
            photo2_TalkingTomPoolGuide()
            
        elif exists(Template(r"tpl1531364913497.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.007, -0.014), resolution=(1920, 1080))):
            
            photo3_TalkingTomPoolGuide()

    
    
#退出游戏，返回主页面    
class back(object): 

    def goback(self):
        sleep(5)
        if exists(Template(r"tpl1533198407725.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.25, -0.206), resolution=(1080, 1920))):
            touch(Template(r"tpl1533198407725.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.25, -0.206), resolution=(1080, 1920)))
            # touch((809.2,741.5))
            sleep(5)
            
        keyevent("back")
        sleep(5)
        if exists(Template(r"tpl1529574337008.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.01), resolution=(1920, 1080))):
            wait(Template(r"tpl1529574337008.png", record_pos=(0.004, -0.01), resolution=(1920, 1080)))
            touch(Template(r"tpl1529574350328.png", record_pos=(-0.083, 0.113), resolution=(1920, 1080)))
            sleep(5)
            
        elif exists(Template(r"tpl1527573475977.png", record_pos=(0.368, 0.156), resolution=(720, 1280))):
            return
        
        elif exists(Template(r"tpl1528423786702.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, 0.253), resolution=(1080, 1920))):
            return
        elif exists(Template(r"tpl1527566292694.png", record_pos=(0.0, 0.264), resolution=(1080, 1920))):
            return
        elif exists(Template(r"tpl1528333874352.png", record_pos=(0.378, -0.023), resolution=(1080, 1920))):
            return

        elif exists(Template(r"tpl1528423693945.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, -0.01), resolution=(1080, 1920))):
            touch(Template(r"tpl1528423709662.png", record_pos=(0.206, 0.19), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1531451790733.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.007, -0.028), resolution=(1080, 1920))):

            touch(Template(r"tpl1531451805138.png", record_pos=(0.005, 0.154), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1528427149465.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, -0.006), resolution=(1080, 1920))):
            touch(Template(r"tpl1528427161090.png", record_pos=(-0.193, 0.182), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1528428493317.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.016, 0.138), resolution=(1080, 1920))):
            touch(Template(r"tpl1528428505556.png", record_pos=(-0.228, 0.418), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1528429781417.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.007, 0.046), resolution=(1080, 1920))):
            touch(Template(r"tpl1528429794954.png", record_pos=(-0.219, 0.148), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1528429834311.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.012), resolution=(1080, 1920))):
            touch(Template(r"tpl1528429848232.png", record_pos=(0.191, 0.118), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1530157329037.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, 0.022), resolution=(1920, 1080))):
            touch(Template(r"tpl1530157343734.png", record_pos=(-0.13, 0.082), resolution=(1920, 1080)))
            sleep(3)
        elif exists(Template(r"tpl1530157256249.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.006, 0.216), resolution=(1920, 1080))):
            touch(Template(r"tpl1530157288008.png", record_pos=(-0.122, 0.219), resolution=(1920, 1080)))





         