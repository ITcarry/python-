data = {'Lilei':94,'lily':80,'lucy':75,'HanMeimei':90}
print data.items()
#reverse = True :从大到小
print sorted(data.iteritems(),key = lambda a : a[1],reverse=True)
'''
场景：
字典的通过values值排名问题
'''