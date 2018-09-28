# -*- encoding=utf8 -*-
__author__ = "zx"

from airtest.core.api import *
auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

"""
hank testcase update 07.18

"""
def HankGifts_Mobile():
    if exists(Template(r"tpl1528803949170.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.357, -0.239), resolution=(1080, 1920))):
    # if exists(Template(r"tpl1528803886903.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.005, -0.003), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528803949170.png", record_pos=(0.357, -0.239), resolution=(1080, 1920)),"新手礼包0.02元")
        touch(Template(r"tpl1528803984785.png", record_pos=(-0.404, -0.239), resolution=(1080, 1920)))
        sleep(3)
        wait(Template(r"tpl1528804005287.png", record_pos=(0.0, -0.004), resolution=(1080, 1920)))
        touch(Template(r"tpl1528804012455.png", record_pos=(-0.004, 0.078), resolution=(1080, 1920)))
        touch(Template(r"tpl1528804025356.png", record_pos=(0.417, -0.826), resolution=(1080, 1920)))
        sleep(5)
    elif exists(Template(r"tpl1527768172551.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.038, -0.2), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527768191639.png", record_pos=(0.038, -0.2), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")
        touch(Template(r"tpl1527768922211.png", record_pos=(-0.405, -0.213), resolution=(1080, 1920)))
        sleep(2)
        touch(Template(r"tpl1527768936144.png", record_pos=(-0.001, 0.067), resolution=(1080, 1920)))
        sleep(2.0)
        keyevent("BACK") 
        sleep(1)

def HankGifts_Telecom():
    if exists(Template(r"tpl1528378124025.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.037), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528378137588.png", record_pos=(0.212, -0.155), resolution=(1080, 1920)), "新手礼包，10元")
        touch(Template(r"tpl1528377486858.png", record_pos=(0.396, -0.169), resolution=(1080, 1920)))
        wait(Template(r"tpl1528377495625.png", record_pos=(-0.001, 0.076), resolution=(1080, 1920)))
        touch(Template(r"tpl1528377503215.png", record_pos=(-0.003, 0.066), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528378056435.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.032), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528378076089.png", record_pos=(0.325, -0.2), resolution=(1080, 1920)), "新手礼包，10元")
        touch(Template(r"tpl1528377486858.png", record_pos=(0.396, -0.169), resolution=(1080, 1920)))
        wait(Template(r"tpl1528377495625.png", record_pos=(-0.001, 0.076), resolution=(1080, 1920)))
        touch(Template(r"tpl1528377503215.png", record_pos=(-0.003, 0.066), resolution=(1080, 1920)))
    sleep(3)
    touch(Template(r"tpl1528370662090.png", record_pos=(0.427, -0.825), resolution=(1080, 1920)))
    sleep(5)

def HankGifts_Unicom():
    if exists(Template(r"tpl1528367858079.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.016, -0.024), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528367879723.png", record_pos=(0.019, -0.037), resolution=(1080, 1920)), "yunos新手礼物金额显示正确，10元")
        touch(Template(r"tpl1528367937576.png", record_pos=(0.35, -0.279), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528369418329.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.154), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528369436278.png", record_pos=(0.314, -0.365), resolution=(1080, 1920)), "baidu新手礼物金额显示正确，10元")
        touch(Template(r"tpl1528369462076.png", record_pos=(-0.399, -0.56), resolution=(1080, 1920)))
        wait(Template(r"tpl1528369473241.png", record_pos=(0.004, -0.001), resolution=(1080, 1920)))
        touch(Template(r"tpl1528369479053.png", record_pos=(0.204, 0.128), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528372540838.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.023), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528372555936.png", record_pos=(0.292, -0.215), resolution=(1080, 1920)), "oppo新手礼物金额显示正确，10元")
        touch(Template(r"tpl1528372581626.png", record_pos=(0.37, -0.375), resolution=(1080, 1920)))
        wait(Template(r"tpl1528372591728.png", record_pos=(0.007, 0.034), resolution=(1080, 1920)))
        touch(Template(r"tpl1528372600454.png", record_pos=(0.202, 0.099), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528372873205.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.014, -0.066), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528372900661.png", record_pos=(-0.239, -0.244), resolution=(1080, 1920)), "sdk360新手礼物金额显示正确，10元")
        touch(Template(r"tpl1528372938339.png", record_pos=(0.381, -0.38), resolution=(1080, 1920)))
        wait(Template(r"tpl1528372952875.png", record_pos=(0.006, -0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1528372975879.png", record_pos=(-0.203, 0.161), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1531906195373.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.045, -0.58), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528374328834.png", record_pos=(-0.337, -0.471), resolution=(1080, 1920)), "sdk4399新手礼物金额显示正确，10元")
        touch(Template(r"tpl1528373763655.png", record_pos=(0.377, -0.588), resolution=(1080, 1920)))
        wait(Template(r"tpl1528373777596.png", record_pos=(0.004, 0.071), resolution=(1080, 1920)))
        touch(Template(r"tpl1528373784488.png", record_pos=(0.004, 0.071), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528374785603.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.009, -0.014), resolution=(1080, 1920))):
        touch(Template(r"tpl1528374798751.png", record_pos=(-0.197, 0.201), resolution=(1080, 1920)))
        wait(Template(r"tpl1528374807498.png", record_pos=(0.01, -0.039), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1528374816565.png", record_pos=(-0.114, 0.289), resolution=(1080, 1920)), "meizu新手礼物金额显示正确，10元")
        touch(Template(r"tpl1528374837583.png", record_pos=(0.44, -0.437), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528374881379.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, 0.046), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528374897782.png", record_pos=(-0.149, -0.44), resolution=(1080, 1920)), "anzhi新手礼物金额显示正确，10元")
        touch(Template(r"tpl1528374920598.png", record_pos=(-0.419, -0.71), resolution=(1080, 1920)))
        wait(Template(r"tpl1528374929621.png", record_pos=(0.006, 0.048), resolution=(1080, 1920)))
        touch(Template(r"tpl1528374952105.png", record_pos=(0.192, 0.169), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528375845584.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.016), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528375861191.png", record_pos=(0.304, -0.12), resolution=(1080, 1920)), "gionee新手礼物金额显示正确，10元")
        touch(Template(r"tpl1528375887939.png", record_pos=(0.315, -0.244), resolution=(1080, 1920)))
        wait(Template(r"tpl1528375899889.png", record_pos=(0.0, -0.006), resolution=(1080, 1920)))
        touch(Template(r"tpl1528375909518.png", record_pos=(-0.191, 0.073), resolution=(1080, 1920)))    
    elif exists(Template(r"tpl1529054798054.png", record_pos=(-0.002, -0.111), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1529054808908.png", record_pos=(0.011, -0.494), resolution=(1080, 1920)),"联想新手礼包金额显示正确，10元")
        touch(Template(r"tpl1529054849572.png", record_pos=(-0.43, -0.741), resolution=(1080, 1920)))
        touch(Template(r"tpl1529054858632.png", record_pos=(0.204, 0.193), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "10.00元", "vivo新手礼包金额显示正确，10元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥10.00", "huawei新手礼包金额显示正确，10元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "10.00元", "xiaomi新手礼包金额显示正确，10元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "10.00", "sumsung新手礼包金额显示正确，10元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
    sleep(1)
    touch(Template(r"tpl1528370662090.png", record_pos=(0.427, -0.825), resolution=(1080, 1920)))
    sleep(5)

def EighteenDiamond_Mobile():
    if exists(Template(r"tpl1527649750274.png", record_pos=(-0.01, -0.018), resolution=(1080, 1920))):
        touch(Template(r"tpl1527649759178.png", record_pos=(-0.206, 0.194), resolution=(1080, 1920)))
        sleep(3)

    if exists(Template(r"tpl1527575835563.png", threshold=0.8, target_pos=5, rgb=False, record_pos=(0.39, -0.24), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527575858091.png", threshold=0.8, target_pos=5, rgb=False, record_pos=(0.392, -0.242), resolution=(1080, 1920)), "420钻石==0.1元显示正确，0.1元")
        sleep(3)
        touch(Template(r"tpl1527575905270.png", threshold=0.8, target_pos=5, rgb=False, record_pos=(-0.404, -0.249), resolution=(1080, 1920)))
        touch(Template(r"tpl1527575920893.png", record_pos=(-0.001, 0.074), resolution=(1080, 1920)))

    elif exists(Template(r"tpl1527768451391.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.338, -0.198), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527768462548.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.344, -0.193), resolution=(1080, 1920)), "420钻石==18元显示正确，18元")
        sleep(3)
        touch(Template(r"tpl1527575905270.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.404, -0.249), resolution=(1080, 1920)))
        touch(Template(r"tpl1527575920893.png", record_pos=(-0.001, 0.074), resolution=(1080, 1920)))

    sleep(5)

def EighteenDiamond_Telecom():
    if exists(Template(r"tpl1528377438942.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, -0.035), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528377450736.png", record_pos=(0.202, -0.16), resolution=(1080, 1920)), "420钻石==18元显示正确，18元")
        touch(Template(r"tpl1528377486858.png", record_pos=(0.396, -0.169), resolution=(1080, 1920)))
        wait(Template(r"tpl1528377495625.png", record_pos=(-0.001, 0.076), resolution=(1080, 1920)))
        touch(Template(r"tpl1528377503215.png", record_pos=(-0.003, 0.066), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528377539076.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.029), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528377551922.png", record_pos=(0.333, -0.207), resolution=(1080, 1920)), "420钻石==18元显示正确，18元")
        touch(Template(r"tpl1528377486858.png", record_pos=(0.396, -0.169), resolution=(1080, 1920)))
        wait(Template(r"tpl1528377495625.png", record_pos=(-0.001, 0.076), resolution=(1080, 1920)))
        touch(Template(r"tpl1528377503215.png", record_pos=(-0.003, 0.066), resolution=(1080, 1920)))
    sleep(5)

def EighteenDiamond_Unicom():
    if exists(Template(r"tpl1528368917135.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.027), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528368939259.png", record_pos=(0.306, -0.075), resolution=(1080, 1920)), "420钻石==18元显示正确，18元")
        touch(Template(r"tpl1528368977126.png", record_pos=(-0.351, -0.285), resolution=(1080, 1920)))
        wait(Template(r"tpl1528368988939.png", record_pos=(-0.006, 0.006), resolution=(1080, 1920)))
        touch(Template(r"tpl1528369012530.png", record_pos=(-0.213, 0.119), resolution=(1080, 1920)))
        wait(Template(r"tpl1528369022152.png", record_pos=(-0.006, 0.073), resolution=(1080, 1920)))
        touch(Template(r"tpl1528369031333.png", record_pos=(-0.005, 0.071), resolution=(1080, 1920)))
    sleep(3)

def EightDiamond_Mobile():
    if exists(Template(r"tpl1527649750274.png", record_pos=(-0.01, -0.018), resolution=(1080, 1920))):
        touch(Template(r"tpl1527649759178.png", record_pos=(-0.206, 0.194), resolution=(1080, 1920)))
        sleep(3)

    if exists(Template(r"tpl1527575661104.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.394, -0.238), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527575673049.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.395, -0.244), resolution=(1080, 1920)), "160钻石==0.3元显示正确，0.3元")
        sleep(3)
        touch(Template(r"tpl1527575136897.png", record_pos=(-0.404, -0.247), resolution=(1080, 1920)))
        touch(Template(r"tpl1527575147415.png", record_pos=(-0.01, 0.074), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1527768359895.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.358, -0.196), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527768379766.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.355, -0.196), resolution=(1080, 1920)), "160钻石==8元显示正确，8元")
        sleep(3)
        touch(Template(r"tpl1527575136897.png", record_pos=(-0.404, -0.247), resolution=(1080, 1920)))
        touch(Template(r"tpl1527575147415.png", record_pos=(-0.01, 0.074), resolution=(1080, 1920)))

    sleep(5)

def EightDiamond_Telecom():
    if exists(Template(r"tpl1528377659906.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.018), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528377672446.png", record_pos=(0.214, -0.164), resolution=(1080, 1920)), "160钻石==8元显示正确，8元")
        touch(Template(r"tpl1528377486858.png", record_pos=(0.396, -0.169), resolution=(1080, 1920)))
        wait(Template(r"tpl1528377495625.png", record_pos=(-0.001, 0.076), resolution=(1080, 1920)))
        touch(Template(r"tpl1528377503215.png", record_pos=(-0.003, 0.066), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528377598914.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.029), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528377619822.png", record_pos=(0.356, -0.204), resolution=(1080, 1920)), "160钻石==8元显示正确，8元")
        touch(Template(r"tpl1528377486858.png", record_pos=(0.396, -0.169), resolution=(1080, 1920)))
        wait(Template(r"tpl1528377495625.png", record_pos=(-0.001, 0.076), resolution=(1080, 1920)))
        touch(Template(r"tpl1528377503215.png", record_pos=(-0.003, 0.066), resolution=(1080, 1920)))
    sleep(5)

def EightDiamond_Unicom():
    # if exists(Template(r"tpl1528369120414.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, -0.029), resolution=(1080, 1920))):
    assert_exists(Template(r"tpl1528369134871.png", record_pos=(0.314, -0.07), resolution=(1080, 1920)), "160钻石==8元显示正确，8元")
    touch(Template(r"tpl1528368977126.png", record_pos=(-0.351, -0.285), resolution=(1080, 1920)))
    wait(Template(r"tpl1528368988939.png", record_pos=(-0.006, 0.006), resolution=(1080, 1920)))
    touch(Template(r"tpl1528369012530.png", record_pos=(-0.213, 0.119), resolution=(1080, 1920)))
    wait(Template(r"tpl1528369022152.png", record_pos=(-0.006, 0.073), resolution=(1080, 1920)))
    touch(Template(r"tpl1528369031333.png", record_pos=(-0.005, 0.071), resolution=(1080, 1920)))
    sleep(5)

def ThreeDiamond_Mobile():
    if exists(Template(r"tpl1527649750274.png", record_pos=(-0.01, -0.018), resolution=(1080, 1920))):
        touch(Template(r"tpl1527649759178.png", record_pos=(-0.206, 0.194), resolution=(1080, 1920)))
        sleep(3)

    if exists(Template(r"tpl1527574771545.png", record_pos=(0.371, -0.238), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527574803191.png", record_pos=(0.369, -0.242), resolution=(1080, 1920)), "72钻石==3元显示正确，3元")
        sleep(2)
        touch(Template(r"tpl1527575136897.png", record_pos=(-0.404, -0.247), resolution=(1080, 1920)))
        touch(Template(r"tpl1527575147415.png", record_pos=(-0.01, 0.074), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1527768286180.png", record_pos=(0.356, -0.202), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527768300859.png", record_pos=(0.356, -0.194), resolution=(1080, 1920)), "72钻石==3元显示正确，3元")
        touch(Template(r"tpl1528884363619.png", record_pos=(0.003, 0.063), resolution=(1080, 1920)))
        sleep(10)
        if exists(Template(r"tpl1528887266834.png", record_pos=(0.001, 0.046), resolution=(720, 1280))):
            assert_exists(Template(r"tpl1528887266834.png", record_pos=(0.001, 0.046), resolution=(720, 1280)),"支付成功")
            keyevent("back")
            sleep(2)
    sleep(5)
    wait(Template(r"tpl1528369285738.png", record_pos=(0.415, -0.819), resolution=(1080, 1920)))
    touch(Template(r"tpl1528369293571.png", record_pos=(0.42, -0.825), resolution=(1080, 1920)))
    sleep(5)
    
def ThreeDiamond_Telecom():
    if exists(Template(r"tpl1528377718938.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.025), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528377734935.png", record_pos=(0.227, -0.164), resolution=(1080, 1920)), "72钻石==3元显示正确，3元")
        touch(Template(r"tpl1528377486858.png", record_pos=(0.396, -0.169), resolution=(1080, 1920)))
        wait(Template(r"tpl1528377495625.png", record_pos=(-0.001, 0.076), resolution=(1080, 1920)))
        touch(Template(r"tpl1528377503215.png", record_pos=(-0.003, 0.066), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528377782024.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, -0.022), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528377796950.png", record_pos=(0.344, -0.195), resolution=(1080, 1920)), "72钻石==3元显示正确，3元")
        touch(Template(r"tpl1528377486858.png", record_pos=(0.396, -0.169), resolution=(1080, 1920)))
        wait(Template(r"tpl1528377495625.png", record_pos=(-0.001, 0.076), resolution=(1080, 1920)))
        touch(Template(r"tpl1528377503215.png", record_pos=(-0.003, 0.066), resolution=(1080, 1920)))
    sleep(5)
    
    wait(Template(r"tpl1528369285738.png", record_pos=(0.415, -0.819), resolution=(1080, 1920)))
    touch(Template(r"tpl1528369293571.png", record_pos=(0.42, -0.825), resolution=(1080, 1920)))
    sleep(5)

def ThreeDiamond_Unicom():
    # if exists(Template(r"tpl1528369238344.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.031), resolution=(1080, 1920))):
    assert_exists(Template(r"tpl1528369251121.png", record_pos=(0.313, -0.077), resolution=(1080, 1920)), "160钻石==3元显示正确，3元")
    touch(Template(r"tpl1528368977126.png", record_pos=(-0.351, -0.285), resolution=(1080, 1920)))
    wait(Template(r"tpl1528368988939.png", record_pos=(-0.006, 0.006), resolution=(1080, 1920)))
    touch(Template(r"tpl1528369012530.png", record_pos=(-0.213, 0.119), resolution=(1080, 1920)))
    wait(Template(r"tpl1528369022152.png", record_pos=(-0.006, 0.073), resolution=(1080, 1920)))
    touch(Template(r"tpl1528369031333.png", record_pos=(-0.005, 0.071), resolution=(1080, 1920)))
    sleep(5)
    wait(Template(r"tpl1528369285738.png", record_pos=(0.415, -0.819), resolution=(1080, 1920)))
    touch(Template(r"tpl1528369293571.png", record_pos=(0.42, -0.825), resolution=(1080, 1920)))
    sleep(5)

def OneHundredNintyEightDiamond_founction():
    if exists(Template(r"tpl1528368519415.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.019, -0.02), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528368532098.png", record_pos=(0.007, -0.037), resolution=(1080, 1920)), "yunos5600钻石==198元显示正确，198元")
        touch(Template(r"tpl1528368585479.png", record_pos=(0.355, -0.28), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528369580085.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, -0.219), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528369592309.png", record_pos=(0.31, -0.36), resolution=(1080, 1920)), "baidu5600钻石==198元显示正确，198元")
        touch(Template(r"tpl1528369462076.png", record_pos=(-0.399, -0.56), resolution=(1080, 1920)))
        wait(Template(r"tpl1528369473241.png", record_pos=(0.004, -0.001), resolution=(1080, 1920)))
        touch(Template(r"tpl1528369479053.png", record_pos=(0.204, 0.128), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528372678499.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.004), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528372697756.png", record_pos=(0.275, -0.183), resolution=(1080, 1920)), "oppo5600钻石==198元显示正确，198元")
        touch(Template(r"tpl1528372581626.png", record_pos=(0.37, -0.375), resolution=(1080, 1920)))
        wait(Template(r"tpl1528372591728.png", record_pos=(0.007, 0.034), resolution=(1080, 1920)))
        touch(Template(r"tpl1528372600454.png", record_pos=(0.202, 0.099), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528373242014.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.012, -0.069), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528373257714.png", record_pos=(-0.201, -0.239), resolution=(1080, 1920)), "sdk3605600钻石==198元显示正确，198元")
        touch(Template(r"tpl1528372938339.png", record_pos=(0.381, -0.38), resolution=(1080, 1920)))
        wait(Template(r"tpl1528372952875.png", record_pos=(0.006, -0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1528372975879.png", record_pos=(-0.203, 0.161), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1531906195373.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.045, -0.58), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528374087168.png", record_pos=(-0.318, -0.467), resolution=(1080, 1920)), "sdk43995600钻石==198元显示正确，198元")
        touch(Template(r"tpl1528373763655.png", record_pos=(0.377, -0.588), resolution=(1080, 1920)))
        wait(Template(r"tpl1528373777596.png", record_pos=(0.004, 0.071), resolution=(1080, 1920)))
        touch(Template(r"tpl1528373784488.png", record_pos=(0.004, 0.071), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528374785603.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.009, -0.014), resolution=(1080, 1920))):
        touch(Template(r"tpl1528374798751.png", record_pos=(-0.197, 0.201), resolution=(1080, 1920)))
        wait(Template(r"tpl1528375060569.png", record_pos=(0.009, -0.031), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1528375071875.png", record_pos=(-0.121, 0.28), resolution=(1080, 1920)),"meizu5600钻石==198元显示正确，198元")
        touch(Template(r"tpl1528374837583.png", record_pos=(0.44, -0.437), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528375002456.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, 0.042), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528375018496.png", record_pos=(-0.147, -0.442), resolution=(1080, 1920)), "anzhi5600钻石==198元显示正确，198元")
        touch(Template(r"tpl1528374920598.png", record_pos=(-0.419, -0.71), resolution=(1080, 1920)))
        wait(Template(r"tpl1528374929621.png", record_pos=(0.006, 0.048), resolution=(1080, 1920)))
        touch(Template(r"tpl1528374952105.png", record_pos=(0.192, 0.169), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528375949550.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.01), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528375964405.png", record_pos=(0.289, -0.11), resolution=(1080, 1920)), "gionee5600钻石==198元显示正确，198元")
        touch(Template(r"tpl1528375887939.png", record_pos=(0.315, -0.244), resolution=(1080, 1920)))
        wait(Template(r"tpl1528375899889.png", record_pos=(0.0, -0.006), resolution=(1080, 1920)))
        touch(Template(r"tpl1528375909518.png", record_pos=(-0.191, 0.073), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528877915440.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.029, 0.006), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528877932431.png", record_pos=(0.01, -0.056), resolution=(1080, 1920)),"yunos5600钻石==198元显示正确。198元")
        touch(Template(r"tpl1528877990401.png", record_pos=(0.35, -0.293), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1529052868751.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.0, -0.119), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1529052878828.png", record_pos=(0.002, -0.498), resolution=(1080, 1920)),"联想5600钻石==198元显示正确，198元")
        touch(Template(r"tpl1529052928759.png", record_pos=(-0.426, -0.743), resolution=(1080, 1920)))
        touch(Template(r"tpl1529052942560.png", record_pos=(0.206, 0.191), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "198.00元", "vivo5600钻石==198元显示正确，198元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥198.00", "huawei5600钻石==198元显示正确，198元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "198.00元", "xiaomi5600钻石==198元显示正确，198元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "198.00", "sumsung5600钻石==198元显示正确，198元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
    sleep(5)

def NintyEightDimond_founction():
    if exists(Template(r"tpl1528368656790.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.018, -0.015), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528368681615.png", record_pos=(0.014, -0.032), resolution=(1080, 1920)), "yunos2600钻石==98元显示正确，98元")
        touch(Template(r"tpl1528368711522.png", record_pos=(0.348, -0.272), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528369641725.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.214), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528369655627.png", record_pos=(0.314, -0.358), resolution=(1080, 1920)), "baidu2600钻石==98元显示正确，98元")
        touch(Template(r"tpl1528369462076.png", record_pos=(-0.399, -0.56), resolution=(1080, 1920)))
        wait(Template(r"tpl1528369473241.png", record_pos=(0.004, -0.001), resolution=(1080, 1920)))
        touch(Template(r"tpl1528369479053.png", record_pos=(0.204, 0.128), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528372742474.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, -0.012), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528372755768.png", record_pos=(0.292, -0.183), resolution=(1080, 1920)), "oppo2600钻石==98元显示正确，98元")
        touch(Template(r"tpl1528372581626.png", record_pos=(0.37, -0.375), resolution=(1080, 1920)))
        wait(Template(r"tpl1528372591728.png", record_pos=(0.007, 0.034), resolution=(1080, 1920)))
        touch(Template(r"tpl1528372600454.png", record_pos=(0.202, 0.099), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528373181124.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.072), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528373198573.png", record_pos=(-0.22, -0.237), resolution=(1080, 1920)), "sdk3602600钻石==98元显示正确，98元")
        touch(Template(r"tpl1528372938339.png", record_pos=(0.381, -0.38), resolution=(1080, 1920)))
        wait(Template(r"tpl1528372952875.png", record_pos=(0.006, -0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1528372975879.png", record_pos=(-0.203, 0.161), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1531906195373.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.045, -0.58), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528373956250.png", record_pos=(-0.347, -0.463), resolution=(1080, 1920)), "sdk43992600钻石==98元显示正确，98元")
        touch(Template(r"tpl1528373763655.png", record_pos=(0.377, -0.588), resolution=(1080, 1920)))
        wait(Template(r"tpl1528373777596.png", record_pos=(0.004, 0.071), resolution=(1080, 1920)))
        touch(Template(r"tpl1528373784488.png", record_pos=(0.004, 0.071), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528374785603.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.009, -0.014), resolution=(1080, 1920))):
        touch(Template(r"tpl1528374798751.png", record_pos=(-0.197, 0.201), resolution=(1080, 1920)))
        wait(Template(r"tpl1528375146601.png", record_pos=(-0.006, -0.031), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1528375158781.png", record_pos=(-0.119, 0.29), resolution=(1080, 1920)),"meizu2600钻石==98元显示正确，98元")
        touch(Template(r"tpl1528374837583.png", record_pos=(0.44, -0.437), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528375217669.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, 0.036), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528375235461.png", record_pos=(-0.143, -0.444), resolution=(1080, 1920)), "anzhi2600钻石==98元显示正确，98元")
        touch(Template(r"tpl1528374920598.png", record_pos=(-0.419, -0.71), resolution=(1080, 1920)))
        wait(Template(r"tpl1528374929621.png", record_pos=(0.006, 0.048), resolution=(1080, 1920)))
        touch(Template(r"tpl1528374952105.png", record_pos=(0.192, 0.169), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528376014019.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.01, -0.016), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528376029490.png", record_pos=(0.306, -0.11), resolution=(1080, 1920)), "gionee2600钻石==98元显示正确，98元")
        touch(Template(r"tpl1528375887939.png", record_pos=(0.315, -0.244), resolution=(1080, 1920)))
        wait(Template(r"tpl1528375899889.png", record_pos=(0.0, -0.006), resolution=(1080, 1920)))
        touch(Template(r"tpl1528375909518.png", record_pos=(-0.191, 0.073), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528878028906.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.023, -0.01), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528878044453.png", record_pos=(-0.001, -0.052), resolution=(1080, 1920)),"yunos2600钻石==98元，98元")
        touch(Template(r"tpl1528877990401.png", record_pos=(0.35, -0.293), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1529053125067.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.006, -0.109), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1529053133949.png", record_pos=(-0.006, -0.5), resolution=(1080, 1920)),"联想 2600钻石==98元，98元")
        touch(Template(r"tpl1529053176564.png", record_pos=(-0.426, -0.746), resolution=(1080, 1920)))
        touch(Template(r"tpl1529053185280.png", record_pos=(0.207, 0.189), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "98.00元", "vivo2600钻石==98元显示正确，98元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥98.00", "huawei2600钻石==98元显示正确，98元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "98.00元", "xiaomi2600钻石==98元显示正确，98元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "98.00", "sumsung2600钻石==98元显示正确，98元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
    sleep(5)

def fourtyDiamond_founction():
    if exists(Template(r"tpl1528368755377.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.014, 0.001), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528368772742.png", record_pos=(0.031, -0.031), resolution=(1080, 1920)), "yunos1000钻石==40元显示正确，40元")
        touch(Template(r"tpl1528368804234.png", record_pos=(0.358, -0.272), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528369690626.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, -0.222), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528369705292.png", record_pos=(0.313, -0.36), resolution=(1080, 1920)), "baidu1000钻石==40元显示正确，40元")
        touch(Template(r"tpl1528369462076.png", record_pos=(-0.399, -0.56), resolution=(1080, 1920)))
        wait(Template(r"tpl1528369473241.png", record_pos=(0.004, -0.001), resolution=(1080, 1920)))
        touch(Template(r"tpl1528369479053.png", record_pos=(0.204, 0.128), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528372806940.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.054), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528372824920.png", record_pos=(0.297, -0.212), resolution=(1080, 1920)), "oppo1000钻石==40元显示正确，40元")
        touch(Template(r"tpl1528372581626.png", record_pos=(0.37, -0.375), resolution=(1080, 1920)))
        wait(Template(r"tpl1528372591728.png", record_pos=(0.007, 0.034), resolution=(1080, 1920)))
        touch(Template(r"tpl1528372600454.png", record_pos=(0.202, 0.099), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528373118592.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.009, -0.064), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528373134092.png", record_pos=(-0.211, -0.235), resolution=(1080, 1920)), "sdk3601000钻石==40元显示正确，40元")
        touch(Template(r"tpl1528372938339.png", record_pos=(0.381, -0.38), resolution=(1080, 1920)))
        wait(Template(r"tpl1528372952875.png", record_pos=(0.006, -0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1528372975879.png", record_pos=(-0.203, 0.161), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1531906195373.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.045, -0.58), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528374151454.png", record_pos=(-0.343, -0.469), resolution=(1080, 1920)), "sdk43991000钻石==40元显示正确，40元")
        touch(Template(r"tpl1528373763655.png", record_pos=(0.377, -0.588), resolution=(1080, 1920)))
        wait(Template(r"tpl1528373777596.png", record_pos=(0.004, 0.071), resolution=(1080, 1920)))
        touch(Template(r"tpl1528373784488.png", record_pos=(0.004, 0.071), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528374785603.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.009, -0.014), resolution=(1080, 1920))):
        touch(Template(r"tpl1528374798751.png", record_pos=(-0.197, 0.201), resolution=(1080, 1920)))
        wait(Template(r"tpl1528375346510.png", record_pos=(-0.001, -0.025), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1528375356085.png", record_pos=(-0.115, 0.286), resolution=(1080, 1920)),"meizu1000钻石==40元显示正确，40元")
        touch(Template(r"tpl1528374837583.png", record_pos=(0.44, -0.437), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528375278746.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.046), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528375292494.png", record_pos=(-0.158, -0.444), resolution=(1080, 1920)), "anzhi1000钻石==40元显示正确，40元")
        touch(Template(r"tpl1528374920598.png", record_pos=(-0.419, -0.71), resolution=(1080, 1920)))
        wait(Template(r"tpl1528374929621.png", record_pos=(0.006, 0.048), resolution=(1080, 1920)))
        touch(Template(r"tpl1528374952105.png", record_pos=(0.192, 0.169), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528376084121.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.004), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528376101569.png", record_pos=(0.297, -0.11), resolution=(1080, 1920)), "gionee1000钻石==40元显示正确，40元")
        touch(Template(r"tpl1528375887939.png", record_pos=(0.315, -0.244), resolution=(1080, 1920)))
        wait(Template(r"tpl1528375899889.png", record_pos=(0.0, -0.006), resolution=(1080, 1920)))
        touch(Template(r"tpl1528375909518.png", record_pos=(-0.191, 0.073), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528878148269.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.018, 0.001), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528878207103.png", record_pos=(0.019, -0.027), resolution=(1080, 1920)),"yunos1000钻石==40元，40元")
        touch(Template(r"tpl1528877990401.png", record_pos=(0.35, -0.293), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1529053219374.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.006, -0.122), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1529053229398.png", record_pos=(-0.004, -0.496), resolution=(1080, 1920)),"联想1000钻石==40元，40元")
        touch(Template(r"tpl1529053267310.png", record_pos=(-0.431, -0.746), resolution=(1080, 1920)))
        touch(Template(r"tpl1529053274301.png", record_pos=(0.2, 0.193), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "40.00元", "vivo1000钻石==40元显示正确，40元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥40.00", "huawei1000钻石==40元显示正确，40元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "40.00元", "xiaomi1000钻石==40元显示正确，40元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "40.00", "sumsung1000钻石==40元显示正确，40元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))

    sleep(3)


class  HankTestingPilots():
    
    def HankGifts(self,channel):
        wait(Template(r"tpl1527572353547.png", record_pos=(-0.372, -0.234), resolution=(1080, 1920)))
        touch(Template(r"tpl1527572388177.png", record_pos=(-0.369, -0.229), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1527572530097.png", record_pos=(-0.001, 0.548), resolution=(1080, 1920)))
        sleep(6)

        if channel == "Mobile":
            HankGifts_Mobile()
            
        elif channel == "Telecom":
            HankGifts_Telecom()
            
        elif channel == "Unicom":
            HankGifts_Unicom()
        
    def OneHundredNintyEightDiamond(self,channel):
        wait(Template(r"tpl1528368026054.png", record_pos=(-0.228, -0.692), resolution=(1080, 1920)))
        touch(Template(r"tpl1528368026054.png", record_pos=(-0.228, -0.692), resolution=(1080, 1920)))
        wait(Template(r"tpl1528368443983.png", record_pos=(0.008, -0.819), resolution=(1080, 1920)))
        wait(Template(r"tpl1528368471583.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.328, -0.204), resolution=(1080, 1920)))
        touch(Template(r"tpl1528368486695.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.309, -0.212), resolution=(1080, 1920)))
        sleep(5)
        
        OneHundredNintyEightDiamond_founction()
        
    def NintyEightDimond(self,channel):
        wait(Template(r"tpl1528368621327.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.006, -0.212), resolution=(1080, 1920)))
        touch(Template(r"tpl1528368633143.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.213), resolution=(1080, 1920)))
        sleep(5)
        
        NintyEightDimond_founction()

    def fourtyDiamond(self,channel):
        wait(Template(r"tpl1528368726620.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.324, -0.208), resolution=(1080, 1920)))
        touch(Template(r"tpl1528368737187.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.322, -0.206), resolution=(1080, 1920)))
        sleep(5)
        
        fourtyDiamond_founction()
        
    def EighteenDiamond(self,channel):
        touch(Template(r"tpl1527575765384.png", record_pos=(-0.326, 0.313), resolution=(1080, 1920)))
        sleep(5)
        
        if channel == "Mobile":
            EighteenDiamond_Mobile()
            
        elif channel == "Telecom":
            EighteenDiamond_Telecom()
            
        elif channel == "Unicom":
            EighteenDiamond_Unicom()
            
    def EightDiamond(self,channel):
        touch(Template(r"tpl1527575436859.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.001, 0.313), resolution=(1080, 1920)))
        sleep(5)
        if channel == "Mobile":
            EightDiamond_Mobile()
            
        elif channel == "Telecom":
            EightDiamond_Telecom()
            
        elif channel == "Unicom":
            EightDiamond_Unicom()
            
    def ThreeDiamond(self,channel):
        touch(Template(r"tpl1527574373331.png", threshold=0.8, target_pos=5, rgb=False, record_pos=(0.313, 0.315), resolution=(1080, 1920)))
        sleep(3)
        if channel == "Mobile":
            ThreeDiamondP_Mobile()
            
        elif channel == "Telecom":
            ThreeDiamond_Telecom()
            
        elif channel == "Unicom":
            ThreeDiamond_Unicom()
    





















