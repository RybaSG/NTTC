import scipy.io as sio

def qpsk_o(file): #funkcja QPSK_odbiornik
    mat = sio.loadmat(file) #testowanie poprawnosci
    y = mat['y']
    vv = mat['v']# testowanie poprawnosci
    v=[]#tworzenie tablicy
    y = y[0, 0]
    vv = vv[0, 0]
    for i in range(len(y)): #petla 8200
        for j in range(len(y[i])): #petla 2
            v.append(y[i][j]) #przypisywanie do tablicy

    if (v == vv).all():
        print("OK")
    else:
        print("nie OK") #sprawdzanie poprawnosci

qpsk_o("demux_4_64800_allCR.mat") #wywolanie funkcji