


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
    
#����ʽ���    
def test(m,n):
    print m+n
    

    
    
def foo(func,*args,**kwargs):
    func(*args,**kwargs)
    print func,args
    
foo(test,1,2)
    
#�����Ǻ������Ϳɱ䳤������foo������
#���õ�ʱ�򣬽��������������ֺͲ����ֱ���Ϊfoo�����Ĳ������뼴��
'''
����ʽ��̵����ã�
��������һ��������з�װ����
'''
'''
ǰ�᣺
�ڱ���У���һ��������ͨ������ȥʵ�ֵ�
'''