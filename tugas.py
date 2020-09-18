import numpy as np


def inputFunction():

    arr = np.array([])
    count = int(input("Jumlah Data Yang Ingin Di Input :"))

    for x in range(count):
        print("Data Ke - ", x)
        inp = input("Masukan input: ")
        arr = np.append(arr, inp)
    return arr


def sortFunction(arr):
    sortResult = np.sort(arr)
    return sortResult


def editFunction(arr):

    x = 0
    x = int(input("indeks : "))
    print(arr[x])

    arr[x] = input("masukkan data baru : ")
    print(arr)
    return arr


def eraseFunction(arr):

    x = int(input("masukan Indeks yang ingin dihapus : "))
    arr = np.delete(arr, x)
    print(arr)
    return arr


ans = True
arr = np.array([])
while ans:
    print("""
        Menu Pengurutan Bilangan
        1.Masukkan Bilangan
        2.Merubah Isi Array
        3.Proses Pengurutan Bilangan
        4.Menghapus Isi Array
        5.Tampilkan Isi Array
        6.Keluar
    """)
    pilihan = input("Pilih Menu (1, 2, 3, 4, 5, 6) ? ")

    if pilihan == '1':
        arr = inputFunction()
    elif pilihan == '2':
        if arr.size == 0:
            print('Silakan masukan bilangan terlebih dahulu.')
            arr = inputFunction()
            editFunction(arr)
        else:
            editFunction(arr)
    elif pilihan == '3':
        if arr.size == 0:
            print('Silakan masukan bilangan terlebih dahulu.')
            arr = inputFunction()
            print(sortFunction(arr))
        else:
            print(sortFunction(arr))
    elif pilihan == '4':
        if arr.size == 0:
            print('Array tidak ada isi!')
            print('Silakan masukan bilangan terlebih dahulu.')
            arr = inputFunction()
            arr = eraseFunction(arr)
        else:
            arr = eraseFunction(arr)
    elif pilihan == '5':
        if arr.size == 0:
            print('Silakan masukan bilangan terlebih dahulu.')
            arr = inputFunction()
            print(arr)
        else:
            print(arr)
    elif pilihan == '6':
        ans = False
    else:
        print("Pilihan salah !")
