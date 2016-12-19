#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: qiansongcao
#desc: python train 4
#---------------------
#2016-12-15 created
#--------------------
import time


class Timepro:
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def __init__(self):
        print(self.now)

    def compare(self, ti1, ti2):
        '''计算时间间隔'''
        i = 0

    def tuisuan(self, ti1, n):
        '''推算'''
        ti1 += ti1


if __name__ == '__main__':
    time1 = Timepro()
