import matplotlib.pyplot as plt
import numpy as np
import time

#Variables
N=35

#Funcion de Fibonacci
def fibonacci(N):
	if N==0:
		return 0	
	if N==1:
		return 1
	else: 
		return fibonacci(N-1)+fibonacci(N-2)

#Funcion que mide el tiempo de la realizacion de Fibonacci
def get_time (N):
	t0 = time.time()
	#Corremos fibonacci(N)
	fibonacci(N)
	t1 = time.time()-t0
	return t1

#Imprimipos el timpo para valores de N
for i in range(N+1):
	print i, get_time(i)
