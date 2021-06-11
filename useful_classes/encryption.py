def split_blocks(message):
    return [message[i:i + 16] for i in range(0, len(message), 16)]

def XoR(t1, t2):
    return bytes([_a ^ _b for _a, _b in zip(t1, t2)])

def CFBencode(plain_text, key, initVector):
    whole_cypher_text = b''
    plain_blocks = split_blocks(plain_text)
    for plain_block in plain_blocks:
        plain_block = plain_block.encode()
        ciphertext = XoR(initVector, key)
        ciphertext = XoR(plain_block, ciphertext)
        whole_cypher_text += ciphertext[0:16]
        initVector = ciphertext
    print(whole_cypher_text)
    return whole_cypher_text


# CFB decoding algorithm
def CFBdecode(whole_cypher_text, key, initVector):
    wholePlainText = ''
    whole_cypher_text = split_blocks(whole_cypher_text)
    for cipher in whole_cypher_text:
        plain = XoR(initVector, key)
        plain = XoR(cipher, plain)
        initVector = cipher
        wholePlainText += plain.decode()
    return wholePlainText


def encrypt(text):
    return CFBencode(text, b'1234567890123456', b'ddddcccc11118888')


def decrypt(text):
    return CFBdecode(text, b'1234567890123456', b'ddddcccc11118888')
