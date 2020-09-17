# Happy Coding -- Ken
import numpy as np

def inputfunction():
    arr = np.array([])
    x = 0
    x = input("Banyak Data Yang Ingin Di Input : ")

    while (conf == 'Y' or conf == 'y'):
        inp = input("Masukan Input : ")
        arr = np.append(arr,inp)
        conf = input ("continue? Y/N : ")

inputfunction()