import numpy as np
def eraseFunction(arr):
        
       
        x = int (input ("masukan Indeks yang ingin dihapus : ") )
        arr = np.delete(arr,x)
        print(arr) 

        return arr


