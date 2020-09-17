import numpy as np


def inputFunction():

    arr = np.array([])
    count = int(input("Jumlah Data Yang Ingin Di Input :"))

    for x in range(count):
        print("Data Ke - ", x)
        inp = input("Masukan input: ")
        arr = np.append(arr, inp)
    return arr


ans = True
arr = ''
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
        print('ok')
    elif pilihan == '3':
        arr = np.array([])
        if arr.size == 0:
            print('Silakan masukan bilangan terlebih dahulu.')
            arr = inputFunction()
            print(np.sort(arr))
            arr = np.sort(arr)
        else:
            afterSort = np.sort(arr)
            print(afterSort)
    elif pilihan == '5':
        print(arr)
    elif pilihan == '6':
        ans = False
    else:
        print("Pilihan salah !")
