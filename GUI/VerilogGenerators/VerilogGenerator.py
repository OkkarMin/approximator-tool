from .VerilogGeneratorFactory import VerilogGeneratorFactory

class VerilogGenerator:
    @staticmethod
    def generate_verilog(user_chosen_options):
        type_of_verilog_code = user_chosen_options['type_of_verilog_code']

        generator = VerilogGeneratorFactory().get_verilog_generator(
            type_of_verilog_code)

        verilog_code = generator.generate_verilog_code(user_chosen_options)

        return verilog_code