import matplotlib.pyplot as plt

def Grafik(x1, x2, x3, x4):
    x = [i for i in range(-8, 12)]
    y = []
    for i in x:
        y.append(x1 * i ** 3 + x2 * i ** 2 + x3 * i + x4)

    plt.plot(x, y)
    plt.xlabel('Ось х')
    plt.ylabel('Ось y')
    plt.title('График функции')
    plt.grid()
    plt.show()

def func(x1, x2, x3, x4):
    text = f'Функция:F = {x1}x³'

    if x2 > 0:
        text = text + f"+{x2}x²"
    elif x2 < 0:
        text = text + f"{x2}x²"

    if x3 > 0:
        text = text + f"+{x3}x"
    elif x3 < 0:
        text = text + f"{x3}x"

    if x4 > 0:
        text = text + f"+{x4}"
    elif x4 < 0:
        text = text + f"{x4}"

    return text