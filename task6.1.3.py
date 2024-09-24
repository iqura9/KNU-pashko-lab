import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad
from tkinter import *
from tkinter import messagebox


def astroid_function(x, y, R=1):
    return (np.abs(x) ** (2 / 3) + np.abs(y) ** (2 / 3)) - R ** (2 / 3)


def y_lower(x, R=1):
    return -((R ** 3 - np.abs(x) ** (2 / 3)) ** (3 / 2))


def y_upper(x, R=1):
    return ((R ** 3 - np.abs(x) ** (2 / 3)) ** (3 / 2))


def calculate_area(R=1):
    x_max = R
    area, error = dblquad(
        lambda y, x: 1,
        -x_max, x_max,
        lambda x: y_lower(x, R),
        lambda x: y_upper(x, R)
    )
    return area


def plot_astroid(R=1):
    x = np.linspace(-R, R, 400)
    y1 = y_upper(x, R)
    y2 = y_lower(x, R)

    plt.figure(figsize=(8, 8))
    plt.fill_between(x, y1, y2, where=(y1 >= y2), color='blue', alpha=0.5)
    plt.plot(x, y1, 'b')
    plt.plot(x, y2, 'b')
    plt.title('Фігура "Астроїда"')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.grid(True)
    plt.show()


def show_area():
    try:
        area = calculate_area()
        result_text.set(f"Площа фігури: {area:.4f}")
    except Exception as e:
        messagebox.showerror("Помилка", f"Виникла помилка при обчисленні площі: {e}")


def plot():
    plot_astroid()


# Створення GUI
root = Tk()
root.title('Фігура "Астроїда"')

button_area = Button(root, text="Обчислити площу", command=show_area)
button_area.pack(pady=10)

button_plot = Button(root, text="Побудувати графік", command=plot)
button_plot.pack(pady=10)

result_text = StringVar()
label_result = Label(root, textvariable=result_text, font=('Arial', 14))
label_result.pack(pady=10)

root.mainloop()
