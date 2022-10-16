from tkinter import * #импортируем библиотеку
from tkinter.ttk import Combobox

def E():
    lbl.configure(text = 'No :]', foreground = 'red')
def show_message():
    btn2.configure(text = ent.get())# получаем введенный текст
window = Tk()
window.title("Добро пожаловать в приложение")
window.geometry('400x250')
lbl = Label(window, text='Hello', font = ('!', 30))
lbl.pack()
btn = Button(window, text='Exit', foreground = 'green', font = ('', 10), command=E)
btn.pack()
#combo = Combobox(window)  
#combo['values'] = (":O", ":3")  
#combo.current(1)  # установите вариант по умолчанию  
#combo.pack()
ent = Entry(window, width=20, background = 'black', foreground = 'white')


ent.focus()
ent.pack()

nText = ent.get()

label = ttk.Label()
label.pack()

btn2 = Button(window, font = (15), command = show_message, foreground = 'blue')
btn2.pack()
#if nText != '':
    #btn2 = Button(window, text=(nText), font=(15))
window.mainloop()
