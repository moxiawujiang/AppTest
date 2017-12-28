#encoding=utf-8
__author__ = '芜疆'
import time
from  appium import webdriver
import unittest
from ddt import  ddt,unpack,data

@ddt
class MyTestCase(unittest.TestCase):
    def  setUp(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion']='5.1'
        desired_caps['deviceName']='85GABMESGZN5'
        desired_caps['appPackage']='com.buestc.wallet'
        desired_caps['appActivity']='.ui.MainActivity'
        desired_caps['unicodeKeyboard']='True'
        desired_caps['resetKeyboard']='True'  #这两个keyboard设置是为了输入中文
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(20)

    @data(("13709048313","1234568"),("13709048615","123456"))
    @unpack
    def test_login_failed(self,username,password):

        self.driver.find_element_by_id("btn_login").click()

        #登录失败
        self.driver.find_element_by_id('et_username').send_keys(username)
        self.driver.find_element_by_id("et_new_stuempno").send_keys(password)
        self.driver.find_element_by_id("btn_login_ok").click()
        if self.driver.find_element_by_id("btn_login_ok").is_displayed():
            result="success"
        else:
            result="fail"
        self.assertEqual("success",result)



    @data(("13709048313","123456","张孝雪"),("13558887052","123456","张粼漪"))
    @unpack
    def test_login_and_logout(self,username,password,realname):

        self.driver.find_element_by_id("btn_login").click()
        #成功登录
        self.driver.find_element_by_id('et_username').clear()
        self.driver.find_element_by_id('et_username').send_keys(username)
        self.driver.find_element_by_id("et_new_stuempno").send_keys(password)
        self.driver.find_element_by_id("btn_login_ok").click()
        self.driver.find_element_by_id('tv_ignore').click()

        name=self.driver.find_element_by_id("home_page_name_tv").text
        self.assertEqual(name,realname)

        self.driver.find_element_by_id('home_page_avater_imageview').click()
        self.driver.find_element_by_id('ica_setting_ib').click()
        self.driver.find_element_by_id('btn_logout').click()
        self.driver.find_element_by_id('button1').click()

    def  tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
