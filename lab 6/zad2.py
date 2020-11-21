
def check_alphabet(a):
    for element in a:
        if element == ' ':
            continue
        elif ord(element) not in range(ord('A'), ord('Z') + 1):
            return False
    return True

def encrypt_vigenere(key, string):
    if False in [check_alphabet(key), check_alphabet(string)]:
        raise ValueError('value not in designated range')
    cipher_text = []
    for i in range(len(string)):
        if string[i] == ' ':
            cipher_text.append(' ')
            continue
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return '' . join(cipher_text)

def decrypt_vigenere(key, cipher_text):
    if False in [check_alphabet(key), check_alphabet(cipher_text)]:
        raise ValueError('value not in designated range')
    orig_text = []
    for i in range(len(cipher_text)):
        if cipher_text[i] == ' ':
            orig_text.append(' ')
            continue
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return '' . join(orig_text)