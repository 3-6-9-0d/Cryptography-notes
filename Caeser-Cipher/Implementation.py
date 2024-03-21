Alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 3

def encrypt_text(plaint_text):
    cipher_text = ''
    plaint_text = plaint_text.upper()
    
    for c in plaint_text:
        index = Alphabet.find(c)
        index = (index + KEY) % len(Alphabet)
        cipher_text = cipher_text + Alphabet[index]

    return cipher_text
    
def decrypt_text(cipher_text):
    plain_text = ''
    cipher_text = cipher_text.upper()

    for c in cipher_text:
        index = Alphabet.find(c)
        index = (index - KEY) % len(Alphabet)
        plain_text = plain_text + Alphabet[index]

    return plain_text
    
if __name__ == '__main__':
    message = 'Kendoesrev'
    encrypted = (encrypt_text(message))
    print(encrypted)
