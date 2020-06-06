import os
from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master, height=0, width=0)
        self.master = master
        self.pack()
        self.open_button = Button(self)
        self.save_button = Button(self)
        self.save_as_button = Button(self)
        self.open_button["text"] = "Open"
        self.save_button["text"] = "Save"
        self.open_button["command"] = self.open
        self.save_button["command"] = self.save
        self.open_button.pack()
        self.save_button.pack()
        self.save_as_button["text"] = "Save As"
        self.save_as_button["command"] = self.save_as
        self.save_as_button.pack()
        self.edit = scrolledtext.ScrolledText(self.master, width = 100)
        self.edit.pack(fill = BOTH, expand = True)
        self.text = "use open button to open a file in hex"
        self.edit.insert('1.0', self.text)
        

    def open(self):
        name = filedialog.askopenfilename()
        if name != "":
            self.file = name
            try:
                os.system(f'xxd -g1 {self.file} {self.file}_temp.txt')
                with open(f'{self.file}_temp.txt') as f:
                    text = f.read()
                    self.edit.delete(1.0, END)
                    self.edit.insert('1.0', text)
                self.master.title(self.file)
                os.remove(f'{self.file}_temp.txt')
            except:
                print (f'cannot display file')
    
    def save(self):
        text = self.edit.get(1.0, END)
        try:
            with open(f'{self.file}_temp.txt', "wb") as f:
                f.write(bytes(text, "utf-8"))
            os.system(f'xxd -r {self.file}_temp.txt {self.file}')
            self.master.title(self.file)
            os.remove(f'{self.file}_temp.txt')
        except Exception as e:
            print (e)

    def save_as(self):
        self.file = filedialog.asksaveasfilename()
        self.save()


root = Tk()
root.title("Hello")
app = Application(master=root)
app.mainloop()
