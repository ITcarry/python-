#coding:gbk
import traceback


class CommonException(Exception):
    def __init__(self, value):
        super(CommonException, self).__init__(
            "Common Exception. Error Message %s " % (value))
        self.value = value
        
    def __str__(self):
        return repr(self.value)


try:
    raise CommonException ('this is a TypeError  Exception')
except CommonException :
    print 'dasfa'
    print  traceback.format_exc()
    
    '''
只需把CommonException 换成自己定义的类名即可

场景举例：
在web编程的时候，出现以下情况，我要将详细结果汇报给调用者
1）	传入参数不合法（传入参数不够、参数value不合法）
2）	例如 调用外部系统接口出错等
3）	自己代码报错   500错误
    
    '''