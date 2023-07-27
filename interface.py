import tkinter
from methods import main_action

class PassGenerator (tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.label_nick = tkinter.Label(self, text="Registration nick")
        self.textarea_nick = tkinter.Entry(self,font="Arial 18")
        self.label_characters = tkinter.Label(self, text="Character limit")
        self.textarea_character = tkinter.Entry(self,font="Arial 18")
        self.data_symbols = tkinter.IntVar()
        self.data_numbers = tkinter.IntVar()
        self.cb_simbols = tkinter.Checkbutton(self,text="Symbols",variable= self.data_symbols,onvalue=1, offvalue=0)
        self.cb_numbers = tkinter.Checkbutton(self,text="Numbers",variable= self.data_numbers,onvalue=1, offvalue=0)
        self.button_generate = tkinter.Button(self, text="Generar", 
                            command= self.start)
        self.create_interface()
    def create_interface(self):
        self.geometry("400x350")
        self.title("PassGenerator")
        self.iconbitmap("key.ico")
        self.resizable(False,False)
        #Nick label and entry field creation
        self.label_nick.place(relwidth=1, relheight=1)
        self.label_nick.pack()
        self.textarea_nick.pack()
        self.textarea_nick.place(x=75,y=30)
        #Character label and entry field creation
        self.label_characters.pack()
        self.label_characters.place(x=160, y=80)
        self.textarea_character.pack()
        self.textarea_character.place(x=75, y=100)
        #Checkbuttons
        self.cb_simbols.pack()
        self.cb_simbols.place(x=75,y=160)
        self.cb_numbers.pack()
        self.cb_numbers.place(x=75+25*len('Symbols'),y=160)
        #Generate button
        self.button_generate.pack()
        self.button_generate.place(x=180,y=200)


    def start(self):
        main_action(self.textarea_nick,self.textarea_character,self.get_symbol_button()
                    ,self.get_nums_button(),self)
    def get_symbol_button(self):
        return self.data_symbols.get()
    def get_nums_button(self):
        return self.data_numbers.get()

if __name__ == "__main__":
    app = PassGenerator()  
    app.mainloop()      