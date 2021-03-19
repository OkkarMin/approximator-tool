import random
import math
import ApproxAdders
from GUI.Utils.PrintToDebugWindow import print
## Error Calculations (AE, MAE, RMSE)

# HEAA


def HEAA(tot_num_bits, inaccurate_bits):
    HEAA_estimate_AE = 0.0
    HEAA_estimate_MAE = 0.0
    HEAA_estimate_RMSE = 0.0

    if (tot_num_bits <= 10):
        print("\n Performing Accurate Error Anaylsis...\n")

        for num1 in range(2**tot_num_bits):
            for num2 in range(2**tot_num_bits):
                accurate_sum = ApproxAdders.accurate_adder(
                    num1, num2, tot_num_bits)
                HEAA_estimate_sum = ApproxAdders.HEAA_approx(
                    num1, num2, tot_num_bits, inaccurate_bits)
                HEAA_estimate_AE += (HEAA_estimate_sum - accurate_sum)
                HEAA_estimate_MAE += abs(HEAA_estimate_sum - accurate_sum)
                HEAA_estimate_RMSE += (HEAA_estimate_sum - accurate_sum)**2

        HEAA_estimate_AE /= (2**(2 * tot_num_bits))
        print()
        print('HEAA average error', HEAA_estimate_AE)
        print()

        HEAA_estimate_MAE /= (2**(2 * tot_num_bits))
        print('HEAA mean absolute error', HEAA_estimate_MAE)
        print()

        HEAA_estimate_RMSE /= (2**(2 * tot_num_bits))
        HEAA_estimate_RMSE = math.sqrt(HEAA_estimate_RMSE)
        print('HEAA Root Mean Square Error', HEAA_estimate_RMSE)
        print()

    else:
        print("\n Since Total Number of bits>10, \n \
        Approximate Error Anaylsis is performed\n \
        using million random input combinations...\n")
        num_rand_values = 1000000
        for it1 in range(num_rand_values):
            num1 = random.randrange(2**tot_num_bits)
            num2 = random.randrange(2**tot_num_bits)
            accurate_sum = ApproxAdders.accurate_adder(num1, num2,
                                                       tot_num_bits)
            HEAA_estimate_sum = ApproxAdders.HEAA_approx(
                num1, num2, tot_num_bits, inaccurate_bits)
            HEAA_estimate_AE += (HEAA_estimate_sum - accurate_sum)
            HEAA_estimate_MAE += abs(HEAA_estimate_sum - accurate_sum)
            HEAA_estimate_RMSE += (HEAA_estimate_sum - accurate_sum)**2
        HEAA_estimate_AE /= num_rand_values
        print()
        print('HEAA average error', HEAA_estimate_AE)
        print()

        HEAA_estimate_MAE /= num_rand_values
        print('HEAA mean absolute error', HEAA_estimate_MAE)
        print()

        HEAA_estimate_RMSE /= num_rand_values
        HEAA_estimate_RMSE = math.sqrt(HEAA_estimate_RMSE)
        print('HEAA Root Mean Square Error', HEAA_estimate_RMSE)
        print()


# HOERAA


