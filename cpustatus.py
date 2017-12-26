__author__ = '芜疆'
#encoding=utf-8
import os
import  time
import csv

class Controller(object):
    def __init__(self,count):
        self.counter=count
        self.alldata=[("执行时间","cpu占用情况")]

    def testprocess(self):
        cmd="adb shell dumpsys cpuinfo | findstr com.buestc.wallet"
        result=os.popen(cmd)
        line=result.readline()
        cpuvalue=line.split("%")[0]
        print(cpuvalue)
        currenttime=self.getCurrentTime()
        self.alldata.append((currenttime,cpuvalue))



    def getCurrentTime(self):
        currenttime=time.strftime("%y-%m-%d %H:%M:%S",time.localtime())
        return  currenttime

    def run(self):
        while self.counter>0:
            self.testprocess()
            self.counter=self.counter-1
            time.sleep(5)

    def saveToCsv(self):
        with open ("cpuinfo.csv","w",newline='') as cpufile:
            writer=csv.writer(cpufile)
            writer.writerows(self.alldata)
            cpufile.close()


if __name__ == '__main__':
    control=Controller(2)
    control.run()
    control.saveToCsv()

