# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
def PlotSID(NomFichier=""):
    data= np.loadtxt(NomFichier, comments='#', delimiter=",", skiprows=12, usecols=[1])
    data_length = len(data) 
    time_data= np.arange(0.0, 24.0 , 24.0/(data_length))
    fig=plt.figure(figsize=(6,5))
    plt.plot(time_data, data)
    plt.xlabel("Temps (Heure en TU)")
    plt.ylabel("Amplitude (V)")
    plt.title("%s" %NomFichier)
    plt.show()
    