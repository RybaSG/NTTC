import scipy.io as sio
import math


def qam64_35_o(file,LDPC):
    mat = sio.loadmat(file)

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



qam64_35_o('demux_64_64800_35.mat',64800)