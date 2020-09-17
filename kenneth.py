# Happy Coding -- Ken
import numpy as np

def inputfunction():
    
    arr = np.array([])
    count = int(input("Jumlah Data Yang Ingin Di Input :"))

    for x in range(count):
        print("Data Ke - ", x)
        inp = input("Masukan input Ke - ")
        arr = np.append(arr, inp)
    return arr

arr = inputfunction()
print(arr)