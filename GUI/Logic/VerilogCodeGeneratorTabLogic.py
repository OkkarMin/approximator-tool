import os
from pprint import pprint
import PySimpleGUI as sg
from GUI.VerilogGenerators.VerilogGenerator import VerilogGenerator
from GUI.Validator import validate
from GUI.Utils.FileSaver import save_to_file


def VerilogCodeGeneratorTabLogic(window, event, values):
    # Extract user chosen options
    # When text input is not number, set is as 4
    # to make sure GUI keep running without crashing
    # input validation is performed when 'Generate' button is pressed
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
    folder_to_save_file = values['folder_to_save_file']

    # Update GUI with respective chosen options
    window['acc_inacc_bits_slider'].update(range=(1, total_bits))
    window['acc_bits'].update(acc_bits)
    window['inacc_bits'].update(total_bits - acc_bits)

    # Default folder to save file is "Desktop" folder
    if folder_to_save_file == '':
        default_path = os.path.expanduser('~/Desktop')
        window['folder_to_save_file_text'].update(default_path)
        folder_to_save_file = default_path
    else:
        window['folder_to_save_file_text'].update(folder_to_save_file)

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

    # When user press 'Generate' button
    if event == 'Generate':
        # Populate user_chosen_options dict for
        # validation and verilog code generation
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
        user_chosen_options['folder_to_save_file'] = folder_to_save_file

        pprint(user_chosen_options)

        is_valid, error_message = validate(user_chosen_options,
                                           'VerilogCodeGeneratorTabValidator')

        if not is_valid:
            sg.popup_non_blocking(
                error_message,
                title="Please check your input",
            )
        else:
            # Generate verilog code
            verilog_code = VerilogGenerator().generate_verilog(
                user_chosen_options)
            print(verilog_code)

            # Save generated verilog code into .v file with proper naming
            save_to_file(verilog_code, user_chosen_options)
