import tkinter as tk
import json
import requests

window = tk.Tk()
window.title("Касаткин Кирилл Александрович")
window.geometry("500x400")

def info():

    username = vvod.get()
    url = f"https://api.github.com/users/{username}"
    user_data = requests.get(url).json()
    information = ("company", "created_at", "email", "id", "name", "url")
    dict = {}
    for i in information:
        dict[i] = user_data.get(i)
    with open("data_file", 'w') as write_file:
        write_file.write(json.dumps(dict, indent=2))

label = tk.Label(window, text="Введите имя пользователя: ")
label.grid(column=0, row=0)

# поле ввода имя пользователя
vvod = tk.Entry(window)
vvod.grid(column=1, row=0)

# кнопка подтверждения имени пользователя
btn = tk.Button(window, text="Подтвердить", width=10, command=info)
btn.grid(column=2, row=0)

window.mainloop()