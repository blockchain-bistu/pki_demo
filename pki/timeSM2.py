# -*- coding: utf-8 -*-

"""
@author: Franklin
@file: timeSM2.py
@time: 2019/10/18 11:13
@dec: 
"""
 
from pki.sm2 import generate_keypair, Sign, Verify, Encrypt, Decrypt
import timeit

def testFunctions():
    pk, sk = generate_keypair()
    print("Test on Sign: ")
    print(timeit.timeit(stmt="Sign(\"hello\", " + str(sk) + ", '12345678abcdef', 64)",
                        setup="from pki.sm2 import Sign", number=10))
    sig = Sign("hello", sk, '12345678abcdef', 64)
    print(timeit.timeit(stmt="Verify("+ str(sig) +", \"hello\","+ str(pk)+", 64)", setup="from pki.sm2 import Verify", number=10))
    # Verify(sig, "hello", pk, len_para)

    print("Test on Encrypt: ")

    text = Encrypt(b"hello", pk, 64, 0)
    print(timeit.timeit(stmt="Encrypt(b\"hello\","+ str(pk)+", 64, 0)", setup="from pki.sm2 import Encrypt", number=10))

    print("Test on Decrypt: ")

    print(timeit.timeit(stmt="Decrypt("+str(text)+", "+str(sk)+", 64)", setup="from pki.sm2 import Decrypt", number=10))


if __name__ == "__main__":
    testFunctions()