import scipy.io as sci
import numpy as np
import math


class QAM16:
    nStreams = 8
    nMod = 4
    nFrames = 100
    rate16200 = (7, 1, 4, 2, 5, 3, 6, 0)
    rate64000 = (0, 5, 1, 2, 4, 7, 3, 6)

    rates = {
        "16200": rate16200,
        "64800": rate64000,
    }

    def __init__(self, input_path, output_path, nLdpc, code_rate):

        matlabFiles = sci.loadmat(input_path)
        self.rate = self.rates[nLdpc]
        if nLdpc == '64800' and code_rate != '3/5':
            self.rate = self.rates["16200"]
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
    qam16_allCR = QAM16("mat_test_files/demux_16_16200_allCR.mat", "out.m", "16200", "1/2")
    qam16_35 = QAM16("mat_test_files/demux_16_64800_35.mat", "out.m", "64800", "3/5")
    qam16_without35 = QAM16("mat_test_files/demux_16_64800_without35.mat", "out.m", "64800", "1/2")


if __name__ == '__main__':
    main()
