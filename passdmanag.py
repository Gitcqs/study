import time
import random
import pickle
import os


class Diction:
    baidupwd = {'cqs': '4682'}
    __database = {'www.baidu.com': baidupwd}

    def __init__(self):
        if (os.path.exists('database.dat')):
            input = open('database.dat', 'rb')
            try:
                self.__database = pickle.load(input)
                print("初始化载入存档数据成功  " + time.strftime("%Y-%m-%d %H:%M:%S",
                                                      time.localtime()))
            except:
                print("初始化载入文件异常")
            finally:
                input.close()
        else:
            print("当前数据存档为空")
        #self.__database['@time']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(
            "you can add('www.***.com','acount','password') to add password to database"
        )
        print(self.__database)  #仅供调试调用。
        print('***********************')

    def filecheck(self):
        if (os.path.exists('database.dat')):
            return True
        else:
            return False

    def add(self, key, subkey, value):
        b = self.__database.copy(
        )  #以防出现RuntimeError: dictionary changed size during iteratio
        for item in b.items():
            if key in list(item):
                self.__database[key][subkey] = value
            else:
                temp = {subkey: value}
                self.__database[key] = temp

    def update(self, key, subkey, value):
        a = False
        b = self.__database.copy(
        )  #以防出现RuntimeError: dictionary changed size during iteratio
        for item in b.items():
            if key in list(item):
                self.__database[key][subkey] = value
                a = True
        if (not a):
            print("error don't have this item:|address|:" + key +
                  ' |account|: ' + subkey + " |yet please add this and retry")
        else:
            print('update success!(更改数据成功）')

    def search(self, key):
        b = self.__database.copy(
        )  #以防出现RuntimeError: dictionary changed size during iteratio
        for item in b.items():
            if key in list(item):
                print(item)

    #使用pickle模块将数据对象保存到文件
    def save(self):
        output = open('database.dat', 'wb')
        try:
            pickle.dump(self.__database, output)
            print("写入数据成功")
        except:
            print("写入文件异常")
        finally:
            output.close()
        #pickle write tp file

        #利用pickle模块从文件中重构python对象
    def load(self):
        input = open('database.dat', 'rb')
        try:
            self.__database = pickle.load(input)
            print("载入数据成功")
        except:
            print("读入入文件异常")
        finally:
            input.close()

    def showAll(self):
        #添加一个页面元素控制
        for item in self.__database.items():
            print(item)
        print('-------------------------------')

    def review(self, num=3):
        words = list(self.__database.keys())
        for i in range(num):
            word = random.choice(words)
            print(word)
            while (True):
                option = input("check:c or skip:s  ")
                if option.startswith('c') or option.startswith('s'):
                    break
                else:
                    print("argument error")

            if option.startswith('c'):
                print(word, ':', self.__database[word])


#module 测试模块
if __name__ == '__main__':
    d = Diction()
    d.add('www.baidu.com', 'test', '123456')
    #d.add('check','查看')
    d.showAll()
    d.add('www.baidu.com', 'test', '88888')
    d.showAll()
    d.add('www.google.com', 'test', '123456')
    d.showAll()
    d.update('www.google.com', 'test', 'modify')
    d.update('www.gogle.com', 'test', 'modify')
    d.showAll()
    d.save()
    d.showAll()
    d.load()
    d.showAll()
    print(d.filecheck())

    #d.review()
    #inp=input("showAll? :y/n  ")
    #if inp=='y':
#d.showAll()
