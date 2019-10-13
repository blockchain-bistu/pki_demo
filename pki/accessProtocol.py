# -*- coding: utf-8 -*-

"""
@author: Franklin
@file: accessProtocol.py
@time: 2019-10-08 17:08
@dec: 
"""
 
from pki.sm2 import Decrypt, Verify
from pki.crc import getCrc32

class accessProtocol:
    def __init__(self, opType, pContent, sContent, checkSum):
        """
        :param opType: 操作类型, 00-登录，01-注册，10-更新，删除，11-查询
        :param pContent: 传输内容
        :param sContent: 加密内容/签名
        :param checkSum: 校验码
        serverSK 服务器私钥， 写死的, hex
        """
        self.opType = opType
        self.pContent = pContent
        self.sContent = sContent
        self.checkSum = checkSum
        self.serverSK = 'd94870929fb991512dc6c9dda9d2e21de3be95f273546bdf6c7d5c8d52ee10a1'
        self.serverPK = '5bdd559a1d2fcdc6c638125e12677b296b81cac5f4d0d3e628af3aab2f11ee328e8cc83c2835696089976bd1f28d8b7946088dc5be3a9674869bafd1cdd082a7'


    def __str__(self):
        string = self.opType+self.pContent+self.sContent+self.checkSum
        return string

    def checkSumValid(self):
        """
        :return: bool,检查校验码是否正确
        """
        # string = self.pContent+self.sContent
        string = self.sContent
        CRC = getCrc32(string=string)
        if CRC == int(self.checkSum):
            return True
        else:
            return False

    def sContentValid(self):
        len_para = 64
        if self.opType == '01':
            valid = Decrypt(self.sContent, self.serverSK, len_para)
            return valid

        if self.opType != '01':
            # pkUser = getPk()
            planit = Verify(self.sContent, self.serverPK, len_para)
            if planit == '':
                return True
            else:
                return False


def getPk(self):
    pass


if __name__ == "__main__":
    data = accessProtocol(
        opType='01',
        pContent='hello',
        sContent='64d3f7b1c489ef7f1b2d601f735bfd9d4e13b4fbc99c1877cb6cecf7e85f84bd2e3f541d3eed0ef7328e8119c56102ffd410842123745c69d30e7ddf97f8dcd308c919726c7041d430637156b458cc2c8fcf073137434d9fc58f6378bb2b77024e3d19f493',
        checkSum='1227288144'
    )
    print(data.checkSumValid())
    print(data.sContentValid())