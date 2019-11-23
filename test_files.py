#!/usr/bin/python3
import os


def main():
    data_values = {
        "modulation_types": ["QPSK", "16QAM", "64QAM", "256QAM"],
        "n_ldpc_values": ["16200", "64800"],
        "code_rate_value": ["1/2", "3/4", "4/5", "5/6", "3/5", "2/3"],
    }

    with open("result.txt", "w+") as result_file:
        result_file.write(
            "There are used parameters, used command "
            "and match returned during testing in this file\n\n"
        )

    test_files = os.listdir("mat_test_files")

    for mat_file_name in test_files:
        file_name = mat_file_name.split(".")[0]
        output_file = "output_files/out_" + mat_file_name

        mat_file_parts = mat_file_name.split(".")[0].split("_")

        modulation_type = mat_file_parts[1] + "QAM"
        ldpc_value = mat_file_parts[2]

        code_rate = []
        # All code rates
        if "allCR" == mat_file_parts[3]:
            for crv in data_values["code_rate_value"]:
                if True:
                    code_rate.append(crv)
        # Only code rate = 3/5
        elif "35" == mat_file_parts[3]:
            for crv in data_values["code_rate_value"]:
                if crv == "3/5":
                    code_rate.append(crv)
        # All code rates except 3/5
        elif "without35" == mat_file_parts[3]:
            for crv in data_values["code_rate_value"]:
                if crv != "3/5":
                    code_rate.append(crv)
        # Only code rate = 2/3
        elif "23" == mat_file_parts[3]:
            for crv in data_values["code_rate_value"]:
                if crv == "2/3":
                    code_rate.append(crv)
        # All code rates except 3/5 and 2/3
        elif "without23-35" == mat_file_parts[3]:
            for crv in data_values["code_rate_value"]:
                if crv not in ["2/3", "3/5"]:
                    code_rate.append(crv)

        for crv in code_rate:
            with open("result.txt", "a") as result_file:
                result_file.write(
                    "Testing parameters: {0}, {1}, {2}, {3}, {4}\n".format(
                        mat_file_name, modulation_type, ldpc_value, crv, output_file
                    )
                )
                result_file.write(
                    "Command:"
                    "python3 nadajniki_marged.py --input_path mat_test_files/{0} "
                    "--modulation {1} --nLdpc {2} --code_rate {3} --output_path {4}\n".format(
                        mat_file_name, modulation_type, ldpc_value, crv, output_file
                    )
                )

            match_result = os.popen(
                "python3 nadajniki_marged.py "
                "--input_path mat_test_files/{0} \
                --modulation {1} \
                --nLdpc {2} \
                --code_rate {3} \
                --output_path {4}".format(
                    mat_file_name, modulation_type, ldpc_value, crv, output_file
                )
            ).read()
            with open("result.txt", "a") as result_file:
                result_file.write(match_result + "\n")

            if "Match: False" in match_result:
                print(
                    "{}{}Error{}: \tIncorrect output generated.\n"
                    "\t\tFile name: {}\n "
                    "\t\tModulation type: {}\n "
                    "\t\tLDPC value: {}\n "
                    "\t\tCode rate value: {}".format(
                        "\033[1m",
                        "\033[91m",
                        "\033[0m",
                        mat_file_name,
                        modulation_type,
                        ldpc_value,
                        crv,
                    )
                )


if __name__ == "__main__":
    main()
