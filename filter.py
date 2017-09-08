

def _chu3(n):
    return n % 3 == 0

b = filter(_chu3,range(1,101))
print b 

#filter 适用于复杂的条件判断
'''定义：对sequence中的item依次执行function(item)，将执行结果为True的item组成
一个List/String/Tuple（取决于sequence的类型）返回'''
'''参数：filter(function,sequence)'''

