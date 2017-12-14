#usr/bin/python
#encoding:utf-8
import csv
import os
import time

__author__ = '芜疆'

class App(object):
    def __init__(self):
        self.content=""
        self.launchtime=0


    #启动app
    def launchapp(self):
        cmd="adb shell am start -W -n com.buestc.wallet/.ui.MainActivity bnds=[282,672][540,960]"  #喜付的首页启动
        self.content=os.popen(cmd)

    #停止app
    def stopapp(self):
        cmd="adb shell am force-stop com.buestc.wallet"
        #cmd='adb shell input keyevent 3'
        os.popen(cmd)

    #获取启动时间
    def getlaunchtime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.launchtime=(line.split(":")[1]).split("\n")[0]
                break
        return self.launchtime

class Controller(object):
    def __init__(self,count):
        self.app=App()
        self.counter=count
        self.alldata=[("执行时间","启动时间")]

    #单次执行过程
    def testprocess(self):
        self.app.launchapp()
        time.sleep(3)
        elpasedtime=self.app.getlaunchtime()
        self.app.stopapp()
        time.sleep(2)
        currenttime=self.getcurrenttime()
        self.alldata.append((currenttime,elpasedtime))

    #多次迭代过程
    def run(self):
        while self.counter>0:
            self.testprocess()
            self.counter = self.counter-1

    #获取当前时间
    def getcurrenttime(self):
        currenttime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currenttime
    #数据的存储
    def savedatatocsv(self):
        with  open("starttime.csv","w",newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerows(self.alldata)
            csvfile.close()

if __name__=="__main__":
    controller=Controller(4)
    controller.run()
    controller.savedatatocsv()
