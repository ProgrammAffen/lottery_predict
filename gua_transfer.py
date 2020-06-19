'''
数字转化为八卦,1为阳爻，0为阴爻
'''

import binary_transfer
def gua_trans(num):
    list_number = binary_transfer.binary_trans(num)
    for i in range(6 - len(list_number)):
        list_number.insert(0,0)
    return list_number

if __name__ == '__main__':
    print(gua_trans(35))
