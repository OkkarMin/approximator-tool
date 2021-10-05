import ApproxAdders
from GUI.Utils.PrintToDebugWindow import print


def analyze(user_chosen_options):
    (
        inacc_bits,
        total_bits,
        adder_first_unsigned_number,
        adder_second_unsigned_number,
        type_of_accuracy_analysis_hardware,
    ) = extract_options(user_chosen_options)

    accurate_adder_sum = ApproxAdders.accurate_adder(
        adder_first_unsigned_number, adder_second_unsigned_number, total_bits
    )

    inaccurate_adder_sum = getattr(
        ApproxAdders, f"{type_of_accuracy_analysis_hardware}_approx"
    )(adder_first_unsigned_number, adder_second_unsigned_number, total_bits, inacc_bits)

    inaccurate_adder_accuracy = (
        1 - (abs(accurate_adder_sum - inaccurate_adder_sum) / accurate_adder_sum)
    ) * 100

    print_analysis(
        accurate_adder_sum,
        inaccurate_adder_sum,
        inaccurate_adder_accuracy,
        type_of_accuracy_analysis_hardware,
    )


def extract_options(user_chosen_options):
    inacc_bits = user_chosen_options["inacc_bits"]
    total_bits = user_chosen_options["total_bits"]
    adder_first_unsigned_number = user_chosen_options["adder_first_unsigned_number"]
    adder_second_unsigned_number = user_chosen_options["adder_second_unsigned_number"]
    type_of_accuracy_analysis_hardware = user_chosen_options[
        "type_of_accuracy_analysis_hardware"
    ]
    return (
        inacc_bits,
        total_bits,
        adder_first_unsigned_number,
        adder_second_unsigned_number,
        type_of_accuracy_analysis_hardware,
    )


def print_analysis(
    accurate_adder_sum,
    inaccurate_adder_sum,
    inaccurate_adder_accuracy,
    type_of_accuracy_analysis_hardware,
):
    print("\nAccurate Adder Sum:\t", accurate_adder_sum, "\n")
    print(
        f"\n{type_of_accuracy_analysis_hardware} Adder Sum:\t",
        inaccurate_adder_sum,
        "\n",
    )
    print(
        f"\n{type_of_accuracy_analysis_hardware} Adder Accuracy %:\t",
        inaccurate_adder_accuracy,
        "\n",
    )
