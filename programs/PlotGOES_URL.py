# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
def PlotGOES_URL(date="", res="",source=""):
    
    url="http://darts.jaxa.jp/pub/sswdb/goes/xray/"+date+"_"+source+"_xr_"+res+".txt"
    # If you wish to retrieve a resource via URL and store it in a temporary location,
    # you can do so via the urlretrieve() function:
    local_filename, headers = urllib.request.urlretrieve(url)
    file = open(local_filename)
    dataGOESS,dataGOESL =np.loadtxt(file, skiprows=18, usecols=[6,7],unpack=True)
    
    data_length2 = len(dataGOESL) #
    time_data2   = np.arange(0.0, 24.0 , 24.0/(data_length2))
    plt.figure(figsize=(10,5))
    plt.plot(time_data2, dataGOESL,color='r',linewidth=3,label="GOES: Long X-Ray (0.1 - 0.8 nanometer)")
    plt.plot(time_data2, dataGOESS,color='k',linewidth=3,label="GOES: Short X-Ray (0.05 - 0.4 nanometer)", alpha=.3)
    plt.title(" GOES Solar X-ray Flux", fontsize=16, weight="bold" )
    plt.yscale('log')
    plt.ylabel("X ray Flux ($Watts/m^2$)")
    plt.ylim(1E-8,1E-2)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.grid()
    plt.show()
