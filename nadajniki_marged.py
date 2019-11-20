import argparse
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
        print("File loaded succeed")
        for frameIndex in range(self.nFrames):
            for bitIndex in range(self.nLdpc):
                nStream = self.rate[bitIndex % self.nStreams]
                mBitIndex = int(math.floor(bitIndex / self.nStreams))
                bit = self.inputData[bitIndex][frameIndex]
                self.outputData[mBitIndex][nStream][frameIndex] = bit
        self.outputData = np.reshape(self.outputData, (int(self.nLdpc / self.nMod), self.nMod, self.nFrames))
        print("Calculated output matrix")
        match = np.all(self.correctOutputData == self.outputData)
        print(f"Match: {match}")
        mat = {"y": self.outputData}
        sci.savemat(f"out_{self.output_path}", mat)


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
        if nLdpc == '64800' and code_rate == '3/5':
            self.rate = self.rates["16200"]
        self.nLdpc = int(nLdpc)
        self.output_path = output_path
        self.inputData = matlabFiles["v"][0][0]
        self.correctOutputData = matlabFiles["y"][0][0]
        self.outputData = np.zeros((int(self.nLdpc / self.nStreams), self.nStreams, self.nFrames), dtype=bool)
        print("File loaded succeed")
        for frameIndex in range(self.nFrames):
            for bitIndex in range(self.nLdpc):
                nStream = self.rate[bitIndex % self.nStreams]
                mBitIndex = int(math.floor(bitIndex / self.nStreams))
                bit = self.inputData[bitIndex][frameIndex]
                self.outputData[mBitIndex][nStream][frameIndex] = bit
        self.outputData = np.reshape(self.outputData, (int(self.nLdpc / self.nMod), self.nMod, self.nFrames))
        print("Calculated output matrix")
        match = np.all(self.correctOutputData == self.outputData)
        print(f"Match: {match}")
        mat = {"y": self.outputData}
        sci.savemat(f"out_{self.output_path}", mat)


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
        sci.savemat(f"out_{self.save_path}", mat)


class QAM256M16200:
    n_streams = 8
    n_mod = 8
    n_frames = 100

    def __init__(self, input_file: str, output_path: str, n_ldpc: int) -> None:
        self.n_frames = 100
        self.n_ldpc = int(n_ldpc)
        self.output_path = output_path
        self.input_file = input_file
        self.input_data_file = np.zeros((self.n_ldpc, self.n_frames))
        self.output_data_file = np.zeros((int(self.n_ldpc / self.n_streams), self.n_streams, self.n_frames))
        self.output_data = np.zeros((int(self.n_ldpc / self.n_streams), self.n_streams, self.n_frames), dtype=bool)

        #####
        try:
            data_from_file = sci.loadmat(self.input_file)
            self.input_data_file = np.array(data_from_file["v"])[0][0]
            self.output_data_file = np.array(data_from_file["y"])[0][0]
        except IOError:
            print("Error: can't find input file!")

        #####
        for frame_number in range(self.n_frames):
            for bit_number in range(int(self.n_ldpc / self.n_streams)):
                temp_input_data = self.input_data_file[bit_number * 8: (bit_number + 1) * 8, frame_number]

                self.output_data[bit_number, :, frame_number] = np.array(
                    [temp_input_data[7], temp_input_data[2], temp_input_data[4], temp_input_data[1], temp_input_data[6],
                     temp_input_data[3], temp_input_data[5], temp_input_data[0], ])

        #####
        dict_out = {"y": self.output_data}

        if (self.output_data == self.output_data_file).all():
            sci.savemat(self.output_path, dict_out)
            print("Data transformed properly")
        else:
            print("Error: data mismatch!")


def main():
    # print("Please run script with input arguments : --input_path --modulation --nLdpc --code_rate --output_path ")
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', default='', help='Input path of Mat file')
    parser.add_argument('--modulation', default='', help='Choosing modulation QAM , QPSK etc')
    parser.add_argument('--nLdpc', default='16200', help='16200 or 64800')
    parser.add_argument('--code_rate', default='3/5', help='code rate for modulation , N/5 ...')
    parser.add_argument('--output_path', default='output.mat', help='Path to output modulated file')
    args = parser.parse_args()

    if args.modulation == 'QPSK':
        demux = QPSK(args.input_path, args.output_path, args.nLdpc)
    elif args.modulation == '16QAM':
        demux = QAM16(args.input_path, args.output_path, args.nLdpc, args.code_rate)
    elif args.modulation == '64QAM':
        # TODO
        print("Should be done")
    elif args.modulation == '256QAM':
        if args.nLdpc == '16200':
            demux = QAM256M16200(args.input_path, args.output_path, args.nLdpc)
        else:
            qam23 = qam256_64800(args.code_rate, args.input_path, args.output_path)
            qam23.demultiplex()
            qam23.checkResult()
            qam23.save()


if __name__ == '__main__':
    main()
