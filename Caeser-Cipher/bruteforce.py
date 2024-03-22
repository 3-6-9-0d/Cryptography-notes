Alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def bruteforce(cipher_text):
    for Key in range(len(Alphabet)):
        plain_text = ''

        cipher_text = cipher_text.upper()
        plain_text = ''

        for c in cipher_text:
            index = Alphabet.find(c)
            index = (index - Key) % len(Alphabet)
            plain_text = plain_text + Alphabet[index]
        print('with Key %s, the result is %s' % (Key,plain_text))
    
    return plain_text


if __name__ == '__main__':
    encrypted = 'VJKUBKUBCBOGUUCIG'
    bruteforce(encrypted)

        