import random
import math
import ApproxMultipliers
import PySimpleGUI as sg

## Multiplier error calculations (AE, MAE, RMSE)

# Error Calculation for PAAM01 Multiplier with different V-cuts


def print(*args):
    sg.Print(*args, font='Helvetica 15')


def PAAM01_VCut(N1, N2, V_val):
    PAAM01_VCut_estimate_AE = 0.0
    PAAM01_VCut_estimate_MAE = 0.0
    PAAM01_VCut_estimate_RMSE = 0.0

    if (N1 <= 10 and N2 <= 10):
        print("\n Performing Accurate Error Anaylsis...\n")

        for num1 in range(2**N1):
            for num2 in range(2**N2):
                accurate_product = ApproxMultipliers.accurate_array_multiplier(
                    num1, num2, N1, N2)
                PAAM01_VCut_product = ApproxMultipliers.PAAM01(
                    num1, num2, N1, N2, V_val)
                PAAM01_VCut_estimate_AE += (PAAM01_VCut_product -
                                            accurate_product)
                PAAM01_VCut_estimate_MAE += abs(PAAM01_VCut_product -
                                                accurate_product)
                PAAM01_VCut_estimate_RMSE += (PAAM01_VCut_product -
                                              accurate_product)**2

        PAAM01_VCut_estimate_AE /= (2**(N1 + N2))
        print()
        print('PAAM01 VCut=', V_val, 'average error', PAAM01_VCut_estimate_AE)
        print()

        PAAM01_VCut_estimate_MAE /= (2**(N1 + N2))
        print('PAAM01 VCut=', V_val, 'mean absolute error',
              PAAM01_VCut_estimate_MAE)
        print()

        PAAM01_VCut_estimate_RMSE /= (2**(N1 + N2))
        PAAM01_VCut_estimate_RMSE = math.sqrt(PAAM01_VCut_estimate_RMSE)
        print('PAAM01 VCut=', V_val, 'Root Mean Square Error',
              PAAM01_VCut_estimate_RMSE)
        print()

    else:
        print("\n Since atleast one of the two input is >10 bits, \n \
        Approximate Error Anaylsis is performed\n \
        using million random input combinations...\n")
        num_rand_values = 1000000
        for it1 in range(num_rand_values):
            num1 = random.randrange(2**N1)
            num2 = random.randrange(2**N2)
            accurate_product = ApproxMultipliers.accurate_array_multiplier(
                num1, num2, N1, N2)
            PAAM01_VCut_product = ApproxMultipliers.PAAM01(
                num1, num2, N1, N2, V_val)
            PAAM01_VCut_estimate_AE += (PAAM01_VCut_product - accurate_product)
            PAAM01_VCut_estimate_MAE += abs(PAAM01_VCut_product -
                                            accurate_product)
            PAAM01_VCut_estimate_RMSE += (PAAM01_VCut_product -
                                          accurate_product)**2

        PAAM01_VCut_estimate_AE /= num_rand_values
        print()
        print('PAAM01 VCut=', V_val, 'average error', PAAM01_VCut_estimate_AE)
        print()

        PAAM01_VCut_estimate_MAE /= num_rand_values
        print('PAAM01 VCut=', V_val, 'mean absolute error',
              PAAM01_VCut_estimate_MAE)
        print()

        PAAM01_VCut_estimate_RMSE /= num_rand_values
        PAAM01_VCut_estimate_RMSE = math.sqrt(PAAM01_VCut_estimate_RMSE)
        print('PAAM01 VCut=', V_val, 'Root Mean Square Error',
              PAAM01_VCut_estimate_RMSE)
        print()
