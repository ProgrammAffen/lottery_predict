def binary_trans(num):
    list_num = []
    while num != 1:
        div = num % 2
        num = num // 2
        list_num.append(div)
    list_num.append(1)
    list_num = list_num[::-1]
    return list_num

if __name__ == '__main__':
    print(binary_trans(6))
