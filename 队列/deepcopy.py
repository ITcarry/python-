#coding:gbk

import copy


def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


input_list = [1, 3, 6, 17, 11, 8, 9, 7]

new_list = copy.deepcopy(input_list)

for item in input_list:
    print item
    if not is_prime(item):
        new_list.remove(item)

print new_list

#深拷贝的用法：
'''
import copy
new_list = copy.deepcopy(old_list)   
'''