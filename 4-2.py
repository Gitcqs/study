#!/usr/bin/python
# -*- coding:utf-8 -*
#author: qiansongcao
#desc: python train 4
#---------------------
#2016-12-15 created
#-------------------
import os


class SearchEn(object):
    def __init__(self):
        self.filelist = os.listdir('./Record')

    def find(self, string):
        count = 0
        result = []
        for file in self.filelist:
            with open('./Record/' + file, 'r') as fp:
                lines = fp.readlines()
                for li in lines:
                    if string in li:
                        result.append(li)
                        count += 1
                        #print(result)
        return result


if __name__ == '__main__':
    search = SearchEn()
    test = 'vim'
    print(search.find(test))
    print(os.listdir('./Record'))