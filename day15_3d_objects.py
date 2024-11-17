# 3d объекты (объекты не совсем 3d, но они находятся на 3d плоскости)
# ПЕРЕД ИСПОЛЬЗОВАНИЕМ ПРОПИШИТЕ В ТЕРМИНАЛ:
# pip install matplotlib
# Если выходит ошибка, то: pip install matplotlib --timeout=30 , если и это не выходит - пробуйте с VPN.

# Импорт библиотек
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Функция отображения круга
def draw_circle(ax):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    z = np.zeros_like(x)

    ax.plot(x, y, z, label='Круг')
    ax.set_title('3D проекция круга')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1, 1, 1])  # Пропорции осей

# Функция отображения треуголника
def draw_triangle(ax):
    vertices = np.array([[0, 1, 0], [-1, -1, 0], [1, -1, 0], [0, 1, 0]])  # Вершины треугольника
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='cyan', alpha=0.5)
    
    ax.set_title('3D проекция треугольника')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1, 1, 1])  # Пропорции осей

# Функция отображения квадрата
def draw_square(ax):
    square = np.array([
        [-1, -1, 0],
        [1, -1, 0],
        [1, 1, 0],
        [-1, 1, 0],
        [-1, -1, 0]  # замыкание
    ])
    ax.plot(square[:, 0], square[:, 1], square[:, 2], label='Квадрат')

    ax.set_title('3D проекция квадрата')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([1, 1, 1])  # Пропорции осей

def main():
    print("Выберите фигуру для отображения:")
    print("1. Круг")
    print("2. Треугольник")
    print("3. Квадрат")

    choice = input("Введите номер (1-3): ")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if choice == '1':
        draw_circle(ax)
    elif choice == '2':
        draw_triangle(ax)
    elif choice == '3':
        draw_square(ax)
    else:
        print("Неправильный выбор. Пожалуйста, введите число от 1 до 3.")
        return

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()