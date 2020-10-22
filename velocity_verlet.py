
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

#Condições iniciais
dt = 0.2 # accuracy (time step)
aceleracao = 2
tempo_simulacao = 10 
x = [1] #posição inicial
v = [0] # velocidade inicial
t = [0] #tempo (array de segundos)

i = 0 


while t[-1] <= tempo_simulacao:

    #posicao
    x_next = x[i] + v[i] * dt + aceleracao * dt**2 * 0.5

    #velocidade
    v_next = v[i] + aceleracao * dt

    #atualização da posicao
    x.append(x_next)

    #atualização do tempo
    t.append(t[i] + dt)

    #atualização da velocidade
    v.append(v_next)
    
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

plt2.plot(t, v, 'ro', label = 'Átomo')
plt2.title('Verlet', fontweight = 'bold', fontsize = 16)
plt2.xlabel('t', fontweight = 'bold', fontsize = 14)
plt2.ylabel('Velocidade (v)', fontweight = 'bold', fontsize = 14)
plt2.grid(True)
plt2.legend()
plt2.show()












