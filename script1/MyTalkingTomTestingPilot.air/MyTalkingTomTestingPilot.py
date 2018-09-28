# -*- encoding=utf8 -*-
__author__ = "zx"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)


"""
tomcat update 2018.07.17

"""


def TomGifts_Mobile_Audit():
    if exists(Template(r"tpl1528441093780.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.043), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441112274.png", record_pos=(0.339, -0.204), resolution=(1080, 1920)), "新手礼包10元")
        touch(Template(r"tpl1528441138102.png", record_pos=(-0.409, -0.215), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441149485.png", record_pos=(-0.005, 0.066), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441157011.png", record_pos=(-0.003, 0.075), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1528441192109.png", record_pos=(0.427, -0.828), resolution=(1080, 1920)))

    elif exists(Template(r"tpl1528697050399.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.031, -0.336), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441112274.png", record_pos=(0.339, -0.204), resolution=(1080, 1920)), "新手礼包10元")
        touch(Template(r"tpl1528441138102.png", record_pos=(-0.409, -0.215), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441149485.png", record_pos=(-0.005, 0.066), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441157011.png", record_pos=(-0.003, 0.075), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1528441192109.png", record_pos=(0.427, -0.828), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535512113943.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.021, -0.319), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441112274.png", record_pos=(0.339, -0.204), resolution=(1080, 1920)), "新手礼包10元")
        touch(Template(r"tpl1528441138102.png", record_pos=(-0.409, -0.215), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441149485.png", record_pos=(-0.005, 0.066), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441157011.png", record_pos=(-0.003, 0.075), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1528441192109.png", record_pos=(0.427, -0.828), resolution=(1080, 1920)))
    sleep(5)

def TomGifts_Mobile():
    if exists(Template(r"tpl1528448987777.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.039, 0.259), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528421848594.png", record_pos=(0.345, -0.238), resolution=(1080, 1920)), "新手礼包0.02元")
        touch(Template(r"tpl1528421889546.png", record_pos=(-0.409, -0.246), resolution=(1080, 1920)))
        wait(Template(r"tpl1528421898131.png", record_pos=(-0.006, 0.073), resolution=(1080, 1920)))
        touch(Template(r"tpl1528421905731.png", record_pos=(-0.001, 0.069), resolution=(1080, 1920)))
    sleep(3)
    touch(Template(r"tpl1528421556186.png", record_pos=(0.431, -0.831), resolution=(1080, 1920)))
    sleep(5)

def TomGifts_Telecom():
    if exists(Template(r"tpl1527648406733.png", threshold=0.8, target_pos=5, rgb=False, record_pos=(-0.008, 0.014), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527648460339.png", record_pos=(0.173, -0.164), resolution=(1080, 1920)), "新手礼物金额显示正确，短信支付10元")  
        touch(Template(r"tpl1527648512484.png", record_pos=(0.394, -0.162), resolution=(1080, 1920)))
        wait(Template(r"tpl1527648598080.png", record_pos=(-0.01, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1527648607439.png", record_pos=(0.001, 0.081), resolution=(1080, 1920)))
        touch(Template(r"tpl1527649823818.png", record_pos=(0.425, -0.83), resolution=(1080, 1920)))
    sleep(5)

def TomGifts_Unicom():
    if exists(Template(r"tpl1527672250730.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.009, -0.559), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527672089646.png", record_pos=(-0.156, -0.443), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")
        touch(Template(r"tpl1527672230811.png", record_pos=(0.459, -0.769), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677081839.png", record_pos=(0.005, 0.053), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672120014.png", record_pos=(0.192, 0.176), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1527677980924.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.013, -0.407), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527678108915.png", record_pos=(0.303, -0.364), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")
        touch(Template(r"tpl1527678097487.png", record_pos=(-0.391, -0.55), resolution=(1080, 1920)))
        wait(Template(r"tpl1527678125141.png", record_pos=(-0.004, 0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1527678132062.png", record_pos=(0.193, 0.133), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1527682036934.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.155), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527682060914.png", record_pos=(0.261, -0.209), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")
        touch(Template(r"tpl1527682075321.png", record_pos=(-0.324, -0.361), resolution=(1080, 1920)))
        wait(Template(r"tpl1527682083601.png", record_pos=(-0.008, 0.077), resolution=(1080, 1920)))
        touch(Template(r"tpl1527682091797.png", record_pos=(0.215, 0.306), resolution=(1080, 1920)))
        wait(Template(r"tpl1527682105349.png", record_pos=(-0.006, 0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1527682112284.png", record_pos=(0.021, 0.077), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1527683061893.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, -0.004), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527683077719.png", record_pos=(0.286, -0.105), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")
        touch(Template(r"tpl1527683098781.png", record_pos=(0.311, -0.234), resolution=(1080, 1920)))
        wait(Template(r"tpl1527683109057.png", record_pos=(0.002, -0.006), resolution=(1080, 1920)))
        touch(Template(r"tpl1527683116049.png", record_pos=(-0.183, 0.075), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1527651508911.png", record_pos=(-0.002, 0.004), resolution=(1080, 1920))):
        touch(Template(r"tpl1527651524750.png", record_pos=(-0.187, 0.196), resolution=(1080, 1920)))
        sleep(3)
        if exists(Template(r"tpl1527683922057.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.017, -0.04), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527683943798.png", record_pos=(-0.134, 0.29), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")
            touch(Template(r"tpl1527683957856.png", record_pos=(0.449, -0.444), resolution=(1080, 1920)))
        if exists(Template(r"tpl1535449216130.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(-0.012, 0.005), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1535449260178.png", record_pos=(-0.005, 0.059), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")
            touch(Template(r"tpl1535449247838.png", record_pos=(-0.414, -0.113), resolution=(1080, 1920)))
            sleep(2)
            touch(Template(r"tpl1535449303464.png", record_pos=(0.306, 0.089), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1527684932953.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.01, -0.121), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527684953396.png", record_pos=(0.316, -0.219), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")
        touch(Template(r"tpl1527684965601.png", record_pos=(0.384, -0.372), resolution=(1080, 1920)))
        wait(Template(r"tpl1527684973519.png", record_pos=(0.002, 0.03), resolution=(1080, 1920)))
        touch(Template(r"tpl1527684977966.png", record_pos=(0.199, 0.103), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1527728664463.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.159), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527728691226.png", record_pos=(-0.237, -0.239), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")
        touch(Template(r"tpl1527728705695.png", record_pos=(0.391, -0.38), resolution=(1080, 1920)))
        wait(Template(r"tpl1527728724579.png", record_pos=(0.0, 0.035), resolution=(1080, 1920)))
        touch(Template(r"tpl1527728735506.png", record_pos=(-0.198, 0.161), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535449402565.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(-0.001, -0.519), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527729726673.png", record_pos=(-0.367, -0.469), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")
        touch(Template(r"tpl1527729740628.png", record_pos=(0.38, -0.583), resolution=(1080, 1920)))
        wait(Template(r"tpl1527729752606.png", record_pos=(-0.006, 0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1527729759991.png", record_pos=(0.009, 0.077), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1527730669789.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.019, 0.095), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527730693209.png", record_pos=(0.026, -0.033), resolution=(1080, 1920)), "yunos新手礼物金额显示正确，10元")
        touch(Template(r"tpl1527730703852.png", record_pos=(0.357, -0.29), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1531709963153.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.035, -0.746), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1531709992694.png", record_pos=(-0.001, -0.526), resolution=(1080, 1920)),"lenovo新手礼物金额显示正确，10元")
        touch(Template(r"tpl1531710032069.png", record_pos=(-0.435, -0.748), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1531710045549.png", record_pos=(0.199, 0.19), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1533004694101.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.002, -0.013), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1533004709840.png", record_pos=(0.011, 0.0), resolution=(1080, 1920)), "yunos新手礼物金额显示正确，10元.")
        touch(Template(r"tpl1533004738343.png", record_pos=(0.348, -0.271), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "10.00元", "vivo新手礼物金额显示正确，10元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥10.00", "huawei新手礼物金额显示正确，10元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "10.00元", "xiaomi新手礼物金额显示正确，10元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "10.00", "sumsung新手礼物金额显示正确，10元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
    sleep(5) 

    touch(Template(r"tpl1527644237801.png", record_pos=(0.423, -0.824), resolution=(1080, 1920)))
    sleep(5)

    
def TomDoubleCoin_Mobile_Audit():
    if exists(Template(r"tpl1528441305384.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.009, -0.041), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441112274.png", record_pos=(0.339, -0.204), resolution=(1080, 1920)), "双倍赚币10元")
        touch(Template(r"tpl1528441138102.png", record_pos=(-0.409, -0.215), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441149485.png", record_pos=(-0.005, 0.066), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441157011.png", record_pos=(-0.003, 0.075), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528697262559.png", record_pos=(0.025, -0.334), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441112274.png", record_pos=(0.339, -0.204), resolution=(1080, 1920)), "双倍赚币10元")
        touch(Template(r"tpl1528441138102.png", record_pos=(-0.409, -0.215), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441149485.png", record_pos=(-0.005, 0.066), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441157011.png", record_pos=(-0.003, 0.075), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535512113943.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.021, -0.319), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441112274.png", record_pos=(0.339, -0.204), resolution=(1080, 1920)), "双倍赚币10元")
        touch(Template(r"tpl1528441138102.png", record_pos=(-0.409, -0.215), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441149485.png", record_pos=(-0.005, 0.066), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441157011.png", record_pos=(-0.003, 0.075), resolution=(1080, 1920)))
    sleep(5)

def TomDoubleCoin_Mobile(string):
    if exists(Template(r"tpl1528448987777.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.039, 0.259), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528421953488.png", record_pos=(0.367, -0.244), resolution=(1080, 1920)), "baidu双倍赚币1.0元")
        wait(Template(r"tpl1528424901154.png", record_pos=(-0.404, -0.392), resolution=(1080, 1920)))
        touch(Template(r"tpl1528424901154.png", record_pos=(-0.404, -0.392), resolution=(1080, 1920)))
        wait(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
    sleep(3)

def TomDoubleCoin_Telecom(string):
    if exists(Template(r"tpl1527648406733.png", threshold=0.8, target_pos=5, rgb=False, record_pos=(-0.008, 0.014), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527648460339.png", record_pos=(0.173, -0.164), resolution=(1080, 1920)), "双倍赚币金额显示正确，短信支付10元")  
        touch(Template(r"tpl1527648512484.png", record_pos=(0.394, -0.162), resolution=(1080, 1920)))
        wait(Template(r"tpl1527648598080.png", record_pos=(-0.01, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1527648607439.png", record_pos=(0.001, 0.081), resolution=(1080, 1920)))
        sleep(5)

def TomDoubleCoin_Unicom(string):
    if  exists(Template(r"tpl1527662109372.png", threshold=0.7999999999999999, target_pos=5, rgb=False, record_pos=(-0.347, -0.287), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527662125530.png", record_pos=(0.306, -0.075), resolution=(1080, 1920)), "双倍赚币金额显示正确，短信支付10元")
        touch(Template(r"tpl1527662109372.png", record_pos=(-0.347, -0.287), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1527667369882.png", record_pos=(-0.211, 0.122), resolution=(1080, 1920)))
        wait(Template(r"tpl1527667384221.png", record_pos=(-0.015, 0.068), resolution=(1080, 1920)))
        touch(Template(r"tpl1527667405874.png", record_pos=(-0.005, 0.076), resolution=(1080, 1920)))
    sleep(5)


def FiveDiamond_Mobile_Audit_Pay():
    # wait(Template(r"tpl1531460723778.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.009, -0.431), resolution=(1080, 1920)))
    # touch(Template(r"tpl1531460736169.png", record_pos=(0.001, -0.422), resolution=(1080, 1920)))
    # if exists(Template(r"tpl1528441707143.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.009, -0.039), resolution=(1080, 1920))):
    #     touch(Template(r"tpl1528437897126.png", threshold=0.7, target_pos=5, rgb=False, record_pos=(0.006, 0.119), resolution=(1080, 1920)))
    #     sleep(5)
    #     wait(Template(r"tpl1528438092368.png", record_pos=(-0.009, -0.012), resolution=(1080, 1920)))
    #     assert_exists(Template(r"tpl1528438115202.png", record_pos=(0.009, -0.018), resolution=(1080, 1920)), "道具下发成功")
    #     keyevent("back")
    #     sleep(3)
    #     touch(Template(r"tpl1527587481767.png", record_pos=(0.416, -0.811), resolution=(1080, 1920)))
    if exists(Template(r"tpl1528441707143.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.009, -0.039), resolution=(1080, 1920))):
        touch(Template(r"tpl1528437897126.png", threshold=0.7, target_pos=5, rgb=False, record_pos=(0.006, 0.119), resolution=(1080, 1920)))
        sleep(5)
        wait(Template(r"tpl1535510465688.png", record_pos=(0.0, -0.015), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1535510465688.png", record_pos=(0.0, -0.015), resolution=(1080, 1920)), "道具下发成功")
        keyevent("back")
        # sleep(3)
        # touch(Template(r"tpl1527587481767.png", record_pos=(0.416, -0.811), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535512113943.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.021, -0.319), resolution=(1080, 1920))):
        touch(Template(r"tpl1535512621804.png", record_pos=(0.024, 0.232), resolution=(1080, 1920)))
        sleep(5)
        wait(Template(r"tpl1535510465688.png", record_pos=(0.0, -0.015), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1535510465688.png", record_pos=(0.0, -0.015), resolution=(1080, 1920)), "道具下发成功")
        keyevent("back")
    sleep(5)

def FiveDiamond_Mobile_Audit():
    if exists(Template(r"tpl1528441707143.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.009, -0.039), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441721591.png", record_pos=(0.356, -0.197), resolution=(1080, 1920)), "5钻石1元")
        touch(Template(r"tpl1528441138102.png", record_pos=(-0.409, -0.215), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441149485.png", record_pos=(-0.005, 0.066), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441157011.png", record_pos=(-0.003, 0.075), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1527487411283.png", record_pos=(0.001, -0.008), resolution=(1080, 1920))):
        touch(Template(r"tpl1527487420629.png", record_pos=(-0.203, 0.194), resolution=(1080, 1920)))
        sleep(3)
        assert_exists(Template(r"tpl1527489258311.png", record_pos=(-0.176, 0.285), resolution=(1080, 1920)), "5钻石==1.0元金额显示正确，1元")
        touch(Template(r"tpl1527488245543.png", record_pos=(0.44, -0.445), resolution=(1080, 1920)))
    sleep(5)

def FiveDiamond_Mobile():
    if exists(Template(r"tpl1528448987777.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.039, 0.259), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528422231393.png", record_pos=(0.366, -0.24), resolution=(1080, 1920)), "5元钻石1.0元")
        touch(Template(r"tpl1528422111148.png", record_pos=(-0.404, -0.398), resolution=(1080, 1920)))
        wait(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
    sleep(3)

def FiveDiamond_Telecom():
    if exists(Template(r"tpl1527663802293.png", record_pos=(0.037, 0.003), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527663802293.png", record_pos=(0.037, 0.003), resolution=(1080, 1920)), "5钻石==4元金额显示正确，支付4元")
        touch(Template(r"tpl1527663841241.png", record_pos=(0.354, -0.277), resolution=(1080, 1920)))
    
    elif exists(Template(r"tpl1527649132299.png", record_pos=(0.188, -0.16), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527649132299.png", record_pos=(0.188, -0.16), resolution=(1080, 1920)), "5钻石==1元金额显示正确，短信支付1元")
        touch(Template(r"tpl1527648512484.png", record_pos=(0.394, -0.162), resolution=(1080, 1920)))
        wait(Template(r"tpl1527648598080.png", record_pos=(-0.01, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1527648607439.png", record_pos=(0.001, 0.081), resolution=(1080, 1920)))

    
    sleep(5)

def FiveDiamond_Unicom():
    if exists(Template(r"tpl1527663802293.png", threshold=0.8999999999999999, target_pos=5, rgb=False, record_pos=(0.037, 0.003), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527663802293.png", record_pos=(0.037, 0.003), resolution=(1080, 1920)), "5钻石==4元金额显示正确，渠道支付4元")
        touch(Template(r"tpl1527663841241.png", record_pos=(0.354, -0.277), resolution=(1080, 1920)))
    elif  exists(Template(r"tpl1527662109372.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.347, -0.287), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527669121302.png", record_pos=(0.337, -0.073), resolution=(1080, 1920)), "5钻石==1元金额显示正确，短信支付1元")
        touch(Template(r"tpl1527662109372.png", record_pos=(-0.347, -0.287), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1527667369882.png", record_pos=(-0.211, 0.122), resolution=(1080, 1920)))
        wait(Template(r"tpl1527667384221.png", record_pos=(-0.015, 0.068), resolution=(1080, 1920)))
        touch(Template(r"tpl1527667405874.png", record_pos=(-0.005, 0.076), resolution=(1080, 1920)))
    sleep(5)

    
def SeventyDiamond_Mobile_Audit():
    if exists(Template(r"tpl1528441379070.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.008, -0.029), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441398013.png", record_pos=(0.331, -0.204), resolution=(1080, 1920)), "70钻石12元")
        touch(Template(r"tpl1528441138102.png", record_pos=(-0.409, -0.215), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441149485.png", record_pos=(-0.005, 0.066), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441157011.png", record_pos=(-0.003, 0.075), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535512113943.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.021, -0.319), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441398013.png", record_pos=(0.331, -0.204), resolution=(1080, 1920)), "70钻石12元")
        touch(Template(r"tpl1528441138102.png", record_pos=(-0.409, -0.215), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441149485.png", record_pos=(-0.005, 0.066), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441157011.png", record_pos=(-0.003, 0.075), resolution=(1080, 1920)))

    sleep(5)

def SeventyDiamond_Mobile():
    if exists(Template(r"tpl1528448987777.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.039, 0.259), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528422379903.png", record_pos=(0.365, -0.235), resolution=(1080, 1920)), "12元钻石0.2元")
        touch(Template(r"tpl1528422111148.png", record_pos=(-0.404, -0.398), resolution=(1080, 1920)))
        wait(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
    sleep(3)
    
def SeventyDiamond_Telecom():
    if exists(Template(r"tpl1527648406733.png", threshold=0.7999999999999999, target_pos=5, rgb=False, record_pos=(-0.008, 0.014), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527648887135.png", record_pos=(0.173, -0.16), resolution=(1080, 1920)), "79钻石==12元金额显示正确，短信支付12元")  
        touch(Template(r"tpl1527648512484.png", record_pos=(0.394, -0.162), resolution=(1080, 1920)))
        wait(Template(r"tpl1527648598080.png", record_pos=(-0.01, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1527648607439.png", record_pos=(0.001, 0.081), resolution=(1080, 1920)))
        sleep(5)

def SeventyDiamond_Unicom():
    if  exists(Template(r"tpl1527662109372.png", threshold=0.7999999999999999, target_pos=5, rgb=False, record_pos=(-0.347, -0.287), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527667794896.png", record_pos=(0.325, -0.069), resolution=(1080, 1920)), "79钻石==12元金额显示正确，短信支付12元")
        touch(Template(r"tpl1527662109372.png", record_pos=(-0.347, -0.287), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1527667369882.png", record_pos=(-0.211, 0.122), resolution=(1080, 1920)))
        wait(Template(r"tpl1527667384221.png", record_pos=(-0.015, 0.068), resolution=(1080, 1920)))
        touch(Template(r"tpl1527667405874.png", record_pos=(-0.005, 0.076), resolution=(1080, 1920)))
        sleep(5)

        
def HundredNinetyDiamond_Mobile_Audit():
    if exists(Template(r"tpl1528441618474.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.0, -0.035), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441641164.png", record_pos=(0.344, -0.198), resolution=(1080, 1920)), "190钻石28元")
        touch(Template(r"tpl1528441138102.png", record_pos=(-0.409, -0.215), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441149485.png", record_pos=(-0.005, 0.066), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441157011.png", record_pos=(-0.003, 0.075), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535512113943.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.021, -0.319), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441641164.png", record_pos=(0.344, -0.198), resolution=(1080, 1920)), "190钻石28元")
        touch(Template(r"tpl1528441138102.png", record_pos=(-0.409, -0.215), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441149485.png", record_pos=(-0.005, 0.066), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441157011.png", record_pos=(-0.003, 0.075), resolution=(1080, 1920)))
    sleep(5)

def HundredNinetyDiamond_Mobile():
    
    if exists(Template(r"tpl1528448987777.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.039, 0.259), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528422493102.png", record_pos=(0.372, -0.241), resolution=(1080, 1920)), "28元钻石0.3元")
        touch(Template(r"tpl1528422111148.png", record_pos=(-0.404, -0.398), resolution=(1080, 1920)))
        wait(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
    sleep(3)

def HundredNinetyDiamond_Telecom():
    if exists(Template(r"tpl1527648406733.png", threshold=0.7999999999999999, target_pos=5, rgb=False, record_pos=(-0.008, 0.014), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527649861738.png", record_pos=(0.181, -0.162), resolution=(1080, 1920)), "190钻石==28元金额显示正确，短信支付28元")  
        touch(Template(r"tpl1527648512484.png", record_pos=(0.394, -0.162), resolution=(1080, 1920)))
        wait(Template(r"tpl1527648598080.png", record_pos=(-0.01, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1527648607439.png", record_pos=(0.001, 0.081), resolution=(1080, 1920)))
        sleep(5)

def HundredNinetyDiamond_Unicom():
    if  exists(Template(r"tpl1527662109372.png", threshold=0.7999999999999999, target_pos=5, rgb=False, record_pos=(-0.347, -0.287), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527667868524.png", record_pos=(0.324, -0.074), resolution=(1080, 1920)), "190钻石==28元金额显示正确，短信支付28元")
        touch(Template(r"tpl1527662109372.png", record_pos=(-0.347, -0.287), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1527667369882.png", record_pos=(-0.211, 0.122), resolution=(1080, 1920)))
        wait(Template(r"tpl1527667384221.png", record_pos=(-0.015, 0.068), resolution=(1080, 1920)))
        touch(Template(r"tpl1527667405874.png", record_pos=(-0.005, 0.076), resolution=(1080, 1920)))
    sleep(5)

    
def BabyEyedrops_Mobile_Audit():
    if exists(Template(r"tpl1528442180374.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.007, -0.033), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528442198285.png", record_pos=(0.335, -0.196), resolution=(1080, 1920)), "婴儿眼药水10元")
        touch(Template(r"tpl1528442124755.png", record_pos=(-0.407, -0.214), resolution=(1080, 1920)))
        wait(Template(r"tpl1528442132633.png", record_pos=(-0.009, 0.071), resolution=(1080, 1920)))
        touch(Template(r"tpl1528442139424.png", record_pos=(-0.008, 0.074), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535512113943.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.021, -0.319), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1535514666534.png", record_pos=(0.071, -0.199), resolution=(1080, 1920)), "婴儿眼药水10元")
        touch(Template(r"tpl1528442124755.png", record_pos=(-0.407, -0.214), resolution=(1080, 1920)))
        wait(Template(r"tpl1528442132633.png", record_pos=(-0.009, 0.071), resolution=(1080, 1920)))
        touch(Template(r"tpl1528442139424.png", record_pos=(-0.008, 0.074), resolution=(1080, 1920)))
    sleep(3)
    touch(Template(r"tpl1528423260202.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, -0.811), resolution=(1080, 1920)))
    sleep(2)
    wait(Template(r"tpl1528423282021.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.42, -0.817), resolution=(1080, 1920)))
    touch(Template(r"tpl1528423297038.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.412, -0.819), resolution=(1080, 1920)))
    sleep(3)

def BabyEyedrops_Mobile():
    if exists(Template(r"tpl1528448987777.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.039, 0.259), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528423219902.png", record_pos=(0.352, -0.235), resolution=(1080, 1920)), "婴儿眼药水0.07元")
        touch(Template(r"tpl1528422111148.png", record_pos=(-0.404, -0.398), resolution=(1080, 1920)))
        wait(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
    sleep(3)
    touch(Template(r"tpl1528423260202.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, -0.811), resolution=(1080, 1920)))
    sleep(2)
    wait(Template(r"tpl1528423282021.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.42, -0.817), resolution=(1080, 1920)))
    touch(Template(r"tpl1528423297038.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.412, -0.819), resolution=(1080, 1920)))
    sleep(3)

def BabyEyedrops_Telecom():
    if exists(Template(r"tpl1527648406733.png", threshold=0.7999999999999999, target_pos=5, rgb=False, record_pos=(-0.008, 0.014), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527648460339.png", record_pos=(0.173, -0.164), resolution=(1080, 1920)), "婴儿眼药水金额显示正确，短信支付10元")  
        touch(Template(r"tpl1527648512484.png", record_pos=(0.394, -0.162), resolution=(1080, 1920)))
        wait(Template(r"tpl1527648598080.png", record_pos=(-0.01, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1527648607439.png", record_pos=(0.001, 0.081), resolution=(1080, 1920)))
    sleep(3)
    touch(Template(r"tpl1528423260202.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, -0.811), resolution=(1080, 1920)))
    sleep(2)
    wait(Template(r"tpl1528423282021.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.42, -0.817), resolution=(1080, 1920)))
    touch(Template(r"tpl1528423297038.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.412, -0.819), resolution=(1080, 1920)))
    sleep(5)

def BabyEyedrops_Unicom():
    # if exists(Template(r"tpl1527662109372.png", threshold=0.7, target_pos=5, rgb=False, record_pos=(-0.347, -0.287), resolution=(1080, 1920))):
    assert_exists(Template(r"tpl1527662125530.png", record_pos=(0.306, -0.075), resolution=(1080, 1920)), "婴儿眼药水金额显示正确，短信支付10元")
    touch(Template(r"tpl1527662109372.png", record_pos=(-0.347, -0.287), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1527667369882.png", record_pos=(-0.211, 0.122), resolution=(1080, 1920)))
    wait(Template(r"tpl1527667384221.png", record_pos=(-0.015, 0.068), resolution=(1080, 1920)))
    touch(Template(r"tpl1527667405874.png", record_pos=(-0.005, 0.076), resolution=(1080, 1920)))
    #baidu-one.apk
    if exists(Template(r"tpl1527580977213.png", record_pos=(0.419, -0.815), resolution=(1080, 1920))):
        touch(Template(r"tpl1527580977213.png", record_pos=(0.419, -0.815), resolution=(1080, 1920)))
        sleep(2)
        touch(Template(r"tpl1527580990945.png", record_pos=(0.421, -0.815), resolution=(1080, 1920)))
    sleep(5)

    
def AdultEyedrops_Mobile_Audit():
    
    if exists(Template(r"tpl1528442090397.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.002, -0.024), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528442105074.png", record_pos=(0.342, -0.208), resolution=(1080, 1920)), "成人眼药水10元")
        touch(Template(r"tpl1528442124755.png", record_pos=(-0.407, -0.214), resolution=(1080, 1920)))
        wait(Template(r"tpl1528442132633.png", record_pos=(-0.009, 0.071), resolution=(1080, 1920)))
        touch(Template(r"tpl1528442139424.png", record_pos=(-0.008, 0.074), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535512113943.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.021, -0.319), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528442105074.png", record_pos=(0.342, -0.208), resolution=(1080, 1920)), "成人眼药水10元")
        touch(Template(r"tpl1528442124755.png", record_pos=(-0.407, -0.214), resolution=(1080, 1920)))
        wait(Template(r"tpl1528442132633.png", record_pos=(-0.009, 0.071), resolution=(1080, 1920)))
        touch(Template(r"tpl1528442139424.png", record_pos=(-0.008, 0.074), resolution=(1080, 1920)))
    sleep(5)

def AdultEyedrops_Mobile():
    if exists(Template(r"tpl1528448987777.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.039, 0.259), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528423118593.png", record_pos=(0.358, -0.235), resolution=(1080, 1920)), "成人眼药水0.01元")
        touch(Template(r"tpl1528422111148.png", record_pos=(-0.404, -0.398), resolution=(1080, 1920)))
        wait(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
    sleep(3)

def AdultEyedrops_Telecom():
    if exists(Template(r"tpl1527648406733.png", threshold=0.7999999999999999, target_pos=5, rgb=False, record_pos=(-0.008, 0.014), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527648460339.png", record_pos=(0.173, -0.164), resolution=(1080, 1920)), "成人眼药水金额显示正确，短信支付10元")  
        touch(Template(r"tpl1527648512484.png", record_pos=(0.394, -0.162), resolution=(1080, 1920)))
        wait(Template(r"tpl1527648598080.png", record_pos=(-0.01, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1527648607439.png", record_pos=(0.001, 0.081), resolution=(1080, 1920)))
    sleep(5)

def AdultEyedrops_Unicom():
    # if exists(Template(r"tpl1527662109372.png", threshold=0.7, target_pos=5, rgb=False, record_pos=(-0.347, -0.287), resolution=(1080, 1920))):
    assert_exists(Template(r"tpl1527662125530.png", record_pos=(0.306, -0.075), resolution=(1080, 1920)), "成人眼药水金额显示正确，短信支付10元")
    touch(Template(r"tpl1527662109372.png", record_pos=(-0.347, -0.287), resolution=(1080, 1920)))
    sleep(1)
    touch(Template(r"tpl1527667369882.png", record_pos=(-0.211, 0.122), resolution=(1080, 1920)))
    wait(Template(r"tpl1527667384221.png", record_pos=(-0.015, 0.068), resolution=(1080, 1920)))
    touch(Template(r"tpl1527667405874.png", record_pos=(-0.005, 0.076), resolution=(1080, 1920)))
    sleep(5)

    
def SailorUniforms_Mobile_Audit():
    if exists(Template(r"tpl1528441861869.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.0, -0.031), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441889148.png", record_pos=(0.335, -0.202), resolution=(1080, 1920)), "水手制服15元")
        touch(Template(r"tpl1528441915152.png", record_pos=(-0.399, -0.208), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441923809.png", record_pos=(-0.001, 0.08), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441929042.png", record_pos=(-0.003, 0.078), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535512113943.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.021, -0.319), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528441889148.png", record_pos=(0.335, -0.202), resolution=(1080, 1920)), "水手制服15元")
        touch(Template(r"tpl1528441915152.png", record_pos=(-0.399, -0.208), resolution=(1080, 1920)))
        wait(Template(r"tpl1528441923809.png", record_pos=(-0.001, 0.08), resolution=(1080, 1920)))
        touch(Template(r"tpl1528441929042.png", record_pos=(-0.003, 0.078), resolution=(1080, 1920)))
    sleep(3)
    wait(Template(r"tpl1528423630689.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.415, -0.673), resolution=(1080, 1920)))
    touch(Template(r"tpl1528423640617.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.417, -0.673), resolution=(1080, 1920)))
    sleep(5)

def SailorUniforms_Mobile():
    if exists(Template(r"tpl1528448987777.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.039, 0.259), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528423573310.png", record_pos=(0.363, -0.244), resolution=(1080, 1920)), "消防员制服5.0元")
        touch(Template(r"tpl1528422111148.png", record_pos=(-0.404, -0.398), resolution=(1080, 1920)))
        wait(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1528422120507.png", record_pos=(-0.005, 0.072), resolution=(1080, 1920)))
    sleep(3)
    wait(Template(r"tpl1528423630689.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.415, -0.673), resolution=(1080, 1920)))
    touch(Template(r"tpl1528423640617.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.417, -0.673), resolution=(1080, 1920)))
    sleep(5)

def SailorUniforms_Telecom():
    if exists(Template(r"tpl1527648406733.png", threshold=0.7999999999999999, target_pos=5, rgb=False, record_pos=(-0.008, 0.014), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527649352935.png", record_pos=(0.177, -0.158), resolution=(1080, 1920)), "消防员制服金额显示正确，短信支付15元")  
        touch(Template(r"tpl1527648512484.png", record_pos=(0.394, -0.162), resolution=(1080, 1920)))
        wait(Template(r"tpl1527648598080.png", record_pos=(-0.01, 0.072), resolution=(1080, 1920)))
        touch(Template(r"tpl1527648607439.png", record_pos=(0.001, 0.081), resolution=(1080, 1920)))

    sleep(2)
    touch(Template(r"tpl1527502146140.png", record_pos=(0.409, -0.676), resolution=(1080, 1920)))
    sleep(5)

def SailorUniforms_Unicom():
    if exists(Template(r"tpl1528422567746.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.019), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528422581512.png", record_pos=(0.31, -0.369), resolution=(1080, 1920)), "baidu水手制服15元")
        touch(Template(r"tpl1528421519368.png", record_pos=(-0.387, -0.553), resolution=(1080, 1920)))
        wait(Template(r"tpl1528421528955.png", record_pos=(0.01, -0.004), resolution=(1080, 1920)))
        touch(Template(r"tpl1528421535924.png", record_pos=(0.214, 0.13), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528424276910.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.007, -0.01), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528424290351.png", record_pos=(0.27, -0.175), resolution=(1080, 1920)), "oppo水手制服15元")
        touch(Template(r"tpl1528424313348.png", record_pos=(0.381, -0.337), resolution=(1080, 1920)))
        wait(Template(r"tpl1528424321400.png", record_pos=(0.019, 0.036), resolution=(1080, 1920)))
        touch(Template(r"tpl1528424327458.png", record_pos=(0.204, 0.096), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535461296521.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.001, -0.517), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1535461311769.png", record_pos=(-0.333, -0.47), resolution=(1080, 1920)), "sdk4399水手制服15元")
        touch(Template(r"tpl1528426530490.png", record_pos=(0.367, -0.588), resolution=(1080, 1920)))
        wait(Template(r"tpl1528426540396.png", record_pos=(-0.005, 0.075), resolution=(1080, 1920)))
        touch(Template(r"tpl1528426545152.png", record_pos=(0.006, 0.074), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535458447502.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.003, -0.044), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1535451529400.png", record_pos=(-0.238, -0.244), resolution=(1080, 1920)), "sdk360水手制服15元")
        touch(Template(r"tpl1528426725465.png", record_pos=(0.39, -0.38), resolution=(1080, 1920)))
        wait(Template(r"tpl1528426736843.png", record_pos=(-0.005, 0.003), resolution=(1080, 1920)))
        touch(Template(r"tpl1528426743595.png", record_pos=(-0.204, 0.166), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528428711970.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, -0.016), resolution=(1080, 1920))):
        touch(Template(r"tpl1528428724926.png", record_pos=(-0.207, 0.189), resolution=(1080, 1920)))
        wait(Template(r"tpl1535458378576.png", record_pos=(0.008, 0.0), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1535451709047.png", record_pos=(0.03, 0.047), resolution=(1080, 1920)), "meizu水手制服15元")
        touch(Template(r"tpl1528428937531.png", record_pos=(-0.419, -0.131), resolution=(1080, 1920)))
        wait(Template(r"tpl1528428945546.png", record_pos=(0.006, 0.031), resolution=(1080, 1920)))
        touch(Template(r"tpl1528428952171.png", record_pos=(0.302, 0.091), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535458568958.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.005, -0.013), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1535458588199.png", record_pos=(0.306, -0.113), resolution=(1080, 1920)), "gionee水手制服15元")
        touch(Template(r"tpl1528429486389.png", record_pos=(0.31, -0.242), resolution=(1080, 1920)))
        wait(Template(r"tpl1528429495480.png", record_pos=(0.008, -0.009), resolution=(1080, 1920)))
        touch(Template(r"tpl1528429503077.png", record_pos=(-0.182, 0.068), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535458708157.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(-0.004, 0.04), resolution=(720, 1280))):
        assert_exists(Template(r"tpl1535451490259.png", record_pos=(-0.165, -0.449), resolution=(720, 1280)), "anzhi水手制服15元")
        touch(Template(r"tpl1528429657769.png", record_pos=(-0.409, -0.705), resolution=(1080, 1920)))
        wait(Template(r"tpl1528429667710.png", record_pos=(0.007, 0.051), resolution=(1080, 1920)))
        touch(Template(r"tpl1528429675233.png", record_pos=(0.194, 0.167), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535460034545.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(-0.002, -0.572), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1532680229542.png", record_pos=(0.007, -0.53), resolution=(1080, 1920)), "lenovo水手制服15元")
        touch(Template(r"tpl1532678356809.png", record_pos=(-0.433, -0.751), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1532678374013.png", record_pos=(0.212, 0.188), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1531461687708.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.003, -0.014), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1531461705783.png", record_pos=(0.009, -0.036), resolution=(1080, 1920)),"yunos水手制服15元")
        touch(Template(r"tpl1531461754757.png", record_pos=(0.36, -0.293), resolution=(1080, 1920)))
    
    elif exists(Template(r"tpl1533004865918.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.002, -0.01), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1533004880976.png", record_pos=(0.013, 0.004), resolution=(1080, 1920)), "yunos水手制服15元.")
        touch(Template(r"tpl1533004900901.png", record_pos=(0.354, -0.269), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "15.00元", "vivo水手制服15元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥15.00", "huawei水手制服15元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "15.00元", "xiaomi水手制服15元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "15.00", "sumsung水手制服15元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
    sleep(5)
    touch(Template(r"tpl1527502146140.png", record_pos=(0.409, -0.676), resolution=(1080, 1920)))
    sleep(5)

def SixthousandTwoHundredFiftyDiamond_Founction():
    if exists(Template(r"tpl1528422672856.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.014), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528422687538.png", record_pos=(0.308, -0.371), resolution=(1080, 1920)), "baidu648元钻石648元")
        touch(Template(r"tpl1528421519368.png", record_pos=(-0.387, -0.553), resolution=(1080, 1920)))
        wait(Template(r"tpl1528421528955.png", record_pos=(0.01, -0.004), resolution=(1080, 1920)))
        touch(Template(r"tpl1528421535924.png", record_pos=(0.214, 0.13), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528424602361.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.007, -0.002), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528424616217.png", record_pos=(0.269, -0.181), resolution=(1080, 1920)), "oppo648元钻石648元")
        touch(Template(r"tpl1528424313348.png", record_pos=(0.381, -0.337), resolution=(1080, 1920)))
        wait(Template(r"tpl1528424321400.png", record_pos=(0.019, 0.036), resolution=(1080, 1920)))
        touch(Template(r"tpl1528424327458.png", record_pos=(0.204, 0.096), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535441367130.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(-0.001, -0.518), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528426586556.png", record_pos=(-0.318, -0.477), resolution=(1080, 1920)), "sdk4399648元钻石648元")
        touch(Template(r"tpl1528426610045.png", record_pos=(0.373, -0.588), resolution=(1080, 1920)))
        wait(Template(r"tpl1528426621315.png", record_pos=(0.004, 0.078), resolution=(1080, 1920)))
        touch(Template(r"tpl1528426626319.png", record_pos=(0.012, 0.076), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528426764575.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.054), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528426778711.png", record_pos=(-0.201, -0.242), resolution=(1080, 1920)), "sdk360648元钻石648元")
        touch(Template(r"tpl1528426725465.png", record_pos=(0.39, -0.38), resolution=(1080, 1920)))
        wait(Template(r"tpl1528426736843.png", record_pos=(-0.005, 0.003), resolution=(1080, 1920)))
        touch(Template(r"tpl1528426743595.png", record_pos=(-0.204, 0.166), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528428711970.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, -0.016), resolution=(1080, 1920))):
        touch(Template(r"tpl1528428724926.png", record_pos=(-0.207, 0.189), resolution=(1080, 1920)))
        wait(Template(r"tpl1528428993373.png", record_pos=(0.012, 0.339), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1528429008685.png", record_pos=(0.02, 0.042), resolution=(1080, 1920)), "meizu648元钻石648元")
        touch(Template(r"tpl1528428937531.png", record_pos=(-0.419, -0.131), resolution=(1080, 1920)))
        wait(Template(r"tpl1528428945546.png", record_pos=(0.006, 0.031), resolution=(1080, 1920)))
        touch(Template(r"tpl1528428952171.png", record_pos=(0.302, 0.091), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528429557572.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, 0.006), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528429569636.png", record_pos=(0.297, -0.114), resolution=(1080, 1920)), "gionee198元钻石648元")
        touch(Template(r"tpl1528429486389.png", record_pos=(0.31, -0.242), resolution=(1080, 1920)))
        wait(Template(r"tpl1528429495480.png", record_pos=(0.008, -0.009), resolution=(1080, 1920)))
        touch(Template(r"tpl1528429503077.png", record_pos=(-0.182, 0.068), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528429709642.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.043), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528429723450.png", record_pos=(-0.146, -0.444), resolution=(1080, 1920)), "anzhi198元钻石648元")
        touch(Template(r"tpl1528429657769.png", record_pos=(-0.409, -0.705), resolution=(1080, 1920)))
        wait(Template(r"tpl1528429667710.png", record_pos=(0.007, 0.051), resolution=(1080, 1920)))
        touch(Template(r"tpl1528429675233.png", record_pos=(0.194, 0.167), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1531461794766.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.009, -0.012), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1531461705783.png", record_pos=(0.009, -0.036), resolution=(1080, 1920)),"yunos648")
        touch(Template(r"tpl1531461754757.png", record_pos=(0.36, -0.293), resolution=(1080, 1920)))
        sleep(5)
    elif exists(Template(r"tpl1533004959366.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.009, -0.018), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1533004989192.png", record_pos=(0.025, 0.003), resolution=(1080, 1920)), "yunos648.")
        touch(Template(r"tpl1533004975869.png", record_pos=(0.351, -0.269), resolution=(1080, 1920)))

    elif exists(Template(r"tpl1532678293409.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.007, -0.749), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1532678444532.png", record_pos=(0.012, -0.532), resolution=(1080, 1920)), "lenovo648元钻石648元")
        touch(Template(r"tpl1532678356809.png", record_pos=(-0.433, -0.751), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1532678374013.png", record_pos=(0.212, 0.188), resolution=(1080, 1920)))

    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "648.00元", "vivo648元钻石648元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥648.00", "huawei648元钻石648元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "648.00元", "xiaomi648元钻石648元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "648.00", "sumsung648元钻石648元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
    sleep(5)

def ThousandFiveHundeedNinetyDiamond_Founction():
    if exists(Template(r"tpl1528422567746.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.019), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528422581512.png", record_pos=(0.31, -0.369), resolution=(1080, 1920)), "baidu198元钻石198元")
        touch(Template(r"tpl1528421519368.png", record_pos=(-0.387, -0.553), resolution=(1080, 1920)))
        wait(Template(r"tpl1528421528955.png", record_pos=(0.01, -0.004), resolution=(1080, 1920)))
        touch(Template(r"tpl1528421535924.png", record_pos=(0.214, 0.13), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528424276910.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.007, -0.01), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528424290351.png", record_pos=(0.27, -0.175), resolution=(1080, 1920)), "oppo198元钻石198元")
        touch(Template(r"tpl1528424313348.png", record_pos=(0.381, -0.337), resolution=(1080, 1920)))
        wait(Template(r"tpl1528424321400.png", record_pos=(0.019, 0.036), resolution=(1080, 1920)))
        touch(Template(r"tpl1528424327458.png", record_pos=(0.204, 0.096), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1535441432882.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.003, -0.517), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528426509331.png", record_pos=(-0.316, -0.472), resolution=(1080, 1920)), "sdk4399198元钻石198元")
        touch(Template(r"tpl1528426530490.png", record_pos=(0.367, -0.588), resolution=(1080, 1920)))
        wait(Template(r"tpl1528426540396.png", record_pos=(-0.005, 0.075), resolution=(1080, 1920)))
        touch(Template(r"tpl1528426545152.png", record_pos=(0.006, 0.074), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528426686405.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.052), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528426705506.png", record_pos=(-0.209, -0.241), resolution=(1080, 1920)), "sdk360198元钻石198元")
        touch(Template(r"tpl1528426725465.png", record_pos=(0.39, -0.38), resolution=(1080, 1920)))
        wait(Template(r"tpl1528426736843.png", record_pos=(-0.005, 0.003), resolution=(1080, 1920)))
        touch(Template(r"tpl1528426743595.png", record_pos=(-0.204, 0.166), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528428711970.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, -0.016), resolution=(1080, 1920))):
        touch(Template(r"tpl1528428724926.png", record_pos=(-0.207, 0.189), resolution=(1080, 1920)))
        wait(Template(r"tpl1528428890653.png", record_pos=(0.024, 0.345), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1528428903154.png", record_pos=(0.033, 0.055), resolution=(1080, 1920)), "meizu198元钻石198元")
        touch(Template(r"tpl1528428937531.png", record_pos=(-0.419, -0.131), resolution=(1080, 1920)))
        wait(Template(r"tpl1528428945546.png", record_pos=(0.006, 0.031), resolution=(1080, 1920)))
        touch(Template(r"tpl1528428952171.png", record_pos=(0.302, 0.091), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528429450735.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.01, -0.002), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528429462438.png", record_pos=(0.289, -0.112), resolution=(1080, 1920)), "gionee198元钻石198元")
        touch(Template(r"tpl1528429486389.png", record_pos=(0.31, -0.242), resolution=(1080, 1920)))
        wait(Template(r"tpl1528429495480.png", record_pos=(0.008, -0.009), resolution=(1080, 1920)))
        touch(Template(r"tpl1528429503077.png", record_pos=(-0.182, 0.068), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528429616321.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.008, 0.046), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1528429630951.png", record_pos=(-0.128, -0.444), resolution=(1080, 1920)), "anzhi198元钻石198元")
        touch(Template(r"tpl1528429657769.png", record_pos=(-0.409, -0.705), resolution=(1080, 1920)))
        wait(Template(r"tpl1528429667710.png", record_pos=(0.007, 0.051), resolution=(1080, 1920)))
        touch(Template(r"tpl1528429675233.png", record_pos=(0.194, 0.167), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1531461687708.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.003, -0.014), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1531461705783.png", record_pos=(0.009, -0.036), resolution=(1080, 1920)),"yunos198")
        touch(Template(r"tpl1531461754757.png", record_pos=(0.36, -0.293), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1533005053664.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.009, -0.007), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1533005068532.png", record_pos=(0.008, 0.006), resolution=(1080, 1920)), "yunos198.")
        touch(Template(r"tpl1533005083890.png", record_pos=(0.348, -0.272), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1532678293409.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(-0.007, -0.749), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1532678323563.png", record_pos=(0.018, -0.528), resolution=(1080, 1920)), "lenovo198元钻石198元")
        touch(Template(r"tpl1532678356809.png", record_pos=(-0.433, -0.751), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1532678374013.png", record_pos=(0.212, 0.188), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "198.00元", "vivo198元钻石198元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥198.00", "huawei198元钻石198元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "198.00元", "xiaomi198元钻石198元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtom.samsung:id/tv_price_aipay").get_text()
    , "198.00", "sumsung198元钻石198元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
    sleep(5)


class TomTestPilot:
        
    def TomGifts(self,channel,is_audit):
        wait(Template(r"tpl1531460601928.png", record_pos=(-0.353, -0.057), resolution=(1080, 1920)))
        touch(Template(r"tpl1531460612387.png", record_pos=(-0.356, -0.044), resolution=(1080, 1920)))

        # wait(Template(r"tpl1528421357765.png", record_pos=(-0.382, -0.032), resolution=(1080, 1920)))
        # touch(Template(r"tpl1528421366163.png", record_pos=(-0.381, -0.035), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1531461569220.png", record_pos=(-0.03, 0.447), resolution=(1080, 1920)))
        # touch(Template(r"tpl1528421415709.png", record_pos=(-0.032, 0.456), resolution=(1080, 1920)))
        sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            TomGifts_Mobile()
            
        elif channel == "Mobile" and is_audit == "isAudit":
            TomGifts_Mobile_Audit()      
        elif channel == "Telecom":
            TomGifts_Telecom() 
            
        elif channel == "Unicom":
            TomGifts_Unicom()
            
    def TomDoubleCoin(self,channel,is_audit):
        wait(Template(r"tpl1527247282191.png", record_pos=(-0.144, -0.677), resolution=(1080, 1920)))
        touch(Template(r"tpl1527247282191.png", record_pos=(-0.144, -0.677), resolution=(1080, 1920)))

        # touch(Template(r"tpl1523171185130.png", threshold=0.8, target_pos=5, rgb=False, record_pos=(-0.149, -0.669), resolution=(720, 1280)))
        sleep(5)
        touch(Template(r"tpl1522736053619.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(-0.329, -0.388), resolution=(720, 1280)))
        sleep(5)
        
        if channel == "Mobile" and is_audit == "noAudit":
            TomDoubleCoin_Mobile(channel)
            
        elif channel == "Mobile" and is_audit == "isAudit":
            TomDoubleCoin_Mobile_Audit()
        elif channel == "Telecom":
            TomDoubleCoin_Telecom(channel)
        
        elif channel == "Unicom":
            TomDoubleCoin_Unicom(channel)
    
    def FiveDiamond(self,channel,is_audit):
        if exists(Template(r"tpl1527663766443.png", threshold=1.0, target_pos=5, rgb=False, record_pos=(0.002, -0.42), resolution=(1080, 1920))):
            touch(Template(r"tpl1527664306428.png", threshold=1.0, target_pos=5, rgb=False, record_pos=(0.002, -0.431), resolution=(1080, 1920)))
        # if exists(Template(r"tpl1527162862856.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.425), resolution=(1080, 1920))):
        #     touch(Template(r"tpl1527162862856.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.425), resolution=(1080, 1920)))
        if exists(Template(r"tpl1531460723778.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.009, -0.431), resolution=(1080, 1920))):
            touch(Template(r"tpl1531460736169.png", record_pos=(0.001, -0.422), resolution=(1080, 1920)))

        sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            FiveDiamond_Mobile()
        
        elif channel == "Mobile" and is_audit == "isAudit":
            FiveDiamond_Mobile_Audit_Pay()
        
        elif channel == "Telecom":
            FiveDiamond_Telecom()
        
        elif channel == "Unicom":
            FiveDiamond_Unicom()
    
    def SeventyDiamond(self,channel,is_audit):
        touch(Template(r"tpl1531461146359.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.334, -0.426), resolution=(1080, 1920)))
        # touch(Template(r"tpl1522736212645.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.333, -0.379), resolution=(720, 1280)))
        sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            SeventyDiamond_Mobile()
        
        elif channel == "Mobile" and is_audit == "isAudit":
            SeventyDiamond_Mobile_Audit()
        
        elif channel == "Telecom":
            SeventyDiamond_Telecom()
        
        elif channel == "Unicom":
            SeventyDiamond_Unicom()
    
    def HundredNinetyDiamond(self,channel,is_audit):
          # touch(Template(r"tpl1522736549159.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.331, 0.017), resolution=(720, 1280)))
        wait(Template(r"tpl1531461285123.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.326, -0.028), resolution=(1080, 1920)))
        touch(Template(r"tpl1531461298973.png", record_pos=(-0.323, -0.025), resolution=(1080, 1920)))
        sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            HundredNinetyDiamond_Mobile()
        
        elif channel == "Mobile" and is_audit == "isAudit":
            HundredNinetyDiamond_Mobile_Audit()
        
        elif channel == "Telecom":
            HundredNinetyDiamond_Telecom()
        
        elif channel == "Unicom":
            HundredNinetyDiamond_Unicom()
    
    def ThousandFiveHundeedNinetyDiamond(self,channel):
        # wait(Template(r"tpl1528422528516.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.02), resolution=(1080, 1920)))
        # touch(Template(r"tpl1528422537036.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.032), resolution=(1080, 1920)))
        wait(Template(r"tpl1531461376628.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.006, -0.029), resolution=(1080, 1920)))
        touch(Template(r"tpl1531461393176.png", record_pos=(0.012, -0.017), resolution=(1080, 1920)))
        sleep(5)
        
        ThousandFiveHundeedNinetyDiamond_Founction()
        
    def SixthousandTwoHundredFiftyDiamond(self,channel):
        wait(Template(r"tpl1531461441630.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.34, -0.022), resolution=(1080, 1920)))
        touch(Template(r"tpl1531461452997.png", record_pos=(0.335, -0.033), resolution=(1080, 1920)))
        # wait(Template(r"tpl1528422639272.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.34, -0.034), resolution=(1080, 1920)))
        # touch(Template(r"tpl1528422649743.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.337, -0.029), resolution=(1080, 1920)))
        sleep(5)
        
        SixthousandTwoHundredFiftyDiamond_Founction()
        touch(Template(r"tpl1527587481767.png", record_pos=(0.416, -0.811), resolution=(1080, 1920)))
        sleep(5)

        
    def ExitShopping(self,channel):
        pass
    
    def BabyEyedrops(self,channel,is_audit):
        # touch(Template(r"tpl1526957457513.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.248, -0.509), resolution=(1080, 1920)))
        touch(Template(r"tpl1531904797506.png", record_pos=(0.277, -0.541), resolution=(1080, 1920)))
        sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            BabyEyedrops_Mobile()
        
        elif channel == "Mobile" and is_audit == "isAudit":
            BabyEyedrops_Mobile_Audit()
        
        elif channel == "Telecom":
            BabyEyedrops_Telecom()
        
        elif channel == "Unicom":
            BabyEyedrops_Unicom()
    
    def AdultEyedrops(self,channel,is_audit):
        
        wait(Template(r"tpl1527558550050.png", record_pos=(-0.38, -0.032), resolution=(1080, 1920)))
        if exists(Template(r"tpl1525748795640.png", record_pos=(0.0, 0.832), resolution=(1080, 1776))):
            touch(Template(r"tpl1525748795640.png", record_pos=(0.0, 0.832), resolution=(1080, 1776)))
            sleep(2)
        if exists(Template(r"tpl1527147605974.png", record_pos=(0.001, 0.738), resolution=(1080, 1920))):
            touch(Template(r"tpl1527147605974.png", record_pos=(0.001, 0.738), resolution=(1080, 1920)))
            sleep(2)
        if not exists(Template(r"tpl1526956415961.png", record_pos=(0.281, 0.269), resolution=(1080, 1920))):
            if exists(Template(r"tpl1526956548895.png", record_pos=(0.01, 0.316), resolution=(1080, 1920))):
                touch(Template(r"tpl1526956564623.png", record_pos=(0.007, 0.309), resolution=(1080, 1920)))
            elif exists(Template(r"tpl1526956653466.png", record_pos=(0.292, 0.315), resolution=(1080, 1920))):
                touch(Template(r"tpl1526956693321.png", record_pos=(0.284, 0.313), resolution=(1080, 1920)))
                sleep(1)
                touch(Template(r"tpl1526956724267.png", record_pos=(-0.004, 0.308), resolution=(1080, 1920)))
                sleep(1)

        if exists(Template(r"tpl1526956161011.png", record_pos=(-0.281, 0.276), resolution=(1080, 1920))):
            touch(Template(r"tpl1526956184561.png", record_pos=(-0.387, 0.753), resolution=(1080, 1920)))
            sleep(1.0)
        touch(Template(r"tpl1526956237275.png", record_pos=(-0.151, 0.217), resolution=(1080, 1920)))
        sleep(1.0)

        touch(Template(r"tpl1525673785344.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.383, 0.439), resolution=(1080, 1920)))
        sleep(1)
        # touch(Template(r"tpl1526957170561.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.213, -0.482), resolution=(1080, 1920)))
        touch(Template(r"tpl1531903964915.png", threshold=0.7, target_pos=5, rgb=False, record_pos=(-0.214, -0.537), resolution=(1080, 1920)))
        sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            AdultEyedrops_Mobile()
        
        elif channel == "Mobile" and is_audit == "isAudit":
            AdultEyedrops_Mobile_Audit()
        
        elif channel == "Telecom":
            AdultEyedrops_Telecom()
        
        elif channel == "Unicom":
            AdultEyedrops_Unicom()
    
    def SailorUniforms(self,channel,is_audit):
        wait(Template(r"tpl1528426037864.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.416, 0.76), resolution=(1080, 1920)))
        touch(Template(r"tpl1528426050759.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.411, 0.762), resolution=(1080, 1920)))
        wait(Template(r"tpl1528425957465.png", record_pos=(-0.234, 0.386), resolution=(1080, 1920)))
        touch(Template(r"tpl1528425967864.png", record_pos=(-0.238, 0.382), resolution=(1080, 1920)))
        sleep(5)
        wait(Template(r"tpl1528425986683.png", record_pos=(-0.376, 0.334), resolution=(1080, 1920)))
        touch(Template(r"tpl1528425996971.png", record_pos=(-0.376, 0.332), resolution=(1080, 1920)))
        sleep(5)
        wait(Template(r"tpl1528423493819.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.404, 0.752), resolution=(1080, 1920)))
        touch(Template(r"tpl1528423504629.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.416, 0.757), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1528423504629.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.416, 0.757), resolution=(1080, 1920)))
        sleep(3)
        wait(Template(r"tpl1528423523746.png", threshold=0.7999999999999999, target_pos=5, rgb=False, record_pos=(0.008, 0.756), resolution=(1080, 1920)))
        touch(Template(r"tpl1528423539456.png", threshold=0.7999999999999999, target_pos=5, rgb=False, record_pos=(-0.008, 0.789), resolution=(1080, 1920)))
        sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            SailorUniforms_Mobile()
        
        elif channel == "Mobile" and is_audit == "isAudit":
            SailorUniforms_Mobile_Audit()
        
        elif channel == "Telecom":
            SailorUniforms_Telecom()
        
        elif channel == "Unicom":
            SailorUniforms_Unicom()
        
        
    







































