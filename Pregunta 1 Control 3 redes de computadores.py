import numpy as np
from numpy import cos, sin, pi
import matplotlib.pyplot as plt

# Señal de ejemplo
def signal(t):
    return cos(2*pi*3*t)+sin(2*pi*2*t)
#Frecuencia maxima f_cos= 6pi/2pi=3 
# Función de muestreo
def sinc(t, compress=1):
    """
    t: vector de tiempo (evitar el cero)
    compress: factor de compresión del vector de tiempo
              > 1 comprime el tiempo, 
    """
    return sin(compress*pi*t)/(compress*pi*t)




def calculate_sincs(fs,tn):
	sincs = []
	for s,n in zip(fs,tn):
		sinc_n=s*sinc(Fs*(tf-n))
		sincs.append(sinc_n)
	sincs = np.array(sincs)
	sincs = np.sum(sincs, axis=0)
	return sincs

def plot(t,f,tn,fs,tf,sincs,mode):
	
	plt.figure()
	if mode==0:
		plt.plot(t, f) 
		plt.title("Función generada")
		
	elif mode==1:
		plt.plot(tf, sincs, 'r--')
		plt.stem(tn, fs, 'r', markerfmt='C3o', use_line_collection=True)
		plt.title("Reconstrucción de la señal")
	else:
		plt.plot(t, f)
		plt.plot(tf, sincs, 'r--')
		plt.stem(tn, fs, 'r', markerfmt='C3o', use_line_collection=True)
		plt.title("Comparativa")
	plt.xlim([0, 1])
	plt.grid(True)
	plt.xlabel("time (s)")
#Se calcula la señal para tener una comparativa visual
t = np.arange(0, 1, 1/500)
f = signal(t)

#Segun el teorema de la frecuencia de muestreo debe ser al menos 2 veces la frecuencia maxima.
Fs =  2*3 # Sampling freq. (Hz or samples per seconds)

#Se  genera el vector de tiempo y se evalua en la señal
tn = np.arange(0,1.0+(1/Fs),1/Fs)	# Discrete x array (or discrete time)
fs = signal(tn) # Discrete samples array


#Calculamos el t para el sinc
tf = np.arange(1e-15, 1, 1/500)

#se calculan los sinc
sincs=calculate_sincs(fs,tn)

#Se gráfica la señal generada
plot(t,f,tn,fs,tf,sincs,0)

#Se gráfica el muestreo y la reconstruccion
plot(t,f,tn,fs,tf,sincs,1)

#Se grafica la comparativa
plot(t,f,tn,fs,tf,sincs,2)

#Se cacula el error y se muestra [30.5%]
error=np.sqrt(np.trapz(np.square(f-sincs), t))
print("RMS:",error)



#=======================================
#Buscando la frecuencia para que el error sea menor a 0.1
Fs=1492
tn = np.arange(0,1.0+(1/Fs),1/Fs)	# Discrete x array (or discrete time)
fs = signal(tn)

sincs=calculate_sincs(fs,tn)

#Se grafica 
plot(t,f,tn,fs,tf,sincs,2)

#error [0.08%]
error=np.sqrt(np.trapz(np.square(f-sincs), t))
print("RMS:",'{:f}'.format(error))




plt.show()