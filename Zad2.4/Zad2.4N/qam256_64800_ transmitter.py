#!/usr/bin/python

import scipy.io as sio
import numpy as np
import math


class qam256_64800:
    nStreams = 16
    nMod = 8
    nLdpc = 64800
    nFrames = 100

    rate35 = (2, 11, 3, 4, 0, 9, 1, 8, 10, 13, 7, 14, 6, 15, 5, 12)
    rate23 = (7, 2, 9, 0, 4, 6, 13, 3, 14, 10, 15, 5, 8, 12, 11, 1)
    rateRest = (15, 1, 13, 3, 8, 11, 9, 5, 10, 6, 4, 7, 12, 2, 14, 0)

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

    def __init__(self, rate):
        self.path = self.paths[rate]
        matlabFiles = sio.loadmat(self.path)

        self.rate = self.rates[rate]
        self.inputData = matlabFiles["v"][0][0]
        self.correctOutputData = matlabFiles["y"][0][0]
        self.outputData = np.zeros((int(self.nLdpc / self.nStreams), self.nStreams, self.nFrames), dtype=bool)

    def demultiplex(self):
        for frameIndex in range(self.nFrames):
            for bitIndex in range(self.nLdpc):
                nStream = self.rate[bitIndex % self.nStreams]
                mBitIndex = int(math.floor(bitIndex / self.nStreams))
                bit = self.inputData[bitIndex][frameIndex]
                self.outputData[mBitIndex][nStream][frameIndex] = bit
        self.outputData = np.reshape(self.outputData, (int(self.nLdpc / self.nMod), self.nMod, self.nFrames))

    def checkResult(self):
        match = np.all(self.correctOutputData == self.outputData)
        print(f"Match: {match}")
        return match

    def save(self):
        mat = {"y": self.outputData}
        sio.savemat(f"out_{self.path}", mat)


qam23 = qam256_64800("rest")
qam23.demultiplex()
qam23.checkResult()
qam23.save()
