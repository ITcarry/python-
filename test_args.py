


#def test_args(*arg,**kwargs):
    #print arg
    #print kwargs
    


#test_args('a','b',c=100,d=1200)
    
   
#def foo(*arg,**kwargs):
    #print 'arg=',arg
    #print 'kwargs=',kwargs
    

#foo(1,2,3,4)
#foo(a=1,b=2,c=3)
#foo(1,2,3,4,a=1,b=2,c=3)
#foo('a',1,None,a=1,b='2',c=3)
    
#函数式编程    
def test(m,n):
    print m+n
    

    
    
def foo(func,*args,**kwargs):
    func(*args,**kwargs)
    print func,args
    
foo(test,1,2)
    
#参数是函数名和可变长参数（foo函数）
#调用的时候，将其他函数的名字和参数分别作为foo函数的参数传入即可
'''
函数式编程的作用：
对所做的一类事情进行封装处理
'''
'''
前提：
在编程中，做一件事情是通过函数去实现的
'''