from GUI.ErrorAnalyzers import AdderErrorAnalyzer, MultiplierErrorAnalyzer
import PySimpleGUI as sg


def AccuracyAnalysisTabLogic(window, event, values):
    # Extract user chosen options
    # When text input is not number, set is as 4
    # to make sure GUI keep running without crashing
    # input validation is performed when 'Generate' button is pressed
    try:
        total_bits = int(values['total_bits_accuracy_analysis'])
        multiplicand_bits = int(values['multiplicand_bits_accuracy_analysis'])
        multiplier_bits = int(values['multiplier_bits_accuracy_analysis'])
        v_cut = int(values['v_cut_accuracy_analysis'])
        adder_first_unsigned_number = int(
            values['adder_first_unsigned_number'])
        adder_second_unsigned_number = int(
            values['adder_second_unsigned_number'])
        multiplier_first_unsigned_number = int(
            values['multiplier_first_unsigned_number'])
        multiplier_second_unsigned_number = int(
            values['multiplier_second_unsigned_number'])
    except ValueError:
        total_bits = 4
        multiplicand_bits = 4
        multiplier_bits = 4
        v_cut = 4
        adder_first_unsigned_number = 12
        adder_second_unsigned_number = 12
        multiplier_first_unsigned_number = 12
        multiplier_second_unsigned_number = 12
    acc_bits = int(values['acc_inacc_bits_slider_accuracy_analysis'])
    inacc_bits = total_bits - acc_bits
    type_of_accuracy_analysis = 'Adder_Accuracy_Analysis' if values[
        'Adder_Accuracy_Analysis'] else 'Multiplier_Accuracy_Analysis'

    # Update GUI with respective chosen options
    window['acc_inacc_bits_slider_accuracy_analysis'].update(
        range=(1, total_bits))
    window['acc_bits_accuracy_analysis'].update(acc_bits)
    window['inacc_bits_accuracy_analysis'].update(total_bits - acc_bits)

    if event == 'Adder_Accuracy_Analysis':
        window[
            'ASIC_FPGA_Adder_Bits_Accuracy_Analysis_Selection_layout'].update(
                visible=True)
        window['acc_inacc_bits_slider_accuracy_analysis_layout'].update(
            visible=True)
        window[
            'ASIC_Multiplier_Bits_Selection_Accuracy_Analysis_layout'].update(
                visible=False)
        window['ASIC_Adder_Accuracy_Analysis_Layout'].update(visible=True)
        window['ASIC_Multiplier_Accuracy_Analysis_Layout'].update(
            visible=False)
        window[
            'ASIC_FPGA_Adder_Actual_Number_Accuracy_Analysis_layout'].update(
                visible=True)
        window[
            'ASIC_Multiplier_Actual_Number_Accuracy_Analysis_layout'].update(
                visible=False)
    elif event == 'Multiplier_Accuracy_Analysis':
        window[
            'ASIC_FPGA_Adder_Bits_Accuracy_Analysis_Selection_layout'].update(
                visible=False)
        window['acc_inacc_bits_slider_accuracy_analysis_layout'].update(
            visible=False)
        window[
            'ASIC_Multiplier_Bits_Selection_Accuracy_Analysis_layout'].update(
                visible=True)
        window['ASIC_Adder_Accuracy_Analysis_Layout'].update(visible=False)
        window['ASIC_Multiplier_Accuracy_Analysis_Layout'].update(visible=True)
        window[
            'ASIC_FPGA_Adder_Actual_Number_Accuracy_Analysis_layout'].update(
                visible=False)
        window[
            'ASIC_Multiplier_Actual_Number_Accuracy_Analysis_layout'].update(
                visible=True)

    # Analyse Accuracy button has been pressed
    if event == 'Analyse Accuracy':
        # Populate user_chosen_options dict for
        user_chosen_options = {}
        user_chosen_options['acc_bits'] = acc_bits
        user_chosen_options['inacc_bits'] = inacc_bits
        user_chosen_options['multiplicand_bits'] = multiplicand_bits
        user_chosen_options['multiplier_bits'] = multiplier_bits
        user_chosen_options['total_bits'] = total_bits
        user_chosen_options[
            'type_of_accuracy_analysis'] = type_of_accuracy_analysis
        if type_of_accuracy_analysis == 'Adder_Accuracy_Analysis':
            type_of_accuracy_analysis_hardware = values[
                'ASIC_Adder_Accuracy_Analysis_Hardware_Type'][0]
        else:
            type_of_accuracy_analysis_hardware = 'MxN PAAM01 with V-cut'
        user_chosen_options[
            'type_of_accuracy_analysis_hardware'] = type_of_accuracy_analysis_hardware
        user_chosen_options['v_cut'] = v_cut
        user_chosen_options[
            'adder_first_unsigned_number'] = adder_first_unsigned_number
        user_chosen_options[
            'adder_second_unsigned_number'] = adder_second_unsigned_number
        user_chosen_options[
            'multiplier_first_unsigned_number'] = multiplier_first_unsigned_number
        user_chosen_options[
            'multiplier_second_unsigned_number'] = multiplier_second_unsigned_number

        # Perform analysis
        sg.Print('Please wait performing computation...', font='Helvetica 15')

        # TODO: implement AccuracyAnalysis

        sg.Print(user_chosen_options)
