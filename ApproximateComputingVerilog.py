import pyverilog.vparser.ast as vast
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
import AdderSumCalc
import VerilogStructuralAdder
import VerilogMultiplierCode

from timeit import default_timer as timer
from datetime import timedelta


def FPGA_Based_VerilogAdder():  # FPGA Based Verilog Adder (Generalized Adder)
    exit_flag = 0
    while True:
        print("Types of Approximate Adders-")
        print("1. Accurate Adder")
        print("2. HEAA")
        print("3. HOERAA")
        print("4. HOAANED")
        print("5. M-HERLOA")

        total_num_adder_types = 5

        print("p. Previous Menu")
        print("q. Quit")
        print()

        adder_type_inp = input("Enter the adder type - \t")
        print()
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

            if adder_type_inp == "1":
                if num_bits < 1:
                    print(
                        "\nWARNING - Total number of adder bits should greater than or equal to 1 ! Please try again!\n"
                    )
                    continue
                AdderType = "Accurate_Adder"
            else:
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
                if adder_type_inp == "2":
                    AdderType = "HEAA_Adder"
                elif adder_type_inp == "3":
                    AdderType = "HOERAA_Adder"
                elif adder_type_inp == "4":
                    AdderType = "HOAANED_Adder"
                elif adder_type_inp == "5":
                    AdderType = "M_HERLOA_Adder"
        else:
            print("\nWARNING - Invalid adder type (Please enter correct adder type)\n")
            continue

        #    AdderType='HOERAA_Adder';
        #    num_bits=32;
        #    num_inacc_bits=8;
        inp_a = "a"
        inp_b = "b"
        input_clk = "clk"
        output_sum = "sum"

        paramlist = vast.Paramlist(())

        if num_bits > 1:
            a_vec = vast.Ioport(
                vast.Input(
                    inp_a,
                    vast.Width(vast.IntConst(ascii(num_bits - 1)), vast.IntConst("0")),
                )
            )
            b_vec = vast.Ioport(
                vast.Input(
                    inp_b,
                    vast.Width(vast.IntConst(ascii(num_bits - 1)), vast.IntConst("0")),
                )
            )
        elif num_bits == 1:
            a_vec = vast.Ioport(vast.Input(inp_a))
            b_vec = vast.Ioport(vast.Input(inp_b))

        clk = vast.Ioport(vast.Input(input_clk))
        sum_vec = vast.Ioport(
            vast.Output(
                output_sum,
                vast.Width(vast.IntConst(ascii(num_bits)), vast.IntConst("0")),
            ),
            vast.Reg(
                output_sum,
                vast.Width(vast.IntConst(ascii(num_bits)), vast.IntConst("0")),
            ),
        )
        portlist = vast.Portlist([a_vec, b_vec, clk, sum_vec])

        input_a = inp_a + "_inp"
        input_b = inp_b + "_inp"

        if num_bits > 1:
            reginp1 = vast.Reg(
                input_a,
                vast.Width(vast.IntConst(ascii(num_bits - 1)), vast.IntConst("0")),
            )
            reginp2 = vast.Reg(
                input_b,
                vast.Width(vast.IntConst(ascii(num_bits - 1)), vast.IntConst("0")),
            )
        elif num_bits == 1:
            reginp1 = vast.Reg(input_a)
            reginp2 = vast.Reg(input_b)

        reginp = [reginp1, reginp2]

        Left_a = vast.Lvalue(vast.Identifier(input_a))
        Right_a = vast.Rvalue(vast.Identifier(inp_a))
        inp_a_2_reg = vast.NonblockingSubstitution(Left_a, Right_a)

        Left_b = vast.Lvalue(vast.Identifier(input_b))
        Right_b = vast.Rvalue(vast.Identifier(inp_b))
        inp_b_2_reg = vast.NonblockingSubstitution(Left_b, Right_b)

        inp_2_reg = [inp_a_2_reg, inp_b_2_reg]
        item1 = [
            vast.Always(
                vast.Sens(vast.Identifier(input_clk), type="posedge"),
                vast.Block(inp_2_reg),
            )
        ]

        if AdderType == "Accurate_Adder":
            item2 = AdderSumCalc.accurate_sum_calc(
                num_bits, input_a, input_b, input_clk, output_sum
            )
            file = AdderType + "_" + NumAdderBits + "_bits"
        elif AdderType == "HEAA_Adder":
            item2 = AdderSumCalc.HEAA_sum_calc(
                num_bits, num_inacc_bits, input_a, input_b, input_clk, output_sum
            )
        elif AdderType == "HOERAA_Adder":
            item2 = AdderSumCalc.HOERAA_sum_calc(
                num_bits, num_inacc_bits, input_a, input_b, input_clk, output_sum
            )
        elif AdderType == "HOAANED_Adder":
            item2 = AdderSumCalc.HOAANED_sum_calc(
                num_bits, num_inacc_bits, input_a, input_b, input_clk, output_sum
            )
        elif AdderType == "HERLOA_Adder":
            item2 = AdderSumCalc.HERLOA_sum_calc(
                num_bits, num_inacc_bits, input_a, input_b, input_clk, output_sum
            )
        elif AdderType == "M_HERLOA_Adder":
            item2 = AdderSumCalc.M_HERLOA_sum_calc(
                num_bits, num_inacc_bits, input_a, input_b, input_clk, output_sum
            )

        if AdderType == "Accurate_Adder":
            file = AdderType + "_" + NumAdderBits + "_bits"
        else:
            file = (
                AdderType
                + "_"
                + NumAdderBits
                + "_bits_"
                + inaccurate_bits_str
                + "_inacc"
            )

        items = reginp + item1 + item2

        ast = vast.ModuleDef(file, paramlist, portlist, items)

        codegen = ASTCodeGenerator()
        rslt = codegen.visit(ast)
        print(rslt)
        verilog_file = open(file + ".v", "w")
        verilog_file.write(rslt)
        verilog_file.close()

        if exit_flag == 1:
            break
    return exit_flag


