
import matplotlib.pyplot as plt

#Condições iniciais
dt = 0.2 # accuracy (time step)
aceleracao = 2
tempo_simulacao = 10 
x = [1] #posição inicial
t = [0] #tempo (array de segundos)

i = 0 

#Algoritmo de Verlet 
#x(t+Δt)=2x(t)−x(t−Δt)+a(t)Δt^2
while t[-1] <= tempo_simulacao:

    #posicao
    x_next = 2 * x[i] - x[i-1] + aceleracao * dt**2

    #atualização da posicao
    x.append(x_next)

    #atualização do tempo
    t.append(t[i] + dt)
    
    #Atualização do loop
    i = i + 1   

#Plot
plt.plot(t, x, 'ro', label = 'Átomo')
plt.title('Verlet', fontweight = 'bold', fontsize = 16)
plt.xlabel('t', fontweight = 'bold', fontsize = 14)
plt.ylabel('X', fontweight = 'bold', fontsize = 14)
plt.grid(True)
plt.legend()
plt.show()












