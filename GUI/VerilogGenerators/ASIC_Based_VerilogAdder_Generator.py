import VerilogStructuralAdder


class ASIC_Based_VerilogAdder_Generator:
    @staticmethod
    def generate_verilog_code(user_chosen_options):
        # To generate verilog_code ASIC_Based_VerilogAdder_Generator requires
        # type_of_hardware_module ['HEAA', 'HOERAA', ...]
        # total_bits
        # inacc_bits
        type_of_hardware_module = user_chosen_options[
            "type_of_hardware_module"]
        total_bits = user_chosen_options["total_bits"]
        inacc_bits = user_chosen_options["inacc_bits"]

        verilog_code = None

        if type_of_hardware_module == 'HEAA':
            verilog_code = VerilogStructuralAdder.HEAA_Generic(
                total_bits, inacc_bits).to_verilog()
        elif type_of_hardware_module == 'HOERAA':
            verilog_code = f'{type_of_hardware_module} code generated'
        elif type_of_hardware_module == 'HOAANED':
            verilog_code = f'{type_of_hardware_module} code generated'
        elif type_of_hardware_module == 'M-HERLOA':
            verilog_code = f'{type_of_hardware_module} code generated'

        return verilog_code
