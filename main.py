from methods import generate_pass
import tkinter
#Create window and edit

def set_text(entry,text):
    entry.set(text)

def get_text(entry):
    return entry.get

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

textarea_password = tkinter.Entry(window_app,font="Arial 18")
textarea_password.configure(state="disabled")
textarea_password.pack()
textarea_password.place(x=75,y=240)
textarea_password.setvar

cb_simbols = tkinter.Checkbutton(window_app,text="Symbols")
cb_simbols.pack()
cb_simbols.place(x=75,y=160)
cb_numbers = tkinter.Checkbutton(window_app,text="Numbers")
cb_numbers.pack()
cb_numbers.place(x=75+25*len('Symbols'),y=160)

button_generate = tkinter.Button(window_app, text="Generar", command= "a")
button_generate.pack()
button_generate.place(x=180,y=200)
print(generate_pass("jose",12,True,True))
window_app.mainloop()







