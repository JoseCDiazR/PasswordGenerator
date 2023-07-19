from methods import main_action
import tkinter
#Create window and edit

def start():
    main_action(textarea_nick,textarea_character,data_symbols,data_numbers,window_app)

window_app = tkinter.Tk()
window_app.geometry("400x350")
window_app.title("PassGenerator")
window_app.iconbitmap("key.ico")
window_app.resizable(False,False)
label_nick = tkinter.Label(window_app, text="Registration nick")
label_nick.place(relwidth=1, relheight=1)
label_nick.pack()
textarea_nick = tkinter.Entry(window_app,font="Arial 18")
textarea_nick.pack()
textarea_nick.place(x=75,y=30)
label_characters = tkinter.Label(window_app, text="Character limit")
label_characters.pack()
label_characters.place(x=160, y=80)

textarea_character = tkinter.Entry(window_app,font="Arial 18")
textarea_character.pack()
textarea_character.place(x=75, y=100)


data_symbols = tkinter.IntVar
cb_simbols = tkinter.Checkbutton(window_app,text="Symbols",variable= data_symbols,onvalue=1, offvalue=0)
cb_simbols.pack()
cb_simbols.place(x=75,y=160)
data_numbers = tkinter.IntVar
cb_numbers = tkinter.Checkbutton(window_app,text="Numbers",variable= data_numbers,onvalue=1, offvalue=0)
cb_numbers.pack()
cb_numbers.place(x=75+25*len('Symbols'),y=160)

button_generate = tkinter.Button(window_app, text="Generar", 
                            command= start)
button_generate.pack()
button_generate.place(x=180,y=200)

window_app.mainloop()







