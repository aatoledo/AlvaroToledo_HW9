import matplotlib.pyplot as plt
import numpy as np

#Cargamos los archivos .csv generados
python = np.loadtxt("times_python.csv")
cpp = np.loadtxt("times_cpp.csv")

#Se realizan la grafica comparativa de los procesos en python y cpp
plt.plot(python[:,0], python[:,1], label = "Python", c = "green")
plt.plot(cpp[:,0], cpp[:,1], label = "C++", c = "red")
#Presentacion
plt.ylabel("Tiempo(s)")
plt.xlabel("N Sucesion de Fibonacci")
plt.title("Python vs Cpp")
plt.legend()
#Guardado
plt.savefig("cpp_vs_python.png")
plt.close()
