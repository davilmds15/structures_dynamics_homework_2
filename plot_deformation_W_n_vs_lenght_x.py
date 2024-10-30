import numpy as np
import matplotlib.pyplot as plt

h = 0.004 #m
b = 0.103 #m
E = 2.75*10**8 #Pa
I = 2.67*10**(-9) #m**4
rho = 636.938 #kg/m**3
A = b*h
x = np.linspace(0.001, 0.5, 1000)
l = 0.5
#betha_l = np.array([1.875104, 4.694091, 7.854757, 10.995541])   #homeworks part 1
betha_l = np.array([3.926602, 7.068583, 10.210176, 13.351768]) #homeworks part 2
#betha_l = np.array([0, 0, 0, 0]) #just testing
betha = betha_l/l
C_n = 1


plt.figure(figsize=(10, 6))

for i in range(4):
    #a_n = (np.sin(betha[i]*l) + np.sinh(betha[i]*l)) / (np.cos(betha[i]*l) + np.cosh(betha[i]*l))              #homeworks part 1
    #W_n = C_n*( np.sin(betha[i]*x) - np.sinh(betha[i]*x) - a_n*( np.cos(betha[i]*x) - np.cosh(betha[i]*x) ) )  #homeworks part 1
    a_n = np.sin(betha[i]*l)/np.sinh(betha[i]*l)                #homeworks part 2
    W_n = C_n*(np.sin(betha[i]*x) + a_n*np.sinh(betha[i]*x))    #homeworks part 2
    plt.plot(x, W_n, label=f'Modo {i + 1}')

plt.xlabel("Comprimento x [m]")
plt.ylabel("Deformação normalizada W_n(x)")
plt.title("Deformação W_n(x) vs. comprimento x")
plt.legend()
plt.grid(True)

plt.show()
