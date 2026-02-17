#!/usr/bin/env python3

import random
import sys
import time
from Crypto.Cipher import AES


def decrypt():
    min_time = 1770937200
    max_time = 1771023599

    with open('ciphertext.bin', 'rb') as f_in:
        data = f_in.read()
        nonce = data[:16]
        tag = data[16:32]
        ciphertext = data[32:]

    for i in range(min_time, max_time + 1):

        random.seed(i)
        key = random.randbytes(16)
        aes = AES.new(key, AES.MODE_GCM, nonce=nonce)

        try:
            plaintext = aes.decrypt_and_verify(ciphertext, tag)
        except ValueError:
            continue

    with open('plaintext.txt', 'wb') as f_out:
        f_out.write(plaintext)

    print('Decryption complete!')

if __name__ == '__main__':
    decrypt()