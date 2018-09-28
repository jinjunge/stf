# -*- encoding=utf8 -*-
__author__ = "zx"

from airtest.core.api import *
auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

"""
test updata 2018.07.17

"""

def TomPoolGifts_Mobile():
    
    assert_equal(poco(text="￥0.01").get_text(), "￥0.01", "新手礼包0.01.")
    touch(Template(r"tpl1527669397124.png", record_pos=(-0.23, -0.169), resolution=(1920, 1080)))
    wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    sleep(5)
    touch(Template(r"tpl1527571911168.png", record_pos=(0.368, -0.159), resolution=(1920, 1080)))
    sleep(5)

def TomPoolGifts_Audit_Mobile():
    if exists(Template(r"tpl1528272926859.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, 0.039), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528266467826.png", record_pos=(0.004, -0.094), resolution=(1920, 1080)),"oppo.apk新手礼包金额显示正确，10元")
        touch(Template(r"tpl1527669397124.png", record_pos=(-0.23, -0.169), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529566213909.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, -0.149), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528337128164.png", record_pos=(0.19, -0.107), resolution=(1920, 1080)), "sdk360.apk新手礼包金额显示正确，10元")
        touch(Template(r"tpl1528337164420.png", record_pos=(-0.227, -0.113), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    sleep(4)
    
    touch(Template(r"tpl1527571911168.png", record_pos=(0.368, -0.159), resolution=(1920, 1080)))
    sleep(5)

def TomPoolGifts_Telecom():

    if exists(Template(r"tpl1528363828302.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, -0.006), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528363919792.png", record_pos=(0.19, -0.107), resolution=(1920, 1080)), "特惠礼包金额显示正确，10元")
        touch(Template(r"tpl1528337164420.png", record_pos=(-0.227, -0.113), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528363957197.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.005, -0.005), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528363973482.png", record_pos=(0.121, -0.086), resolution=(1920, 1080)), "特惠礼包金额显示正确，10元")
        touch(Template(r"tpl1528363998651.png", record_pos=(0.22, -0.092), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    sleep(3)
    wait(Template(r"tpl1527571911168.png", record_pos=(0.368, -0.159), resolution=(1920, 1080)))
    touch(Template(r"tpl1527571911168.png", record_pos=(0.368, -0.159), resolution=(1920, 1080)))
    sleep(5)

def TomPoolGifts_Unicom():
    if exists(Template(r"tpl1529410412302.png", threshold=0.95, target_pos=5, rgb=False, record_pos=(0.005, -0.032), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529410429049.png", record_pos=(-0.3, 0.01), resolution=(1920, 1080)),"lenove新手礼包金额显示正确，10元")
        touch(Template(r"tpl1529410465414.png", record_pos=(-0.468, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1529410475677.png", record_pos=(-0.001, 0.021), resolution=(1920, 1080)))
        touch(Template(r"tpl1529410482870.png", record_pos=(0.114, 0.108), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528352345454.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.005, 0.028), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528352365765.png", record_pos=(0.156, -0.113), resolution=(1920, 1080)), "coolp新手礼包金额显示正确，10元")
        touch(Template(r"tpl1528352402590.png", record_pos=(-0.193, -0.198), resolution=(1920, 1080)))
        wait(Template(r"tpl1528352414754.png", record_pos=(-0.003, 0.044), resolution=(1920, 1080)))
        touch(Template(r"tpl1528352425321.png", record_pos=(0.119, 0.172), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528357186822.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528357213499.png", record_pos=(-0.165, -0.132), resolution=(1920, 1080)), "baidu新手礼包金额显示正确，10元")
        touch(Template(r"tpl1528357251521.png", record_pos=(-0.439, -0.235), resolution=(1920, 1080)))
        wait(Template(r"tpl1528357262594.png", record_pos=(0.004, -0.007), resolution=(1920, 1080)))
        touch(Template(r"tpl1528357269382.png", record_pos=(0.116, 0.076), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528358117101.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.004, -0.006), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528358131080.png", record_pos=(0.156, -0.109), resolution=(1920, 1080)), "oppo新手礼包金额显示正确，10元")
        touch(Template(r"tpl1528279468542.png", record_pos=(0.216, -0.164), resolution=(1920, 1080)))
        wait(Template(r"tpl1528279514095.png", record_pos=(-0.007, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1528279543219.png", record_pos=(0.111, 0.061), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528359599336.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.009, -0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528359614504.png", record_pos=(-0.013, -0.032), resolution=(1920, 1080)), "yunos新手礼包金额显示正确，10元")
        touch(Template(r"tpl1528338654956.png", record_pos=(0.195, -0.164), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528359708922.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, 0.002), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528359727927.png", record_pos=(-0.261, -0.079), resolution=(1920, 1080)), "sdk360新手礼包金额显示正确，10元")
        touch(Template(r"tpl1528337290755.png", record_pos=(0.364, -0.155), resolution=(1920, 1080)))
        wait(Template(r"tpl1528337304258.png", record_pos=(0.004, 0.005), resolution=(1920, 1080)))
        touch(Template(r"tpl1528337318791.png", record_pos=(-0.116, 0.093), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528361195991.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.007, -0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528361218492.png", record_pos=(-0.295, -0.144), resolution=(1920, 1080)), "sdk4399新手礼包金额显示正确，10元")
        touch(Template(r"tpl1528339611657.png", record_pos=(0.309, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1528339624794.png", record_pos=(0.004, 0.04), resolution=(1920, 1080)))
        touch(Template(r"tpl1528339631035.png", record_pos=(-0.004, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529410531577.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.011, -0.02), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529411163720.png", record_pos=(-0.306, -0.034), resolution=(1920, 1080)), "anzhi新手礼包金额显示正确，10元")
        touch(Template(r"tpl1528342595576.png", record_pos=(0.455, -0.77), resolution=(1080, 1920)))
        wait(Template(r"tpl1528342607756.png", record_pos=(0.001, 0.044), resolution=(1080, 1920)))
        touch(Template(r"tpl1528342651218.png", record_pos=(0.18, 0.176), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1531304369614.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.006, -0.01), resolution=(1920, 1080))):
        touch(Template(r"tpl1528341540841.png", record_pos=(-0.109, 0.114), resolution=(1920, 1080)))
        wait(Template(r"tpl1531304127209.png", record_pos=(-0.009, -0.003), resolution=(1920, 1080)))
        assert_exists(Template(r"tpl1531304151408.png", record_pos=(0.016, -0.134), resolution=(1920, 1080)),"meizu新手礼包金额显示正确，10元")
        touch(Template(r"tpl1531304185713.png", record_pos=(0.258, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1531304197469.png", record_pos=(0.002, 0.018), resolution=(1920, 1080)))
        touch(Template(r"tpl1531304204906.png", record_pos=(0.237, 0.054), resolution=(1920, 1080)))

        # wait(Template(r"tpl1528362137533.png", record_pos=(-0.002, -0.006), resolution=(1920, 1080)))
        # assert_exists(Template(r"tpl1528362148436.png", record_pos=(-0.067, 0.161), resolution=(1920, 1080)), "meizu新手礼包金额显示正确，10元")
        # touch(Template(r"tpl1528341614588.png", record_pos=(0.249, -0.244), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528362838520.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, 0.003), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528362874540.png", record_pos=(0.17, -0.058), resolution=(1920, 1080)), "gionee新手礼包金额显示正确，10元")
        touch(Template(r"tpl1528350858743.png", record_pos=(0.176, -0.132), resolution=(1920, 1080)))
        wait(Template(r"tpl1528349942281.png", record_pos=(0.0, -0.007), resolution=(1920, 1080)))
        touch(Template(r"tpl1528349953734.png", record_pos=(-0.109, 0.047), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529407343123.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.044), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529407424909.png", record_pos=(-0.294, 0.018), resolution=(1920, 1080)),"lenove新手礼包金额显示正确，10元")
        touch(Template(r"tpl1529407486112.png", record_pos=(-0.463, -0.203), resolution=(1920, 1080)))
        wait(Template(r"tpl1529407497081.png", record_pos=(-0.007, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1529407506651.png", record_pos=(0.12, 0.108), resolution=(1920, 1080)))    
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
    sleep(3)
    wait(Template(r"tpl1527571911168.png", record_pos=(0.368, -0.159), resolution=(1920, 1080)))
    touch(Template(r"tpl1527571911168.png", record_pos=(0.368, -0.159), resolution=(1920, 1080)))
    sleep(5)

def ThirtyCoin_Mobile():

    assert_equal(poco(text="￥0.3").get_text(), "￥0.3", "一泳圈金额显示正确，0.3元.")
    touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
    wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))

    # if exists(Template(r"tpl1527670496380.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.223, -0.148), resolution=(1920, 1080))):
    #     assert_exists(Template(r"tpl1527670496380.png", record_pos=(0.223, -0.148), resolution=(1920, 1080)),"一泳圈金额显示正确，0.3元")
    #     touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
    #     wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    #     touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    # if exists(Template(r"tpl1527670825397.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.161, -0.16), resolution=(1920, 1080))):
    #     assert_exists(Template(r"tpl1527670825397.png", record_pos=(0.161, -0.16), resolution=(1920, 1080)),"一泳圈金额显示正确，0.28元")
    # 
    #     touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
    #     wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    #     touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    sleep(5)

def ThirtyCoin__Audit_Mobile():
    if exists(Template(r"tpl1528334623292.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.032), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528334645093.png", record_pos=(-0.005, -0.095), resolution=(1920, 1080)), "一泳圈金额显示正确，30元")
        touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529566269856.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, -0.153), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528276089853.png", record_pos=(0.189, -0.11), resolution=(1920, 1080)), "一泳圈金额显示正确，30元")
        touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    sleep(3)
    
def ThirtyCoin_Telecom():
    if exists(Template(r"tpl1528276151208.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.019), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528364765185.png", record_pos=(0.188, -0.106), resolution=(1920, 1080)), "一泳圈金额显示正确，30元")
        touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    if exists(Template(r"tpl1528364849810.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, -0.007), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528364863055.png", record_pos=(0.118, -0.086), resolution=(1920, 1080)), "一泳圈金额显示正确，30元")
        touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    sleep(5)

def ThirtyCoin_Unicom():
    if exists(Template(r"tpl1528353069920.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.01), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528353085406.png", record_pos=(0.215, -0.037), resolution=(1920, 1080)), "一泳圈金额显示正确，30元")
        touch(Template(r"tpl1528353109328.png", record_pos=(-0.251, -0.153), resolution=(1920, 1080)))
        wait(Template(r"tpl1528353121109.png", record_pos=(-0.002, 0.002), resolution=(1920, 1080)))
        touch(Template(r"tpl1528353130690.png", record_pos=(-0.149, 0.054), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1531224719217.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.008, -0.019), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528353085406.png", record_pos=(0.215, -0.037), resolution=(1920, 1080)), "一泳圈金额显示正确，30元")
        touch(Template(r"tpl1528353109328.png", record_pos=(-0.251, -0.153), resolution=(1920, 1080)))
        wait(Template(r"tpl1528353121109.png", record_pos=(-0.002, 0.002), resolution=(1920, 1080)))
        touch(Template(r"tpl1528353130690.png", record_pos=(-0.149, 0.054), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    sleep(5)

def TwelveCoin_Mobile():
    assert_equal(poco(text="￥0.2").get_text(), "￥0.2", "一泳圈金额显示正确，0.2元.")
    touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
    wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))

    # if exists(Template(r"tpl1529397907669.png", record_pos=(0.22, -0.133), resolution=(1920, 1080))):
    #     assert_exists(Template(r"tpl1529397907669.png", record_pos=(0.22, -0.133), resolution=(1920, 1080)),"一桶金币金额显示正确，0.2元")
    #     touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
    #     wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    #     touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    # elif exists(Template(r"tpl1527671030809.png", record_pos=(0.163, -0.161), resolution=(1920, 1080))):
    #     assert_exists(Template(r"tpl1527671030809.png", record_pos=(0.163, -0.161), resolution=(1920, 1080)),"一桶金币金额显示正确，0.19元")
    #     touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
    #     wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    #     touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))

    sleep(5)

def TwelveCoin_Audit_Mobile():
    if exists(Template(r"tpl1528334743884.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, 0.018), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528334781435.png", record_pos=(0.002, -0.095), resolution=(1920, 1080)), "一桶金币金额显示正确，12元")
        touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529566300789.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, -0.153), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528276169059.png", record_pos=(0.189, -0.108), resolution=(1920, 1080)), "一桶金币金额显示正确，12元")
        touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    sleep(3)

def TwelveCoin_Telecom():
    if exists(Template(r"tpl1528276151208.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.019), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528364725960.png", record_pos=(0.181, -0.111), resolution=(1920, 1080)), "一桶金币金额显示正确，12元")
        touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    if exists(Template(r"tpl1528364802466.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.009), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528364816813.png", record_pos=(0.127, -0.079), resolution=(1920, 1080)), "一桶金币金额显示正确，12元")
        touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    sleep(5)

def TwelveCoin_Unicom():
    if exists(Template(r"tpl1528353227153.png", threshold=0.9000000000000001, target_pos=5, rgb=False, record_pos=(-0.007, -0.014), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528353244100.png", record_pos=(0.223, -0.035), resolution=(1920, 1080)), "一桶金币金额显示正确，12元")
        touch(Template(r"tpl1528353109328.png", record_pos=(-0.251, -0.153), resolution=(1920, 1080)))
        wait(Template(r"tpl1528353121109.png", record_pos=(-0.002, 0.002), resolution=(1920, 1080)))
        touch(Template(r"tpl1528353130690.png", record_pos=(-0.149, 0.054), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1531219755389.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.004, -0.019), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528353244100.png", record_pos=(0.223, -0.035), resolution=(1920, 1080)), "一桶金币金额显示正确，12元")
        touch(Template(r"tpl1528353109328.png", record_pos=(-0.251, -0.153), resolution=(1920, 1080)))
        wait(Template(r"tpl1528353121109.png", record_pos=(-0.002, 0.002), resolution=(1920, 1080)))
        touch(Template(r"tpl1528353130690.png", record_pos=(-0.149, 0.054), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    sleep(5)

def sixCoin_Mobile():
    assert_equal(poco(text="￥1.0").get_text(), "￥1.0", "一泳圈金额显示正确，1.0元.")
    touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
    wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))

    # if exists(Template(r"tpl1529398027902.png", record_pos=(0.223, -0.132), resolution=(1920, 1080))):
    #         assert_exists(Template(r"tpl1529398027902.png", record_pos=(0.223, -0.132), resolution=(1920, 1080)),"几枚金币支付金额显示正确，1.0元")
    #         touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
    #         wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    #         touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    # elif exists(Template(r"tpl1527671191480.png", record_pos=(0.161, -0.16), resolution=(1920, 1080))):
    #         assert_exists(Template(r"tpl1527671191480.png", record_pos=(0.161, -0.16), resolution=(1920, 1080)),"几枚金币支付金额显示正确，0.95元")
    #         touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
    #         wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    #         touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    sleep(5)

def sixCoin_Audit_Mobile():
    if exists(Template(r"tpl1528334848030.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, 0.044), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528334865026.png", record_pos=(0.0, -0.093), resolution=(1920, 1080)), "几枚金币支付金额显示正确，6元")
        touch(Template(r"tpl1528334905061.png", record_pos=(-0.218, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529566322892.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, -0.151), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528337632846.png", record_pos=(0.211, -0.109), resolution=(1920, 1080)), "几枚金币支付金额显示正确，6元")
        touch(Template(r"tpl1527670554980.png", record_pos=(-0.229, -0.156), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    sleep(3)

def sixCoin_Telecom():
    if exists(Template(r"tpl1528364521719.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, -0.014), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528364541225.png", record_pos=(0.193, -0.109), resolution=(1920, 1080)), "几枚金币支付金额显示正确，6元")
        touch(Template(r"tpl1528337164420.png", record_pos=(-0.227, -0.113), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528364577293.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528364591707.png", record_pos=(0.12, -0.088), resolution=(1920, 1080)), "几枚金币支付金额显示正确，6元")
        touch(Template(r"tpl1528337164420.png", record_pos=(-0.227, -0.113), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    sleep(5)

def sixCoin_Unicom():
    if exists(Template(r"tpl1528353293069.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.007, -0.011), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528353309346.png", record_pos=(0.221, -0.041), resolution=(1920, 1080)), "几枚金币支付金额显示正确，6元")
        touch(Template(r"tpl1528353109328.png", record_pos=(-0.251, -0.153), resolution=(1920, 1080)))
        wait(Template(r"tpl1528353121109.png", record_pos=(-0.002, 0.002), resolution=(1920, 1080)))
        touch(Template(r"tpl1528353130690.png", record_pos=(-0.149, 0.054), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1531218963878.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.005, -0.015), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528353309346.png", record_pos=(0.221, -0.041), resolution=(1920, 1080)), "几枚金币支付金额显示正确，6元")
        touch(Template(r"tpl1528353109328.png", record_pos=(-0.251, -0.153), resolution=(1920, 1080)))
        wait(Template(r"tpl1528353121109.png", record_pos=(-0.002, 0.002), resolution=(1920, 1080)))
        touch(Template(r"tpl1528353130690.png", record_pos=(-0.149, 0.054), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    sleep(5)

def TwentyGiftBag_Mobile():
    assert_equal(poco(text="￥0.01").get_text(), "￥0.01", "小小金币0.01元.")
    touch(Template(r"tpl1527669397124.png", record_pos=(-0.23, -0.169), resolution=(1920, 1080)))
    wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    # if exists(Template(r"tpl1527669327566.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.145, -0.16), resolution=(1920, 1080))):
    #         assert_exists(Template(r"tpl1527669327566.png", record_pos=(0.145, -0.16), resolution=(1920, 1080)),"小小金币金额显示正确，0元")
    #         touch(Template(r"tpl1527669397124.png", record_pos=(-0.23, -0.169), resolution=(1920, 1080)))
    #         wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    #         touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    sleep(5)

def TwentyGiftBag_Audit_Mobile():
    if exists(Template(r"tpl1528335215908.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, 0.031), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528335228751.png", record_pos=(0.0, -0.093), resolution=(1920, 1080)), "小小金币金额显示正确，20元")
        touch(Template(r"tpl1528334905061.png", record_pos=(-0.218, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529566368255.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, -0.152), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529563224762.png", record_pos=(0.193, -0.11), resolution=(1920, 1080)), "小小金币金额显示正确，20元")
        touch(Template(r"tpl1528337164420.png", record_pos=(-0.227, -0.113), resolution=(1920, 1080)))

        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))

    sleep(3)
    
def TwentyGiftBag_Telecom():
    if exists(Template(r"tpl1528364379823.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, -0.014), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528364396511.png", record_pos=(0.109, -0.091), resolution=(1920, 1080)), "小小金币金额显示正确，20元")
        touch(Template(r"tpl1528337164420.png", record_pos=(-0.227, -0.113), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528364435657.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.013), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528364452736.png", record_pos=(0.186, -0.107), resolution=(1920, 1080)), "小小金币金额显示正确，20元")
        touch(Template(r"tpl1528337164420.png", record_pos=(-0.227, -0.113), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    sleep(5)

def TwentyGiftBag_Unicom():
    if exists(Template(r"tpl1528353389199.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, -0.019), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528353457364.png", record_pos=(0.22, -0.042), resolution=(1920, 1080)), "小小金币金额显示正确，20元")
        touch(Template(r"tpl1528353109328.png", record_pos=(-0.251, -0.153), resolution=(1920, 1080)))
        wait(Template(r"tpl1528353121109.png", record_pos=(-0.002, 0.002), resolution=(1920, 1080)))
        touch(Template(r"tpl1528353130690.png", record_pos=(-0.149, 0.054), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1531219027480.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.007, -0.006), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528353457364.png", record_pos=(0.22, -0.042), resolution=(1920, 1080)), "小小金币金额显示正确，20元")
        touch(Template(r"tpl1528353109328.png", record_pos=(-0.251, -0.153), resolution=(1920, 1080)))
        wait(Template(r"tpl1528353121109.png", record_pos=(-0.002, 0.002), resolution=(1920, 1080)))
        touch(Template(r"tpl1528353130690.png", record_pos=(-0.149, 0.054), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    sleep(5)

def TenGiftBag_Mobile():
    assert_equal(poco(text="￥0.02").get_text(), "￥0.02", "特惠礼包0.02元.")
    touch(Template(r"tpl1527669397124.png", record_pos=(-0.23, -0.169), resolution=(1920, 1080)))
    wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))

    # if exists(Template(r"tpl1527671522404.png", record_pos=(0.148, -0.161), resolution=(1920, 1080))):
    #     assert_exists(Template(r"tpl1527671522404.png", record_pos=(0.148, -0.161), resolution=(1920, 1080)),"特惠礼包金额显示正确，0.01元")
    #     touch(Template(r"tpl1527669397124.png", record_pos=(-0.23, -0.169), resolution=(1920, 1080)))
    #     wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    #     touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    sleep(2)
    wait(Template(r"tpl1527580857016.png", record_pos=(0.458, -0.241), resolution=(1920, 1080)))
    touch(Template(r"tpl1527580857016.png", record_pos=(0.458, -0.241), resolution=(1920, 1080)))
    sleep(5)

def TenGiftBag_Audit_Mobile():
    if exists(Template(r"tpl1528335171508.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.028), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528335186497.png", record_pos=(0.002, -0.095), resolution=(1920, 1080)), "特惠礼包金额显示正确，10元")
        touch(Template(r"tpl1528334905061.png", record_pos=(-0.218, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529566394869.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, -0.152), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528337128164.png", record_pos=(0.19, -0.107), resolution=(1920, 1080)), "特惠礼包金额显示正确，10元")
        touch(Template(r"tpl1528337164420.png", record_pos=(-0.227, -0.113), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    sleep(3)

    wait(Template(r"tpl1527580857016.png", record_pos=(0.458, -0.241), resolution=(1920, 1080)))
    touch(Template(r"tpl1527580857016.png", record_pos=(0.458, -0.241), resolution=(1920, 1080)))
    sleep(5)

def TenGiftBag_Telecom():
    if exists(Template(r"tpl1528338088320.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.009), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528337128164.png", record_pos=(0.19, -0.107), resolution=(1920, 1080)), "特惠礼包金额显示正确，10元")
        touch(Template(r"tpl1528337164420.png", record_pos=(-0.227, -0.113), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528364246951.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528364264112.png", record_pos=(0.123, -0.088), resolution=(1920, 1080)), "特惠礼包金额显示正确，10元")
        touch(Template(r"tpl1528337164420.png", record_pos=(-0.227, -0.113), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    sleep(3)
    wait(Template(r"tpl1527580857016.png", record_pos=(0.458, -0.241), resolution=(1920, 1080)))
    touch(Template(r"tpl1527580857016.png", record_pos=(0.458, -0.241), resolution=(1920, 1080)))
    sleep(5)

def TenGiftBag_Unicom():
    if exists(Template(r"tpl1528353507033.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.007), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528353525496.png", record_pos=(0.215, -0.039), resolution=(1920, 1080)), "特惠礼包金额显示正确，10元")
        touch(Template(r"tpl1528353109328.png", record_pos=(-0.251, -0.153), resolution=(1920, 1080)))
        wait(Template(r"tpl1528353121109.png", record_pos=(-0.002, 0.002), resolution=(1920, 1080)))
        touch(Template(r"tpl1528353130690.png", record_pos=(-0.149, 0.054), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1531219197100.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.011, -0.01), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528353525496.png", record_pos=(0.215, -0.039), resolution=(1920, 1080)), "特惠礼包金额显示正确，10元")
        touch(Template(r"tpl1528353109328.png", record_pos=(-0.251, -0.153), resolution=(1920, 1080)))
        wait(Template(r"tpl1528353121109.png", record_pos=(-0.002, 0.002), resolution=(1920, 1080)))
        touch(Template(r"tpl1528353130690.png", record_pos=(-0.149, 0.054), resolution=(1920, 1080)))
        wait(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
        touch(Template(r"tpl1527670587769.png", record_pos=(-0.002, 0.037), resolution=(1920, 1080)))
    sleep(3)
    wait(Template(r"tpl1527580857016.png", record_pos=(0.458, -0.241), resolution=(1920, 1080)))
    touch(Template(r"tpl1527580857016.png", record_pos=(0.458, -0.241), resolution=(1920, 1080)))
    sleep(5)

def ThreeHundredTwentyEightCoin_Founction():
    if exists(Template(r"tpl1528279387136.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.009, 0.012), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528279402891.png", record_pos=(0.131, -0.091), resolution=(1920, 1080)), "oppo.apk---一大泳池的金币金额显示正确，328元")
        touch(Template(r"tpl1528279468542.png", record_pos=(0.216, -0.164), resolution=(1920, 1080)))
        wait(Template(r"tpl1528279514095.png", record_pos=(-0.007, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1528279543219.png", record_pos=(0.111, 0.061), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528337237227.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.0), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528337257868.png", record_pos=(-0.249, -0.076), resolution=(1920, 1080)), "sdk360.apk一大泳池的金币金额显示正确，328元")
        touch(Template(r"tpl1528337290755.png", record_pos=(0.364, -0.155), resolution=(1920, 1080)))
        wait(Template(r"tpl1528337304258.png", record_pos=(0.004, 0.005), resolution=(1920, 1080)))
        touch(Template(r"tpl1528337318791.png", record_pos=(-0.116, 0.093), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528338603697.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528338622308.png", record_pos=(0.013, -0.032), resolution=(1920, 1080)), "yunos大泳池的金币金额显示正确，328元")
        touch(Template(r"tpl1528338654956.png", record_pos=(0.195, -0.164), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528339551136.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, -0.007), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528339568813.png", record_pos=(-0.283, -0.144), resolution=(1920, 1080)), "sdk4399大泳池的金币金额显示正确，328元")
        touch(Template(r"tpl1528339611657.png", record_pos=(0.309, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1528339624794.png", record_pos=(0.004, 0.04), resolution=(1920, 1080)))
        touch(Template(r"tpl1528339631035.png", record_pos=(-0.004, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528340473556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.005, -0.007), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528340523284.png", record_pos=(-0.176, -0.127), resolution=(1920, 1080)), "baidu大泳池的金币金额显示正确，328元")
        touch(Template(r"tpl1528340586329.png", record_pos=(-0.443, -0.235), resolution=(1920, 1080)))
        wait(Template(r"tpl1528340598861.png", record_pos=(0.004, 0.0), resolution=(1920, 1080)))
        touch(Template(r"tpl1528340611458.png", record_pos=(0.116, 0.073), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529563881253.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.008), resolution=(1920, 1080))):
        touch(Template(r"tpl1528341540841.png", record_pos=(-0.109, 0.114), resolution=(1920, 1080)))
        wait(Template(r"tpl1529562665510.png", record_pos=(0.0, -0.003), resolution=(1920, 1080)))
        assert_exists(Template(r"tpl1529562674421.png", record_pos=(0.016, -0.135), resolution=(1920, 1080)),"meizu大泳池的金币金额显示正确，328元")
        touch(Template(r"tpl1529562707187.png", record_pos=(0.253, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1529562717171.png", record_pos=(-0.001, 0.017), resolution=(1920, 1080)))
        touch(Template(r"tpl1529562724386.png", record_pos=(0.23, 0.053), resolution=(1920, 1080)))
        # wait(Template(r"tpl1528341556788.png", record_pos=(-0.004, -0.007), resolution=(1920, 1080)))
        # assert_exists(Template(r"tpl1528341573793.png", record_pos=(-0.072, 0.165), resolution=(1920, 1080)), "meizu大泳池的金币金额显示正确，328元")
        # touch(Template(r"tpl1528341614588.png", record_pos=(0.249, -0.244), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529410575553.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.009, -0.018), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529464332407.png", record_pos=(-0.287, -0.032), resolution=(1920, 1080)), "anzhi大泳池的金币金额显示正确，328元")
        touch(Template(r"tpl1528342595576.png", record_pos=(0.455, -0.77), resolution=(1080, 1920)))
        wait(Template(r"tpl1528342607756.png", record_pos=(0.001, 0.044), resolution=(1080, 1920)))
        touch(Template(r"tpl1528342651218.png", record_pos=(0.18, 0.176), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528349839895.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.002), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528349860106.png", record_pos=(0.162, -0.061), resolution=(1920, 1080)), "gionee大泳池的金币金额显示正确，328元")
        touch(Template(r"tpl1528350858743.png", record_pos=(0.176, -0.132), resolution=(1920, 1080)))
        wait(Template(r"tpl1528349942281.png", record_pos=(0.0, -0.007), resolution=(1920, 1080)))
        touch(Template(r"tpl1528349953734.png", record_pos=(-0.109, 0.047), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528352477457.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.024), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528352500612.png", record_pos=(0.146, -0.114), resolution=(1920, 1080)), "coolp大泳池的金币金额显示正确，328元")
        touch(Template(r"tpl1528352402590.png", record_pos=(-0.193, -0.198), resolution=(1920, 1080)))
        wait(Template(r"tpl1528352414754.png", record_pos=(-0.003, 0.044), resolution=(1920, 1080)))
        touch(Template(r"tpl1528352425321.png", record_pos=(0.119, 0.172), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529407343123.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.044), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529407424909.png", record_pos=(-0.294, 0.018), resolution=(1920, 1080)),"lenove大泳池的金币金额显示正确，328元")
        touch(Template(r"tpl1529407486112.png", record_pos=(-0.463, -0.203), resolution=(1920, 1080)))
        wait(Template(r"tpl1529407497081.png", record_pos=(-0.007, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1529407506651.png", record_pos=(0.12, 0.108), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "328.00元", "vivo大泳池的金币金额显示正确，328元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥328.00", "huawei大泳池的金币金额显示正确，328元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "328.00元", "xiaomi大泳池的金币金额显示正确，328元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
        , "328.00", "sumsung大泳池的金币金额显示正确，328元.")   

        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))

    sleep(5)

def OneHundredTwentyEightCoin_Founction():
    if exists(Template(r"tpl1528334236613.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, 0.009), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528334261424.png", record_pos=(0.139, -0.088), resolution=(1920, 1080)), "oppo.apk一儿童泳池的金币金额显示正确，128元")
        touch(Template(r"tpl1528334372647.png", record_pos=(0.211, -0.167), resolution=(1920, 1080)))
        wait(Template(r"tpl1528334388294.png", record_pos=(-0.005, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1528334398457.png", record_pos=(0.111, 0.059), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528337370019.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.007), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528337400565.png", record_pos=(-0.249, -0.078), resolution=(1920, 1080)), "sdk360.apk一儿童泳池的金币金额显示正确，128元")
        touch(Template(r"tpl1528337290755.png", record_pos=(0.364, -0.155), resolution=(1920, 1080)))
        wait(Template(r"tpl1528337304258.png", record_pos=(0.004, 0.005), resolution=(1920, 1080)))
        touch(Template(r"tpl1528337318791.png", record_pos=(-0.116, 0.093), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528339067390.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.007, 0.002), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528339084391.png", record_pos=(0.002, -0.03), resolution=(1920, 1080)), "yunos儿童泳池的金币金额显示正确，128元")
        touch(Template(r"tpl1528338654956.png", record_pos=(0.195, -0.164), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528340047685.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.005), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528340062792.png", record_pos=(-0.29, -0.144), resolution=(1920, 1080)), "sdk4399儿童泳池的金币金额显示正确，128元")
        touch(Template(r"tpl1528339611657.png", record_pos=(0.309, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1528339624794.png", record_pos=(0.004, 0.04), resolution=(1920, 1080)))
        touch(Template(r"tpl1528339631035.png", record_pos=(-0.004, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528340998524.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.004, -0.005), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528341017618.png", record_pos=(-0.172, -0.128), resolution=(1920, 1080)), "baidu儿童泳池的金币金额显示正确，128元")
        touch(Template(r"tpl1528340586329.png", record_pos=(-0.443, -0.235), resolution=(1920, 1080)))
        wait(Template(r"tpl1528340598861.png", record_pos=(0.004, 0.0), resolution=(1920, 1080)))
        touch(Template(r"tpl1528340611458.png", record_pos=(0.116, 0.073), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529563881253.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.008), resolution=(1920, 1080))):
        touch(Template(r"tpl1528341540841.png", record_pos=(-0.109, 0.114), resolution=(1920, 1080)))
        wait(Template(r"tpl1529562786086.png", record_pos=(0.004, -0.002), resolution=(1920, 1080)))
        assert_exists(Template(r"tpl1529562800936.png", record_pos=(0.022, -0.134), resolution=(1920, 1080)),"meizu儿童泳池的金币金额显示正确，128元")
        touch(Template(r"tpl1529562707187.png", record_pos=(0.253, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1529562717171.png", record_pos=(-0.001, 0.017), resolution=(1920, 1080)))
        touch(Template(r"tpl1529562724386.png", record_pos=(0.23, 0.053), resolution=(1920, 1080)))

        # wait(Template(r"tpl1528341951676.png", record_pos=(0.0, -0.005), resolution=(1920, 1080)))
        # assert_exists(Template(r"tpl1528341963463.png", record_pos=(-0.068, 0.165), resolution=(1920, 1080)), "meizu儿童泳池的金币金额显示正确，128元")
        # touch(Template(r"tpl1528341614588.png", record_pos=(0.249, -0.244), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529410607338.png", threshold=0.95, target_pos=5, rgb=False, record_pos=(-0.003, -0.022), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529464358235.png", record_pos=(-0.3, -0.03), resolution=(1920, 1080)),"anzhi儿童泳池的金币金额显示正确，128元")
        touch(Template(r"tpl1528342595576.png", record_pos=(0.455, -0.77), resolution=(1080, 1920)))
        wait(Template(r"tpl1528342607756.png", record_pos=(0.001, 0.044), resolution=(1080, 1920)))
        touch(Template(r"tpl1528342651218.png", record_pos=(0.18, 0.176), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528350394532.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, 0.002), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528350413733.png", record_pos=(0.162, -0.058), resolution=(1920, 1080)), "gionee儿童泳池的金币金额显示正确，128元")
        touch(Template(r"tpl1528349926682.png", record_pos=(0.176, -0.139), resolution=(1920, 1080)))
        wait(Template(r"tpl1528349942281.png", record_pos=(0.0, -0.007), resolution=(1920, 1080)))
        touch(Template(r"tpl1528349953734.png", record_pos=(-0.109, 0.047), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528352617477.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.021), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528352632267.png", record_pos=(0.153, -0.115), resolution=(1920, 1080)), "coolp儿童泳池的金币金额显示正确，128元")
        touch(Template(r"tpl1528352402590.png", record_pos=(-0.193, -0.198), resolution=(1920, 1080)))
        wait(Template(r"tpl1528352414754.png", record_pos=(-0.003, 0.044), resolution=(1920, 1080)))
        touch(Template(r"tpl1528352425321.png", record_pos=(0.119, 0.172), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529407864521.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.034), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529407877000.png", record_pos=(-0.289, 0.02), resolution=(1920, 1080)),"lenove儿童泳池的金币金额显示正确，128元")
        touch(Template(r"tpl1529407486112.png", record_pos=(-0.463, -0.203), resolution=(1920, 1080)))
        wait(Template(r"tpl1529407497081.png", record_pos=(-0.007, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1529407506651.png", record_pos=(0.12, 0.108), resolution=(1920, 1080)))   
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "128.00元", "vivo儿童泳池的金币金额显示正确，128元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥128.00", "huawei儿童泳池的金币金额显示正确，128元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "128.00元", "xiaomi儿童泳池的金币金额显示正确，128元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "128.00", "sumsung儿童泳池的金币金额显示正确，128元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))

    sleep(3)

def NintyEightCoin_Founction():
    if exists(Template(r"tpl1528334459793.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, 0.0), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528334478379.png", record_pos=(0.146, -0.088), resolution=(1920, 1080)), "oppo.apk一浴缸的金币金额显示正确，98元")
        touch(Template(r"tpl1528334519875.png", record_pos=(0.214, -0.162), resolution=(1920, 1080)))
        wait(Template(r"tpl1528334388294.png", record_pos=(-0.005, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1528334398457.png", record_pos=(0.111, 0.059), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528337477213.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, 0.002), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528337494646.png", record_pos=(-0.265, -0.07), resolution=(1920, 1080)), "sdk浴缸的金币金额显示正确，98元")
        touch(Template(r"tpl1528337290755.png", record_pos=(0.364, -0.155), resolution=(1920, 1080)))
        wait(Template(r"tpl1528337304258.png", record_pos=(0.004, 0.005), resolution=(1920, 1080)))
        touch(Template(r"tpl1528337318791.png", record_pos=(-0.116, 0.093), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528339010499.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.005, -0.007), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528339026610.png", record_pos=(-0.002, -0.035), resolution=(1920, 1080)), "yunos浴缸的金币金额显示正确，98元")
        touch(Template(r"tpl1528338654956.png", record_pos=(0.195, -0.164), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528339991402.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, 0.002), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528340006663.png", record_pos=(-0.298, -0.148), resolution=(1920, 1080)), "sdk4399浴缸的金币金额显示正确，98元")
        touch(Template(r"tpl1528339611657.png", record_pos=(0.309, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1528339624794.png", record_pos=(0.004, 0.04), resolution=(1920, 1080)))
        touch(Template(r"tpl1528339631035.png", record_pos=(-0.004, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528340937839.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, -0.009), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528340954926.png", record_pos=(-0.167, -0.127), resolution=(1920, 1080)), "baidu浴缸的金币金额显示正确，98元")
        touch(Template(r"tpl1528340586329.png", record_pos=(-0.443, -0.235), resolution=(1920, 1080)))
        wait(Template(r"tpl1528340598861.png", record_pos=(0.004, 0.0), resolution=(1920, 1080)))
        touch(Template(r"tpl1528340611458.png", record_pos=(0.116, 0.073), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529563881253.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.008), resolution=(1920, 1080))):
        touch(Template(r"tpl1528341540841.png", record_pos=(-0.109, 0.114), resolution=(1920, 1080)))
        wait(Template(r"tpl1529562893169.png", record_pos=(0.001, -0.003), resolution=(1920, 1080)))
        assert_exists(Template(r"tpl1529562902791.png", record_pos=(0.023, -0.133), resolution=(1920, 1080)),"meizu浴缸的金币金额显示正确，98元")
        touch(Template(r"tpl1529562707187.png", record_pos=(0.253, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1529562717171.png", record_pos=(-0.001, 0.017), resolution=(1920, 1080)))
        touch(Template(r"tpl1529562724386.png", record_pos=(0.23, 0.053), resolution=(1920, 1080)))
        # wait(Template(r"tpl1528341881051.png", record_pos=(-0.008, -0.009), resolution=(1920, 1080)))
        # assert_exists(Template(r"tpl1528341903192.png", record_pos=(-0.068, 0.158), resolution=(1920, 1080)), "meizu浴缸的金币金额显示正确，98元")
        # touch(Template(r"tpl1528341614588.png", record_pos=(0.249, -0.244), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529410638635.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, -0.026), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529464179270.png", record_pos=(-0.304, -0.031), resolution=(1920, 1080)), "anzhi浴缸的金币金额显示正确，98元")
        touch(Template(r"tpl1528342595576.png", record_pos=(0.455, -0.77), resolution=(1080, 1920)))
        wait(Template(r"tpl1528342607756.png", record_pos=(0.001, 0.044), resolution=(1080, 1920)))
        touch(Template(r"tpl1528342651218.png", record_pos=(0.18, 0.176), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528350335184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, -0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528350353124.png", record_pos=(0.169, -0.056), resolution=(1920, 1080)), "gionee浴缸的金币金额显示正确，98元")
        touch(Template(r"tpl1528349926682.png", record_pos=(0.176, -0.139), resolution=(1920, 1080)))
        wait(Template(r"tpl1528349942281.png", record_pos=(0.0, -0.007), resolution=(1920, 1080)))
        touch(Template(r"tpl1528349953734.png", record_pos=(-0.109, 0.047), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528352674249.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, 0.023), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528352691415.png", record_pos=(0.158, -0.111), resolution=(1920, 1080)), "coolp浴缸的金币金额显示正确，98元")
        touch(Template(r"tpl1528352402590.png", record_pos=(-0.193, -0.198), resolution=(1920, 1080)))
        wait(Template(r"tpl1528352414754.png", record_pos=(-0.003, 0.044), resolution=(1920, 1080)))
        touch(Template(r"tpl1528352425321.png", record_pos=(0.119, 0.172), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529407792978.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.041), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529407807904.png", record_pos=(-0.301, 0.015), resolution=(1920, 1080)),"lenove浴缸的金币金额显示正确，98元")
        touch(Template(r"tpl1529407486112.png", record_pos=(-0.463, -0.203), resolution=(1920, 1080)))
        wait(Template(r"tpl1529407497081.png", record_pos=(-0.007, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1529407506651.png", record_pos=(0.12, 0.108), resolution=(1920, 1080)))    
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "98.00元", "vivo浴缸的金币金额显示正确，98元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥98.00", "huawei浴缸的金币金额显示正确，98元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "98.00元", "xiaomi浴缸的金币金额显示正确，98元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "98.00", "sumsung浴缸的金币金额显示正确，98元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))

    sleep(3)

def FiftyGiftBag_Founction():
    if exists(Template(r"tpl1528335501067.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.002), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528335520283.png", record_pos=(0.144, -0.091), resolution=(1920, 1080)), "oppo.apk一优惠礼包金额显示正确，50元")
        touch(Template(r"tpl1528334519875.png", record_pos=(0.214, -0.162), resolution=(1920, 1080)))
        wait(Template(r"tpl1528334388294.png", record_pos=(-0.005, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1528334398457.png", record_pos=(0.111, 0.059), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528337681361.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.006, -0.005), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528337704871.png", record_pos=(-0.265, -0.079), resolution=(1920, 1080)), "sdk优惠礼包金额显示正确，50元")
        touch(Template(r"tpl1528337290755.png", record_pos=(0.364, -0.155), resolution=(1920, 1080)))
        wait(Template(r"tpl1528337304258.png", record_pos=(0.004, 0.005), resolution=(1920, 1080)))
        touch(Template(r"tpl1528337318791.png", record_pos=(-0.116, 0.093), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528338936974.png", threshold=0.95, target_pos=5, rgb=False, record_pos=(0.002, -0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528338955545.png", record_pos=(-0.005, -0.032), resolution=(1920, 1080)), "yunos优惠礼包金额显示正确，50元")
        touch(Template(r"tpl1528338654956.png", record_pos=(0.195, -0.164), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528339907259.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.009), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528339923379.png", record_pos=(-0.296, -0.144), resolution=(1920, 1080)), "sdk4399优惠礼包金额显示正确，50元")
        touch(Template(r"tpl1528339611657.png", record_pos=(0.309, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1528339624794.png", record_pos=(0.004, 0.04), resolution=(1920, 1080)))
        touch(Template(r"tpl1528339631035.png", record_pos=(-0.004, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528340860970.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, -0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528340876442.png", record_pos=(-0.159, -0.125), resolution=(1920, 1080)), "baidu优惠礼包金额显示正确，50元")
        touch(Template(r"tpl1528340586329.png", record_pos=(-0.443, -0.235), resolution=(1920, 1080)))
        wait(Template(r"tpl1528340598861.png", record_pos=(0.004, 0.0), resolution=(1920, 1080)))
        touch(Template(r"tpl1528340611458.png", record_pos=(0.116, 0.073), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529563881253.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.008), resolution=(1920, 1080))):
        touch(Template(r"tpl1528341540841.png", record_pos=(-0.109, 0.114), resolution=(1920, 1080)))
        wait(Template(r"tpl1529562974982.png", record_pos=(0.006, -0.001), resolution=(1920, 1080)))
        assert_exists(Template(r"tpl1529562982263.png", record_pos=(0.016, -0.136), resolution=(1920, 1080)),"meizu优惠礼包金额显示正确，50元")
        touch(Template(r"tpl1529562707187.png", record_pos=(0.253, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1529562717171.png", record_pos=(-0.001, 0.017), resolution=(1920, 1080)))
        touch(Template(r"tpl1529562724386.png", record_pos=(0.23, 0.053), resolution=(1920, 1080)))
        # wait(Template(r"tpl1528341815726.png", record_pos=(-0.002, -0.009), resolution=(1920, 1080)))
        # assert_exists(Template(r"tpl1528341826894.png", record_pos=(-0.072, 0.163), resolution=(1920, 1080)), "meizu优惠礼包金额显示正确，50元")
        # touch(Template(r"tpl1528341614588.png", record_pos=(0.249, -0.244), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529410675825.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.013, -0.026), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529464966119.png", record_pos=(-0.304, -0.035), resolution=(1920, 1080)), "anzhi优惠礼包金额显示正确，50元")
        touch(Template(r"tpl1528342595576.png", record_pos=(0.455, -0.77), resolution=(1080, 1920)))
        wait(Template(r"tpl1528342607756.png", record_pos=(0.001, 0.044), resolution=(1080, 1920)))
        touch(Template(r"tpl1528342651218.png", record_pos=(0.18, 0.176), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528350203050.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.002), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528350224734.png", record_pos=(0.169, -0.058), resolution=(1920, 1080)), "gionee优惠礼包金额显示正确，50元")
        touch(Template(r"tpl1528349926682.png", record_pos=(0.176, -0.139), resolution=(1920, 1080)))
        wait(Template(r"tpl1528349942281.png", record_pos=(0.0, -0.007), resolution=(1920, 1080)))
        touch(Template(r"tpl1528349953734.png", record_pos=(-0.109, 0.047), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528352735646.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.023), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528352749486.png", record_pos=(0.155, -0.118), resolution=(1920, 1080)), "coolp优惠礼包金额显示正确，50元")
        touch(Template(r"tpl1528352402590.png", record_pos=(-0.193, -0.198), resolution=(1920, 1080)))
        wait(Template(r"tpl1528352414754.png", record_pos=(-0.003, 0.044), resolution=(1920, 1080)))
        touch(Template(r"tpl1528352425321.png", record_pos=(0.119, 0.172), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529407734218.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, -0.038), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529407747511.png", record_pos=(-0.292, 0.02), resolution=(1920, 1080)),"lenove优惠礼包金额显示正确，50元")
        touch(Template(r"tpl1529407486112.png", record_pos=(-0.463, -0.203), resolution=(1920, 1080)))
        wait(Template(r"tpl1529407497081.png", record_pos=(-0.007, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1529407506651.png", record_pos=(0.12, 0.108), resolution=(1920, 1080)))    
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "50.00元", "vivo优惠礼包金额显示正确，50元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥50.00", "huawei优惠礼包金额显示正确，50元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "50.00元", "xiaomi优惠礼包金额显示正确，50元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "50.00", "sumsung优惠礼包金额显示正确，50元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))

    sleep(3)

def OneHundredFourtyEightExchangeTwentyGiftBag_Founction():
    if exists(Template(r"tpl1528335424615.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528335439379.png", record_pos=(0.137, -0.086), resolution=(1920, 1080)), "oppo.apk一特价礼包金额显示正确，148元")
        touch(Template(r"tpl1528334519875.png", record_pos=(0.214, -0.162), resolution=(1920, 1080)))
        wait(Template(r"tpl1528334388294.png", record_pos=(-0.005, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1528334398457.png", record_pos=(0.111, 0.059), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528337851043.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, -0.009), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528337871189.png", record_pos=(-0.256, -0.078), resolution=(1920, 1080)), "sdk特价礼包金额显示正确，148元")
        touch(Template(r"tpl1528337290755.png", record_pos=(0.364, -0.155), resolution=(1920, 1080)))
        wait(Template(r"tpl1528337304258.png", record_pos=(0.004, 0.005), resolution=(1920, 1080)))
        touch(Template(r"tpl1528337318791.png", record_pos=(-0.116, 0.093), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528338836058.png", threshold=0.95, target_pos=5, rgb=False, record_pos=(0.01, -0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528338854391.png", record_pos=(0.002, -0.024), resolution=(1920, 1080)), "yunos特价礼包金额显示正确，148元")
        touch(Template(r"tpl1528338654956.png", record_pos=(0.195, -0.164), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528339843316.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.007), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528339864255.png", record_pos=(-0.283, -0.144), resolution=(1920, 1080)), "sdk4399特价礼包金额显示正确，148元")
        touch(Template(r"tpl1528339611657.png", record_pos=(0.309, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1528339624794.png", record_pos=(0.004, 0.04), resolution=(1920, 1080)))
        touch(Template(r"tpl1528339631035.png", record_pos=(-0.004, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528340790859.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.006), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528340806877.png", record_pos=(-0.17, -0.127), resolution=(1920, 1080)), "baidu特价礼包金额显示正确，148元")
        touch(Template(r"tpl1528340586329.png", record_pos=(-0.443, -0.235), resolution=(1920, 1080)))
        wait(Template(r"tpl1528340598861.png", record_pos=(0.004, 0.0), resolution=(1920, 1080)))
        touch(Template(r"tpl1528340611458.png", record_pos=(0.116, 0.073), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529563881253.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.008), resolution=(1920, 1080))):
        touch(Template(r"tpl1528341540841.png", record_pos=(-0.109, 0.114), resolution=(1920, 1080)))
        wait(Template(r"tpl1529563077691.png", record_pos=(0.005, 0.002), resolution=(1920, 1080)))
        assert_exists(Template(r"tpl1529563092908.png", record_pos=(0.021, -0.136), resolution=(1920, 1080)),"meizu特价礼包金额显示正确，148元")
        touch(Template(r"tpl1529562707187.png", record_pos=(0.253, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1529562717171.png", record_pos=(-0.001, 0.017), resolution=(1920, 1080)))
        touch(Template(r"tpl1529562724386.png", record_pos=(0.23, 0.053), resolution=(1920, 1080)))
        # wait(Template(r"tpl1528341758811.png", record_pos=(-0.004, -0.009), resolution=(1920, 1080)))
        # assert_exists(Template(r"tpl1528341770316.png", record_pos=(-0.07, 0.165), resolution=(1920, 1080)), "meizu特价礼包金额显示正确，148元")
        # touch(Template(r"tpl1528341614588.png", record_pos=(0.249, -0.244), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529410710105.png", threshold=0.95, target_pos=5, rgb=False, record_pos=(0.001, -0.025), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529464231705.png", record_pos=(-0.299, -0.033), resolution=(1920, 1080)), "anzhi特价礼包金额显示正确，148元")
        touch(Template(r"tpl1528342595576.png", record_pos=(0.455, -0.77), resolution=(1080, 1920)))
        wait(Template(r"tpl1528342607756.png", record_pos=(0.001, 0.044), resolution=(1080, 1920)))
        touch(Template(r"tpl1528342651218.png", record_pos=(0.18, 0.176), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528350139616.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, -0.007), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528350156250.png", record_pos=(0.164, -0.065), resolution=(1920, 1080)), "gionee特价礼包金额显示正确，148元")
        touch(Template(r"tpl1528349926682.png", record_pos=(0.176, -0.139), resolution=(1920, 1080)))
        wait(Template(r"tpl1528349942281.png", record_pos=(0.0, -0.007), resolution=(1920, 1080)))
        touch(Template(r"tpl1528349953734.png", record_pos=(-0.109, 0.047), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528352786973.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.004, 0.019), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528352802314.png", record_pos=(0.151, -0.11), resolution=(1920, 1080)), "coolp特价礼包金额显示正确，148元")
        touch(Template(r"tpl1528352402590.png", record_pos=(-0.193, -0.198), resolution=(1920, 1080)))
        wait(Template(r"tpl1528352414754.png", record_pos=(-0.003, 0.044), resolution=(1920, 1080)))
        touch(Template(r"tpl1528352425321.png", record_pos=(0.119, 0.172), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))

    elif exists(Template(r"tpl1529407657552.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, -0.035), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529407674839.png", record_pos=(-0.294, 0.019), resolution=(1920, 1080)),"lenove特价礼包金额显示正确，148元")
        touch(Template(r"tpl1529407486112.png", record_pos=(-0.463, -0.203), resolution=(1920, 1080)))
        wait(Template(r"tpl1529407497081.png", record_pos=(-0.007, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1529407506651.png", record_pos=(0.12, 0.108), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "148.00元", "vivo特价礼包金额显示正确，148元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥148.00", "huawei特价礼包金额显示正确，148元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "148.00元", "xiaomi特价礼包金额显示正确，148元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "148.00", "sumsung特价礼包金额显示正确，148元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))

    sleep(3)

def OneHundredFourtyEightExchangeTwoThousandGiftBag_Founction():
    if exists(Template(r"tpl1528335281834.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, 0.004), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528335297361.png", record_pos=(0.139, -0.088), resolution=(1920, 1080)), "oppo.apk一金币礼包金额显示正确，148元")
        touch(Template(r"tpl1528334519875.png", record_pos=(0.214, -0.162), resolution=(1920, 1080)))
        wait(Template(r"tpl1528334388294.png", record_pos=(-0.005, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1528334398457.png", record_pos=(0.111, 0.059), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528337923414.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.002, -0.009), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528337938122.png", record_pos=(-0.26, -0.079), resolution=(1920, 1080)), "sdk金币礼包金额显示正确，148元")
        touch(Template(r"tpl1528337290755.png", record_pos=(0.364, -0.155), resolution=(1920, 1080)))
        wait(Template(r"tpl1528337304258.png", record_pos=(0.004, 0.005), resolution=(1920, 1080)))
        touch(Template(r"tpl1528337318791.png", record_pos=(-0.116, 0.093), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528338759980.png", threshold=0.95, target_pos=5, rgb=False, record_pos=(0.002, 0.0), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528338775994.png", record_pos=(-0.002, -0.03), resolution=(1920, 1080)), "yunos金币礼包金额显示正确，148元")
        touch(Template(r"tpl1528338654956.png", record_pos=(0.195, -0.164), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528339737542.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.002, 0.002), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528339754570.png", record_pos=(-0.288, -0.142), resolution=(1920, 1080)), "sdk4399金币礼包金额显示正确，148元")
        touch(Template(r"tpl1528339611657.png", record_pos=(0.309, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1528339624794.png", record_pos=(0.004, 0.04), resolution=(1920, 1080)))
        touch(Template(r"tpl1528339631035.png", record_pos=(-0.004, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528340722809.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.009), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528340739682.png", record_pos=(-0.167, -0.125), resolution=(1920, 1080)), "baidu金币礼包金额显示正确，148元")
        touch(Template(r"tpl1528340586329.png", record_pos=(-0.443, -0.235), resolution=(1920, 1080)))
        wait(Template(r"tpl1528340598861.png", record_pos=(0.004, 0.0), resolution=(1920, 1080)))
        touch(Template(r"tpl1528340611458.png", record_pos=(0.116, 0.073), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529563881253.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.008), resolution=(1920, 1080))):
        touch(Template(r"tpl1528341540841.png", record_pos=(-0.109, 0.114), resolution=(1920, 1080)))
        wait(Template(r"tpl1529563157901.png", record_pos=(0.001, 0.002), resolution=(1920, 1080)))
        assert_exists(Template(r"tpl1529563092908.png", record_pos=(0.021, -0.136), resolution=(1920, 1080)),"meizu特价礼包金额显示正确，148元")
        touch(Template(r"tpl1529562707187.png", record_pos=(0.253, -0.212), resolution=(1920, 1080)))
        wait(Template(r"tpl1529562717171.png", record_pos=(-0.001, 0.017), resolution=(1920, 1080)))
        touch(Template(r"tpl1529562724386.png", record_pos=(0.23, 0.053), resolution=(1920, 1080)))
        # wait(Template(r"tpl1528341705686.png", record_pos=(0.0, -0.014), resolution=(1920, 1080)))
        # assert_exists(Template(r"tpl1528341716924.png", record_pos=(-0.073, 0.16), resolution=(1920, 1080)), "meizu金币礼包金额显示正确，148元")
        # touch(Template(r"tpl1528341614588.png", record_pos=(0.249, -0.244), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529410744498.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.001, -0.029), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529464231705.png", record_pos=(-0.299, -0.033), resolution=(1920, 1080)), "anzhi金币礼包金额显示正确，148元")
        touch(Template(r"tpl1528342595576.png", record_pos=(0.455, -0.77), resolution=(1080, 1920)))
        wait(Template(r"tpl1528342607756.png", record_pos=(0.001, 0.044), resolution=(1080, 1920)))
        touch(Template(r"tpl1528342651218.png", record_pos=(0.18, 0.176), resolution=(1080, 1920)))
    elif exists(Template(r"tpl1528350072855.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.003, -0.009), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528350094254.png", record_pos=(0.172, -0.056), resolution=(1920, 1080)), "gionee金币礼包金额显示正确，148元")
        touch(Template(r"tpl1528349926682.png", record_pos=(0.176, -0.139), resolution=(1920, 1080)))
        wait(Template(r"tpl1528349942281.png", record_pos=(0.0, -0.007), resolution=(1920, 1080)))
        touch(Template(r"tpl1528349953734.png", record_pos=(-0.109, 0.047), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1528352833581.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.0, 0.016), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1528352856097.png", record_pos=(0.144, -0.113), resolution=(1920, 1080)), "coolp金币礼包金额显示正确，148元")
        touch(Template(r"tpl1528352402590.png", record_pos=(-0.193, -0.198), resolution=(1920, 1080)))
        wait(Template(r"tpl1528352414754.png", record_pos=(-0.003, 0.044), resolution=(1920, 1080)))
        touch(Template(r"tpl1528352425321.png", record_pos=(0.119, 0.172), resolution=(1920, 1080)))
        wait(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
        touch(Template(r"tpl1527669421465.png", record_pos=(-0.001, 0.039), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1529407587930.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.005, -0.028), resolution=(1920, 1080))):
        assert_exists(Template(r"tpl1529407605946.png", record_pos=(-0.298, 0.013), resolution=(1920, 1080)),"lenove金币礼包金额显示正确，148元")
        touch(Template(r"tpl1529407486112.png", record_pos=(-0.463, -0.203), resolution=(1920, 1080)))
        wait(Template(r"tpl1529407497081.png", record_pos=(-0.007, 0.019), resolution=(1920, 1080)))
        touch(Template(r"tpl1529407506651.png", record_pos=(0.12, 0.108), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530155301952.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, 0.003), resolution=(1920, 1080))):
        touch(Template(r"tpl1530155320364.png", record_pos=(-0.155, 0.086), resolution=(1920, 1080)))
        sleep(8)
        assert_equal(poco("com.vivo.sdkplugin:id/i_").get_text(), "148.00元", "vivo金币礼包金额显示正确，148元.")
        keyevent("back")
        sleep(3)
        keyevent("back")
    elif exists(Template(r"tpl1530164858184.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.127, -0.757), resolution=(1080, 1920))):
        assert_equal(poco("com.huawei.hwid:id/b_meramount").get_text(),"¥148.00", "huawei金币礼包金额显示正确，148元.")
        touch(Template(r"tpl1530164996370.png", record_pos=(-0.421, -0.751), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165022530.png", record_pos=(-0.006, 0.532), resolution=(1080, 1920)))
        touch(Template(r"tpl1530165030342.png", record_pos=(0.222, 0.656), resolution=(1080, 1920)))
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530236317556.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.163, 0.083), resolution=(1280, 720))):
        assert_equal(poco("com.xiaomi.gamecenter.sdk.service:id/payment_title_price").get_text(), "148.00元", "xiaomi金币礼包金额显示正确，148元.")
        keyevent("back")
        wait(Template(r"tpl1530165045814.png", record_pos=(-0.035, 0.048), resolution=(1920, 1080)))
        touch(Template(r"tpl1530165060809.png", record_pos=(-0.035, 0.049), resolution=(1920, 1080)))
    elif exists(Template(r"tpl1530237898181.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.003, -0.203), resolution=(1920, 1080))):
        assert_equal(poco("com.outfit7.talkingtompool.samsung:id/tv_price_aipay").get_text()
    , "148.00", "sumsung金币礼包金额显示正确，148元.")
        touch(Template(r"tpl1530238055400.png", record_pos=(-0.46, -0.207), resolution=(1920, 1080)))
        wait(Template(r"tpl1530238068500.png", record_pos=(0.119, 0.091), resolution=(1920, 1080)))
        touch(Template(r"tpl1530238076685.png", record_pos=(0.124, 0.094), resolution=(1920, 1080)))

    sleep(3)

       
class TomPoolTestPilot():
          
    def TomPoolGifts(self,channel,is_audit):
         # if exists(Template(r"tpl1527574564592.png", threshold=0.65, target_pos=5, rgb=False, record_pos=(-0.455, -0.077), resolution=(1920, 1080))):
        #     touch(Template(r"tpl1527572048444.png", threshold=0.6, target_pos=5, rgb=False, record_pos=(-0.454, -0.078), resolution=(1920, 1080)))
        # elif exists(Template(r"tpl1527647654639.png", threshold=0.8, target_pos=5, rgb=False, record_pos=(-0.45, -0.076), resolution=(1920, 1080))):
        #     touch(Template(r"tpl1527647654639.png", threshold=0.8, target_pos=5, rgb=False, record_pos=(-0.45, -0.076), resolution=(1920, 1080)))
        # elif exists(Template(r"tpl1531222136909.png", threshold=0.9000000000000002, target_pos=5, rgb=False, record_pos=(-0.405, -0.031), resolution=(1920, 1080))):
        #     touch(Template(r"tpl1531222194552.png", record_pos=(-0.454, 0.022), resolution=(1920, 1080)))
        touch((74.0,590.5))
        sleep(5) 
        touch(Template(r"tpl1527572401251.png", record_pos=(0.019, 0.132), resolution=(1920, 1080)))
        sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            TomPoolGifts_Mobile()
            
        elif channel == "Mobile" and is_audit == "isAudit":
            TomPoolGifts_Audit_Mobile()
            
        elif channel == "Telecom":
            TomPoolGifts_Telecom()
            
        elif channel == "Unicom":
            TomPoolGifts_Unicom()
                    
    def ThreeHundredTwentyEightCoin(self,channel):
        wait(Template(r"tpl1529398566741.png", record_pos=(-0.469, -0.198), resolution=(1920, 1080)))
        touch(Template(r"tpl1529398673580.png", record_pos=(-0.47, -0.195), resolution=(1920, 1080)))
        # touch(Template(r"tpl1527576464387.png", record_pos=(-0.47, -0.194), resolution=(1920, 1080)))
        sleep(5)
        wait(Template(r"tpl1527576789382.png", record_pos=(-0.291, 0.009), resolution=(1920, 1080)))
        touch(Template(r"tpl1527576789382.png", record_pos=(-0.291, 0.009), resolution=(1920, 1080)))
        sleep(5)
        
        ThreeHundredTwentyEightCoin_Founction()
        
    def OneHundredTwentyEightCoin(self,channel):
        wait(Template(r"tpl1527592047254.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.052, 0.011), resolution=(1920, 1080)))
        touch(Template(r"tpl1527578802465.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.049, 0.011), resolution=(1920, 1080)))
        sleep(5)
        
        OneHundredTwentyEightCoin_Founction()

        
    def NintyEightCoin(self,channel):
        wait(Template(r"tpl1527592207592.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.186, 0.013), resolution=(1920, 1080)))
        touch(Template(r"tpl1527579097688.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.187, 0.013), resolution=(1920, 1080)))
        sleep(5)
        
        NintyEightCoin_Founction()
        
    def ThirtyCoin(self,channel,is_audit):
        wait(Template(r"tpl1529398864940.png", record_pos=(-0.239, 0.226), resolution=(1920, 1080)))
        touch(Template(r"tpl1527579377176.png", record_pos=(-0.29, 0.227), resolution=(1920, 1080)))
        sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            ThirtyCoin_Mobile()
            
        elif channel == "Mobile" and is_audit == "isAudit": 
            ThirtyCoin_Audit_Mobile()
            
        elif channel == "Telecom":
            ThirtyCoin_Telecom()
            
        elif channel == "Unicom":
            ThirtyCoin_Unicom()
            
    def TwelveCoin(self,channel,is_audit):
        wait(Template(r"tpl1529398879619.png", record_pos=(0.002, 0.223), resolution=(1920, 1080)))
        touch(Template(r"tpl1527580251691.png", record_pos=(-0.051, 0.226), resolution=(1920, 1080)))
        sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            TwelveCoin_Mobile()
            
        elif channel == "Mobile" and is_audit == "isAudit": 
            TwelveCoin_Audit_Mobile()
            
        elif channel == "Telecom":
            TwelveCoin_Telecom()
            
        elif channel == "Unicom":
            TwelveCoin_Unicom()
            
    def sixCoin(self,channel,is_audit):
        wait(Template(r"tpl1529398892702.png", record_pos=(0.238, 0.222), resolution=(1920, 1080)))
        touch(Template(r"tpl1527580508895.png", record_pos=(0.191, 0.228), resolution=(1920, 1080)))
        sleep(6)

        if channel == "Mobile" and is_audit == "noAudit":
            sixCoin_Mobile()
            
        elif channel == "Mobile" and is_audit == "isAudit": 
            sixCoin_Audit_Mobile()
        
        elif channel == "Telecom":
            sixCoin_Telecom()
            
        elif channel == "Unicom":
            sixCoin_Unicom()
            
    def FiftyGiftBag(self,channel):
        wait(Template(r"tpl1527583937304.png", record_pos=(0.077, -0.26), resolution=(1920, 1080)))
        touch(Template(r"tpl1527583937304.png", record_pos=(0.077, -0.26), resolution=(1920, 1080)))
        sleep(5)
        wait(Template(r"tpl1527584022629.png", record_pos=(-0.253, 0.009), resolution=(1920, 1080)))

        touch(Template(r"tpl1527584022629.png", record_pos=(-0.253, 0.009), resolution=(1920, 1080)))
        sleep(3)
        
        FiftyGiftBag_Founction()
        
    def OneHundredFourtyEightExchangeTwentyGiftBag(self,channel):
        # wait(Template(r"tpl1529399849920.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.006, -0.068), resolution=(1920, 1080)))
        # touch(Template(r"tpl1529400155084.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(-0.001, -0.066), resolution=(1920, 1080)))
        touch((959.5, 482.6))
        sleep(5)
        
        OneHundredFourtyEightExchangeTwentyGiftBag_Founction()

    def OneHundredFourtyEightExchangeTwoThousandGiftBag(self,channel):
        # wait(Template(r"tpl1529399866401.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.248, -0.069), resolution=(1920, 1080)))
        # touch(Template(r"tpl1529400176409.png", threshold=0.9, target_pos=5, rgb=False, record_pos=(0.255, -0.068), resolution=(1920, 1080)))
        touch((1436.3, 542.5))
        sleep(5)
        
        OneHundredFourtyEightExchangeTwoThousandGiftBag_Founction()
        
    def TwentyGiftBag(self,channel,is_audit):
        if exists(Template(r"tpl1527584689802.png", record_pos=(-0.253, 0.239), resolution=(1920, 1080))):
            touch(Template(r"tpl1527584689802.png", record_pos=(-0.253, 0.239), resolution=(1920, 1080)))
            sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            TwentyGiftBag_Mobile()
            
        elif channel == "Mobile" and is_audit == "isAudit": 
            TwentyGiftBag_Audit_Mobile()
        
        elif channel == "Telecom":
            TwentyGiftBag_Telecom()
            
        elif channel == "Unicom":
            TwentyGiftBag_Unicom()
            
    def TenGiftBag(self,channel,is_audit):
        if exists(Template(r"tpl1527585059777.png", record_pos=(-0.001, 0.242), resolution=(1920, 1080))):
            touch(Template(r"tpl1527585059777.png", record_pos=(-0.001, 0.242), resolution=(1920, 1080)))
            sleep(5)

        if channel == "Mobile" and is_audit == "noAudit":
            TenGiftBag_Mobile()
            
        elif channel == "Mobile" and is_audit == "isAudit": 
            TenGiftBag_Audit_Mobile()
        
        elif channel == "Telecom":
            TenGiftBag_Telecom()
            
        elif channel == "Unicom":
            TenGiftBag_Unicom()
            
    
        
    
    
























































