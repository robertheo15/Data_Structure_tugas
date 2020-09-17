import numpy as np


def inputFunction():
    arr = np.array([])
    conf = 'Y'
    while (conf == 'Y' or conf == 'y'):
        inp = input("Masukan Input : ")
        arr = np.append(arr, inp)
        conf = input("continue? Y/N : ")


print('Menu Pengurutan Bilangan')
print('1.Masukkan Bilangan')
print('2.Merubah Isi Array')
print('3.Proses Pengurutan Bilangan')
print('4.Menghapus Isi Array')
print('5.Tampilkan Isi Array')
print('6.Keluar')
pilihan = input("Pilih Menu (1, 2, 3, 4, 5, 6) ? ")

if pilihan == 1:
    inputFunction()
