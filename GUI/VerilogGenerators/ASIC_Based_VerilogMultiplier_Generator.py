class ASIC_Based_VerilogMultiplier_Generator:
    @staticmethod
    def generate_verilog_code(user_chosen_options):
        type_of_hardware_module = user_chosen_options["type_of_hardware_module"]
        return f'{user_chosen_options["type_of_verilog_code"]}_Generator generated: {type_of_hardware_module} code'
