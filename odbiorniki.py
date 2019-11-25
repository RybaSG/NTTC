#!/usr/bin/python

import scipy.io as sci
import numpy as np

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
                        tempBits[7],    # 7:0          
                        tempBits[3],    # 3:1
                        tempBits[1],    # 1:2
                        tempBits[5],    # 5:3    
                        tempBits[2],    # 2:4
                        tempBits[6],    # 6:5
                        tempBits[4],    # 4:6
                        tempBits[0]     # 0:7      
                    ]
                )
                
                for bit in range(MOD):
                    tempLDPC.append(decode[bit])

            inputData[:, frame] = np.array(tempLDPC)

        if(inputDataMat == inputData).all():
            print("Data check passed")
            #save to mat
            dictionaryInput = {"v": inputData}
            print("Result saved as \"input2_3RX.mat\"\n")
            sci.savemat("input2_3RX.mat", dictionaryInput)
        else:
            print("Data check failed")
    else:
        print("Wrong input\n")


            

1