import AdderError
import MultiplierError

from timeit import default_timer as timer
from datetime import timedelta


def ApproxAdderError():
    exit_flag = 0
    while True:
        print("Types of Approximate Adders-")
        print("1. HEAA ")
        print("2. HOERAA ")
        print("3. HOAANED ")
        print("4. M-HERLOA ")

        total_num_adder_types = 4

        print("p. Previous Menu")
        print("q. Quit")
        print()

        adder_type_inp = input("Enter the Adder type - \t")
        if adder_type_inp == "q" or adder_type_inp == "Q":
            exit_flag = 1
            break
        elif adder_type_inp == "p" or adder_type_inp == "P":
            exit_flag = 0
            break

        elif (
            adder_type_inp.isnumeric()
            and int(adder_type_inp) >= 1
            and int(adder_type_inp) <= total_num_adder_types
        ):
            NumAdderBits = input("Enter total number of adder bits - \t")
            num_bits = int(NumAdderBits)
            print()
            if num_bits < 4:
                print(
                    "\nWARNING - Total number of adder bits should greater than or equal to 4 ! Please try again!\n"
                )
                continue
            inaccurate_bits_str = input("Enter number of inaccurate bits - \t")
            num_inacc_bits = int(inaccurate_bits_str)
            if num_inacc_bits > num_bits - 1 or num_inacc_bits < 3:
                print(
                    "\nWARNING - The number of inaccurate bits should lie between 3 and "
                    + str(num_bits - 1)
                    + "! Please try again!\n"
                )
                continue

            start = timer()

            if adder_type_inp == "1":
                AdderError.HEAA(num_bits, num_inacc_bits)

            elif adder_type_inp == "2":
                AdderError.HOERAA(num_bits, num_inacc_bits)

            elif adder_type_inp == "3":
                AdderError.HOAANED(num_bits, num_inacc_bits)

            elif adder_type_inp == "4":
                AdderError.M_HERLOA(num_bits, num_inacc_bits)

            end = timer()

            print(
                "\nTime taken to generate Verilog code = ",
                timedelta(seconds=end - start),
                " seconds",
            )

        else:
            print("\nWARNING - Invalid adder type (Please enter correct adder type)\n")
            continue

        if exit_flag == 1:
            break
    return exit_flag


def ApproxMultiplierError():
    exit_flag = 0
    while True:
        print("Types of Approximate Multipliers-")
        print("1. PAAM01 ")

        total_num_multiplier_types = 1

        print("p. Previous Menu")
        print("q. Quit")
        print()

        multiplier_type_inp = input("Enter the Multiplier type - \t")
        if multiplier_type_inp == "q" or multiplier_type_inp == "Q":
            exit_flag = 1
            break
        elif multiplier_type_inp == "p" or multiplier_type_inp == "P":
            exit_flag = 0
            break

        elif (
            multiplier_type_inp.isnumeric()
            and int(multiplier_type_inp) >= 1
            and int(multiplier_type_inp) <= total_num_multiplier_types
        ):
            N1_str = input("Enter total number of multiplicand bits - \t")
            N1 = int(N1_str)
            print()
            N2_str = input("Enter total number of multiplier bits - \t")
            N2 = int(N2_str)
            print()

            if N1 < 3 or N2 < 3:
                print(
                    "\nWARNING - Total number of multiplicand and multiplier bits \n \
                should greater than or equal to 3 ! Please try again!\n"
                )
                continue

            if multiplier_type_inp == "1":
                V_val_str = input("Enter position of V-cut - \t")
                V_val = int(V_val_str)
                if V_val > (N1 + N2 - 3) or V_val < 0:
                    print(
                        "\nWARNING - The position of V-cut should lie between 0 and "
                        + str(N1 + N2 - 3)
                        + "! Please try again!\n"
                    )
                    continue

                start = timer()

                MultiplierError.PAAM01_VCut(N1, N2, V_val)

                end = timer()

                print(
                    "\nTime taken to generate Verilog code = ",
                    timedelta(seconds=end - start),
                    " seconds",
                )
            # We can add elif statement here if we use more multiplier types other than PAAM01-Vcut later on

        else:
            print(
                "\nWARNING - Invalid multiplier type (Please enter correct multiplier type)\n"
            )
            continue

        if exit_flag == 1:
            break
    return exit_flag


def runError():

    exit_flag = 0

    while True:
        print("Types of Computational Circuit:\t")
        print("1. Approximate Adder Error Analysis")
        print("2. Approximate Multiplier Error Analysis")
        print("p. Previous Menu")
        print("q. Quit")
        print()
        user_inp = input("Enter your choice - \t")

        if user_inp == "1":
            exit_flag = ApproxAdderError()
        elif user_inp == "2":
            exit_flag = ApproxMultiplierError()
        elif user_inp == "p" or user_inp == "P":
            exit_flag = 0
            break
        elif user_inp == "q" or user_inp == "Q":
            exit_flag = 1
            break
        else:
            print("\nWARNING: Invalid choice. Please enter a valid choice\n")

        if exit_flag == 1:
            break

    return exit_flag
