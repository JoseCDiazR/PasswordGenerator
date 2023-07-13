import random

UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = UPPERCASE_LETTERS.lower()
NUMBERS = "0123456789"
SYMBOLS = "{|}~[\\]^_`:;<=>?!#$%&\'()*+,-./"
options = (UPPERCASE_LETTERS,LOWERCASE_LETTERS,)

def generate_pass(nick,limit,selected_numbers,selected_symbols):

    password = list()
    #Generate pass only with lower and upper case lettes 
    for i in range(limit):
        password.append(random.choice(random.choice(options)))

    if nick not in password:
        if selected_numbers and not selected_symbols :
            password[random.randint(0, len(password)-1)] = random.choice(NUMBERS)
            pass      
        elif selected_symbols and not selected_numbers:
            password[random.randint(0, len(password)-1)] = random.choice(SYMBOLS)
            pass
        elif selected_symbols and  selected_numbers:
            created_positions = False
            while not created_positions:
                position_symbol = random.randint(0, len(password)-1)
                position_number = random.randint(0, len(password)-1)
                if position_symbol != position_number:
                    password[position_symbol] = random.choice(SYMBOLS)
                    password[position_number] = random.choice(NUMBERS)
                    break        
        else:
            pass
    return ''.join(password)

def get_data (nick,character,symbols,numbers):
    nick_data = nick.get()
    character_data = character.get()
    symbols_data= True if symbols.get() == 1 else False
    numbers_data = True if numbers.get() == 1 else False

    generate_pass(nick_data,character_data,symbols_data,numbers_data)

    