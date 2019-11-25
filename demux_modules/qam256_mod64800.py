import scipy.io as sci
import numpy as np
import math


class QAM256L64800:
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

    def __init__(self, rate, input_path, save_path):

        matlabFiles = sci.loadmat(input_path)
        self.rate = self.rates[rate]
        self.save_path = save_path
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
        sci.savemat(f"self.save_path", mat)


def main():
    qam256 = QAM256L64800("2/3", "mat_test_files/demux_256_64800_23.mat", "out.mat")
    qam256.demultiplex()
    qam256.checkResult()
    qam256.save()


if __name__ == '__main__':
    main()
