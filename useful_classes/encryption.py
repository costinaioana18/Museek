def split_blocks(message):
    return [message[i:i+16] for i in range(0, len(message), 16)]

def XoR(t1,t2):
    return bytes([_a ^ _b for _a, _b in zip(t1, t2)])

def ECBdecode(wholeCipherText,key):
    print("\n ...decrypting using ECB...\n")
    wholePlainText=''
    wholeCipherText=split_blocks(wholeCipherText)
    for cipher in wholeCipherText:
        plain=XoR(cipher,key)
        wholePlainText+=plain.decode()
    #print(wholePlainText)
    return wholePlainText

def ECBencode(plain_text,key):
    wholeCipherText=b''
    plain_blocks=split_blocks(plain_text)
    for plain_block in plain_blocks:
        plain_block=plain_block.encode()
        ciphertext=XoR(plain_block,key)
        wholeCipherText+=ciphertext[0:16]
    return wholeCipherText

def encrypt(text):
    return ECBencode(text,b'1234567890123456')

def decrypt(text):
    return ECBdecode(text,b'1234567890123456')