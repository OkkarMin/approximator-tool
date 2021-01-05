import PySimpleGUI as sg


def get_layout():
    layout = [[sg.T('Type of Verilog Code')],
              [
                  sg.R('ASIC Verilog Adder',
                       'type',
                       enable_events=True,
                       default=True,
                       key='ASIC_Based_VerilogAdder'),
                  sg.R('ASIC Verilog Multiplier',
                       'type',
                       key='ASIC_Based_VerilogMultiplier',
                       enable_events=True)
              ],
              [
                  sg.R('FPGA Verilog Adder',
                       'type',
                       enable_events=True,
                       key='FPGA_Based_VerilogAdder')
              ],
              horizontal_line(), [sg.T('Number of bits')],
              [
                  sg.T('Total bits'),
                  sg.Drop(values=[i for i in range(1, 33)],
                          auto_size_text=True,
                          enable_events=True,
                          default_value=10,
                          key='total_bits')
              ],
              [sg.T('Accurate bits', size=(25, 1)),
               sg.T('Inaccurate bits')],
              [
                  sg.T('4', size=(3, 1), pad=((40, 0), (0, 0)),
                       key='acc_bits'),
                  sg.Slider(range=(1, 10),
                            default_value=4,
                            enable_events=True,
                            disable_number_display=True,
                            orientation='h',
                            key='acc_inacc_bits_slider'),
                  sg.T('6', size=(3, 1), key='inacc_bits')
              ],
              horizontal_line(), [sg.T('Type of hardware module')],
              [
                  sg.Column(ASIC_Verilog_Adder_layout(),
                            key='ASIC_Verilog_Adder_Layout'),
                  sg.Column(ASIC_Verilog_Multiplier_layout(),
                            visible=False,
                            key='ASIC_Verilog_Multiplier_Layout'),
                  sg.Column(FPGA_Verilog_Adder_layout(),
                            visible=False,
                            key='FPGA_Verilog_Adder_Layout')
              ],
              horizontal_line(), [sg.B('Generate'),
                                  sg.B('Exit')]]

    return layout


def horizontal_line():
    return [sg.T('_' * 100, size=(65, 1))]


### Layout for type of hardware modules
def ASIC_Verilog_Adder_layout():
    return [[
        sg.Listbox(values=('HEAA', 'HOERAA', 'HOAANED', 'M-HERLOA'),
                   default_values=('HEAA'),
                   size=(10, 4),
                   key='ASIC_Based_VerilogAdder_Hardware_Type')
    ]]


def ASIC_Verilog_Multiplier_layout():
    return [[
        sg.Listbox(values=('MxN Accurate Multiplier',
                           'MxN Accurate Binary Array Multipler',
                           'MxN PAAM01 with V-cut'),
                   default_values=('MxN Accurate Multiplier'),
                   size=(20, 3),
                   key='ASIC_Based_VerilogMultiplier_Hardware_Type')
    ]]


def FPGA_Verilog_Adder_layout():
    return [[
        sg.Listbox(values=('HEAA', 'HOERAA', 'HOAANED', 'M-HERLOA'),
                   default_values=('HEAA'),
                   size=(10, 4),
                   key='FPGA_Based_VerilogAdder_Hardware_Type')
    ]]
###