def ASIC_Based_VerilogAdder():  # ASIC Based Verilog Adder (Generalized Adder)
    exit_flag = 0
    while True:
        print("Types of Approximate ASIC based Adder codes-")
        print("1. HEAA ")
        # print('1. HEAA (32 bit adder with 10 inaccurate bits');
        print("2. HOERAA")
        # print('2. HOERAA (32 bit adder with 10 inaccurate bits');
        print("3. HOAANED")
        # print('3. HOAANED (32 bit adder with 10 inaccurate bits');
        print("4. M-HERLOA")
        # print('4. M-HERLOA (32 bit adder with 10 inaccurate bits');
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
                verilog_code = VerilogStructuralAdder.HEAA_Generic(
                    num_bits, num_inacc_bits
                ).to_verilog()
                file = "heaa_" + str(num_bits) + "b" + str(num_inacc_bits) + "inacc.v"
                # verilog_code = VerilogStructuralAdder.HEAA_32_bits_10_inaccurate().to_verilog();
                # file='heaa_32b.v';
            elif adder_type_inp == "2":
                verilog_code = VerilogStructuralAdder.HOERAA_Generic(
                    num_bits, num_inacc_bits
                ).to_verilog()
                file = "hoeraa_" + str(num_bits) + "b" + str(num_inacc_bits) + "inacc.v"
            ##                verilog_code = VerilogStructuralAdder.HOERAA_32_bits_10_inaccurate().to_verilog();
            ##                file='hoeraa_32b.v';
            elif adder_type_inp == "3":
                verilog_code = VerilogStructuralAdder.HOAANED_Generic(
                    num_bits, num_inacc_bits
                ).to_verilog()
                file = (
                    "hoaaned_" + str(num_bits) + "b" + str(num_inacc_bits) + "inacc.v"
                )
            ##                verilog_code = VerilogStructuralAdder.HOAANED_32_bits_10_inaccurate().to_verilog();
            ##                file='hoaaned_32b.v';
            elif adder_type_inp == "4":
                verilog_code = VerilogStructuralAdder.M_HERLOA_Generic(
                    num_bits, num_inacc_bits
                ).to_verilog()
                file = (
                    "m_herloa_" + str(num_bits) + "b" + str(num_inacc_bits) + "inacc.v"
                )
            ##                verilog_code = VerilogStructuralAdder.M_HERLOA_32_bits_10_inaccurate().to_verilog();
            ##                file='mherloa_32b.v';
            else:
                print(
                    "\nWARNING - Invalid adder type (Please enter correct adder type)\n"
                )
                continue

        print(verilog_code)
        verilog_file = open(file, "w")
        verilog_file.write(verilog_code)
        verilog_file.close()

        end = timer()

        print(
            "\nTime taken to generate Verilog code = ",
            timedelta(seconds=end - start),
            " seconds",
        )

        if exit_flag == 1:
            break
    return exit_flag


