import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

def paraboloid(x, y):
    return x**2 + y**2

def surface_area_paraboloid(r_max):
    def integrand(r, theta):
        z_r = 2 * r
        return r * np.sqrt(1 + z_r**2)

    area, error = dblquad(
        integrand,
        0, 2 * np.pi,
        lambda theta: 0, lambda theta: r_max 
    )
    return area

def plot_paraboloid(r_max):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-r_max, r_max, 400)
    y = np.linspace(-r_max, r_max, 400)
    X, Y = np.meshgrid(x, y)
    Z = paraboloid(X, Y)

    ax.plot_surface(X, Y, Z, cmap='winter')

    ax.set_title('Еліптичний параболоїд')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

r_max = 2

area = surface_area_paraboloid(r_max)
print(f"Площа поверхні еліптичного параболоїда: {area:.4f}")

plot_paraboloid(r_max)
