import scipy.io as sio
import math


def qam256_35_o(file, LDPC):
    mat = sio.loadmat(file)

    y = mat['y']
    yy = y[0, 0]

    v = mat['v']
    vv = v[0, 0]

    substreams = 16
    nmod = 8

    V = [0] * LDPC

    for i in range(len(yy)):
        for j in range(len(yy[i])):
            if ((i * nmod + j) % substreams == 0):
                V[4 + math.floor((i * nmod + j) / substreams) * substreams] = yy[i, j]

            if ((i * nmod + j) % substreams == 1):
                V[6 + math.floor((i * nmod + j) / substreams) * substreams] = yy[i, j]

            if ((i * nmod + j) % substreams == 2):
                V[(0 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 3):
                V[(2 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 4):
                V[(3 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 5):
                V[(14 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 6):
                V[(12 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]
            #
            if ((i * nmod + j) % substreams == 7):
                V[(10 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 8):
                V[(7 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 9):
                V[(5 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 10):
                V[(8 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 11):
                V[(1 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 12):
                V[(15 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 13):
                V[(9 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 14):
                V[(11 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

            if ((i * nmod + j) % substreams == 15):
                V[(13 + math.floor((i * nmod + j) / substreams) * substreams)] = yy[i, j]

    if (V == vv).all():
        print("OK")
    else:
        print("nie OK")


qam256_35_o('demux_256_64800_35.mat', 64800)
