import scipy.io as sci
import numpy as np
import math


class QPSK:
    nStreams = 2
    nMod = 2
    nFrames = 100
    mainRate = (0, 1)

    def __init__(self, input_path, output_path, nLdpc):

        matlabFiles = sci.loadmat(input_path)
        self.rate = self.mainRate
        self.nLdpc = int(nLdpc)
        self.output_path = output_path
        self.inputData = matlabFiles["v"][0][0]
        self.correctOutputData = matlabFiles["y"][0][0]
        self.outputData = np.zeros((int(self.nLdpc / self.nStreams), self.nStreams, self.nFrames), dtype=bool)

        for frameIndex in range(self.nFrames):
            for bitIndex in range(self.nLdpc):
                nStream = self.rate[bitIndex % self.nStreams]
                mBitIndex = int(math.floor(bitIndex / self.nStreams))
                bit = self.inputData[bitIndex][frameIndex]
                self.outputData[mBitIndex][nStream][frameIndex] = bit
        self.outputData = np.reshape(self.outputData, (int(self.nLdpc / self.nMod), self.nMod, self.nFrames))

        match = np.all(self.correctOutputData == self.outputData)
        print(f"Match: {match}")
        mat = {"y": self.outputData}
        sci.savemat(self.output_path, mat)


def main():
    qam4 = QPSK("mat_test_files/demux_4_64800_allCR.mat", "out.m", "64800")


if __name__ == '__main__':
    main()
