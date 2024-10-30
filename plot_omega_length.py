import numpy as np
import matplotlib.pyplot as plt

h = 0.004 #m
b = 0.103 #m
#l = 0.5 #m
E = 2.75*10**8 #Pa
I = 2.67*10**(-9) #m**4
rho = 636.938 #kg/m**3
A = b*h
l = np.linspace(0.3, 0.612, 100)
betha_l = np.array([3.926602, 7.068583, 10.210176, 13.351768])

# Criar gráfico para ω_n
plt.figure(figsize=(10, 6))
for i in range(4):
    omega_n = (betha_l[i]**2) * np.sqrt(E * I / (rho * A * l**4))
    plt.plot(l, omega_n, label=f'Modo {i + 1}')

# Configurações do gráfico para ω_n
plt.xticks(np.arange(0.3, 0.612, 0.05))
plt.yticks(np.arange(0, 3500, 200))
plt.xlabel("Comprimento (l) [m]")
plt.ylabel("Frequência Natural (ω) [rad/s]")
plt.title("Frequências Naturais (ω) vs. Comprimento (l) para Diferentes Modos")
plt.legend()
plt.grid(True)
#plt.savefig('omega_n_plot.png')  # Salvar imagem como arquivo
#plt.close()  # Fechar a figura para liberar memória


# Criar gráfico para f_n
plt.figure(figsize=(10, 6))
for i in range(4):
    omega_n = (betha_l[i]**2) * np.sqrt(E * I / (rho * A * l**4))
    f_n = omega_n / (2 * np.pi)
    plt.plot(l, f_n, label=f'Modo {i + 1}')

# Configurações do gráfico para f_n
plt.xticks(np.arange(0.3, 0.612, 0.05))
plt.yticks(np.arange(0, 530, 25))
plt.xlabel("Comprimento (l) [m]")
plt.ylabel("Frequência Natural (f) [Hz]")
plt.title("Frequências Naturais (f) vs. Comprimento (l) para Diferentes Modos")
plt.legend()
plt.grid(True)
#plt.savefig('f_n_plot.png')  # Salvar imagem como arquivo
#plt.close()  # Fechar a figura para liberar memória
plt.show()
