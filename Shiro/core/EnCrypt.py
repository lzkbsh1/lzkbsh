import base64
import os
import uuid
from Crypto.Cipher import AES


def CBC(key, Hex):
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    mode = AES.MODE_CBC
    iv = uuid.uuid4().bytes
    file_body = pad(Hex)
    encryptor = AES.new(base64.b64decode(key), mode, iv)
    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))
    return base64_ciphertext

def GCM(key,Hex):
    iv = os.urandom(16)
    cipher = AES.new(base64.b64decode(key), AES.MODE_GCM, iv)
    ciphertext, tag = cipher.encrypt_and_digest(Hex)
    ciphertext = ciphertext + tag
    Text = base64.b64encode(iv + ciphertext)
    return Text

'''
加密算法全部来自网上，不是自己写的
'''

