#!/usr/bin/env python3

import scipy.io as sci
import numpy as np


class Demultiplexer:
    def __init__(
        self, n_ldpc: int, n_cells: int, n_substreams: int, input_file: str
    ) -> None:
        self.n_frames = 100
        self.n_ldpc = n_ldpc
        self.n_cells = n_cells
        self.n_substreams = n_substreams
        self.input_file = input_file
        self.input_data_file = np.zeros((self.n_ldpc, self.n_frames))
        self.output_data_file = np.zeros(
            (self.n_cells, self.n_substreams, self.n_frames)
        )
        self.output_data = np.zeros(
            (self.n_cells, self.n_substreams, self.n_frames), dtype=bool
        )

    def get_data_from_file(self) -> None:
        try:
            data_from_file = sci.loadmat(self.input_file)
        except IOError:
            print("Error: can't find input file!")
        self.input_data_file = np.array(data_from_file["v"])[0][0]
        self.output_data_file = np.array(data_from_file["y"])[0][0]

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
        np.save("demux_256_16200_allCR_output", self.output_data)

    def save_data_as_mat(self) -> None:
        dict_out = {"y": self.output_data}
        sci.savemat("demux_256_16200_allCR_output.mat", dict_out)



def main():
    data_to_demux = Demultiplexer(
        n_ldpc=16200,
        n_cells=2025,
        n_substreams=8,
        input_file="demux_256_16200_allCR.mat",
    )

    data_to_demux.get_data_from_file()
    data_to_demux.transform_input_data()

    if (data_to_demux.output_data == data_to_demux.output_data_file).all():
        # np.save("demux256_16200_allCR_output", data_to_demux.output_data)
        data_to_demux.save_data_as_mat()
        print("Data transformed properly")
    else:
        print("Error: data mismatch!")


if __name__ == "__main__":
    main()
