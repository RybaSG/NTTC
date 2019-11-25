#!/usr/bin/env python3

import scipy.io as sci
import numpy as np


class QAM256M16200:
    n_substreams = 8
    n_mod = 8
    n_frames = 0
    n_ldpc = 16200
    input_data_file: np.ndarray
    output_data_file: np.ndarray
    output_data: np.ndarray

    def __init__(self, input_file: str, output_file: str) -> None:
        self.input_file = input_file
        self.output_file = output_file

    def get_data_from_file(self) -> None:
        try:
            # Load data from mat file
            data_from_file = sci.loadmat(self.input_file)

            # Define the in/out-put data dimensions
            self.n_frames = data_from_file["v"][0][0].shape[1]
            self.input_data_file = np.zeros((self.n_ldpc, self.n_frames))
            self.output_data_file = np.zeros(
                (int(self.n_ldpc / self.n_substreams), self.n_substreams, self.n_frames)
            )
            self.output_data = np.zeros(
                (int(self.n_ldpc / self.n_substreams), self.n_substreams, self.n_frames),
                dtype=bool,
            )

            # Save input data to variables
            self.input_data_file = np.array(data_from_file["v"])[0][0]
            self.output_data_file = np.array(data_from_file["y"])[0][0]

        except IOError:
            print("Error: can't find input file!")

    def transform_input_data(self) -> None:
        for frame_number in range(self.n_frames):
            for bit_number in range(int(self.n_ldpc / self.n_substreams)):
                temp_input_data = self.input_data_file[
                    bit_number * 8 : (bit_number + 1) * 8, frame_number
                ]

                self.output_data[bit_number, :, frame_number] = np.array(
                    [
                        temp_input_data[7],
                        temp_input_data[2],
                        temp_input_data[4],
                        temp_input_data[1],
                        temp_input_data[6],
                        temp_input_data[3],
                        temp_input_data[5],
                        temp_input_data[0],
                    ]
                )

    def save_data_as_npy(self) -> None:
        if (self.output_data == self.output_data_file).all():
            print("Data are correct")
            np.save("demux_256_16200_allCR_output", self.output_data)
        else:
            print("Data mismatch")

    def save_data_as_mat(self) -> None:
        dict_out = {"y": self.output_data}
        if (self.output_data == self.output_data_file).all():
            print("Data are correct")
            sci.savemat(self.output_file, dict_out)
        else:
            print("Data mismatch")


def main():
    data_to_demux = QAM256M16200(
        input_file="demux_256_16200_allCR.mat", output_file="output_file.mat"
    )

    data_to_demux.get_data_from_file()
    data_to_demux.transform_input_data()
    data_to_demux.save_data_as_mat()


if __name__ == "__main__":
    main()
