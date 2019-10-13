# -*- coding: utf-8 -*-

"""
@author: Franklin
@file: crc.py
@time: 2019-10-11 15:40
@dec: 
"""
 


from zlib import crc32

def getCrc32(string):
    byteString = bytes(string, encoding='utf-8')
    resCRC = crc32(byteString)
    return resCRC

if __name__ == "__main__":
    string = "64d3f7b1c489ef7f1b2d601f735bfd9d4e13b4fbc99c1877cb6cecf7e85f84bd2e3f541d3eed0ef7328e8119c56102ffd410842123745c69d30e7ddf97f8dcd308c919726c7041d430637156b458cc2c8fcf073137434d9fc58f6378bb2b77024e3d19f493"
    print(getCrc32(string))