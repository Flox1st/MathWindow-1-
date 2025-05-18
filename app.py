from tkinter import *
from tkinter import ttk as t
from half_del import half_delil
from gold_rat import gold_rat
from Fibo import Fibon
import matplotlib.pyplot as plt
import Help

def window():
    def click_button1():
        #step 1
        x1 = float(entry.get())
        x2 = float(entry2.get())
        x3 = float(entry3.get())
        x4 = float(entry4.get())
        a, b = entry5.get().split(',')
        a = float(a)
        b = float(b)
        if b < a:
            a, b = b, a
            print("Граница b оказалась меньше границы a, поэтому их значения были поменяны местами")
        E = float(entry6.get())

        text = Help.func(x1, x2, x3, x4)
        label["text"] = text

        seek_x, k = half_delil(x1, x2, x3, x4, a, b, E)

        print(f"Искомое значение {seek_x}, количество кругов {k}, значение f(x) = {seek_x ** 3 * x1 +seek_x ** 2 * x2 + seek_x * x3 + x4}")

        Help.Grafik(x1, x2, x3, x4)

    def click_button2():
        #step 1
        x1 = float(entry.get())
        x2 = float(entry2.get())
        x3 = float(entry3.get())
        x4 = float(entry4.get())
        a, b = entry5.get().split(',')
        a = float(a)
        b = float(b)
        if b < a:
            a, b = b, a
            print("Граница b оказалась меньше границы a, поэтому их значения были поменяны местами")
        E = float(entry6.get())

        text = Help.func(x1, x2, x3, x4)
        label["text"] = text

        seek_x, k = gold_rat(x1, x2, x3, x4, a, b, E)

        print(
            f"Искомое значение {seek_x}, количество кругов {k}, значение f(x) = {seek_x ** 3 * x1 + seek_x ** 2 * x2 + seek_x * x3 + x4}")

        Help.Grafik(x1, x2, x3, x4)

    def click_button3():
        # step 1
        x1 = float(entry.get())
        x2 = float(entry2.get())
        x3 = float(entry3.get())
        x4 = float(entry4.get())
        a, b = entry5.get().split(',')
        a = float(a)
        b = float(b)
        if b < a:
            a, b = b, a
            print("Граница b оказалась меньше границы a, поэтому их значения были поменяны местами")
        E = float(entry6.get())
        l = E * 2

        text = Help.func(x1, x2, x3, x4)
        label["text"] = text

        seek_x, k = Fibon(x1, x2, x3, x4, a, b, E, l)

        print(
            f"Искомое значение {seek_x}, количество кругов {k}, значение f(x) = {seek_x ** 3 * x1 + seek_x ** 2 * x2 + seek_x * x3 + x4}")

        Help.Grafik(x1, x2, x3, x4)

    root = Tk()
    root.title('My App')
    root.geometry('800x600')


    for c in range(10): root.columnconfigure(index = c, weight = 1)
    for r in range(10): root.rowconfigure(index = r, weight = 1)


    entry = t.Entry()
    entry.grid(row = 0, column = 0)
    entry.insert(0, 'X^3')

    entry2 = t.Entry()
    entry2.grid(row = 1, column = 0)
    entry2.insert(0, 'X^2')

    entry3 = t.Entry()
    entry3.grid(row = 2, column = 0)
    entry3.insert(0, 'X')

    entry4 = t.Entry()
    entry4.grid(row = 3, column = 0)
    entry4.insert(0, 'Свободный член')

    entry5 = t.Entry()
    entry5.grid(row = 4, column = 0)
    entry5.insert(0, 'Ограничения')

    entry6 = t.Entry()
    entry6.grid(row = 5, column = 0)
    entry6.insert(0, 'Точность')

    btn = t.Button(text = 'Половинчатое деление', command=click_button1)
    btn.grid(row = 1, column = 3)

    btn2 = t.Button(text='Золотое сечение', command=click_button2)
    btn2.grid(row=2, column=3)

    btn = t.Button(text='Фибоначи', command=click_button3)
    btn.grid(row=3, column=3)

    label = t.Label()
    label.grid(row = 3, column = 1)

    label1 = t.Label(text = 'НЕ ВВОДИТЕ БУКВЫ')
    label1.grid(row=1, column=1)

    root.mainloop()

