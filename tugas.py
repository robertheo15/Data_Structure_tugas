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
    if pilihan == '2':
        print('ok')
    if pilihan == '3':
        if arr == '':
            print('Silakan masukan bilangan terlebih dahulu.')
            arr = inputFunction()
            print(np.sort(arr))
        else:
            print(np.sort(arr))
    if pilihan == '6':
        ans = False
    else:
        print("Pilihan salah !")
