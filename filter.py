

def _chu3(n):
    return n % 3 == 0

b = filter(_chu3,range(1,101))
print b 

#filter �����ڸ��ӵ������ж�
'''���壺��sequence�е�item����ִ��function(item)����ִ�н��ΪTrue��item���
һ��List/String/Tuple��ȡ����sequence�����ͣ�����'''
'''������filter(function,sequence)'''

