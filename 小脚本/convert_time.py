#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Function: 时间戳转换
Create Time: 2017年03月10日 星期五 11时38分17秒
Author: squareoftwo
"""

import re
import sys
import time

def strptime_2_timestamp():
    '''
    将字符串时间转换为时间戳：
    2017-03-10 15:25:00 -> 1489130700
    '''
    a = sys.argv[1]
    timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    print(timeStamp)

def timestamp_2_strptime():
    '''
    将时间戳转换为字符串时间：
    1489130700 -> 2017-03-10 15:25:00
    '''
    timeStamp = sys.argv[1]
    timeArray = time.localtime(float(timeStamp))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)
    
if __name__ == "__main__":
    if re.match(r'^\d{10}$', sys.argv[1]):
        timestamp_2_strptime()
    elif re.match(r'^\d{4}-\d{1,2}-\d{1,2}', sys.argv[1]):
        strptime_2_timestamp()
    else:
        print('时间戳格式：1-10位数字\n日期时间字符串格式：Y-m-d H:M:S')
