# Happy Coding -- Ken
import numpy as np

def inputfunction():
    arr = np.array([])
    conf = 'Y'
    while (conf == 'Y' or conf == 'y'):
        inp = input("Masukan Input : ")
        arr = np.append(arr,inp)
        conf = input ("continue? Y/N : ")
