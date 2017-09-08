#coding:gbk

import sys

stock_price = {'google':716, 'apple':105, 'facebook':109, 'microsoft':50, 'baidu':190, '360':75, 'alibaba':80}
_buycar = []
_input = raw_input('please input your money:')

minprice = min(stock_price.values())

print '目前可以购买如下股票：'
for key,value in stock_price.items():
    print key,value
print '你现在有%s$,选择一支股票吧！'%(_input)

while _input > minprice:
    _buy = raw_input('please input your choice :')
    print '你选择的股票是%s'%_buy
    _price = int(stock_price[_buy])
    
    if _price < _input:
        _buycar.append(_buy)
        
    _input = int(_input)-int(_price)
    
    print '您的余额：%s'%_input
    
    if _input < minprice:
        print 'sorry, you have no enough money to buy any stock'
        print '你已经购买如下股票：'
        for x in _buycar:
            print x
        break
    else:
        print '目前可以购买如下股票：'
        for key,value in stock_price.items():
            print key,value
        print '你现在有%s$,选择一支股票吧！'%(_input)        