def HOERAA(tot_num_bits, inaccurate_bits):
    HOERAA_estimate_AE = 0.0
    HOERAA_estimate_MAE = 0.0
    HOERAA_estimate_RMSE = 0.0

    if (tot_num_bits <= 10):
        print("\n Performing Accurate Error Anaylsis...\n")

        for num1 in range(2**tot_num_bits):
            for num2 in range(2**tot_num_bits):
                accurate_sum = ApproxAdders.accurate_adder(
                    num1, num2, tot_num_bits)
                HOERAA_estimate_sum = ApproxAdders.HOERAA_approx(
                    num1, num2, tot_num_bits, inaccurate_bits)
                HOERAA_estimate_AE += (HOERAA_estimate_sum - accurate_sum)
                HOERAA_estimate_MAE += abs(HOERAA_estimate_sum - accurate_sum)
                HOERAA_estimate_RMSE += (HOERAA_estimate_sum - accurate_sum)**2

        HOERAA_estimate_AE /= (2**(2 * tot_num_bits))
        print()
        print('HOERAA average error', HOERAA_estimate_AE)
        print()

        HOERAA_estimate_MAE /= (2**(2 * tot_num_bits))
        print('HOERAA mean absolute error', HOERAA_estimate_MAE)
        print()

        HOERAA_estimate_RMSE /= (2**(2 * tot_num_bits))
        HOERAA_estimate_RMSE = math.sqrt(HOERAA_estimate_RMSE)
        print('HOERAA Root Mean Square Error', HOERAA_estimate_RMSE)
        print()

    else:
        print("\n Since Total Number of bits>10, \n \
        Approximate Error Anaylsis is performed\n \
        using million random input combinations...\n")
        num_rand_values = 1000000
        for it1 in range(num_rand_values):
            num1 = random.randrange(2**tot_num_bits)
            num2 = random.randrange(2**tot_num_bits)
            accurate_sum = ApproxAdders.accurate_adder(num1, num2,
                                                       tot_num_bits)
            HOERAA_estimate_sum = ApproxAdders.HOERAA_approx(
                num1, num2, tot_num_bits, inaccurate_bits)
            HOERAA_estimate_AE += (HOERAA_estimate_sum - accurate_sum)
            HOERAA_estimate_MAE += abs(HOERAA_estimate_sum - accurate_sum)
            HOERAA_estimate_RMSE += (HOERAA_estimate_sum - accurate_sum)**2
        HOERAA_estimate_AE /= num_rand_values
        print()
        print('HOERAA average error', HOERAA_estimate_AE)
        print()

        HOERAA_estimate_MAE /= num_rand_values
        print('HOERAA mean absolute error', HOERAA_estimate_MAE)
        print()

        HOERAA_estimate_RMSE /= num_rand_values
        HOERAA_estimate_RMSE = math.sqrt(HOERAA_estimate_RMSE)
        print('HOERAA Root Mean Square Error', HOERAA_estimate_RMSE)
        print()


# HOAANED


def HOAANED(tot_num_bits, inaccurate_bits):
    HOAANED_estimate_AE = 0.0
    HOAANED_estimate_MAE = 0.0
    HOAANED_estimate_RMSE = 0.0

    if (tot_num_bits <= 10):
        print("\n Performing Accurate Error Anaylsis...\n")

        for num1 in range(2**tot_num_bits):
            for num2 in range(2**tot_num_bits):
                accurate_sum = ApproxAdders.accurate_adder(
                    num1, num2, tot_num_bits)
                HOAANED_estimate_sum = ApproxAdders.HOAANED_approx(
                    num1, num2, tot_num_bits, inaccurate_bits)
                HOAANED_estimate_AE += (HOAANED_estimate_sum - accurate_sum)
                HOAANED_estimate_MAE += abs(HOAANED_estimate_sum -
                                            accurate_sum)
                HOAANED_estimate_RMSE += (HOAANED_estimate_sum -
                                          accurate_sum)**2

        HOAANED_estimate_AE /= (2**(2 * tot_num_bits))
        print()
        print('HOAANED average error', HOAANED_estimate_AE)
        print()

        HOAANED_estimate_MAE /= (2**(2 * tot_num_bits))
        print('HOAANED mean absolute error', HOAANED_estimate_MAE)
        print()

        HOAANED_estimate_RMSE /= (2**(2 * tot_num_bits))
        HOAANED_estimate_RMSE = math.sqrt(HOAANED_estimate_RMSE)
        print('HOAANED Root Mean Square Error', HOAANED_estimate_RMSE)
        print()

    else:
        print("\n Since Total Number of bits>10, \n \
        Approximate Error Anaylsis is performed\n \
        using million random input combinations...\n")
        num_rand_values = 1000000
        for it1 in range(num_rand_values):
            num1 = random.randrange(2**tot_num_bits)
            num2 = random.randrange(2**tot_num_bits)
            accurate_sum = ApproxAdders.accurate_adder(num1, num2,
                                                       tot_num_bits)
            HOAANED_estimate_sum = ApproxAdders.HOAANED_approx(
                num1, num2, tot_num_bits, inaccurate_bits)
            HOAANED_estimate_AE += (HOAANED_estimate_sum - accurate_sum)
            HOAANED_estimate_MAE += abs(HOAANED_estimate_sum - accurate_sum)
            HOAANED_estimate_RMSE += (HOAANED_estimate_sum - accurate_sum)**2
        HOAANED_estimate_AE /= num_rand_values
        print()
        print('HOAANED average error', HOAANED_estimate_AE)
        print()

        HOAANED_estimate_MAE /= num_rand_values
        print('HOAANED mean absolute error', HOAANED_estimate_MAE)
        print()

        HOAANED_estimate_RMSE /= num_rand_values
        HOAANED_estimate_RMSE = math.sqrt(HOAANED_estimate_RMSE)
        print('HOAANED Root Mean Square Error', HOAANED_estimate_RMSE)
        print()


