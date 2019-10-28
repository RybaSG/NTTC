#!/usr/bin/python

import scipy.io as sio
import numpy as np
import math 


class qam256_64800:
	nStreams = 16
	nMod = 8
	nLdpc = 64800
	nFrames = 100
	
	rate35 = {
		0: 2, 1: 11, 2: 3, 3: 4, 4: 0, 5: 9, 6: 1, 7: 8, 
		8: 10, 9: 13, 10: 7, 11: 14, 12: 6, 13: 15, 14: 5, 15: 12					
	}
	
	rate23 = { 
		0: 7, 1: 2, 2: 9, 3: 0, 4: 4, 5: 6, 6: 13, 7: 3, 
		8: 14, 9: 10, 10: 15, 11: 5, 12: 8, 13: 12, 14: 11, 15: 1					
	}

	rateRest = {
		0: 15, 1: 1, 2: 13, 3: 3, 4: 8, 5: 11, 6: 9, 7: 5, 
		8: 10, 9: 6, 10: 4, 11: 7, 12: 12, 13: 2, 14: 14, 15: 0					
	}
	
	rates = {
		"2/3": rate23,
		"3/5": rate35,
		"rest": rateRest
	}

	paths = {
		"2/3": 'demux_256_64800_23.mat',
		"3/5": 'demux_256_64800_35.mat',
		"rest": 'demux_256_64800_without23-35.mat'
	}

	
	def __init__(self, rate = "rest"):
		self.path = self.paths[rate]
		matlabFiles = sio.loadmat(self.path)
		
		self.rate = self.rates[rate]
		self.inputData = matlabFiles["v"][0][0]
		self.correctOutputData = matlabFiles["y"][0][0]
		self.outputData = np.zeros((int(self.nLdpc/self.nStreams), self.nStreams, self.nFrames), dtype = int)
		
		
	def demultiplex(self):
		for frameIndex in range(self.nFrames):
			for bitIndex in range(self.nLdpc):
				nStream = self.rate[bitIndex%self.nStreams]
				mBitIndex = int(math.floor(bitIndex/self.nStreams))
				bit = self.inputData[bitIndex][frameIndex]
				self.outputData[mBitIndex][nStream][frameIndex] = bit
		self.outputData = np.reshape(self.outputData, (int(self.nLdpc/self.nMod), self.nMod, self.nFrames))
		
		
	def checkResult(self):
		match = np.all(self.correctOutputData == self.outputData)
		print(f"Match: {match}")
		return match


	def save(self):
		mat = {"y": self.outputData}
		sio.savemat(f"out_{self.path}", mat)
	



qam23 = qam256_64800("2/3")
qam23.demultiplex()
qam23.checkResult()
qam23.save()