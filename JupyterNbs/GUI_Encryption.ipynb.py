ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt_text(plain_text,key):
    cipher_text = ''
    plain_text = plain_text.upper()
    for c in plain_text:
        index =  ALPHABET.find(c)
        index = (index + key) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]
    return cipher_text

import ipywidgets as widgets
from ipywidgets import HBox, VBox
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
%matplotlib inline
@widgets.interact
def f(key=(0,len(ALPHABET)),a=widgets.Text(value='HELLO', disabled=False)):
    print(encrypt_text(a,key))
