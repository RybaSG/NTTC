#!/usr/bin/env python3

import scipy.io as sci
import numpy as np


class QAM256M16200:
    n_streams = 8
    n_mod = 8
    n_frames = 100

    def __init__(self, input_file: str, output_path: str, n_ldpc: str) -> None:
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
    demux = QAM256M16200(input_file="demux_256_16200_allCR.mat", output_path="out_file.mat", n_ldpc=16200)


if __name__ == '__main__':
    main()
