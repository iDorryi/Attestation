from datetime import datetime, date, time

class Note:
    def __init__(self,name,date,text):
        self.name=name
        self.date=date
        self.text=text

    def info(self):
        print(f'Название: {self.name}\nДата создания: {self.date}\nТекст заметки: {self.text}')

def noteCreating():
    note= Note(input("Введите название заметки:"),datetime.now(),input("Введите тело заметки:"))
    notes_list.append(note)
    save(notes_list) 
    print("Заметка успешно сохранена")

def notesPrint(notes_list):
    count=1
    index= len(notes_list)
    while(index>0):
        index=index-1
        print(f"{count}. Название: {notes_list[index].name}, Дата создания: {notes_list[index].date}")
        count=count+1


def notesObserve(notes_list, mode): 
    check=True
    while(check):    
        index=input("Для просмотра заметки введите ее порядковый номер\nДля выхода в меню введите 0: ")
        try:
            index=int(index)
            if (index==0):
                check=False
            elif (0<=index<=len(notes_list)):
                notes_list[len(notes_list)-index].info()
                if (mode==2):
                    notes_list[len(notes_list)-index].name=input("Введите новое имя заметки: ")
                    notes_list[len(notes_list)-index].text=input("Введите новое тело заметки: ")
                    save(notes_list) 
                    print("Заметка успешно редактирована!")
                    check=False
                if (mode==3):
                    delete=input("Для удаления заметки введите ДА\nДля отмены удаления введите люое другое значение:")
                    if (delete=="ДА"):
                        notes_list.pop(len(notes_list)-index)
                        save(notes_list)                    
                        print("Заметка успешно удалена!")
                        check=False
        except:
            pass
        
def save(notes_list):
    file = open("Notes.txt", "w+", encoding='utf-8')
    index= len(notes_list)
    while(index>0):
        index=index-1
        file.write(f"{notes_list[index].name}|{notes_list[index].date}|{notes_list[index].text}\n")
    file.close()    


notes_list=[]
check1=True
while (check1):
    load=input("Для загрузки заметок из файла введите 0,\nДля создания нового списка введите 1:")
    if (load=="0"):
        file = open("Notes.txt", "r", encoding='utf-8')
        for line in file:
            result = line.split("|")
            note=Note(result[0], result[1], result[2])
            notes_list.append(note)
        check1=False
    if (load=="1"):
        check1=False

check=True
while(check):
    print("----------------")
    mode=input("Для создания новой заметки введите 1,\nДля просмотра существующих заметок введите 2,\n\
Для редактирования существующих заметок введите 3,\nДля удаления существующих заметок введите 4,\n\
Для выхода из программы введите 0:")
    if (mode=="1"):
        noteCreating()
    elif (mode=="2"):
        notesPrint(notes_list)
        notesObserve(notes_list,1)
    elif (mode=="3"):
        notesPrint(notes_list)
        notesObserve(notes_list,2)
    elif (mode=="4"):
        notesPrint(notes_list)
        notesObserve(notes_list,3)
    elif (mode=="0"):
        check=False
