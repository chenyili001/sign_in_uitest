# -*- encoding=utf8 -*-
__author__ = "v_chenyili"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
#import pytest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from time import sleep
poco = AndroidUiautomationPoco()

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/92cd64a3",
    ])

# script content
print("start...")
#连接设备
#connect_device("Android://127.0.0.1:5037/8604b079")  
#开启设备
start_app("com.bilibili.comic")
sleep(10)
poco(name="com.bilibili.comic:id/comic_home_tab_mine").click()
sleep(3)
sign = poco(text = "已签").click()
sleep(3)
# 点击当天进行签到
# poco(name="com.bilibili.comic:id/tv_sign_credits").click()
qd=poco("android.widget.LinearLayout").offspring("com.bilibili.comic:id/rv_activities_sign_content").child("android.widget.RelativeLayout")
print(len(qd))
for i in range(0,len(qd)):
    if i == 2:
        poco(name = "com.bilibili.comic:id/tv_sign_credits").click()
sleep(5)
# 点击关闭签到本
poco(name="com.bilibili.comic:id/iv_activities_sign_cancel").click() 
sleep(3)
# 关闭app
stop_app("com.bilibili.comic")

