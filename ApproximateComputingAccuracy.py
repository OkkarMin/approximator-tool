import ApproxAdders
import ApproxMultipliers


def ApproxAdderAccuracy():
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

            num1_str = input("Enter the first number to be added (unsigned) - \t")
            num1 = int(num1_str)
            if num1 > (2 ** num_bits - 1) or num1 < 0:
                print(
                    "\nWARNING - The number should lie between 0 and "
                    + str(2 ** num_bits - 1)
                    + "! Please try again!\n"
                )
                continue

            num2_str = input("Enter the second number to be added (unsigned) - \t")
            num2 = int(num2_str)
            if num2 > (2 ** num_bits - 1) or num2 < 0:
                print(
                    "\nWARNING - The number should lie between 0 and "
                    + str(2 ** num_bits - 1)
                    + "! Please try again!\n"
                )
                continue

            accurate_sum = ApproxAdders.accurate_adder(num1, num2, num_bits)
            print("\nAccurate Adder Sum:\t", accurate_sum, "\n")

            if adder_type_inp == "1":
                HEAA_sum = ApproxAdders.HEAA_approx(
                    num1, num2, num_bits, num_inacc_bits
                )
                print("\nHEAA Approx Adder Sum:\t", HEAA_sum, "\n")
                HEAA_Accuracy = (
                    1 - (abs(accurate_sum - HEAA_sum) / (accurate_sum))
                ) * 100
                if HEAA_Accuracy < 0:
                    HEAA_Accuracy = 0
                print("\nHEAA Approx Adder Accuracy:\t", HEAA_Accuracy, "\n")

            elif adder_type_inp == "2":
                HOERAA_sum = ApproxAdders.HOERAA_approx(
                    num1, num2, num_bits, num_inacc_bits
                )
                print("\nHOERAA Approx Adder Sum:\t", HOERAA_sum, "\n")
                HOERAA_Accuracy = (
                    1 - (abs(accurate_sum - HOERAA_sum) / (accurate_sum))
                ) * 100
                if HOERAA_Accuracy < 0:
                    HOERAA_Accuracy = 0
                print("\nHOERAA Approx Adder Accuracy:\t", HOERAA_Accuracy, "\n")

            elif adder_type_inp == "3":
                HOAANED_sum = ApproxAdders.HOAANED_approx(
                    num1, num2, num_bits, num_inacc_bits
                )
                print("\nHOAANED Approx Adder Sum:\t", HOAANED_sum, "\n")
                HOAANED_Accuracy = (
                    1 - (abs(accurate_sum - HOAANED_sum) / (accurate_sum))
                ) * 100
                if HOAANED_Accuracy < 0:
                    HOAANED_Accuracy = 0
                print("\nHOAANED Approx Adder Accuracy:\t", HOAANED_Accuracy, "\n")

            elif adder_type_inp == "4":
                M_HERLOA_sum = ApproxAdders.M_HERLOA_approx(
                    num1, num2, num_bits, num_inacc_bits
                )
                print("\nM-HERLOA Approx Adder Sum:\t", M_HERLOA_sum, "\n")
                M_HERLOA_Accuracy = (
                    1 - (abs(accurate_sum - M_HERLOA_sum) / (accurate_sum))
                ) * 100
                if M_HERLOA_Accuracy < 0:
                    M_HERLOA_Accuracy = 0
                print("\nM-HERLOA Approx Adder Accuracy:\t", M_HERLOA_Accuracy, "\n")

        else:
            print("\nWARNING - Invalid adder type (Please enter correct adder type)\n")
            continue

        if exit_flag == 1:
            break
    return exit_flag


def ApproxMultiplierAccuracy():
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

            num1_str = input("Enter the first number to be added (unsigned) - \t")
            num1 = int(num1_str)
            if num1 > (2 ** N1 - 1) or num1 < 0:
                print(
                    "\nWARNING - The number should lie between 0 and "
                    + str(2 ** N1 - 1)
                    + "! Please try again!\n"
                )
                continue

            num2_str = input("Enter the second number to be added (unsigned) - \t")
            num2 = int(num2_str)
            if num2 > (2 ** N2 - 1) or num2 < 0:
                print(
                    "\nWARNING - The number should lie between 0 and "
                    + str(2 ** N2 - 1)
                    + "! Please try again!\n"
                )
                continue

            accurate_product = ApproxMultipliers.accurate_array_multiplier(
                num1, num2, N1, N2
            )
            print("\nAccurate Multiplier Product:\t", accurate_product, "\n")

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

                PAAM01_VCut_product = ApproxMultipliers.PAAM01(
                    num1, num2, N1, N2, V_val
                )
                print(
                    "\nPAAM01-Vcut Approx Multiplier Product:\t",
                    PAAM01_VCut_product,
                    "\n",
                )
                PAAM01_VCut_Accuracy = (
                    1
                    - (abs(accurate_product - PAAM01_VCut_product) / (accurate_product))
                ) * 100
                if PAAM01_VCut_Accuracy < 0:
                    PAAM01_VCut_Accuracy = 0
                print(
                    "\nPAAM01-Vcut Approx Multiplier Accuracy:\t",
                    PAAM01_VCut_Accuracy,
                    "\n",
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


def runAccuracy():

    exit_flag = 0

    while True:
        print("Types of Computational Circuit:\t")
        print("1. Approximate Adder Accuracy Analysis")
        print("2. Approximate Multiplier Accuracy Analysis")
        print("p. Previous Menu")
        print("q. Quit")
        print()
        user_inp = input("Enter your choice - \t")

        if user_inp == "1":
            exit_flag = ApproxAdderAccuracy()
        elif user_inp == "2":
            exit_flag = ApproxMultiplierAccuracy()
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
