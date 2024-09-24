import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def integrand(x):
    return 1 / (1 + x + x ** 2)


def monte_carlo_integration(num_points, custom_points=None):
    if custom_points is not None:
        x = np.array(custom_points)
    else:
        x = np.random.uniform(0, 1, num_points)
    y = np.random.uniform(0, 2, len(x))

    under_curve = y < integrand(x)
    integral = np.sum(under_curve) / len(x) * 2

    return integral, x, y, under_curve


class MonteCarloApp:
    def __init__(self, master):
        self.master = master
        master.title("Метод Монте-Карло для обчислення інтегралу")

        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.method_var = tk.StringVar(value="random")
        ttk.Label(self.frame, text="Спосіб введення точок:").grid(row=0, column=0, sticky=tk.W)
        self.random_radio = ttk.Radiobutton(self.frame, text="Випадкові", variable=self.method_var, value="random",
                                            command=self.toggle_point_entry)
        self.random_radio.grid(row=0, column=1, sticky=tk.W)
        self.manual_radio = ttk.Radiobutton(self.frame, text="Вручну", variable=self.method_var, value="manual",
                                            command=self.toggle_point_entry)
        self.manual_radio.grid(row=0, column=2, sticky=tk.W)

        ttk.Label(self.frame, text="Кількість точок:").grid(row=1, column=0, sticky=tk.W)
        self.points_entry = ttk.Entry(self.frame)
        self.points_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E))
        self.points_entry.insert(0, "10000")

        self.manual_points_label = ttk.Label(self.frame, text="Введіть точки (через кому):")
        self.manual_points_entry = ttk.Entry(self.frame)

        self.calculate_button = ttk.Button(self.frame, text="Обчислити", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=3, pady=10)

        self.result_label = ttk.Label(self.frame, text="")
        self.result_label.grid(row=4, column=0, columnspan=3)

        self.points_text = tk.Text(self.frame, height=5, width=60)
        self.points_text.grid(row=5, column=0, columnspan=3, pady=5)

        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=3)

    def toggle_point_entry(self):
        method = self.method_var.get()
        if method == "manual":
            self.manual_points_label.grid(row=2, column=0, sticky=tk.W)
            self.manual_points_entry.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E))
            self.points_entry.config(state='disabled')
        else:
            self.manual_points_label.grid_remove()
            self.manual_points_entry.grid_remove()
            self.points_entry.config(state='normal')

    def calculate(self):
        method = self.method_var.get()
        try:
            if method == "manual":
                points_str = self.manual_points_entry.get()
                custom_points = [float(p.strip()) for p in points_str.split(',')]
                custom_points = [p for p in custom_points if 0 <= p <= 1]
                if not custom_points:
                    messagebox.showerror("Помилка", "Введіть хоча б одну коректну точку в інтервалі [0, 1].")
                    return
                integral, x, y, under_curve = monte_carlo_integration(len(custom_points), custom_points)
            else:
                num_points = int(self.points_entry.get())
                integral, x, y, under_curve = monte_carlo_integration(num_points)

            self.result_label.config(text=f"Обчислене значення інтегралу: {integral:.6f}")

            self.points_text.delete(1.0, tk.END)
            points_display_limit = 10 
            if len(x) > points_display_limit:
                display_x = x[:points_display_limit]
                display_y = y[:points_display_limit]
                points_info = "Перші 10 точок (x, y):\n"
            else:
                display_x = x
                display_y = y
                points_info = "Точки (x, y):\n"

            for xi, yi in zip(display_x, display_y):
                points_info += f"({xi:.4f}, {yi:.4f})\n"

            self.points_text.insert(tk.END, points_info)

            self.ax.clear()
            self.ax.scatter(x[~under_curve], y[~under_curve], color='red', alpha=0.5, s=10, label='Над кривою')
            self.ax.scatter(x[under_curve], y[under_curve], color='blue', alpha=0.5, s=10, label='Під кривою')

            x_plot = np.linspace(0, 1, 1000)
            self.ax.plot(x_plot, integrand(x_plot), 'g-', lw=2, label='Інтегральна функція')

            self.ax.set_xlim(0, 1)
            self.ax.set_ylim(0, 2)
            self.ax.set_title("Візуалізація методу Монте-Карло")
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.legend()

            self.canvas.draw()
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові значення.")

root = tk.Tk()
app = MonteCarloApp(root)
root.mainloop()
