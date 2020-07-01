import time
lottery_list = []
f = open('/home/maoqi001/pywork/lotter_data.txt','r')
while True:
    data = f.readline()
    info_list = data.split("\t")
    lottery_list.append(info_list)
    if not data:
        break


if __name__ == "__main__":
    print(int(lottery_list[99][0]))