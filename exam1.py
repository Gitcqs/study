#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sqrt
def check(integer):      #质因子分解
	if(not isinstance(integer,int)):
		return 'error'
	else:
		a=[a for a in range(2,integer) if 0 not in [a%d for d in range(2,int(sqrt(integer))+1)]]
		return [a for a in a if integer%a==0]
		#return a


#print (check(55))

	    
def check2(string):       #4不使       
    a,b,c,d=0,0,0,0
    if(len(string)<10):
        return "weak!"
    else:
        for s in string:
            if(s.isupper()):
                a=1
            if(s.islower()):
                b=1
            if(s.isdigit()):
                c=1
            if ([i for i in ['_','!','@','#'] if s==i]):
                d=1
    if(a+b+c+d>2):
        return "strong"
    else:
        return "weak"
    
print(check2("asdfeghjJ4"))
    
        
        
    
