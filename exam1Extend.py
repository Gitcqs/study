import time
class Diction:
    __database={'@auther':'cqs',}
    def __init__(self):
        self.__database={'@auther':'cqs','@time':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
        print('you can add(words) an check history using show()')
        print(self.__database)

    def add(self,key,word):
            self.__database[key]=word
    def showAll(self):
        #添加一个页面元素控制
        for item in self.__database.items():
            print(self.__database)
        
