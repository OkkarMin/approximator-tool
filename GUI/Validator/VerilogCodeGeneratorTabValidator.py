class VerilogCodeGeneratorTabValidator:
    def execute_validation(user_chosen_options):
        is_valid = True
        error_message = ""

        # Extract variables from user_chosen_options dict
        acc_bits = user_chosen_options["acc_bits"]
        inacc_bits = user_chosen_options["inacc_bits"]
        multiplicand_bits = user_chosen_options["multiplicand_bits"]
        multiplier_bits = user_chosen_options["multiplier_bits"]
        total_bits = user_chosen_options["total_bits"]
        type_of_hardware_module = user_chosen_options["type_of_hardware_module"]
        type_of_verilog_code = user_chosen_options["type_of_verilog_code"]
        v_cut = user_chosen_options["v_cut"]
        adder_value_error = user_chosen_options["adder_value_error"]
        multiplier_value_error = user_chosen_options["multiplier_value_error"]
        vcut_value_error = user_chosen_options["vcut_value_error"]
        # Determine type of adder accurate or inaccurate
        accurate_adder = (
            True
            if (
                type_of_verilog_code == "FPGA_Based_VerilogAdder"
                and type_of_hardware_module == "Accurate Adder"
            )
            else False
        )

        inaccurate_adder = (
            True
            if (
                type_of_verilog_code == "ASIC_Based_VerilogAdder"
                or type_of_verilog_code == "FPGA_Based_VerilogAdder"
                and not type_of_hardware_module == "Accurate Adder"
            )
            else False
        )

        approx_multiplier = (
            True
            if (
                type_of_verilog_code == 'ASIC_Based_VerilogMultiplier'
            )
            else False
        )

        # Accurate Adder inputs must be integer
        if accurate_adder and adder_value_error==1:
            is_valid = False
            error_message = "Inputs filled by the user must be integer"
        
        # Accurate Adder should have total_bits >= 1
        elif accurate_adder and not total_bits >= 1:
            is_valid = False
            error_message = "Total bits should be >= 1 for Accurate Adders"

        # Inccurate Adder inputs must be integer
        elif inaccurate_adder and adder_value_error==1:
            is_valid = False
            error_message = "Inputs filled by the user must be integer"
        # Inaccurate Adders should have total_bits >= 4
        elif inaccurate_adder and not total_bits >= 4:
            is_valid = False
            error_message = "Total bits should be >= 4 for Inaccurate Adders"

        # Inaccurate Adders should have inacc_bits >=3 but <= total_bits - 1
        elif inaccurate_adder and not (3 <= inacc_bits <= total_bits - 1):
            is_valid = False
            error_message = "Inaccurate bits should be >= 3 but <= Total bits-1"

        elif approx_multiplier and multiplier_value_error==1:
            is_valid = False
            error_message = "Inputs filled by the user must be integer" 

        # Total multiplicand bits and multiplier bits should be >=3
        
        elif approx_multiplier and not (multiplicand_bits >= 3 and multiplier_bits >= 3):
            is_valid = False
            error_message = (
                "Total Multiplicand bits and Total Multiplier bits should be >= 3"
            )
        elif type_of_hardware_module == "MxN AAM01 with V-cut" and vcut_value_error==1:
            is_valid = False
            error_message = "Inputs filled by the user must be integer" 
        # V-cut should be > 0 but <= multiplicand_bits
        elif type_of_hardware_module == "MxN AAM01 with V-cut" and not (
            0 < v_cut <= (multiplicand_bits + multiplier_bits - 3)
        ):
            is_valid = False
            error_message = "V-cut should be > 0 but <= (Total Multiplicand bits + Total Multiplier bits - 3) "

        return is_valid, error_message
