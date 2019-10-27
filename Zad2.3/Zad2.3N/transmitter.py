#!/usr/bin/env python3
"""
Z2.3N 256-QAM, N_LDPC = 16200, code rate 2/3) - transmitter
Pages 40-43

+-----------------------+-------+-------+-------+-------+-------+-------+-------+-------+
|   di mod N_substreams |   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |
|-----------------------+-------+-------+-------+-------+-------+-------+-------+-------+
|           e           |   7   |   3   |   1   |   5   |   2   |   6   |   4   |   0   |
+-----------------------+-------+-------+-------+-------+-------+-------+-------+-------+
"""
import scipy.io as sci
import numpy as np

N_FRAMES = 100
N_LDPC = 16200
N_CELLS = 2025
N_SUBSTREAMS = 8
N_MOD = 8

all_data = sci.loadmat("demux_256_16200_allCR.mat")

input_data = np.array(all_data['v'])[0][0]
output_data_check = np.array(all_data['y'])[0][0]
print(input_data.shape)
print(output_data_check.shape)

output_data = np.zeros((N_FRAMES, N_CELLS, N_SUBSTREAMS))

for frame_number in range(N_FRAMES):
    for i in range(int(N_LDPC / N_SUBSTREAMS)):
        temp_input_data = input_data[i * 8:(i + 1) * 8, frame_number]

        output_data[frame_number][i][:] = np.array([temp_input_data[7], temp_input_data[2], temp_input_data[4],
                                                    temp_input_data[1], temp_input_data[6], temp_input_data[3],
                                                    temp_input_data[5], temp_input_data[0]])

np.save("demux_256_16200_allCR_output", output_data)
