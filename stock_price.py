#coding:gbk

import sys

stock_price = {'google':716, 'apple':105, 'facebook':109, 'microsoft':50, 'baidu':190, '360':75, 'alibaba':80}
_buycar = []
_input = raw_input('please input your money:')

minprice = min(stock_price.values())

print 'Ŀǰ���Թ������¹�Ʊ��'
for key,value in stock_price.items():
    print key,value
print '��������%s$,ѡ��һ֧��Ʊ�ɣ�'%(_input)

while _input > minprice:
    _buy = raw_input('please input your choice :')
    print '��ѡ��Ĺ�Ʊ��%s'%_buy
    _price = int(stock_price[_buy])
    
    if _price < _input:
        _buycar.append(_buy)
        
    _input = int(_input)-int(_price)
    
    print '������%s'%_input
    
    if _input < minprice:
        print 'sorry, you have no enough money to buy any stock'
        print '���Ѿ��������¹�Ʊ��'
        for x in _buycar:
            print x
        break
    else:
        print 'Ŀǰ���Թ������¹�Ʊ��'
        for key,value in stock_price.items():
            print key,value
        print '��������%s$,ѡ��һ֧��Ʊ�ɣ�'%(_input)        
