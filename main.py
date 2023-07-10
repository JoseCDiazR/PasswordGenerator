from methods import generate_pass
import tkinter
#Create window and edit
window_app = tkinter.Tk()
window_app.geometry("400x400")
window_app.title("PassGenerator")
window_app.iconbitmap("key.ico")
label_nick = tkinter.Label(window_app, text="Nick de registro")
label_nick.place(relwidth=1, relheight=1)
label_nick.pack()
textarea_nick = tkinter.Entry(window_app,font="Arial 18")
textarea_nick.pack()

label_characters = tkinter.Label(window_app, text="Límite de caracteres")
label_characters.place(relwidth=3, relheight=3)
label_characters.pack()
label_characters.place(x=75,y=200)

textarea_character = tkinter.Entry(window_app,font="Arial 18")
textarea_character.pack()
textarea_character.place(x=75, y=120)
button_generate = tkinter.Button(window_app, text="Generar", command=None )
button_generate.pack()

textarea_password = tkinter.Entry(window_app,font="Arial 18")
textarea_password.pack()
textarea_password.place(x=75,y=300)


window_app.mainloop()


"""
nick = input("Introduce el nick de registro: ")
limit = int (input("Introduce el límite de caracteres: "))

"""
print(generate_pass("jose",12))










