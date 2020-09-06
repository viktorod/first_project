
# Проект: название в разработке
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim   
from scipy.constants import g

# Создание пространства
fig, ax = plt.subplots()

# Создание тела
thing, = plt.plot( [],[], marker = 'o' , color ='r' )

# Функция траектории тела брошенного под углом к горизонту
def trajectory(V0, t, alpha):
    """ 
    Функция строит траектории движения тела. 
    На вход подаются:
    V0 - Начальная скорость тела
    t - время движения тела
    alpha - угол к горизонту 
    """
    # Полное время полета
    t_full = ((2 * V0 * np.sin(alpha)) / g)
    # По факту пределы (меняются от V0 и alpha) 
    l_max = ((V0 ** 2) * np.sin(2 * alpha)) / g
    H_max = ((V0 ** 2) * (np.sin(alpha) ** 2)) / (2 * g)
    ax.set_xlim(0, (l_max + 1))
    ax.set_ylim(0, H_max + 1)
    # Проекции скоростей на оси X и Y (меняются от alpha)
    V0x = V0 * np.cos(alpha)
    V0y = V0 * np.sin(alpha)
    # Координаты тела (меняются от V0 и t)
    x = V0x * t
    y = V0y * t - (g * (t**2) / 2)
    
    return x, y

# Создание анимации движения брошенного тела
def animate(i):
    thing.set_data(trajectory(5, i, np.pi/12))
    ax.set_title('Тело брошенное под углом к горизонту')

ani = anim.FuncAnimation(fig, 
                         animate, 
                         frames = np.linspace(0, 4 * np.pi, 300),
                         interval = 10)
c = trajectory(5, np.linspace(0, 4 * np.pi, 300), np.pi/12)

# Украшение 
plt.plot(c[0], c[1], color = 'k')
plt.xlabel('Coord - x')
plt.ylabel('Coord - y')
plt.grid()

ani.save('prkt.gif')


