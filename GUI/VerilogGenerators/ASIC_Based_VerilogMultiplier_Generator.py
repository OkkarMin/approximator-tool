import VerilogMultiplierCode


class ASIC_Based_VerilogMultiplier_Generator:
    @staticmethod
    def generate_verilog_code(user_chosen_options):
        # To generate verilog_code, ASIC_Based_VerilogMultiplier_Generator requires
        # type_of_hardware_module ['MxN Accurate Multiplier', 'MxN Accurate Binary Array Multiplier', ...]
        # multiplicand_bits
        # multiplier_bits
        # v_cut (only used for 'MxN PAAM01 with V-Cut)
        type_of_hardware_module = user_chosen_options["type_of_hardware_module"]
        multiplicand_bits = user_chosen_options["multiplicand_bits"]
        multiplier_bits = user_chosen_options["multiplier_bits"]
        v_cut = user_chosen_options["v_cut"]

        verilog_code = None

        if type_of_hardware_module == "MxN Accurate Multiplier":
            verilog_code = VerilogMultiplierCode.accurate_MxN_multiplier(
                multiplicand_bits, multiplier_bits
            ).to_verilog()
        elif type_of_hardware_module == "MxN Accurate Binary Array Multiplier":
            verilog_code = VerilogMultiplierCode.accurate_MxN_binary_array_multiplier(
                multiplicand_bits, multiplier_bits
            ).to_verilog()
        elif type_of_hardware_module == "MxN PAAM01 with V-cut":
            verilog_code = (
                VerilogMultiplierCode.PAAM01_V_cut_MxN_binary_array_multiplier(
                    multiplicand_bits, multiplier_bits, v_cut
                ).to_verilog()
            )

        return verilog_code
