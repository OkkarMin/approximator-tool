import os
import PySimpleGUI as sg
import GUI.GUILayout
from GUI.VerilogGenerators.VerilogGenerator import VerilogGenerator
from pprint import pprint

sg.theme('SystemDefault')
sg.SetOptions(font=('Helvetica', 15))

window = sg.Window(
    'Approximate Computing Tool',
    GUI.GUILayout.get_layout(),
)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':  # If user closed window with X or if user clicked "Exit" button then exit
        break

    # Extract user chosen options
    # When text input is not number, set is as 4
    try:
        total_bits = int(values['total_bits'])
        multiplicand_bits = int(values['multiplicand_bits'])
        multiplier_bits = int(values['multiplier_bits'])
        v_cut = int(values['v_cut'])
    except ValueError:
        total_bits = 4
        multiplicand_bits = 4
        multiplier_bits = 4
        v_cut = 4
    acc_bits = int(values['acc_inacc_bits_slider'])
    inacc_bits = total_bits - acc_bits
    type_of_verilog_code = [k for k, v in values.items() if v is True][0]
    type_of_hardware_module = values[f'{type_of_verilog_code}_Hardware_Type'][
        0]
    path_to_save_file = values['path_to_save_file']

    # Update GUI with respective chosen options
    window['acc_inacc_bits_slider'].update(range=(1, total_bits))
    window['acc_bits'].update(acc_bits)
    window['inacc_bits'].update(total_bits - acc_bits)

    # Default path to save file is "Desktop" folder
    if path_to_save_file == '':
        default_path = os.path.expanduser('~/Desktop')
        window['path_to_save_file_text'].update(default_path)
        path_to_save_file = default_path
    else:
        window['path_to_save_file_text'].update(path_to_save_file)

    # Toggles number of bits selection & hardware type Listbox options
    # based on type of verilog code chosen
    if event == 'ASIC_Based_VerilogAdder':
        window['ASIC_FPGA_Adder_Bits_Selection_layout'].update(visible=True)
        window['ASIC_Multiplier_Bits_Selection_layout'].update(visible=False)
        window['ASIC_Verilog_Adder_Layout'].update(visible=True)
        window['ASIC_Verilog_Multiplier_Layout'].update(visible=False)
        window['FPGA_Verilog_Adder_Layout'].update(visible=False)
        window['acc_inacc_bits_slider_layout'].update(visible=True)
    elif event == 'ASIC_Based_VerilogMultiplier':
        window['ASIC_FPGA_Adder_Bits_Selection_layout'].update(visible=False)
        window['ASIC_Multiplier_Bits_Selection_layout'].update(visible=True)
        window['ASIC_Verilog_Adder_Layout'].update(visible=False)
        window['ASIC_Verilog_Multiplier_Layout'].update(visible=True)
        window['FPGA_Verilog_Adder_Layout'].update(visible=False)
        window['acc_inacc_bits_slider_layout'].update(visible=False)
    elif event == 'FPGA_Based_VerilogAdder':
        if type_of_hardware_module == 'Accurate Adder':
            window['acc_inacc_bits_slider_layout'].update(visible=False)
        window['ASIC_FPGA_Adder_Bits_Selection_layout'].update(visible=True)
        window['ASIC_Multiplier_Bits_Selection_layout'].update(visible=False)
        window['ASIC_Verilog_Adder_Layout'].update(visible=False)
        window['ASIC_Verilog_Multiplier_Layout'].update(visible=False)
        window['FPGA_Verilog_Adder_Layout'].update(visible=True)
    # Accurate and Inaccurate bits selection slider should not be visible for
    # FPGA Accurate Adder
    elif event == 'FPGA_Based_VerilogAdder_Hardware_Type':
        if type_of_hardware_module == 'Accurate Adder':
            window['acc_inacc_bits_slider_layout'].update(visible=False)
        else:
            window['acc_inacc_bits_slider_layout'].update(visible=True)

    # V-cut input should only show up for 'MxN PAAM01 with V-cut'
    if type_of_hardware_module == 'MxN PAAM01 with V-cut':
        window['v_cut_text'].update(visible=True)
        window['v_cut'].update(visible=True)
    else:
        window['v_cut_text'].update(visible=False)
        window['v_cut'].update(visible=False)

    if event == 'Generate':
        # Populate user_chosen_options dict for verilog code generation
        user_chosen_options = {}
        user_chosen_options['acc_bits'] = acc_bits
        user_chosen_options['inacc_bits'] = inacc_bits
        user_chosen_options['multiplicand_bits'] = multiplicand_bits
        user_chosen_options['multiplier_bits'] = multiplier_bits
        user_chosen_options['total_bits'] = total_bits
        user_chosen_options['type_of_hardware_module'] = values[
            f'{type_of_verilog_code}_Hardware_Type'][0]
        user_chosen_options['type_of_verilog_code'] = type_of_verilog_code
        user_chosen_options['v_cut'] = v_cut

        pprint(user_chosen_options)

        # Generate verilog code
        verilog_code = VerilogGenerator().generate_verilog(user_chosen_options)
        print(verilog_code)

        # Save generated verilog code into .v file
        full_file_path = f'{path_to_save_file}/{type_of_verilog_code}_{type_of_hardware_module}_{total_bits}b{inacc_bits}inacc.v'
        with open(full_file_path, 'w') as f:
            f.write(verilog_code)

window.close()