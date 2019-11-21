# -*- coding: utf-8 -*-

"""
@author: Franklin
@file: crc.py
@time: 2019-10-11 15:40
@dec: 
"""
 


# from zlib import crc32
from binascii import crc32

def getCrc32(string):
    byteString = bytes(string, encoding='utf-8')
    resCRC = crc32(byteString)
    return '%x' % (resCRC & 0xffffffff)

if __name__ == "__main__":
    string = "3610a686"
    print(getCrc32(string), type(getCrc32(string)))