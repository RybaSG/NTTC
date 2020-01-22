import argparse
import sys

from demux_modules import qam256_mod16200, qam256_mod64800, qpsk, qam16, qam64


def main():
    # print("Please run script with input arguments : --input_path --modulation --nLdpc --code_rate --output_path ")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_path", default="", help="Input path of Mat file"
    )
    parser.add_argument(
        "--modulation", default="", help="Choosing modulation QAM , QPSK etc"
    )
    parser.add_argument(
        "--nLdpc", default="16200", help="16200 or 64800"
    )
    parser.add_argument(
        "--code_rate", default="3/5", help="code rate for modulation , N/5 ..."
    )
    parser.add_argument(
        "--output_path", default="output.mat", help="Path to output modulated file"
    )
    args = parser.parse_args()

    data_values = {
        "modulation_types": ["4QAM", "QPSK", "16QAM", "64QAM", "256QAM"],
        "n_ldpc_values": ["16200", "64800"],
        "code_rate_value": ["1/2", "3/4", "4/5", "5/6", "3/5", "2/3"],
    }

    if args.modulation not in data_values["modulation_types"]:
        sys.exit(
            "Modulation equals {0}. It should be one of {1}".format(
                args.modulations, data_values["modulation_types"]
            )
        )

    if args.nLdpc not in data_values["n_ldpc_values"]:
        sys.exit(
            "LDPC equals {0}. Is should be one of {1}".format(
                args.nLdpc, data_values["n_ldpc_values"]
            )
        )

    if args.code_rate not in data_values["code_rate_value"]:
        sys.exit(
            "Code rate equals {0} should be on of {1}".format(
                args.code_rate, data_values["code_rate_value"]
            )
        )

    if args.modulation in ["4QAM", "QPSK"]:
        demux = qpsk.QPSK(args.input_path, args.output_path, args.nLdpc)
    elif args.modulation == "16QAM":
        demux = qam16.QAM16(
            args.input_path, args.output_path, args.nLdpc, args.code_rate
        )
    elif args.modulation == "64QAM":
        temp_code_rate = args.code_rate
        if args.code_rate not in ["2/3", "3/5"]:
            temp_code_rate = "rest"
        demux = qam64.QAM64(args.input_path, args.output_path, args.nLdpc, temp_code_rate)
        demux.demultiplex()
        demux.check_result()
        demux.save()

    elif args.modulation == "256QAM":
        if args.nLdpc == "16200":
            demux = qam256_mod16200.QAM256L16200(args.input_path, args.output_path)
            demux.get_data_from_file()
            demux.transform_input_data()
            demux.save_data_as_mat()
        elif args.nLdpc == "64800":
            temp_code_rate = args.code_rate
            if args.code_rate not in ["2/3", "3/5"]:
                temp_code_rate = "rest"
            qam23 = qam256_mod64800.QAM256L64800(
                temp_code_rate, args.input_path, args.output_path
            )
            qam23.demultiplex()
            qam23.checkResult()
            qam23.save()
        else:
            print("Invalid ldpc value")


if __name__ == "__main__":
    main()
