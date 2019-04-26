print("""
        登 鹳 雀 楼
        - 【唐】王之涣
        白日依山尽，
        黄河入海流。
        欲穷千里目，
        更上一层楼。
""")

print('cmd下运行python或py')

import datetime

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

import math

r = float(input('请输入圆的半径:'))
s = r * r * math.pi
print(s)

print("""
    isdigit()
    True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
    False: 汉字数字
    Error: 无

    isdecimal()
    True: Unicode数字，，全角数字（双字节）
    False: 罗马数字，汉字数字
    Error: byte数字（单字节）

    isnumeric()
    True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
    False: 无
    Error: byte数字（单字节）
""")
