from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import Menu
from tkinter import filedialog
from tkinter import scrolledtext



window = Tk()
window.title("Касаткин Кирилл Александрович")
window.geometry('500x400')

tab_control = ttk.Notebook(window)
tab_1 = ttk.Frame(tab_control)
tab_2 = ttk.Frame(tab_control)
tab_3 = ttk.Frame(tab_control)
tab_control.add(tab_1, text = 'Калькулятор')
tab_control.add(tab_2, text = 'Чекбоксы')
tab_control.add(tab_3, text = 'Файл')
tab_control.pack(expand=1, fill='both')



#......................КАЛЬКУЛЯТОР...................

def result():
    a, b, c = txt_chis_first.get(), signs.get(), txt_chis_second.get()
    if b == "+":
        lbl_2.configure(text = int(a) + int(c))
    elif b == "-":
        lbl_2.configure(text = int(a) - int(c))
    elif b == "*":
        lbl_2.configure(text = int(a) * int(c))
    elif b == "/":
        lbl_2.configure(text = int(a) / int(c))

txt_chis_first = Entry(tab_1, width=5)
txt_chis_first.grid(column=0, row=0)

txt_chis_second = Entry(tab_1, width=5)
txt_chis_second.grid(column=2, row=0)

signs = Combobox(tab_1, width=5)
signs['values'] = ('+', '-', '*', '/')
signs.grid(column=1, row=0)

btn = Button(tab_1, text='=', width=5, command=result)
btn.grid(column=4, row=0)

lbl_2 = Label(tab_1)
lbl_2.grid(column=5, row=0)


#.........................ЧЕКБОКСЫ...................

def proverka():
    a,b,c = chk_state_1_value.get(),chk_state_2_value.get(),chk_state_3_value.get()
    if a == b == c == "":
        mb.showinfo("Предупреждение!", "Выберите вариант!")
        return
    mb.showinfo("Подтверждение", f"Вы выбрали {a} {b} {c} Вариант")

chk_btn = Button(tab_2, text="Подтвердить", command=proverka)
chk_btn.grid(column=0, row=5)

chk_state_1_value = StringVar()
chk_state_2_value = StringVar()
chk_state_3_value = StringVar()

chk_1 = Checkbutton(tab_2, text='Первый', variable=chk_state_1_value, onvalue="Первый", offvalue="")
chk_1.grid(column=0, row=0)
chk_2 = Checkbutton(tab_2, text='Второй', variable=chk_state_2_value, onvalue="Второй", offvalue="")
chk_2.grid(column=0, row=1)
chk_3 = Checkbutton(tab_2, text='Третий', variable=chk_state_3_value, onvalue="Третий", offvalue="")
chk_3.grid(column=0, row=2)



#.........................ФАЙЛ...................
def download():
    file_name = filedialog.askopenfilename(filetypes=(("All", "*"), ("Text", "*.txt")))
    with open(file_name, "r") as f:
        txt.insert(INSERT, f.read())

txt = scrolledtext.ScrolledText(tab_3)
menu3 = Menu(window)
window.config(menu = menu3)
file_menu=Menu(menu3, tearoff=0)
file_menu.add_command(label="Загрузить", command=download)
menu3.add_cascade(label='Файл', menu=file_menu)

txt.pack(expand=1, fill="both")





window.mainloop()