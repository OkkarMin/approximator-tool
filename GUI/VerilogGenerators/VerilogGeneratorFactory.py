from .ASIC_Based_VerilogAdder_Generator import ASIC_Based_VerilogAdder_Generator
from .ASIC_Based_VerilogMultiplier_Generator import (
    ASIC_Based_VerilogMultiplier_Generator,
)
from .FPGA_Based_VerilogAdder_Generator import FPGA_Based_VerilogAdder_Generator


class VerilogGeneratorFactory:
    @staticmethod
    def get_verilog_generator(type_of_verilog_code):
        if type_of_verilog_code == "ASIC_Based_VerilogAdder":
            return ASIC_Based_VerilogAdder_Generator()
        elif type_of_verilog_code == "ASIC_Based_VerilogMultiplier":
            return ASIC_Based_VerilogMultiplier_Generator()
        elif type_of_verilog_code == "FPGA_Based_VerilogAdder":
            return FPGA_Based_VerilogAdder_Generator()
