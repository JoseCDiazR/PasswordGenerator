import random
import tkinter
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = UPPERCASE_LETTERS.lower()
NUMBERS = "0123456789"
SYMBOLS = "{|}~[\\]^_`:;<=>?!#$%&\'()*+,-./"
options = (UPPERCASE_LETTERS,LOWERCASE_LETTERS,)
def create_output(data,interface):
    label_password = None
    if label_password:
        label_password.destroy()
    label_password = tkinter.Label(interface, text=data)
    label_password.configure(state="disabled")
    label_password.pack()
    label_password.place(x=180,y=240)  

def generate_pass(nick,limit,selected_numbers,selected_symbols,interface):

    password = list()
    #Generate pass only with lower and upper case lettes 
    for i in range(int (limit)):
        password.append(random.choice(random.choice(options)))

    if nick not in ''.join(password):
        if selected_numbers and not selected_symbols :
            password[random.randint(0, len(password)-1)] = random.choice(NUMBERS)

        elif selected_symbols and not selected_numbers:
            password[random.randint(0, len(password)-1)] = random.choice(SYMBOLS)

        elif selected_symbols and  selected_numbers:
            created_positions = False
            while not created_positions:
                position_symbol = random.randint(0, len(password)-1)
                position_number = random.randint(0, len(password)-1)
                if position_symbol != position_number:
                    password[position_symbol] = random.choice(SYMBOLS)
                    password[position_number] = random.choice(NUMBERS)
                    created_positions = True 

    create_output(''.join(password),interface)    

def get_data (nick,character,symbols,numbers):
    nick_data = nick.get()
    character_data = character.get()
    symbols_data= True if symbols == 1 else False
    numbers_data = True if numbers == 1 else False
    return nick_data,character_data,numbers_data,symbols_data

def main_action (nick,character,symbols,numbers,interface):
    nick_data,character_data, symbols_data,numbers_data = get_data (nick,character,symbols,numbers)
    generate_pass(nick_data,character_data, symbols_data,numbers_data,interface)

    