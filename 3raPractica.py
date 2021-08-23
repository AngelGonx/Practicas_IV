import random
import matplotlib.pyplot as plt
print(random.randint(1,20))
print(random.randrange(0, 100, 11))

#Acomodar una lista al azar

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Lista original',lista)
random.shuffle(lista)
print('Lista después del tornado', lista)

campana = [random.gauss(1, 0.5) for i in range(1000)]
plt.hist(campana, bins = 15)
plt.show()