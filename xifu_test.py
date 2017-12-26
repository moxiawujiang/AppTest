#coding=utf-8
__author__ = '芜疆'
import time
from  appium import webdriver
import os



desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion']='5.1'
desired_caps['deviceName']='85GABMESGZN5'
desired_caps['appPackage']='com.buestc.wallet'
desired_caps['appActivity']='.ui.MainActivity'
desired_caps['unicodeKeyboard']='True'
desired_caps['resetKeyboard']='True'  #这两个keyboard设置是为了输入中文

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(5)
driver.find_element_by_id("btn_login").click()

#登录失败
driver.find_element_by_id('et_username').send_keys('13709048313')
driver.find_element_by_id("et_new_stuempno").send_keys('1234567')
try:
    if driver.switch_to.alert().text=="账号或密码错误":
        print('密码错误登录失败pass')
except Exception as e:
    print(e)


#成功登录
driver.find_element_by_id('et_username').send_keys('13709048313')
driver.find_element_by_id("et_new_stuempno").send_keys('123456')
driver.find_element_by_id("btn_login_ok").click()
driver.find_element_by_id('tv_ignore').click()

name=driver.find_element_by_id("home_page_name_tv").text
if name=='张孝雪':
    print("登录成功pass")
else:
    print("登录成功fail")


driver.find_element_by_id('home_page_avater_imageview').click()
driver.find_element_by_id('ica_setting_ib').click()
driver.find_element_by_id('btn_logout').click()
driver.find_element_by_id('button1').click()
driver.quit()



time.sleep(5)



