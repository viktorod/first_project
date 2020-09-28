# проектъ
# Все необходимые библиотеки
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c 

# Объединение ну фактически двух синусоид
def dopler(v):  
    """Функция объединяет две последующие
       синусоиды(волны от источника звука),
       на вход подается v - скорость 
       предпологаемого объекта в м/с
    """
    def dopler_1(ny):
        """(Все слова далее относятся к этим двум функциям)
           Функция рисует по факту синусойду
           на вход подается ny - частота в Гц
        """
        # типа просто какие-то формулы из астради
        lyamda_0 = c/ny 
        lyamda = v/ny
        delta_lyamda = (lyamda - lyamda_0)
        beta = delta_lyamda/lyamda_0
        # уравнение синусоиды
        t = np.linspace(0, 10, 100)
        y = beta * np.sin(lyamda * t)
        #  украшение синусоиды
        plt.plot(t,y,'-',color = 'b')
    # призыв функии
    dopler_1(5)
    
    def dopler_2(ny):
        
        # тоже самое что и выше
        lyamda_0 = c/ny 
        lyamda = v/ny
        delta_lyamda = (lyamda - lyamda_0)
        beta = delta_lyamda/lyamda_0
        
        t1 = np.linspace(-5, 0, 100)
        y1 = (beta * np.sin(lyamda * t1))
        
        plt.plot(t1,y1,'-',color = 'r')
        
    dopler_2(1)
# призыв объединяющей функции
dopler(22)

# Якобы машина которая сигналит
plt.plot([0],[0], 'o', ms = 10, color='k')

