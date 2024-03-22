import sys
plain_text = str(sys.argv[1]) 
key              = int(sys.argv[2])
choice        = int(sys.argv[3])
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt_text(plain_text,key):
    cipher_text = ''
    plain_text = plain_text.upper()
    #define each alphabet to be indexed in terms of 0 to 25
    for c in plain_text:
        index =  ALPHABET.find(c)
        index = (index + key) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]
    return cipher_text
if choice == 1:
        print(encrypt_text(plain_text,key))
if choice == 2:
    for i in range(0,len(ALPHABET)):
        key=i
        print(encrypt_text(plain_text,key))
 
