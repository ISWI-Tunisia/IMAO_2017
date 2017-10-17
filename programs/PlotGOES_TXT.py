# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def PlotGOES_URL(NomFichier=""):
    dataGOESS,dataGOESL = np.loadtxt(NomFichier, skiprows=18, usecols=[6,7],unpack=True)
    data_length2 = len(dataGOESL) #
    time_data2   = np.arange(0.0, 24.0 , 24.0/(1.0 * data_length2))
    plt.figure(figsize=(10, 7))
    plt.plot(time_data2, dataGOESL,color='r',linewidth=3,label="GOES: Long X-Ray (0.1 - 0.8 nanometer)")
    plt.plot(time_data2, dataGOESS,color='k',linewidth=3,label="GOES: Short X-Ray (0.05 - 0.4 nanometer)", alpha=.3)
    plt.title(" GOES Solar X-ray Flux", fontsize=16, weight="bold" )
    plt.yscale('log')
    plt.ylabel("X ray Flux ($Watts/m^2$)")
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()