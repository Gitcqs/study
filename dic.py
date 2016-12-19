import time
import random
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
            print(item)
    def review(self,num=3):
        words=list(self.__database.keys())
        for i in range(num):
            word=random.choice(words)
            print(word)
            while(True):
                option=input("check:c or skip:s  ")
                if option.startswith('c') or option.startswith('s'):
                    break
                else:
                    print("argument error")
            
            if option.startswith('c'):
                print( word,':',self.__database[word])


if __name__=='__main__':
    d= Diction()
    d.add('help','帮助')
    d.add('check','查看')
    #d.showAll()
    d.review()
    inp=input("showAll? :y/n  ")
    if inp=='y':
        d.showAll()
    
    
        
