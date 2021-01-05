import PySimpleGUI as sg
import GUI.GUILayout
from pprint import pprint

sg.theme('SystemDefault')
sg.set_options()

window = sg.Window('Approximate Computing Tool',
                   GUI.GUILayout.get_layout(),
                   font=('Helvetica', 15))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':  # If user closed window with X or if user clicked "Exit" button then exit
        break

    # Extract user chosen options
    total_bits = values['total_bits']
    acc_bits = int(values['acc_inacc_bits_slider'])
    inacc_bits = total_bits - acc_bits

    # Update GUI with respective chosen options
    window['acc_inacc_bits_slider'].update(range=(1, total_bits))
    window['acc_bits'].update(acc_bits)
    window['inacc_bits'].update(total_bits - acc_bits)
    print(event, total_bits, acc_bits, inacc_bits)

    # Toggles hardware type Listbox options based on type of verilog code chosen
    if event == 'ASIC_Based_VerilogAdder':
        window['ASIC_Verilog_Adder_Layout'].update(visible=True)
        window['ASIC_Verilog_Multiplier_Layout'].update(visible=False)
        window['FPGA_Verilog_Adder_Layout'].update(visible=False)
    elif event == 'ASIC_Based_VerilogMultiplier':
        window['ASIC_Verilog_Adder_Layout'].update(visible=False)
        window['ASIC_Verilog_Multiplier_Layout'].update(visible=True)
        window['FPGA_Verilog_Adder_Layout'].update(visible=False)
    elif event == 'FPGA_Based_VerilogAdder':
        window['ASIC_Verilog_Adder_Layout'].update(visible=False)
        window['ASIC_Verilog_Multiplier_Layout'].update(visible=False)
        window['FPGA_Verilog_Adder_Layout'].update(visible=True)

    if event == 'Generate':
        chosen_options = {} # populate dictionary with user chosen options
        type_of_verilog_code = [k for k, v in values.items() if v is True][0]
        chosen_options['type_of_verilog_code'] = type_of_verilog_code         
        chosen_options['total_bits'] = total_bits
        chosen_options['acc_bits'] = acc_bits
        chosen_options['inacc_bits'] = inacc_bits
        chosen_options['type_of_hardware_module'] = values[f'{type_of_verilog_code}_Hardware_Type'][0]

        pprint(chosen_options)

window.close()