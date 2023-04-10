import tkinter
from tkinter import *
import os
from tkinter import messagebox
from tkinter.filedialog import *

file_name = None
def create_a_note():
    global file_name
    file_name = "Без названия"
    text_area.delete('1.0', END)

def save_as():
    out = asksaveasfile(mode = 'w', defaultextension= '.txt')
    data = text_area.get('1.0', END)
    try: 
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror('Ой!', "Нельзя сохранить файл")

def open_file():
    global file_name
    inp = askopenfile(mode = 'r')
    if inp is None: 
        return
        file_name = inp.name
    data = inp.read()
    text_area.delete('1.0', END)
    text_area.insert('1.0', data)

def cut():
	text_area.event_generate("<<Cut>>")

def copy():
	text_area.event_generate("<<Copy>>")

def paste():
	text_area.event_generate("<<Paste>>")



    
    

root = Tk()
root.title ("Заметки")
root.geometry("400x400")

text_area = Text(root, width =400, height = 400)
text_area.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
edit_menu = Menu(menu_bar, tearoff=0)
help_menu = Menu(menu_bar, tearoff=0)
helpmenu2 = Menu(help_menu, tearoff=0)

scroll_bar = Scrollbar(text_area)	
file = None




                          
file_menu.add_command(label = "Создать", command = create_a_note)
file_menu.add_command(label = "Открыть", command = open_file)
file_menu.add_command(label = "Сохранить как", command = save_as)
file_menu.add_separator()
file_menu.add_command(label= "Выйти", command = quit)   


edit_menu.add_command(label = "Копировать", command = copy)
edit_menu.add_command(label = "Вставить", command = paste)
edit_menu.add_command(label = "Вырезать", command = cut)
help_menu.add_command(label = "О программе")
helpmenu2.add_command(label = "Локальная справка")
helpmenu2.add_command(label = "На сайте")
 






menu_bar.add_cascade(label = "Файл", menu = file_menu)
menu_bar.add_cascade(label= "Редактирование", menu = edit_menu)	
menu_bar.add_cascade(label= "Помощь", menu = help_menu)
help_menu.add_cascade(label="Помощь",menu= helpmenu2)
 

 

root.config(menu = menu_bar)
root.mainloop()

