#!/usr/bin/python

import scipy.io as sio
import numpy as np
import math 

mat = sio.loadmat('demux_256_16200_allCR.mat')

inputData = mat["v"][0][0]
#inputData = np.transpose(inputData)
correctOutputData = mat["y"][0][0]
outputData = np.zeros((2025,8,100), dtype = int)

nStreams = 8
nMod = 8
nLdpc = 16200
nFrames = 100

rate35 = {
	0: 7,
	1: 3,
	2: 1,
	3: 5,
	4: 2,
	5: 6,
	6: 4,
	7: 0,						
}


for frameIndex in range(nFrames):
	for bitIndex in range(nLdpc):
		nStream = rate35[bitIndex%nStreams]
		mBitIndex = int(math.floor(bitIndex/nStreams))
		bit = inputData[bitIndex][frameIndex]
		outputData[mBitIndex][nStream][frameIndex] = bit
#		print(mBitIndex, nStream, frameIndex)
		

#for frameIndex, frame in enumerate(inputData):
#	for bitIndex, bit  in enumerate(inputData[0]):
#		nStream = rate35[bitIndex%(nStreams-1)]
#		mBitIndex = int(math.floor(bitIndex/8))
#		outputData[mBitIndex][nStream][frameIndex] = bit
##		print(bitIndex, nStream, mBitIndex, bit)
		
		

print(np.shape(inputData))
print(np.shape(outputData))
print(outputData[0][0])
print(" ")
print(correctOutputData[0][0])



