# -*- coding: UTF-8 -*-
import time
from selenium import webdriver

brower = webdriver.Safari()

brower.get("https://signin.aliyun.com/login.htm")

time.sleep(3)
brower.find_element_by_id("user_principal_name").send_keys("yiclouduser@vanke")
time.sleep(1)
brower.find_element_by_id("J_FormNext").click()

time.sleep(5)
