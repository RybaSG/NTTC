import scipy.io as sci
import numpy as np
import math
##funkcje##

def qpsk_o(file):  # funkcja QPSK_odbiornik
    mat = sci.loadmat(file)  # testowanie poprawnosci
    y = mat['y']
    vv = mat['v']  # testowanie poprawnosci
    V = []  # tworzenie tablicy
    y = y[0, 0]
    vv = vv[0, 0]
    for i in range(len(y)):  # petla 8200
        for j in range(len(y[i])):  # petla 2
            V.append(y[i][j])  # przypisywanie do tablicy

    if (V == vv).all():
        print("OK")
    else:
        print("nie OK")  # sprawdzanie poprawnosci

    if file == "mat_test_files/demux_4_16200_allCR.mat":
        mat_out = {"v_output": V}
        sci.savemat(f"demux_4_16200_allCR_out", mat_out)
    elif file == "mat_test_files/demux_4_64800_allCR.mat" :
        mat_out = {"v_output": V}
        sci.savemat(f"demux_4_64800_allCR_out", mat_out)


def qam16_wo35_o(file, LDPC): #
    mat = sci.loadmat(file)

    y = mat['y']
    yy = y[0, 0]

    v = mat['v']
    vv = v[0, 0]

    substreams = 8
    nmod = 4

    V = [0]*LDPC

    for i in range (len(yy)):
        for j in range (len(yy[i])):
            if ((i * nmod + j) % substreams == 0):
                V[7 + math.floor((i * nmod + j) / substreams) * substreams] = yy[i, j]

            if ((i * nmod + j) % substreams == 1):
                V[1 + math.floor((i * nmod + j) / substreams) * substreams]= yy[i, j]
            #
            if ((i * nmod + j) % substreams == 2):
                V[(3 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]
            #
            if ((i * nmod + j) % substreams == 3):
                V[(5 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if((i * nmod + j) % substreams == 4):
                V[(2 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 5):
                V[(4 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]
            #
            if ((i * nmod + j) % substreams == 6):
                V[(6 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]
            #
            if ((i * nmod + j) % substreams == 7):
                V[(0 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]

    if(V == vv).all():
        print("OK")
    else:
        print("nie OK")
    if file == "mat_test_files/demux_16_16200_allCR.mat":
        mat_out = {"v_output": V}
        sci.savemat(f"demux_16_16200_allCR_out", mat_out)
    elif file == "mat_test_files/demux_16_64800_without35.mat":
        mat_out = {"v_output": V}
        sci.savemat(f"demux_16_64800_without35_out", mat_out)



def qam16_35_o(file,LDPC):
    mat = sci.loadmat(file)

    y= mat['y']
    yy = y[0, 0]

    v = mat['v']
    vv = v[0, 0]#vv dane z pliku

    substreams=8
    nmod=4


    V=[0]*LDPC

    for i in range (len(yy)):
        for j in range (len(yy[i])):
            if ((i * nmod + j) % substreams == 0):
                V[0 + math.floor((i * nmod + j) / substreams) * substreams] = yy[i, j]

            if ((i * nmod + j) % substreams == 1):
                V[2 + math.floor((i * nmod + j) / substreams) * substreams] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 2):
                V[(3 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 3):
                V[(6 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if((i * nmod + j) % substreams == 4):
                V[(4 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 5):
                V[(1 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]
            #
            if ((i * nmod + j) % substreams == 6):
                V[(7 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]
            #
            if ((i * nmod + j) % substreams == 7):
                V[(5 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]

    if(V == vv).all():
        print("OK")
    else:
        print("nie OK")

    mat_out = {"v_output": V}
    sci.savemat(f"demux_16_64800_35_out", mat_out)

def qam64_wo35_o(file, LDPC):
    mat = sci.loadmat(file)

    y = mat['y']
    yy = y[0, 0]

    v = mat['v']
    vv = v[0, 0]

    substreams = 12
    nmod = 6

    V = [0] * LDPC

    for i in range(len(yy)):
        for j in range(len(yy[i])):
            if ((i * nmod + j) % substreams == 0):
                V[11 + math.floor((i * nmod + j) / substreams) * substreams] = yy[i, j]

            if ((i * nmod + j) % substreams == 1):
                V[8 + math.floor((i * nmod + j) / substreams) * substreams] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 2):
                V[(5 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 3):
                V[(2 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 4):
                V[(10 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 5):
                V[(7 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 6):
                V[(4 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 7):
                V[(1 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 8):
                V[(9 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 9):
                V[(6 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 10):
                V[(3 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 11):
                V[(0 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

    if (V == vv).all():
        print("OK")
    else:
        print("nie OK")
    if file == "mat_test_files/demux_64_16200_allCR.mat":
        mat_out = {"v_output": V}
        sci.savemat(f"demux_64_16200_allCR_out", mat_out)
    elif file == "mat_test_files/demux_64_64800_without35.mat":
        mat_out = {"v_output": V}
        sci.savemat(f"demux_64_64800_without35_out", mat_out)


def qam64_35_o(file,LDPC):
    mat = sci.loadmat(file)

    y= mat['y']
    yy = y[0, 0]

    v = mat['v']
    vv = v[0, 0]

    substreams=12
    nmod=6


    V=[0]*LDPC

    for i in range (len(yy)):
        for j in range (len(yy[i])):
            if ((i * nmod + j) % substreams == 0):
                V[4 + math.floor((i * nmod + j) / substreams) * substreams] = yy[i, j]

            if ((i * nmod + j) % substreams == 1):
                V[6 + math.floor((i * nmod + j) / substreams) * substreams] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 2):
                V[(0 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 3):
                V[(5 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if((i * nmod + j) % substreams == 4):
                V[(8 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 5):
                V[(10 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]
            #
            if ((i * nmod + j) % substreams == 6):
                V[(2 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]
            #
            if ((i * nmod + j) % substreams == 7):
                V[(1 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]

            if ((i * nmod + j) % substreams == 8):
                V[(7 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]

            if ((i * nmod + j) % substreams == 9):
                V[(3 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]

            if ((i * nmod + j) % substreams == 10):
                V[(11 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]

            if ((i * nmod + j) % substreams == 11):
                V[(9 + math.floor((i * nmod + j) / substreams) * substreams)]= yy[i, j]

    if(V == vv).all():
        print("OK")
    else:
        print("nie OK")
    mat_out = {"v_output": V}
    sci.savemat(f"demux_64_64800_35_out", mat_out)

while True:
    print("1) 2.1 O")
    print("2) 2.2 O")
    print("3) 2.3 O")
    choice = input("Proszę wybrać odbiornik: ")

    if choice == "3":
        print("\n")
        FRAMES = 100
        LDPC = 16200
        SUBSTREAMS = 8
        MOD = 8
        CELLS = int(LDPC / SUBSTREAMS)

        matData = sci.loadmat("mat_test_files/demux_256_16200_allCR.mat")

        inputDataMat = np.array(matData["v"])[0][0]
        outputDataMat = np.array(matData["y"])[0][0]

        inputData = np.zeros((LDPC, FRAMES))

        # 16200 bits x 100 FRAMES
        for frame in range(FRAMES):
            tempLDPC = []
            for cell in range(CELLS):
                tempBits = outputDataMat[cell, :, frame]

                decode = np.array(
                    [
                        tempBits[7],  # 7:0
                        tempBits[3],  # 3:1
                        tempBits[1],  # 1:2
                        tempBits[5],  # 5:3
                        tempBits[2],  # 2:4
                        tempBits[6],  # 6:5
                        tempBits[4],  # 4:6
                        tempBits[0]  # 0:7
                    ]
                )

                for bit in range(MOD):
                    tempLDPC.append(decode[bit])

            inputData[:, frame] = np.array(tempLDPC)

        if (inputDataMat == inputData).all():
            print("Data check passed")
            # save to mat
            dictionaryInput = {"v": inputData}
            print("Result saved as \"input2_3RX.mat\"\n")
            sci.savemat("input2_3RX.mat", dictionaryInput)
        else:
            print("Data check failed")

    elif choice == "1":
        print("demux_4_16200_allCR.mat")
        qpsk_o("mat_test_files/demux_4_16200_allCR.mat")
        print("demux_4_64800_allCR.mat")
        qpsk_o("mat_test_files/demux_4_64800_allCR.mat")
        print("demux_16_64800_without35.mat")
        qam16_wo35_o('mat_test_files/demux_16_64800_without35.mat', 64800)
        print("demux_16_16200_allCR.mat")
        qam16_wo35_o('mat_test_files/demux_16_16200_allCR.mat', 16200)
        print("demux_16_64800_35.mat")
        qam16_35_o('mat_test_files/demux_16_64800_35.mat', 64800)

    elif choice == "2":
        print("demux_16_64800_without35.mat")
        qam64_wo35_o('mat_test_files/demux_64_64800_without35.mat', 64800)
        print("demux_16_16200_allCR.mat")
        qam64_wo35_o('mat_test_files/demux_64_16200_allCR.mat', 16200)
        print("demux_16_64800_35.mat")
        qam64_35_o('mat_test_files/demux_64_64800_35.mat', 64800)

    else:
        print("Wrong input\n")


1