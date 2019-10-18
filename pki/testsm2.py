import unittest
from pki.sm2 import generate_keypair, Sign, Verify, Encrypt, Decrypt
import timeit

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.pk, self.sk = generate_keypair()

    def test_Sign_run(self):
        sig = Sign("hello", self.sk, '12345678abcdef', 64)
        verify_res = Verify(sig, "hello", self.pk, 64)
        print("Test on Verify: ")
        self.assertEqual(verify_res, True, msg="Verify Wrong!")



    def test_Encrypt_run(self):
        text = Encrypt(b"hello", self.pk, 64, 0)
        decryptRes = Decrypt(text, self.sk, 64)

        self.assertEqual(decryptRes, b'hello', msg='Decrypt Wrong!')


if __name__ == '__main__':

    unittest.main()

