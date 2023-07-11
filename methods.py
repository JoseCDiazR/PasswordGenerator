import random

UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = UPPERCASE_LETTERS.lower()
NUMBERS = "0123456789"
SIMBOLS = "{|}~[\\]^_`:;<=>?!#$%&\'()*+,-./"

options = (UPPERCASE_LETTERS,LOWERCASE_LETTERS,NUMBERS,SIMBOLS)
def generate_pass(nick,limit):
    password = ""
    for i in range(limit):
        password +=random.choice(random.choice(options))  
    return password 
