import numpy as np

def editFunction(): 

    arr = np.array([12, 23, 34, 45, 56])
    x = 0
    x = int(input("indeks : "))
    print(arr[x])

    arr[x] = input("masukkan data baru : ")
    print(arr)

editFunction()