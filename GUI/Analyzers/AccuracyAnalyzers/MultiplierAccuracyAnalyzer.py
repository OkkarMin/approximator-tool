import ApproxMultipliers
from GUI.Utils.PrintToDebugWindow import print


def analyze(user_chosen_options):
    multiplicand_bits = user_chosen_options["multiplicand_bits"]
    multiplier_bits = user_chosen_options["multiplier_bits"]
    multiplier_first_unsigned_number = user_chosen_options[
        "multiplier_first_unsigned_number"
    ]
    multiplier_second_unsigned_number = user_chosen_options[
        "multiplier_second_unsigned_number"
    ]
    v_cut = user_chosen_options["v_cut"]

    accurate_multiplier_product = ApproxMultipliers.accurate_array_multiplier(
        multiplier_first_unsigned_number,
        multiplier_second_unsigned_number,
        multiplicand_bits,
        multiplier_bits,
    )

    inaccurate_multiplier_product = ApproxMultipliers.PAAM01(
        multiplier_first_unsigned_number,
        multiplier_second_unsigned_number,
        multiplicand_bits,
        multiplier_bits,
        v_cut,
    )

    inaccurate_multiplier_accuracy = (
        1
        - (
            abs(accurate_multiplier_product - inaccurate_multiplier_product)
            / accurate_multiplier_product
        )
    ) * 100

    print_analysis(
        accurate_multiplier_product,
        inaccurate_multiplier_product,
        inaccurate_multiplier_accuracy,
    )


def print_analysis(
    accurate_multiplier_product,
    inaccurate_multiplier_product,
    inaccurate_multiplier_accuracy,
):
    print("\nAccurate Multiplier Product:\t", accurate_multiplier_product, "\n")
    print("\nAAM01-Vcut Multiplier Product:\t", inaccurate_multiplier_product, "\n")
    print(
        "\nAAM01-Vcut Multiplier Accuracy %:\t", inaccurate_multiplier_accuracy, "\n"
    )