# M-HERLOA


def M_HERLOA(tot_num_bits, inaccurate_bits):
    M_HERLOA_estimate_AE = 0.0
    M_HERLOA_estimate_MAE = 0.0
    M_HERLOA_estimate_RMSE = 0.0

    if (tot_num_bits <= 10):
        print("\n Performing Accurate Error Anaylsis...\n")

        for num1 in range(2**tot_num_bits):
            for num2 in range(2**tot_num_bits):
                accurate_sum = ApproxAdders.accurate_adder(
                    num1, num2, tot_num_bits)
                M_HERLOA_estimate_sum = ApproxAdders.M_HERLOA_approx(
                    num1, num2, tot_num_bits, inaccurate_bits)
                M_HERLOA_estimate_AE += (M_HERLOA_estimate_sum - accurate_sum)
                M_HERLOA_estimate_MAE += abs(M_HERLOA_estimate_sum -
                                             accurate_sum)
                M_HERLOA_estimate_RMSE += (M_HERLOA_estimate_sum -
                                           accurate_sum)**2

        M_HERLOA_estimate_AE /= (2**(2 * tot_num_bits))
        print()
        print('M_HERLOA average error', M_HERLOA_estimate_AE)
        print()

        M_HERLOA_estimate_MAE /= (2**(2 * tot_num_bits))
        print('M_HERLOA mean absolute error', M_HERLOA_estimate_MAE)
        print()

        M_HERLOA_estimate_RMSE /= (2**(2 * tot_num_bits))
        M_HERLOA_estimate_RMSE = math.sqrt(M_HERLOA_estimate_RMSE)
        print('M_HERLOA Root Mean Square Error', M_HERLOA_estimate_RMSE)
        print()

    else:
        print("\n Since Total Number of bits>10, \n \
        Approximate Error Anaylsis is performed\n \
        using million random input combinations...\n")
        num_rand_values = 1000000
        for it1 in range(num_rand_values):
            num1 = random.randrange(2**tot_num_bits)
            num2 = random.randrange(2**tot_num_bits)
            accurate_sum = ApproxAdders.accurate_adder(num1, num2,
                                                       tot_num_bits)
            M_HERLOA_estimate_sum = ApproxAdders.M_HERLOA_approx(
                num1, num2, tot_num_bits, inaccurate_bits)
            M_HERLOA_estimate_AE += (M_HERLOA_estimate_sum - accurate_sum)
            M_HERLOA_estimate_MAE += abs(M_HERLOA_estimate_sum - accurate_sum)
            M_HERLOA_estimate_RMSE += (M_HERLOA_estimate_sum - accurate_sum)**2
        M_HERLOA_estimate_AE /= num_rand_values
        print()
        print('M_HERLOA average error', M_HERLOA_estimate_AE)
        print()

        M_HERLOA_estimate_MAE /= num_rand_values
        print('M_HERLOA mean absolute error', M_HERLOA_estimate_MAE)
        print()

        M_HERLOA_estimate_RMSE /= num_rand_values
        M_HERLOA_estimate_RMSE = math.sqrt(M_HERLOA_estimate_RMSE)
        print('M_HERLOA Root Mean Square Error', M_HERLOA_estimate_RMSE)
        print()
