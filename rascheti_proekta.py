
# Расчеты к проекту ну просто так
# Необходимые библиотеки
import numpy as np
from scipy.constants import g

# Параметры которые мы хотим менять
V0 = 15
alpha = np.pi/12 

# Наверно формулы нужных нам параметров вытекающих из прошлых
t_full = ((2 * V0 * np.sin(alpha)) / g)
print('t_full =', t_full)

l_max = ((V0 ** 2) * np.sin(2 * alpha)) / g
print('l_max =', l_max)

H_max = ((V0 ** 2) * (np.sin(alpha) ** 2)) / (2 * g)
print('H_max =', H_max)


