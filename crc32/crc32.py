# – coding:utf-8 –

import datetime
import binascii


def showTime():

    print(datetime.datetime.now().strftime("%H:%M:%S"))


def crack():
    crcs = set([
        0xd1f4eb9a,0x68db86df,0x12e25234,0x43c8520f,0x30dddcb8,0xde244e55,0x764e4149,0xb6f1716c,0x1f9714b8,0x5b1b0637
    ])

    r = range(32, 127)
    for a in r:
        for b in r:
            for c in r:
                for d in r:
                    txt = chr(a) + chr(b) + chr(c) + chr(d)
                    crc = binascii.crc32(txt.encode())
                    if (crc & 0xFFFFFFFF) in crcs:
                        with open(".\\flag.txt",'a') as f:
                            f.write(txt+'\n')

                        print(crc & 0xFFFFFFFF)
                        print('~'+txt)


if __name__ == '__main__':

    showTime()
    crack()
    print("破解結束")