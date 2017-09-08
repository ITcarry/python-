
def test(x,y,z):
    return x+y+z

#print test(1,2,3)


m = lambda x,y,z : x+y+z
print m(1,2,3)

'''
通过lambda：
一行代码执行一个函数，前边是参数，后边是返回值
调用方式：
m = lambda x,y,z : x+y+z
print m(1,2,3)
'''