def ASIC_Based_VerilogMultiplier():  # ASIC Based Verilog Multiplier
    # ( Currently only 8x6 and 8x8 multipliers only -
    # Need to generalize later for user defined multiplier size and V-cuts )
    exit_flag = 0
    while True:
        print("Types of Approximate Multiplier-")
        print("1. MxN Accurate Multiplier")
        print("2. MxN Accurate Binary Array Multiplier")
        print("3. MxN AAM01 with V-cut")
        total_num_multiplier_types = 3
        ##        print('1. 8x6 Accurate Multiplier');
        ##        print('2. 8x6 Accurate Binary Array Multiplier');
        ##        print('3. PAAM-01 v0 8x6 Approximate Multiplier');
        ##        print('4. PAAM-01 v1 8x6 Approximate Multiplier');
        ##        print('5. PAAM-01 v2 8x6 Approximate Multiplier');
        ##        print('6. PAAM-01 v3 8x6 Approximate Multiplier');
        ##        print('7. PAAM-01 v4 8x6 Approximate Multiplier');
        ##        print('8. PAAM-01 v5 8x6 Approximate Multiplier');
        ##        print('9. PAAM-01 v6 8x6 Approximate Multiplier');
        ##        print('10. PAAM-01 v7 8x6 Approximate Multiplier');
        ##        print('11. 8x8 Accurate Multiplier');
        ##        print('12. 8x8 Accurate Binary Array Multiplier');
        ##        print('13. PAAM-01 v0 8x8 Approximate Multiplier');
        ##        print('14. PAAM-01 v1 8x8 Approximate Multiplier');
        ##        print('15. PAAM-01 v2 8x8 Approximate Multiplier');
        ##        print('16. PAAM-01 v3 8x8 Approximate Multiplier');
        ##        print('17. PAAM-01 v4 8x8 Approximate Multiplier');
        ##        print('18. PAAM-01 v5 8x8 Approximate Multiplier');
        ##        print('19. PAAM-01 v6 8x8 Approximate Multiplier');
        ##        print('20. PAAM-01 v7 8x8 Approximate Multiplier');
        print("p. Previous Menu")
        print("q. Quit")
        print()
        multiplier_type_inp = input("Enter the multiplier type - \t")
        if multiplier_type_inp == "q" or multiplier_type_inp == "Q":
            exit_flag = 1
            break
        elif multiplier_type_inp == "p" or multiplier_type_inp == "P":
            exit_flag = 0
            break
        else:
            if (
                multiplier_type_inp.isnumeric()
                and int(multiplier_type_inp) >= 1
                and int(multiplier_type_inp) <= total_num_multiplier_types
            ):
                Num_M_Bits = input("Enter total number of multiplicand bits - \t")
                M = int(Num_M_Bits)
                print()
                if M < 3:
                    print(
                        "\nWARNING - Total number of multiplicand bits should greater than or equal to 3 ! Please try again!\n"
                    )
                    continue
                Num_N_Bits = input("Enter total number of multiplier bits - \t")
                N = int(Num_N_Bits)
                print()
                if N < 3:
                    print(
                        "\nWARNING - Total number of multiplier bits should greater than or equal to 3 ! Please try again!\n"
                    )
                    continue

                start = timer()

                if multiplier_type_inp == "1":
                    verilog_code = VerilogMultiplierCode.accurate_MxN_multiplier(
                        M, N
                    ).to_verilog()
                    file = "multiplier_" + str(M) + "x" + str(N) + ".v"
                elif multiplier_type_inp == "2":
                    verilog_code = (
                        VerilogMultiplierCode.accurate_MxN_binary_array_multiplier(
                            M, N
                        ).to_verilog()
                    )
                    file = "bam_" + str(M) + "x" + str(N) + ".v"
                elif multiplier_type_inp == "3":
                    V_cut_str = input(
                        "Enter position of V-cut (between 0 and "
                        + str(M + N - 3)
                        + " both inclusive) - \t"
                    )
                    V_cut = int(V_cut_str)
                    if V_cut > (M + N - 3) or V_cut < 0:
                        print(
                            "\nWARNING - The position of V-cut should lie between 0 and "
                            + str(M + N - 3)
                            + " (both inclusive)! Please try again!\n"
                        )
                        continue
                    verilog_code = (
                        VerilogMultiplierCode.PAAM01_V_cut_MxN_binary_array_multiplier(
                            M, N, V_cut
                        ).to_verilog()
                    )
                    file = (
                        "paam_01_V_" + str(V_cut) + "_" + str(M) + "x" + str(N) + ".v"
                    )

            else:
                print(
                    "\nWARNING - Invalid multiplier type (Please enter correct multiplier type)\n"
                )
                continue

        ##            if(multiplier_type_inp=='1'):
        ##                verilog_code = VerilogMultiplierCode.accurate_8x6_multiplier().to_verilog();
        ##                file='multiplier_8x6.v';
        ##            elif(multiplier_type_inp=='2'):
        ##                verilog_code = VerilogMultiplierCode.accurate_8x6_binary_array_multiplier().to_verilog();
        ##                file='bam_8x6.v';
        ##            elif(multiplier_type_inp=='3'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v0_8x6_multiplier().to_verilog();
        ##                file='paam01_v0_8x6.v';
        ##            elif(multiplier_type_inp=='4'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v1_8x6_multiplier().to_verilog();
        ##                file='paam01_v1_8x6.v';
        ##            elif(multiplier_type_inp=='5'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v2_8x6_multiplier().to_verilog();
        ##                file='paam01_v2_8x6.v';
        ##            elif(multiplier_type_inp=='6'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v3_8x6_multiplier().to_verilog();
        ##                file='paam01_v3_8x6.v';
        ##            elif(multiplier_type_inp=='7'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v4_8x6_multiplier().to_verilog();
        ##                file='paam01_v4_8x6.v';
        ##            elif(multiplier_type_inp=='8'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v5_8x6_multiplier().to_verilog();
        ##                file='paam01_v5_8x6.v';
        ##            elif(multiplier_type_inp=='9'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v6_8x6_multiplier().to_verilog();
        ##                file='paam01_v6_8x6.v';
        ##            elif(multiplier_type_inp=='10'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v7_8x6_multiplier().to_verilog();
        ##                file='paam01_v7_8x6.v';
        ##            elif(multiplier_type_inp=='11'):
        ##                verilog_code = VerilogMultiplierCode.accurate_8x8_multiplier().to_verilog();
        ##                file='multiplier_8x8.v';
        ##            elif(multiplier_type_inp=='12'):
        ##                verilog_code = VerilogMultiplierCode.accurate_8x8_binary_array_multiplier().to_verilog();
        ##                file='bam_8x8.v';
        ##            elif(multiplier_type_inp=='13'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v0_8x8_multiplier().to_verilog();
        ##                file='paam01_v0_8x8.v';
        ##            elif(multiplier_type_inp=='14'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v1_8x8_multiplier().to_verilog();
        ##                file='paam01_v1_8x8.v';
        ##            elif(multiplier_type_inp=='15'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v2_8x8_multiplier().to_verilog();
        ##                file='paam01_v2_8x8.v';
        ##            elif(multiplier_type_inp=='16'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v3_8x8_multiplier().to_verilog();
        ##                file='paam01_v3_8x8.v';
        ##            elif(multiplier_type_inp=='17'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v4_8x8_multiplier().to_verilog();
        ##                file='paam01_v4_8x8.v';
        ##            elif(multiplier_type_inp=='18'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v5_8x8_multiplier().to_verilog();
        ##                file='paam01_v5_8x8.v';
        ##            elif(multiplier_type_inp=='19'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v6_8x8_multiplier().to_verilog();
        ##                file='paam01_v6_8x8.v';
        ##            elif(multiplier_type_inp=='20'):
        ##                verilog_code = VerilogMultiplierCode.paam01_v7_8x8_multiplier().to_verilog();
        ##                file='paam01_v7_8x8.v';

        ##            else:
        ##                print("\nWARNING - Invalid multiplier type (Please enter correct multiplier type)\n");
        ##                continue;

        print(verilog_code)
        verilog_file = open(file, "w")
        verilog_file.write(verilog_code)
        verilog_file.close()

        end = timer()

        print(
            "\nTime taken to generate Verilog code = ",
            timedelta(seconds=end - start),
            " seconds",
        )

        if exit_flag == 1:
            break
    return exit_flag


def runVerilog():

    exit_flag = 0

    while True:
        print("Types of Verilog Codes:\t")
        print("1. FPGA Based Approximate Adder")
        print("2. ASIC Based Approximate Adder")
        print("3. ASIC Based Approximate Multiplier")
        print("p. Previous Menu")
        print("q. Quit")
        print()
        user_inp = input("Enter your choice - \t")

        if user_inp == "1":
            exit_flag = FPGA_Based_VerilogAdder()
        elif user_inp == "2":
            exit_flag = ASIC_Based_VerilogAdder()
        elif user_inp == "3":
            exit_flag = ASIC_Based_VerilogMultiplier()
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
