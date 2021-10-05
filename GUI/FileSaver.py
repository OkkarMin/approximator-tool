def save_to_file(verilog_code, user_chosen_options):
    # Extract variables from user_chosen_options dict
    acc_bits = user_chosen_options["acc_bits"]
    inacc_bits = user_chosen_options["inacc_bits"]
    multiplicand_bits = user_chosen_options["multiplicand_bits"]
    multiplier_bits = user_chosen_options["multiplier_bits"]
    total_bits = user_chosen_options["total_bits"]
    type_of_hardware_module = user_chosen_options["type_of_hardware_module"]
    type_of_hardware_module = type_of_hardware_module.replace("-", "_")
    type_of_hardware_module = type_of_hardware_module.replace(" ", "_")
    type_of_verilog_code = user_chosen_options["type_of_verilog_code"]
    v_cut = user_chosen_options["v_cut"]
    folder_to_save_file = user_chosen_options["folder_to_save_file"]

    # Determine accurate/inaccurate adder or multiplier
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

    multiplier = (
        True if (type_of_verilog_code == "ASIC_Based_VerilogMultiplier") else False
    )

    # Prepare full_file_path to save with folder path first
    full_file_path = folder_to_save_file

    # Adder file naming style
    if accurate_adder:
        full_file_path += f"/{type_of_verilog_code}_Accurate_Adder_{total_bits}bits.v"
    elif inaccurate_adder:
        full_file_path += f"/{type_of_verilog_code}_{type_of_hardware_module}_{total_bits}bits_{inacc_bits}inacc_bits.v"

    # Multiplier file naming style
    if multiplier:
        if type_of_hardware_module == "MxN PAAM01 with V-cut":
            full_file_path += (
                f"/PAAM01_{multiplicand_bits}x{multiplier_bits}_V_cut_{v_cut}.v"
            )
        else:
            full_file_path += f"/{type_of_verilog_code}_{type_of_hardware_module}_{multiplicand_bits}x{multiplier_bits}.v"

    with open(full_file_path, "w") as f:
        f.write(verilog_code)
