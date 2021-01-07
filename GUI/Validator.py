def validate(user_chosen_options):
    valid = True
    error_message = ''

    # Extract variables from user_chosen_options dict
    acc_bits = user_chosen_options['acc_bits']
    inacc_bits = user_chosen_options['inacc_bits']
    multiplicand_bits = user_chosen_options['multiplicand_bits']
    multiplier_bits = user_chosen_options['multiplier_bits']
    total_bits = user_chosen_options['total_bits']
    type_of_hardware_module = user_chosen_options['type_of_hardware_module']
    type_of_verilog_code = user_chosen_options['type_of_verilog_code']
    v_cut = user_chosen_options['v_cut']

    # Determine type of adder accurate or inaccurate
    accurate_adder = True if (
        type_of_verilog_code == 'FPGA_Based_VerilogAdder'
        and type_of_hardware_module == 'Accurate Adder') else False
    inaccurate_adder = not accurate_adder

    # Accurate Adder should have total_bits >= 1
    if (accurate_adder and not total_bits >= 1):
        valid = False
        error_message = 'Total bits should be >= 1 for Accurate Adders'

    # Inaccurate Adders should have total_bits >= 4
    if (inaccurate_adder and not total_bits >= 4):
        valid = False
        error_message = 'Total bits should be >= 4 for Inaccurate Adders'

    # Inaccurate Adders should have inacc_bits >=3 but <= total_bits - 1
    if (inaccurate_adder and not (3 <= inacc_bits <= total_bits - 1)):
        valid = False
        error_message = 'Inaccurate bits should be >= 3 but <= Total bits-1'

    # Total multiplicand bits and multiplier bits should be >=3
    if (not (multiplicand_bits >= 3 and multiplier_bits >= 3)):
        valid = False
        error_message = 'Total Multiplicand bits and Total Multiplier bits should be >= 3'

    # V-cut should be > 0 but <= multiplicand_bits
    if (type_of_hardware_module == 'MxN PAAM01 with V-cut'
            and not (0 < v_cut <= multiplicand_bits)):
        valid = False
        error_message = 'V-cut should be >0 but <= Total Multiplicand bits'

    return valid, error_message
