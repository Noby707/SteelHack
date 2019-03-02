from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import serial
import os



def getArduinoData():
	# file_object = open('distance.txt', 'w')
	
	ser = serial.Serial('/dev/tty96B0', 9600)
	ser.write(0)
	dista = []

	for i in range(1000):
		print(i)
		dista.append(ser.readline())
		# print(ser.readline())

	# print(dista)

	dista = [i.decode('ascii').replace('\n', '') for i in dista]

	# print(dista)

	for i in dista:
		print(i)
		# file_object.write(i)
	# file_object.close()

	return dista


# with open('../Map/Data') as file:
    # data = file.read()
    # lines = data.split("\n")

def Plot(data):
    graph_data = []
    x = []
    y = []
    z = []
    Z= []
    for i in range(len(data)):
        data[i]= data[i].replace(".","")
        z.append(int(data[i]))

    for i in z:
        Z.append([i])


    fig = plt.figure()
    ax = fig.gca(projection='3d')


    X = np.arange(2, 3, 0.001)
    Y = np.arange(3, 4, 0.001)
    X, Y = np.meshgrid(X, Y)
    Z = np.array(Z)
    surf = ax.plot_surface(X, Y, Z,
                           linewidth=1, antialiased=False)
    plt.show()


Plot(getArduinoData())