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
ֻ���CommonException �����Լ��������������

����������
��web��̵�ʱ�򣬳��������������Ҫ����ϸ����㱨��������
1��	����������Ϸ��������������������value���Ϸ���
2��	���� �����ⲿϵͳ�ӿڳ����
3��	�Լ����뱨��   500����
    
    '''