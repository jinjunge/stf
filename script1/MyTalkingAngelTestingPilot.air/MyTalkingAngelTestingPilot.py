# -*- encoding=utf8 -*-
__author__ = "zx"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

"""
angle update 2018.07.18.

"""

def AngelGifts_Mobile():
    if exists(Template(r"tpl1527598363491.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.0, -0.004), resolution=(1080, 1920))):
        touch(Template(r"tpl1527598382336.png", record_pos=(0.004, 0.073), resolution=(1080, 1920)))
        touch(Template(r"tpl1527598395368.png", record_pos=(0.387, -0.774), resolution=(1080, 1920)))
        sleep(5)
    elif exists(Template(r"tpl1527752952940.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.004, -0.06), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527752976249.png", record_pos=(0.37, -0.269), resolution=(1080, 1920)), "新手特惠礼包金额显示正确，10元")
        touch(Template(r"tpl1527752741845.png", record_pos=(-0.402, -0.29), resolution=(1080, 1920)))
        wait(Template(r"tpl1527752769487.png", record_pos=(0.0, -0.006), resolution=(1080, 1920))) 
        touch(Template(r"tpl1527752776770.png", record_pos=(-0.004, 0.073), resolution=(1080, 1920)))
        sleep(5)
        # touch(Template(r"tpl1527598395368.png", record_pos=(0.387, -0.774), resolution=(1080, 1920)))
        touch(Template(r"tpl1531710091138.png", record_pos=(0.38, -0.774), resolution=(1080, 1920)))

def AngelGifts_Telecom():
    if exists(Template(r"tpl1527663228362.png", record_pos=(-0.011, -0.056), resolution=(1080, 1920))):

        assert_exists(Template(r"tpl1527663244092.png", record_pos=(0.183, -0.157), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")

        touch(Template(r"tpl1527663280045.png", record_pos=(0.396, -0.161), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1527663287389.png", record_pos=(0.007, 0.069), resolution=(1080, 1920)))
        # touch(Template(r"tpl1527663949158.png", record_pos=(0.391, -0.769), resolution=(1080, 1920)))
        touch(Template(r"tpl1531710091138.png", record_pos=(0.38, -0.774), resolution=(1080, 1920)))

    sleep(5)

def AngelGifts_Unicom():
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
    elif exists(Template(r"tpl1531725768180.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, -0.524), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527729726673.png", record_pos=(-0.367, -0.469), resolution=(1080, 1920)), "新手礼物金额显示正确，10元")
        touch(Template(r"tpl1527729740628.png", record_pos=(0.38, -0.583), resolution=(1080, 1920)))
        wait(Template(r"tpl1527729752606.png", record_pos=(-0.006, 0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1527729759991.png", record_pos=(0.009, 0.077), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1527730669789.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.019, 0.095), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527730693209.png", record_pos=(0.026, -0.033), resolution=(1080, 1920)), "yunos新手礼物金额显示正确，10元")
        touch(Template(r"tpl1527730703852.png", record_pos=(0.357, -0.29), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1531709963153.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.035, -0.746), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1531709992694.png", record_pos=(-0.001, -0.526), resolution=(1080, 1920)),"lenovo新手礼物金额显示正确，10元")
        touch(Template(r"tpl1531710032069.png", record_pos=(-0.435, -0.748), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1531710045549.png", record_pos=(0.199, 0.19), resolution=(1080, 1920)))
    # elif exists(Template(r"tpl1531723135361.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.007, -0.006), resolution=(1080, 1920))):
    #     touch(Template(r"tpl1531723149896.png", record_pos=(0.343, -0.285), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1531725835480.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.007, -0.008), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1531725863420.png", record_pos=(0.016, -0.005), resolution=(1080, 1920)),"新手礼物金额显示正确，10元")
        touch(Template(r"tpl1531725888168.png", record_pos=(0.348, -0.268), resolution=(1080, 1920)))

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
    # touch(Template(r"tpl1527663949158.png", record_pos=(0.391, -0.769), resolution=(1080, 1920)))
    touch(Template(r"tpl1531710091138.png", record_pos=(0.38, -0.774), resolution=(1080, 1920)))

def AngelDoubleCoin_Mobile():
    if exists(Template(r"tpl1527599086344.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.004, -0.046), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527599140699.png", record_pos=(0.38, -0.273), resolution=(1080, 1920)), "双倍赚币金额显示正确，0.01元")

        touch(Template(r"tpl1527599173437.png", record_pos=(-0.402, -0.279), resolution=(1080, 1920)))

        touch(Template(r"tpl1527599204966.png", record_pos=(0.0, 0.073), resolution=(1080, 1920)))
        sleep(5)
    elif exists(Template(r"tpl1527752895434.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.004, -0.053), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527752906565.png", record_pos=(0.372, -0.271), resolution=(1080, 1920)), "双倍赚币金额显示正确，10元")
        touch(Template(r"tpl1527599173437.png", record_pos=(-0.402, -0.279), resolution=(1080, 1920)))
        touch(Template(r"tpl1527599204966.png", record_pos=(0.0, 0.073), resolution=(1080, 1920)))
        sleep(5)

def AngelDoubleCoin_Telecom():
    if exists(Template(r"tpl1527663414582.png", record_pos=(-0.002, -0.048), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527663436228.png", record_pos=(0.204, -0.169), resolution=(1080, 1920)), "双倍赚币金额显示正确，10元")
        touch(Template(r"tpl1527663458872.png", record_pos=(0.396, -0.159), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1527663513292.png", record_pos=(0.002, 0.079), resolution=(1080, 1920)))
        sleep(5)

def AngelDoubleCoin_Unicom():
    if exists(Template(r"tpl1527672330100.png", record_pos=(0.004, 0.025), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527672559013.png", record_pos=(0.327, -0.07), resolution=(1080, 1920)), "双倍赚币金额显示正确，10元")
        touch(Template(r"tpl1527672372577.png", record_pos=(-0.35, -0.295), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677126331.png", record_pos=(-0.008, 0.004), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672384671.png", record_pos=(-0.201, 0.129), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677141798.png", record_pos=(-0.014, 0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672400877.png", record_pos=(-0.004, 0.07), resolution=(1080, 1920)))
        sleep(5)
    elif exists(Template(r"tpl1531722191852.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, 0.159), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527672559013.png", record_pos=(0.327, -0.07), resolution=(1080, 1920)), "双倍赚币金额显示正确，10元")
        touch(Template(r"tpl1527672372577.png", record_pos=(-0.35, -0.295), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677126331.png", record_pos=(-0.008, 0.004), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672384671.png", record_pos=(-0.201, 0.129), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677141798.png", record_pos=(-0.014, 0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672400877.png", record_pos=(-0.004, 0.07), resolution=(1080, 1920)))
        sleep(5)



def HeapDiamond_Mobile():
    if exists(Template(r"tpl1527599316640.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.398, -0.264), resolution=(1080, 1920))):
    # if exists(Template(r"tpl1527599303892.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.048), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527599316640.png", record_pos=(0.398, -0.264), resolution=(1080, 1920)), "成堆钻石金额显示正确，0.4元")
        touch(Template(r"tpl1527599173437.png", record_pos=(-0.402, -0.279), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1527599204966.png", record_pos=(0.0, 0.073), resolution=(1080, 1920)))
        sleep(5)
    if exists(Template(r"tpl1527753105025.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.002, -0.05), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527753127492.png", record_pos=(0.381, -0.268), resolution=(1080, 1920)), "成堆钻石金额显示正确，4元")
        touch(Template(r"tpl1528783370796.png", record_pos=(0.001, 0.067), resolution=(1080, 1920)))
        sleep(5)
        if exists(Template(r"tpl1528783746126.png", record_pos=(-0.011, 0.004), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1528783746126.png", record_pos=(-0.011, 0.004), resolution=(1080, 1920)),"支付成功")
            keyevent("back")
            sleep(5)
        else:
            assert_not_exists(Template(r"tpl1528783746126.png", record_pos=(-0.011, 0.004), resolution=(1080, 1920)),"支付失败")
            wait(Template(r"tpl1527753149769.png", record_pos=(-0.119, -0.002), resolution=(1080, 1920)))
            touch(Template(r"tpl1527599204966.png", record_pos=(0.0, 0.073), resolution=(1080, 1920)))
        sleep(1)

def HeapDiamond_Telecom():
    if exists(Template(r"tpl1527663554895.png", record_pos=(-0.006, -0.056), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527663569493.png", record_pos=(0.194, -0.159), resolution=(1080, 1920)), "成堆钻石金额显示正确，4元")
        touch(Template(r"tpl1527663458872.png", record_pos=(0.396, -0.159), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1527663513292.png", record_pos=(0.002, 0.079), resolution=(1080, 1920)))
        sleep(5)

def HeapDiamond_Unicom():
    if exists(Template(r"tpl1527672686232.png", threshold=0.85, target_pos=5, rgb=False, record_pos=(0.002, -0.046), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527672716968.png", record_pos=(0.334, -0.069), resolution=(1080, 1920)), "成堆钻石金额显示正确，4元")
        touch(Template(r"tpl1527672372577.png", record_pos=(-0.35, -0.295), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677126331.png", record_pos=(-0.008, 0.004), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672384671.png", record_pos=(-0.201, 0.129), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677141798.png", record_pos=(-0.014, 0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672400877.png", record_pos=(-0.004, 0.07), resolution=(1080, 1920)))
        sleep(5)
    elif exists(Template(r"tpl1531722191852.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, 0.159), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527672716968.png", record_pos=(0.334, -0.069), resolution=(1080, 1920)), "成堆钻石金额显示正确，4元")
        touch(Template(r"tpl1527672372577.png", record_pos=(-0.35, -0.295), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677126331.png", record_pos=(-0.008, 0.004), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672384671.png", record_pos=(-0.201, 0.129), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677141798.png", record_pos=(-0.014, 0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672400877.png", record_pos=(-0.004, 0.07), resolution=(1080, 1920)))
        sleep(5)



def BaggedDiamond_Mobile():
    if exists(Template(r"tpl1527599406401.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.002, -0.054), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527599417209.png", record_pos=(0.385, -0.264), resolution=(1080, 1920)), "袋装钻石金额显示正确，0.1元")
        touch(Template(r"tpl1527599173437.png", record_pos=(-0.402, -0.279), resolution=(1080, 1920)))
        sleep(1)
        touch(Template(r"tpl1527599204966.png", record_pos=(0.0, 0.073), resolution=(1080, 1920)))
        sleep(1)
    elif exists(Template(r"tpl1527753175560.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.009, -0.055), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527753201831.png", record_pos=(0.369, -0.271), resolution=(1080, 1920)), "袋装钻石金额显示正确，10元")
        touch(Template(r"tpl1527599173437.png", record_pos=(-0.402, -0.279), resolution=(1080, 1920)))
        wait(Template(r"tpl1527753244983.png", record_pos=(-0.167, -0.006), resolution=(1080, 1920)))
        touch(Template(r"tpl1527599204966.png", record_pos=(0.0, 0.073), resolution=(1080, 1920)))
        sleep(4)

def BaggedDiamond_Telecom():
    if exists(Template(r"tpl1527663641775.png", record_pos=(0.002, -0.05), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527663653114.png", record_pos=(0.183, -0.157), resolution=(1080, 1920)), "袋装钻石金额显示正确，10元")
        touch(Template(r"tpl1527663458872.png", record_pos=(0.396, -0.159), resolution=(1080, 1920)))
        sleep(3)
        touch(Template(r"tpl1527663513292.png", record_pos=(0.002, 0.079), resolution=(1080, 1920)))
        sleep(5)

def BaggedDiamond_Unicom():
    if exists(Template(r"tpl1527672770137.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, -0.039), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527672780027.png", record_pos=(0.322, -0.067), resolution=(1080, 1920)), "袋装钻石金额显示正确，10元")
        touch(Template(r"tpl1527672372577.png", record_pos=(-0.35, -0.295), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677126331.png", record_pos=(-0.008, 0.004), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672384671.png", record_pos=(-0.201, 0.129), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677141798.png", record_pos=(-0.014, 0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672400877.png", record_pos=(-0.004, 0.07), resolution=(1080, 1920)))
        sleep(5)
    elif exists(Template(r"tpl1531722191852.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, 0.159), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1527672780027.png", record_pos=(0.322, -0.067), resolution=(1080, 1920)), "袋装钻石金额显示正确，10元")
        touch(Template(r"tpl1527672372577.png", record_pos=(-0.35, -0.295), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677126331.png", record_pos=(-0.008, 0.004), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672384671.png", record_pos=(-0.201, 0.129), resolution=(1080, 1920)))
        wait(Template(r"tpl1527677141798.png", record_pos=(-0.014, 0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1527672400877.png", record_pos=(-0.004, 0.07), resolution=(1080, 1920)))
        sleep(5)


def Wardrobe_Mobile():
    wait(Template(r"tpl1527587517549.png", record_pos=(-0.412, 0.549), resolution=(1080, 1920)))

    touch(Template(r"tpl1527587527271.png", record_pos=(-0.418, 0.554), resolution=(1080, 1920)))
    sleep(5)
    #/*******进入衣柜页面*******/
    wait(Template(r"tpl1527587571762.png", record_pos=(-0.213, 0.104), resolution=(1080, 1920)))
    touch(Template(r"tpl1527587579296.png", record_pos=(-0.15, 0.11), resolution=(1080, 1920)))
    sleep(1)
    wait(Template(r"tpl1527590095585.png", record_pos=(0.381, 0.006), resolution=(1080, 1920)))
    touch(Template(r"tpl1527590107298.png", record_pos=(0.375, 0.005), resolution=(1080, 1920)))
    sleep(1)
    wait(Template(r"tpl1528106134996.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.009, 0.706), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106154947.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.421, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106175844.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.709), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106203453.png", record_pos=(0.002, 0.711), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106216940.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.711), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528966476391.png", record_pos=(0.0, 0.708), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1531726723951.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.008, 0.707), resolution=(1080, 1920)))
    #独角兽连体服20元
    if exists(Template(r"tpl1531726723951.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.008, 0.707), resolution=(1080, 1920))):
        touch(Template(r"tpl1527594289941.png", record_pos=(-0.002, 0.798), resolution=(1080, 1920)))
        sleep(5)
        if exists(Template(r"tpl1527753765235.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.0, -0.131), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527753799274.png", record_pos=(0.367, -0.277), resolution=(1080, 1920)), "独角兽连体服金额显示正确，20元")
            touch(Template(r"tpl1527753840718.png", record_pos=(-0.407, -0.29), resolution=(1080, 1920)))
            wait(Template(r"tpl1527753848022.png", record_pos=(-0.105, -0.002), resolution=(1080, 1920)))
            touch(Template(r"tpl1527753859931.png", record_pos=(0.0, 0.079), resolution=(1080, 1920)))
            sleep(3)
        elif exists(Template(r"tpl1527594455011.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.394, -0.268), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527594455011.png", record_pos=(0.394, -0.268), resolution=(1080, 1920)), "独角兽连体服金额显示正确，0.5元")
            touch(Template(r"tpl1527753840718.png", record_pos=(-0.407, -0.29), resolution=(1080, 1920)))
            wait(Template(r"tpl1527753848022.png", record_pos=(-0.105, -0.002), resolution=(1080, 1920)))
            touch(Template(r"tpl1527753859931.png", record_pos=(0.0, 0.079), resolution=(1080, 1920)))
            sleep(3)

    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106288416.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, 0.711), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106303241.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.005, 0.713), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106335366.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.713), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1531726788787.png", record_pos=(0.028, 0.716), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106365844.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.71), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106378755.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.708), resolution=(1080, 1920)))
    if exists(Template(r"tpl1527599702571.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, 0.704), resolution=(1080, 1920))):
        touch(Template(r"tpl1527594431271.png", record_pos=(-0.002, 0.794), resolution=(1080, 1920)))
        sleep(5)
        if exists(Template(r"tpl1527594455011.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.394, -0.268), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527594455011.png", record_pos=(0.394, -0.268), resolution=(1080, 1920)), "金丝花朵金额显示正确，0.5元")        
            touch(Template(r"tpl1527594528177.png", record_pos=(-0.406, -0.273), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527594551086.png", record_pos=(0.003, 0.076), resolution=(1080, 1920)))
            sleep(3)
        elif exists(Template(r"tpl1527753878774.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.004, -0.137), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527753887902.png", record_pos=(0.369, -0.266), resolution=(1080, 1920)), "金丝花朵金额显示正确，15元")
            touch(Template(r"tpl1527594528177.png", record_pos=(-0.406, -0.273), resolution=(1080, 1920)))
            wait(Template(r"tpl1527753905804.png", record_pos=(-0.112, -0.011), resolution=(1080, 1920)))
            touch(Template(r"tpl1527594551086.png", record_pos=(0.003, 0.076), resolution=(1080, 1920)))
            sleep(3)

    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106401219.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.007, 0.704), resolution=(1080, 1920)))
    if exists(Template(r"tpl1527599731185.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.711), resolution=(1080, 1920))):
        touch(Template(r"tpl1527594602753.png", record_pos=(0.001, 0.795), resolution=(1080, 1920)))
        sleep(8)
        if exists(Template(r"tpl1527594626919.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.393, -0.265), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527594626919.png", record_pos=(0.393, -0.265), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，0.8元")       
            touch(Template(r"tpl1527594642633.png", record_pos=(-0.406, -0.281), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527594551086.png", record_pos=(0.003, 0.076), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527753929917.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.004, -0.131), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527753937706.png", record_pos=(0.372, -0.268), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，15元")
            touch(Template(r"tpl1527594642633.png", record_pos=(-0.406, -0.281), resolution=(1080, 1920)))
            wait(Template(r"tpl1527753955502.png", record_pos=(-0.131, -0.006), resolution=(1080, 1920)))
            touch(Template(r"tpl1527594551086.png", record_pos=(0.003, 0.076), resolution=(1080, 1920)))

    sleep(3)
    touch(Template(r"tpl1528378639771.png", record_pos=(0.425, -0.821), resolution=(1080, 1920)))
    sleep(5)

def Wardrobe_Telecom():
    wait(Template(r"tpl1527587517549.png", record_pos=(-0.412, 0.549), resolution=(1080, 1920)))

    touch(Template(r"tpl1527587527271.png", record_pos=(-0.418, 0.554), resolution=(1080, 1920)))
    sleep(5)
    #/*******进入衣柜页面*******/
    wait(Template(r"tpl1527587571762.png", record_pos=(-0.213, 0.104), resolution=(1080, 1920)))

    touch(Template(r"tpl1527587579296.png", record_pos=(-0.15, 0.11), resolution=(1080, 1920)))

    sleep(1)

    wait(Template(r"tpl1527590095585.png", record_pos=(0.381, 0.006), resolution=(1080, 1920)))
    touch(Template(r"tpl1527590107298.png", record_pos=(0.375, 0.005), resolution=(1080, 1920)))

    wait(Template(r"tpl1528106134996.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.009, 0.706), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106154947.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.421, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106175844.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.709), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528967748168.png", record_pos=(-0.001, 0.707), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106216940.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.711), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528967761560.png", record_pos=(0.0, 0.709), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528967776399.png", record_pos=(0.002, 0.706), resolution=(1080, 1920)))
    #独角兽连体服20元
    if exists(Template(r"tpl1528967787103.png", record_pos=(-0.004, 0.709), resolution=(1080, 1920))):
        touch(Template(r"tpl1527594289941.png", record_pos=(-0.002, 0.798), resolution=(1080, 1920)))
        wait(Template(r"tpl1528117949343.png", record_pos=(-0.008, -0.044), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1528117957505.png", record_pos=(0.196, -0.162), resolution=(1080, 1920)), "独角兽连体服金额显示正确，20元")
        touch(Template(r"tpl1527753840718.png", record_pos=(-0.407, -0.29), resolution=(1080, 1920)))
        wait(Template(r"tpl1527753848022.png", record_pos=(-0.105, -0.002), resolution=(1080, 1920)))
        touch(Template(r"tpl1527753859931.png", record_pos=(0.0, 0.079), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106288416.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, 0.711), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106303241.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.005, 0.713), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106335366.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.713), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528967807321.png", record_pos=(0.002, 0.706), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106365844.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.71), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106378755.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.708), resolution=(1080, 1920)))
    if exists(Template(r"tpl1527599702571.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, 0.704), resolution=(1080, 1920))):
        touch(Template(r"tpl1527594431271.png", record_pos=(-0.002, 0.794), resolution=(1080, 1920)))
        wait(Template(r"tpl1528117857426.png", record_pos=(0.005, -0.033), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1528117871540.png", record_pos=(0.196, -0.162), resolution=(1080, 1920)), "金丝花朵金额显示正确，15元")
        touch(Template(r"tpl1527594528177.png", record_pos=(-0.406, -0.273), resolution=(1080, 1920)))
        wait(Template(r"tpl1527753905804.png", record_pos=(-0.112, -0.011), resolution=(1080, 1920)))
        touch(Template(r"tpl1527594551086.png", record_pos=(0.003, 0.076), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106401219.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.007, 0.704), resolution=(1080, 1920)))
    if exists(Template(r"tpl1527599731185.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.711), resolution=(1080, 1920))):
        touch(Template(r"tpl1527594602753.png", record_pos=(0.001, 0.795), resolution=(1080, 1920)))
        wait(Template(r"tpl1528117900318.png", record_pos=(-0.003, -0.044), resolution=(1080, 1920)))
        assert_exists(Template(r"tpl1528117909942.png", record_pos=(0.198, -0.164), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，15元")
        touch(Template(r"tpl1527594642633.png", record_pos=(-0.406, -0.281), resolution=(1080, 1920)))
        wait(Template(r"tpl1527753955502.png", record_pos=(-0.131, -0.006), resolution=(1080, 1920)))
        touch(Template(r"tpl1527594551086.png", record_pos=(0.003, 0.076), resolution=(1080, 1920)))
    sleep(3)
    touch(Template(r"tpl1528378639771.png", record_pos=(0.425, -0.821), resolution=(1080, 1920)))
    sleep(5)

def Wardrobe_Unicom():
    wait(Template(r"tpl1527587517549.png", record_pos=(-0.412, 0.549), resolution=(1080, 1920)))

    touch(Template(r"tpl1527587527271.png", record_pos=(-0.418, 0.554), resolution=(1080, 1920)))
    sleep(5)
    #/*******进入衣柜页面*******/
    wait(Template(r"tpl1527587571762.png", record_pos=(-0.213, 0.104), resolution=(1080, 1920)))

    touch(Template(r"tpl1527587579296.png", record_pos=(-0.15, 0.11), resolution=(1080, 1920)))

    wait(Template(r"tpl1527590095585.png", record_pos=(0.381, 0.006), resolution=(1080, 1920)))
    touch(Template(r"tpl1527590107298.png", record_pos=(0.375, 0.005), resolution=(1080, 1920)))

    wait(Template(r"tpl1528106134996.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.009, 0.706), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106154947.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.421, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106175844.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.709), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106203453.png", record_pos=(0.002, 0.711), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106216940.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.711), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528966841829.png", record_pos=(-0.001, 0.707), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528967142594.png", record_pos=(-0.004, 0.707), resolution=(1080, 1920)))
    #独角兽连体服20元
    if exists(Template(r"tpl1528967142594.png", record_pos=(-0.004, 0.707), resolution=(1080, 1920))):
        touch(Template(r"tpl1527594289941.png", record_pos=(-0.002, 0.798), resolution=(1080, 1920)))
        sleep(10)
        if exists(Template(r"tpl1527674048114.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.042, -0.363), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527674351835.png", record_pos=(-0.162, -0.444), resolution=(1080, 1920)), "独角兽连体服金额显示正确，20元")
            touch(Template(r"tpl1527674567638.png", record_pos=(0.46, -0.763), resolution=(1080, 1920)))
            wait(Template(r"tpl1527674084472.png", record_pos=(0.002, 0.041), resolution=(1080, 1920)))
            touch(Template(r"tpl1527674092029.png", record_pos=(0.206, 0.178), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527679767503.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.019, -0.143), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527679786604.png", record_pos=(0.305, -0.364), resolution=(1080, 1920)), "独角兽连体服金额显示正确，20元")
            touch(Template(r"tpl1527679801966.png", record_pos=(-0.395, -0.544), resolution=(1080, 1920)))
            wait(Template(r"tpl1527679811422.png", record_pos=(-0.004, 0.054), resolution=(1080, 1920)))
            touch(Template(r"tpl1527679822985.png", record_pos=(0.19, 0.13), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527682329987.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.017, -0.14), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527682340884.png", record_pos=(0.257, -0.214), resolution=(1080, 1920)), "独角兽连体服金额显示正确，20元")
            touch(Template(r"tpl1527682075321.png", record_pos=(-0.324, -0.361), resolution=(1080, 1920)))
            wait(Template(r"tpl1527682083601.png", record_pos=(-0.008, 0.077), resolution=(1080, 1920)))
            touch(Template(r"tpl1527682091797.png", record_pos=(0.215, 0.306), resolution=(1080, 1920)))
            wait(Template(r"tpl1527682105349.png", record_pos=(-0.006, 0.002), resolution=(1080, 1920)))
            touch(Template(r"tpl1527682112284.png", record_pos=(0.021, 0.077), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527683274875.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, 0.006), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527683285366.png", record_pos=(0.291, -0.106), resolution=(1080, 1920)), "独角兽连体服金额显示正确，20元")
            touch(Template(r"tpl1527650602939.png", record_pos=(0.307, -0.241), resolution=(1080, 1920)))
            wait(Template(r"tpl1527683168491.png", record_pos=(-0.002, -0.011), resolution=(1080, 1920)))
            touch(Template(r"tpl1527650614937.png", record_pos=(-0.179, 0.077), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527651508911.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, 0.004), resolution=(1080, 1920))):
            touch(Template(r"tpl1527651524750.png", record_pos=(-0.187, 0.196), resolution=(1080, 1920)))
            sleep(3)
            if exists(Template(r"tpl1527684108631.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, -0.025), resolution=(1080, 1920))):
                assert_exists(Template(r"tpl1527684125485.png", record_pos=(-0.135, 0.284), resolution=(1080, 1920)), "独角兽连体服金额显示正确，20元")
                touch(Template(r"tpl1527684139284.png", record_pos=(0.447, -0.443), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527685138097.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.005, -0.096), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527685150782.png", record_pos=(0.304, -0.183), resolution=(1080, 1920)), "独角兽连体服金额显示正确，20元")
            touch(Template(r"tpl1527652530297.png", record_pos=(0.387, -0.337), resolution=(1080, 1920)))
            wait(Template(r"tpl1527685023416.png", record_pos=(0.019, 0.044), resolution=(1080, 1920)))
            touch(Template(r"tpl1527652550914.png", record_pos=(0.2, 0.105), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527728889734.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, -0.136), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527728899597.png", record_pos=(-0.242, -0.237), resolution=(1080, 1920)), "独角兽连体服金额显示正确，20元")
            touch(Template(r"tpl1527659582096.png", record_pos=(0.394, -0.38), resolution=(1080, 1920)))
            wait(Template(r"tpl1527728778463.png", record_pos=(0.02, 0.051), resolution=(1080, 1920)))
            touch(Template(r"tpl1527659593378.png", record_pos=(-0.196, 0.169), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527729907234.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.073, -0.38), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527729916344.png", record_pos=(-0.367, -0.473), resolution=(1080, 1920)), "独角兽连体服金额显示正确，20元")
            touch(Template(r"tpl1527660676777.png", record_pos=(0.38, -0.585), resolution=(1080, 1920)))
            wait(Template(r"tpl1527729802656.png", record_pos=(0.0, -0.006), resolution=(1080, 1920)))
            touch(Template(r"tpl1527660685940.png", record_pos=(0.0, 0.081), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527730864261.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.066, -0.033), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527730881455.png", record_pos=(0.024, -0.033), resolution=(1080, 1920)), "yunos独角兽连体服金额显示正确，20元")
            touch(Template(r"tpl1527730901234.png", record_pos=(0.357, -0.29), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1528250839726.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.013, -0.014), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1528250853456.png", record_pos=(0.005, -0.001), resolution=(1080, 1920)), "yunos独角兽连体服金额显示正确，20元")
            touch(Template(r"tpl1528250874346.png", record_pos=(0.351, -0.276), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1531710520174.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.001, -0.746), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1531711081493.png", record_pos=(0.021, -0.528), resolution=(1080, 1920)),"lenovo独角兽连体服金额显示正确，20元")
            touch(Template(r"tpl1531710573541.png", record_pos=(-0.448, -0.759), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1531710591599.png", record_pos=(0.201, 0.192), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
            touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
            sleep(8)
            assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "20.00元", "vivo独角兽连体服金额显示正确，20元.")
            keyevent("back")
            sleep(3)
            keyevent("back")
        elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
            assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥20.00", "huawei独角兽连体服金额显示正确，20元.")
            touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
            touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
            assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "20.00元", "xiaomi独角兽连体服金额显示正确，20元.")
            keyevent("back")
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
            assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
        , "20.00", "sumsung独角兽连体服金额显示正确，20元.")
            touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
            wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
            touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
    sleep(3)
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106288416.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, 0.711), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106303241.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.005, 0.713), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106335366.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.713), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528967172747.png", record_pos=(-0.002, 0.706), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106365844.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.71), resolution=(1080, 1920)))
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106378755.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.708), resolution=(1080, 1920)))
    if exists(Template(r"tpl1527599702571.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, 0.704), resolution=(1080, 1920))):
        touch(Template(r"tpl1527594431271.png", record_pos=(-0.002, 0.794), resolution=(1080, 1920)))
        sleep(8)
        if exists(Template(r"tpl1527674169469.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.094, -0.354), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527674187116.png", record_pos=(-0.156, -0.444), resolution=(1080, 1920)), "金丝花朵金额显示正确，15元")
            touch(Template(r"tpl1527674567638.png", record_pos=(0.46, -0.763), resolution=(1080, 1920)))
            wait(Template(r"tpl1527674220514.png", record_pos=(-0.006, 0.044), resolution=(1080, 1920)))
            touch(Template(r"tpl1527674227805.png", record_pos=(0.189, 0.17), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527679911690.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.004, -0.257), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527679932622.png", record_pos=(0.306, -0.368), resolution=(1080, 1920)), "金丝花朵金额显示正确，15元")
            touch(Template(r"tpl1527679801966.png", record_pos=(-0.395, -0.544), resolution=(1080, 1920)))
            wait(Template(r"tpl1527679811422.png", record_pos=(-0.004, 0.054), resolution=(1080, 1920)))
            touch(Template(r"tpl1527679822985.png", record_pos=(0.19, 0.13), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527682397578.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.15), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527682410266.png", record_pos=(0.261, -0.207), resolution=(1080, 1920)), "金丝花朵金额显示正确，15元")
            touch(Template(r"tpl1527682075321.png", record_pos=(-0.324, -0.361), resolution=(1080, 1920)))
            wait(Template(r"tpl1527682083601.png", record_pos=(-0.008, 0.077), resolution=(1080, 1920)))
            touch(Template(r"tpl1527682091797.png", record_pos=(0.215, 0.306), resolution=(1080, 1920)))
            wait(Template(r"tpl1527682105349.png", record_pos=(-0.006, 0.002), resolution=(1080, 1920)))
            touch(Template(r"tpl1527682112284.png", record_pos=(0.021, 0.077), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527683337923.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.0), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527683346778.png", record_pos=(0.294, -0.111), resolution=(1080, 1920)), "金丝花朵金额显示正确，15元")
            touch(Template(r"tpl1527650602939.png", record_pos=(0.307, -0.241), resolution=(1080, 1920)))
            wait(Template(r"tpl1527683168491.png", record_pos=(-0.002, -0.011), resolution=(1080, 1920)))
            touch(Template(r"tpl1527650614937.png", record_pos=(-0.179, 0.077), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527651508911.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, 0.004), resolution=(1080, 1920))):
            touch(Template(r"tpl1527651524750.png", record_pos=(-0.187, 0.196), resolution=(1080, 1920)))
            sleep(3)
            if exists(Template(r"tpl1527684236341.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.03), resolution=(1080, 1920))):
                assert_exists(Template(r"tpl1527684245842.png", record_pos=(-0.14, 0.291), resolution=(1080, 1920)), "金丝花朵金额显示正确，15元")
                touch(Template(r"tpl1527684139284.png", record_pos=(0.447, -0.443), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527685206962.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.008, -0.116), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527685228756.png", record_pos=(0.316, -0.213), resolution=(1080, 1920)), "金丝花朵金额显示正确，15元")
            touch(Template(r"tpl1527652530297.png", record_pos=(0.387, -0.337), resolution=(1080, 1920)))
            wait(Template(r"tpl1527685023416.png", record_pos=(0.019, 0.044), resolution=(1080, 1920)))
            touch(Template(r"tpl1527652550914.png", record_pos=(0.2, 0.105), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527728958502.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.149), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527728974634.png", record_pos=(-0.231, -0.239), resolution=(1080, 1920)), "金丝花朵金额显示正确，15元")
            touch(Template(r"tpl1527659582096.png", record_pos=(0.394, -0.38), resolution=(1080, 1920)))
            wait(Template(r"tpl1527728778463.png", record_pos=(0.02, 0.051), resolution=(1080, 1920)))
            touch(Template(r"tpl1527659593378.png", record_pos=(-0.196, 0.169), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527729980543.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.062, -0.374), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527729990715.png", record_pos=(-0.365, -0.469), resolution=(1080, 1920)), "金丝花朵金额显示正确，15元")
            touch(Template(r"tpl1527660676777.png", record_pos=(0.38, -0.585), resolution=(1080, 1920)))
            wait(Template(r"tpl1527729802656.png", record_pos=(0.0, -0.006), resolution=(1080, 1920)))
            touch(Template(r"tpl1527660685940.png", record_pos=(0.0, 0.081), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527730952411.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.071, -0.031), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527730982734.png", record_pos=(0.026, -0.039), resolution=(1080, 1920)), "金丝花朵金额显示正确，15元")
            touch(Template(r"tpl1527730992753.png", record_pos=(0.357, -0.294), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1528250917173.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.019, -0.023), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1528250927455.png", record_pos=(0.007, -0.027), resolution=(1080, 1920)), "yunos金丝花朵金额显示正确，15元")
            touch(Template(r"tpl1528250942706.png", record_pos=(0.355, -0.276), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1531710520174.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.001, -0.746), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1531711174552.png", record_pos=(0.01, -0.535), resolution=(1080, 1920)),"lenovo金丝花朵金额显示正确，15元")
            touch(Template(r"tpl1531710573541.png", record_pos=(-0.448, -0.759), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1531710591599.png", record_pos=(0.201, 0.192), resolution=(1080, 1920)))

        elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
            touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
            sleep(8)
            assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "15.00元", "vivo金丝花朵金额显示正确，15元.")
            keyevent("back")
            sleep(3)
            keyevent("back")
        elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
            assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥15.00", "huawei金丝花朵金额显示正确，15元.")
            touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
            touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
            assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "15.00元", "xiaomi金丝花朵金额显示正确，15元.")
            keyevent("back")
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
            assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
        , "15.00", "sumsung金丝花朵金额显示正确，15元.")
            touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
            wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
            touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
    sleep(3)
    touch(Template(r"tpl1528106188828.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.419, 0.764), resolution=(1080, 1920)))
    wait(Template(r"tpl1528106401219.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.007, 0.704), resolution=(1080, 1920)))
    if exists(Template(r"tpl1527599731185.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.711), resolution=(1080, 1920))):
        touch(Template(r"tpl1527594602753.png", record_pos=(0.001, 0.795), resolution=(1080, 1920)))
        sleep(8)
        if exists(Template(r"tpl1527674252940.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.044, -0.336), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527674274518.png", record_pos=(-0.161, -0.445), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，15元")
            touch(Template(r"tpl1527674567638.png", record_pos=(0.46, -0.763), resolution=(1080, 1920)))
            wait(Template(r"tpl1527674307409.png", record_pos=(0.002, 0.063), resolution=(1080, 1920)))
            touch(Template(r"tpl1527674314457.png", record_pos=(0.185, 0.172), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527679997674.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.008, -0.253), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527680020578.png", record_pos=(0.301, -0.361), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，15元")
            touch(Template(r"tpl1527679801966.png", record_pos=(-0.395, -0.544), resolution=(1080, 1920)))
            wait(Template(r"tpl1527679811422.png", record_pos=(-0.004, 0.054), resolution=(1080, 1920)))
            touch(Template(r"tpl1527679822985.png", record_pos=(0.19, 0.13), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527682397578.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.15), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527682410266.png", record_pos=(0.261, -0.207), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，15元")
            touch(Template(r"tpl1527682075321.png", record_pos=(-0.324, -0.361), resolution=(1080, 1920)))
            wait(Template(r"tpl1527682083601.png", record_pos=(-0.008, 0.077), resolution=(1080, 1920)))
            touch(Template(r"tpl1527682091797.png", record_pos=(0.215, 0.306), resolution=(1080, 1920)))
            wait(Template(r"tpl1527682105349.png", record_pos=(-0.006, 0.002), resolution=(1080, 1920)))
            touch(Template(r"tpl1527682112284.png", record_pos=(0.021, 0.077), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527683337923.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.0), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527683346778.png", record_pos=(0.294, -0.111), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，15元")
            touch(Template(r"tpl1527650602939.png", record_pos=(0.307, -0.241), resolution=(1080, 1920)))
            wait(Template(r"tpl1527683168491.png", record_pos=(-0.002, -0.011), resolution=(1080, 1920)))
            touch(Template(r"tpl1527650614937.png", record_pos=(-0.179, 0.077), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527651508911.png", record_pos=(-0.002, 0.004), resolution=(1080, 1920))):
            touch(Template(r"tpl1527651524750.png", record_pos=(-0.187, 0.196), resolution=(1080, 1920)))
            sleep(3)
            if exists(Template(r"tpl1527684236341.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.03), resolution=(1080, 1920))):
                assert_exists(Template(r"tpl1527684245842.png", record_pos=(-0.14, 0.291), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，15元")
                touch(Template(r"tpl1527684139284.png", record_pos=(0.447, -0.443), resolution=(1080, 1920)))

        elif exists(Template(r"tpl1527685206962.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.008, -0.116), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527685228756.png", record_pos=(0.316, -0.213), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，15元")
            touch(Template(r"tpl1527652530297.png", record_pos=(0.387, -0.337), resolution=(1080, 1920)))
            wait(Template(r"tpl1527685023416.png", record_pos=(0.019, 0.044), resolution=(1080, 1920)))
            touch(Template(r"tpl1527652550914.png", record_pos=(0.2, 0.105), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527728958502.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.149), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527728974634.png", record_pos=(-0.231, -0.239), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，15元")
            touch(Template(r"tpl1527659582096.png", record_pos=(0.394, -0.38), resolution=(1080, 1920)))
            wait(Template(r"tpl1527728778463.png", record_pos=(0.02, 0.051), resolution=(1080, 1920)))
            touch(Template(r"tpl1527659593378.png", record_pos=(-0.196, 0.169), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527729980543.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.062, -0.374), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527729990715.png", record_pos=(-0.365, -0.469), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，15元")
            touch(Template(r"tpl1527660676777.png", record_pos=(0.38, -0.585), resolution=(1080, 1920)))
            wait(Template(r"tpl1527729802656.png", record_pos=(0.0, -0.006), resolution=(1080, 1920)))
            touch(Template(r"tpl1527660685940.png", record_pos=(0.0, 0.081), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527730952411.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.071, -0.031), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527730982734.png", record_pos=(0.026, -0.039), resolution=(1080, 1920)), "梦幻闪亮裙装金额显示正确，15元")
            touch(Template(r"tpl1527730992753.png", record_pos=(0.357, -0.294), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1528250976506.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.009, -0.016), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1528250996173.png", record_pos=(0.006, -0.008), resolution=(1080, 1920)), "yunos梦幻闪亮裙装金额显示正确，15元")
            touch(Template(r"tpl1528251010891.png", record_pos=(0.353, -0.272), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1531710520174.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.001, -0.746), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1531711209115.png", record_pos=(-0.001, -0.522), resolution=(1080, 1920)),"lenovo梦幻闪亮裙装金额显示正确，15元")
            touch(Template(r"tpl1531710573541.png", record_pos=(-0.448, -0.759), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1531710591599.png", record_pos=(0.201, 0.192), resolution=(1080, 1920)))

        elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
            touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
            sleep(8)
            assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "15.00元", "vivo梦幻闪亮裙装金额显示正确，15元.")
            keyevent("back")
            sleep(3)
            keyevent("back")
        elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
            assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥15.00", "huawei梦幻闪亮裙装金额显示正确，15元.")
            touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
            touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
            assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "15.00元", "xiaomi梦幻闪亮裙装金额显示正确，15元.")
            keyevent("back")
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
            assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
        , "15.00", "sumsung梦幻闪亮裙装金额显示正确，15元.")
            touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
            wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
            touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
    sleep(3)
    touch(Template(r"tpl1528378639771.png", record_pos=(0.425, -0.821), resolution=(1080, 1920)))
    sleep(5)


class AngelTestPilot(object):
    def AngelGifts(self,channel):
        # touch(Template(r"tpl1527598302373.png", record_pos=(0.411, -0.271), resolution=(1080, 1920)))
        # touch(Template(r"tpl1527598320009.png", record_pos=(0.002, 0.468), resolution=(1080, 1920)))
        sleep(10)
        touch(Template(r"tpl1531723736361.png", record_pos=(0.41, -0.269), resolution=(1080, 1920)))
        sleep(6)
        # touch((531.5,1350.3))
        touch(Template(r"tpl1531709659766.png", record_pos=(-0.001, 0.338), resolution=(1080, 1920)))
        sleep(5)

        if channel == "Mobile":
            AngelGifts_Mobile()
            
        elif channel == "Telecom":
            AngelGifts_Telecom()
            
        elif channel == "Unicom":
            AngelGifts_Unicom()
            
    def AngelDoubleCoin(self,channel):
        wait(Template(r"tpl1527599903703.png", record_pos=(-0.357, -0.591), resolution=(1080, 1920)))
        touch(Template(r"tpl1527599921571.png", record_pos=(-0.365, -0.598), resolution=(1080, 1920)))
        sleep(5)
        touch(Template(r"tpl1527599066660.png", record_pos=(0.325, -0.006), resolution=(1080, 1920)))
        sleep(5)

        if channel == "Mobile":
            AngelDoubleCoin_Mobile()
            
        elif channel == "Telecom":
            AngelDoubleCoin_Telecom()
            
        elif channel == "Unicom":
            AngelDoubleCoin_Unicom()
            
    def HeapDiamond(self,channel):
        touch(Template(r"tpl1527599216990.png", record_pos=(-0.328, -0.417), resolution=(1080, 1920)))
        sleep(5)

        if channel == "Mobile":
            HeapDiamond_Mobile()
            
        elif channel == "Telecom":
            HeapDiamond_Telecom()
            
        elif channel == "Unicom":
            HeapDiamond_Unicom()
            
    def BaggedDiamond(self,channel):
        touch(Template(r"tpl1527599391322.png", record_pos=(-0.002, -0.411), resolution=(1080, 1920)))
        sleep(3)
        if channel == "Mobile":
            BaggedDiamond_Mobile()
            
        elif channel == "Telecom":
            BaggedDiamond_Telecom()
            
        elif channel == "Unicom":
            BaggedDiamond_Unicom()
            
    def BoxPackedDiamond(self,channel):
        touch(Template(r"tpl1527599463530.png", record_pos=(0.331, -0.413), resolution=(1080, 1920)))
        sleep(5)
        if exists(Template(r"tpl1527644716454.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.273, -0.161), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527644775618.png", record_pos=(-0.175, -0.445), resolution=(1080, 1920)), "盒装钻石金额显示正确，40元")
            touch(Template(r"tpl1527644801686.png", record_pos=(-0.408, -0.696), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527644835114.png", record_pos=(0.192, 0.169), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527643071165.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.269), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527599490728.png", record_pos=(0.324, -0.37), resolution=(1080, 1920)), "盒装钻石金额显示正确，40元")
            touch(Template(r"tpl1527600277427.png", record_pos=(-0.389, -0.557), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527600288825.png", record_pos=(0.196, 0.126), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527648900904.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, -0.132), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527648931062.png", record_pos=(0.277, -0.215), resolution=(1080, 1920)), "盒装钻石金额显示正确，40元")
            touch(Template(r"tpl1527648944474.png", record_pos=(-0.323, -0.363), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527648957939.png", record_pos=(0.209, 0.305), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527648972826.png", record_pos=(0.002, 0.071), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527650550106.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.008, -0.015), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527650586484.png", record_pos=(0.306, -0.115), resolution=(1080, 1920)), "盒装钻石金额显示正确，40元")
            touch(Template(r"tpl1527650602939.png", record_pos=(0.307, -0.241), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527650614937.png", record_pos=(-0.179, 0.077), resolution=(1080, 1920)))
            sleep(3)
        elif exists(Template(r"tpl1527651508911.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.002, 0.004), resolution=(1080, 1920))):
            touch(Template(r"tpl1527651524750.png", record_pos=(-0.187, 0.196), resolution=(1080, 1920)))
            sleep(3)
            if exists(Template(r"tpl1527651566800.png", record_pos=(-0.01, -0.027), resolution=(1080, 1920))):
                assert_exists(Template(r"tpl1527651582908.png", record_pos=(-0.13, 0.29), resolution=(1080, 1920)), "盒装钻石金额显示正确，40元")
                touch(Template(r"tpl1527651608130.png", record_pos=(0.447, -0.439), resolution=(1080, 1920)))
                sleep(3)
        elif exists(Template(r"tpl1527652474165.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.008, -0.134), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527652505598.png", record_pos=(0.295, -0.219), resolution=(1080, 1920)), "盒装钻石金额显示正确，40元")
            touch(Template(r"tpl1527652530297.png", record_pos=(0.387, -0.337), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527652550914.png", record_pos=(0.2, 0.105), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527659542375.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.007, -0.088), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527659566644.png", record_pos=(-0.242, -0.237), resolution=(1080, 1920)), "盒装钻石金额显示正确，40元")
            touch(Template(r"tpl1527659582096.png", record_pos=(0.394, -0.38), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527659593378.png", record_pos=(-0.196, 0.169), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527660627775.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.389), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527660641068.png", record_pos=(-0.335, -0.471), resolution=(1080, 1920)), "盒装钻石金额显示正确，40元")
            touch(Template(r"tpl1527660676777.png", record_pos=(0.38, -0.585), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527660685940.png", record_pos=(0.0, 0.081), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527661453839.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.017, -0.03), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527661476355.png", record_pos=(0.02, -0.041), resolution=(1080, 1920)), "yunos盒装钻石金额显示正确，40元")
            touch(Template(r"tpl1527661500069.png", record_pos=(0.361, -0.292), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527672250730.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.009, -0.559), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1533104884194.png", record_pos=(-0.152, -0.441), resolution=(1080, 1920)), "anzhi盒装钻石金额显示正确，40元")
            touch(Template(r"tpl1527672230811.png", record_pos=(0.459, -0.769), resolution=(1080, 1920)))
            wait(Template(r"tpl1527677081839.png", record_pos=(0.005, 0.053), resolution=(1080, 1920)))
            touch(Template(r"tpl1527672120014.png", record_pos=(0.192, 0.176), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1531710520174.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.001, -0.746), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1531710543179.png", record_pos=(-0.003, -0.528), resolution=(1080, 1920)),"lenovo盒装钻石金额显示正确，40元")
            touch(Template(r"tpl1531710573541.png", record_pos=(-0.448, -0.759), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1531710591599.png", record_pos=(0.201, 0.192), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
            touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
            sleep(8)
            assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "40.00元", "vivo盒装钻石金额显示正确，40元.")
            keyevent("back")
            sleep(3)
            keyevent("back")
        elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
            assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥40.00", "huawei盒装钻石金额显示正确，40元.")
            touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
            touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
            assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "40.00元", "xiaomi盒装钻石金额显示正确，40元.")
            keyevent("back")
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
            assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
        , "40.00", "sumsung盒装钻石金额显示正确，40元.")
            touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
            wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
            touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
        sleep(5)
    
    def SBoxAssemblyDiamond(self,channel):
        touch(Template(r"tpl1527599526351.png", record_pos=(-0.321, -0.009), resolution=(1080, 1920)))
        sleep(5)
        if exists(Template(r"tpl1527644899117.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.309, -0.146), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527644923087.png", record_pos=(-0.143, -0.442), resolution=(1080, 1920)), "小箱钻石金额显示正确，80元")
            touch(Template(r"tpl1527644935978.png", record_pos=(-0.408, -0.696), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527644948503.png", record_pos=(0.182, 0.179), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527599541125.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.254), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527599556164.png", record_pos=(0.308, -0.356), resolution=(1080, 1920)), "小箱钻石金额显示正确，80元")
            touch(Template(r"tpl1527600277427.png", record_pos=(-0.389, -0.557), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527600288825.png", record_pos=(0.196, 0.126), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527649636116.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.017, -0.165), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527649042680.png", record_pos=(0.255, -0.215), resolution=(1080, 1920)), "小箱钻石金额显示正确，80元")
            touch(Template(r"tpl1527648944474.png", record_pos=(-0.323, -0.363), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527648957939.png", record_pos=(0.209, 0.305), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527648972826.png", record_pos=(0.002, 0.071), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527650678519.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.011, -0.004), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527650698110.png", record_pos=(0.304, -0.108), resolution=(1080, 1920)), "小箱钻石金额显示正确，80元")
            touch(Template(r"tpl1527650602939.png", record_pos=(0.307, -0.241), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527650614937.png", record_pos=(-0.179, 0.077), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527651508911.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.002, 0.004), resolution=(1080, 1920))):
            touch(Template(r"tpl1527651524750.png", record_pos=(-0.187, 0.196), resolution=(1080, 1920)))
            sleep(3)
            if exists(Template(r"tpl1527651737759.png", record_pos=(0.006, -0.035), resolution=(1080, 1920))):
                assert_exists(Template(r"tpl1527651749625.png", record_pos=(-0.117, 0.284), resolution=(1080, 1920)), "小箱钻石金额显示正确，80元")
                touch(Template(r"tpl1527651608130.png", record_pos=(0.447, -0.439), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527652586613.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.131), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527652598272.png", record_pos=(0.289, -0.217), resolution=(1080, 1920)), "小箱钻石金额显示正确，80元")
            touch(Template(r"tpl1527652530297.png", record_pos=(0.387, -0.337), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527652550914.png", record_pos=(0.2, 0.105), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527659637013.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.007, -0.154), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527659649633.png", record_pos=(-0.244, -0.237), resolution=(1080, 1920)), "小箱钻石金额显示正确，80元")
            touch(Template(r"tpl1527659582096.png", record_pos=(0.394, -0.38), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527659593378.png", record_pos=(-0.196, 0.169), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527660736256.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.007, -0.383), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527660745397.png", record_pos=(-0.335, -0.468), resolution=(1080, 1920)), "小箱钻石金额显示正确，80元")
            touch(Template(r"tpl1527660676777.png", record_pos=(0.38, -0.585), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527660685940.png", record_pos=(0.0, 0.081), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527661550699.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.013, -0.017), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527661561337.png", record_pos=(0.002, -0.031), resolution=(1080, 1920)), "yunos小箱钻石金额显示正确，80元")
            touch(Template(r"tpl1527661500069.png", record_pos=(0.361, -0.292), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1533105049518.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.008, -0.381), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1533105080998.png", record_pos=(-0.144, -0.445), resolution=(1080, 1920)), "anzhi小箱钻石金额显示正确，80元.")
            touch(Template(r"tpl1527672230811.png", record_pos=(0.459, -0.769), resolution=(1080, 1920)))
            wait(Template(r"tpl1527677081839.png", record_pos=(0.005, 0.053), resolution=(1080, 1920)))
            touch(Template(r"tpl1527672120014.png", record_pos=(0.192, 0.176), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1531710520174.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.001, -0.746), resolution=(1080, 1920))):

            assert_exists(Template(r"tpl1531710755911.png", record_pos=(0.003, -0.533), resolution=(1080, 1920)),"lenovo小箱钻石金额显示正确，80元")
            touch(Template(r"tpl1531710573541.png", record_pos=(-0.448, -0.759), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1531710591599.png", record_pos=(0.201, 0.192), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
            touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
            sleep(8)
            assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "80.00元", "vivo小箱钻石金额显示正确，80元.")
            keyevent("back")
            sleep(3)
            keyevent("back")
        elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
            assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥80.00", "huawei小箱钻石金额显示正确，80元.")
            touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
            touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
            assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "80.00元", "xiaomi小箱钻石金额显示正确，80元.")
            keyevent("back")
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
            assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
        , "80.00", "sumsung小箱钻石金额显示正确，80元.")
            touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
            wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
            touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
        sleep(5)

    def BBoxAssemblyDiamond(self,channel):
        touch(Template(r"tpl1527599596811.png", record_pos=(-0.006, -0.007), resolution=(1080, 1920)))
        sleep(9)
        if exists(Template(r"tpl1527645008297.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.302, -0.154), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527645035911.png", record_pos=(-0.133, -0.44), resolution=(1080, 1920)), "大箱钻石金额显示正确，200元")
            touch(Template(r"tpl1527645049957.png", record_pos=(-0.408, -0.698), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527645060335.png", record_pos=(0.203, 0.181), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527599612086.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.256), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527599620369.png", record_pos=(0.306, -0.361), resolution=(1080, 1920)), "大箱钻石金额显示正确，200元")
            touch(Template(r"tpl1527600277427.png", record_pos=(-0.389, -0.557), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527642722005.png", record_pos=(0.202, 0.126), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527649103179.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.156), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527649124954.png", record_pos=(0.249, -0.213), resolution=(1080, 1920)), "大箱钻石金额显示正确，200元")
            touch(Template(r"tpl1527648944474.png", record_pos=(-0.323, -0.363), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527648957939.png", record_pos=(0.209, 0.305), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527648972826.png", record_pos=(0.002, 0.071), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527650808749.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.01, -0.002), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527650823554.png", record_pos=(0.303, -0.108), resolution=(1080, 1920)), "大箱钻石金额显示正确，200元")
            touch(Template(r"tpl1527650602939.png", record_pos=(0.307, -0.241), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527650614937.png", record_pos=(-0.179, 0.077), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527651508911.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.002, 0.004), resolution=(1080, 1920))):
            touch(Template(r"tpl1527651524750.png", record_pos=(-0.187, 0.196), resolution=(1080, 1920)))
            sleep(3)
            if exists(Template(r"tpl1527651796868.png", record_pos=(0.01, -0.023), resolution=(1080, 1920))):
                assert_exists(Template(r"tpl1527651805617.png", record_pos=(-0.125, 0.284), resolution=(1080, 1920)), "大箱钻石金额显示正确，200元")
                touch(Template(r"tpl1527651608130.png", record_pos=(0.447, -0.439), resolution=(1080, 1920)))
                sleep(3)
        elif exists(Template(r"tpl1527652639051.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.015, -0.121), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527652649099.png", record_pos=(0.27, -0.213), resolution=(1080, 1920)), "大箱钻石金额显示正确，200元")
            touch(Template(r"tpl1527652530297.png", record_pos=(0.387, -0.337), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527652550914.png", record_pos=(0.2, 0.105), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527659695394.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.002, -0.141), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527659709961.png", record_pos=(-0.225, -0.239), resolution=(1080, 1920)), "大箱钻石金额显示正确，200元")
            touch(Template(r"tpl1527659582096.png", record_pos=(0.394, -0.38), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527659593378.png", record_pos=(-0.196, 0.169), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1531726921112.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.009, -0.521), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527660802078.png", record_pos=(-0.319, -0.466), resolution=(1080, 1920)), "大箱钻石金额显示正确，200元")
            touch(Template(r"tpl1527660676777.png", record_pos=(0.38, -0.585), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1527660685940.png", record_pos=(0.0, 0.081), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1527661598315.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(0.017, -0.013), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1527661610896.png", record_pos=(0.006, -0.039), resolution=(1080, 1920)), "yunos大箱钻石金额显示正确，200元")
            touch(Template(r"tpl1527661500069.png", record_pos=(0.361, -0.292), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1531726993743.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.009, -0.019), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1531727013040.png", record_pos=(0.014, 0.017), resolution=(1080, 1920)),"yunos大箱钻石金额显示正确，200元")
            touch(Template(r"tpl1531727049047.png", record_pos=(0.347, -0.272), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1533105351928.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(0.001, -0.353), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1533105365313.png", record_pos=(-0.131, -0.439), resolution=(1080, 1920)), "anzhi大箱钻石金额显示正确，200元.")
            touch(Template(r"tpl1527672230811.png", record_pos=(0.459, -0.769), resolution=(1080, 1920)))
            wait(Template(r"tpl1527677081839.png", record_pos=(0.005, 0.053), resolution=(1080, 1920)))
            touch(Template(r"tpl1527672120014.png", record_pos=(0.192, 0.176), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1531710520174.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.001, -0.746), resolution=(1080, 1920))):
            assert_exists(Template(r"tpl1531710846605.png", record_pos=(0.014, -0.535), resolution=(1080, 1920)),"lenovo大箱钻石金额显示正确，200元")
            touch(Template(r"tpl1531710573541.png", record_pos=(-0.448, -0.759), resolution=(1080, 1920)))
            sleep(3)
            touch(Template(r"tpl1531710591599.png", record_pos=(0.201, 0.192), resolution=(1080, 1920)))
        elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
            touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
            sleep(8)
            assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "200.00元", "vivo大箱钻石金额显示正确，200元.")
            keyevent("back")
            sleep(3)
            keyevent("back")
        elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
            assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥200.00", "huawei大箱钻石金额显示正确，200元.")
            touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
            touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
            assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "200.00元", "xiaomi大箱钻石金额显示正确，200元.")
            keyevent("back")
            wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
            touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
        elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
            assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
        , "200.00", "sumsung大箱钻石金额显示正确，200元.")
            touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
            wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
            touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))
        sleep(5)
        touch(Template(r"tpl1527599641133.png", record_pos=(0.415, -0.822), resolution=(1080, 1920)))
        sleep(5)

    def UnicornConjoined(self,channel):
        # if channel == "Mobile":
        #     pass
        # elif channel == "Telecom":
        #     pass
        # elif channel == "Unicom":
            pass   
    def GoldenSilkFlowers(self,channel):
        # if channel == "Mobile":
        #     pass
        # elif channel == "Telecom":
        #     pass
        # elif channel == "Unicom":
            pass   
    def DreamShinyDress(self,channel):
        # if channel == "Mobile":
        #     pass
        # elif channel == "Telecom":
        #     pass
        # elif channel == "Unicom":
            pass   
    
    def Wardrobe(self,channel):
        if channel == "Mobile":
            Wardrobe_Mobile()
            
        elif channel == "Telecom":
            Wardrobe_Telecom()
            
        elif channel == "Unicom":
            Wardrobe_Unicom()
            
    
    
    
    
    
    

















































