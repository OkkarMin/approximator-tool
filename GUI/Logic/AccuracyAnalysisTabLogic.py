import PySimpleGUI as sg
from GUI.Analyzers.AccuracyAnalyzers import (
    AdderAccuracyAnalyzer,
    MultiplierAccuracyAnalyzer,
)
from GUI.Validator import validate


def AccuracyAnalysisTabLogic(window, event, values):
    # Extract user chosen options
    # When text input is not number, set an error flag
    # to make sure GUI keep running without crashing
    # input validation is performed when 'Generate' button is pressed
    try:
        total_bits = int(values["total_bits_accuracy_analysis"])
        adder_first_unsigned_number = int(values["adder_first_unsigned_number"])
        adder_second_unsigned_number = int(values["adder_second_unsigned_number"])
        accuracy_analysis_adder_value_error=0
    except ValueError:
        total_bits = 4
        adder_first_unsigned_number = 12
        adder_second_unsigned_number = 12
        accuracy_analysis_adder_value_error=1

    try:
        multiplicand_bits = int(values["multiplicand_bits_accuracy_analysis"])
        multiplier_bits = int(values["multiplier_bits_accuracy_analysis"])
        v_cut = int(values["v_cut_accuracy_analysis"])
        multiplier_first_unsigned_number = int(
            values["multiplier_first_unsigned_number"]
        )
        multiplier_second_unsigned_number = int(
            values["multiplier_second_unsigned_number"]
        )
        accuracy_analysis_multiplier_value_error=0
    except ValueError:
        multiplicand_bits = 4
        multiplier_bits = 4
        v_cut = 4
        multiplier_first_unsigned_number = 12
        multiplier_second_unsigned_number = 12
        accuracy_analysis_multiplier_value_error=1


    acc_bits = int(values["acc_inacc_bits_slider_accuracy_analysis"])
    inacc_bits = total_bits - acc_bits
    type_of_accuracy_analysis = (
        "Adder_Accuracy_Analysis"
        if values["Adder_Accuracy_Analysis"]
        else "Multiplier_Accuracy_Analysis"
    )

    # Update GUI with respective chosen options
    window["acc_inacc_bits_slider_accuracy_analysis"].update(range=(1, total_bits))
    window["acc_bits_accuracy_analysis"].update(acc_bits)
    window["inacc_bits_accuracy_analysis"].update(total_bits - acc_bits)

    if event == "Adder_Accuracy_Analysis":
        window["ASIC_FPGA_Adder_Bits_Accuracy_Analysis_Selection_layout"].update(
            visible=True
        )
        window["acc_inacc_bits_slider_accuracy_analysis_layout"].update(
            visible=True,
        )
        window["ASIC_Multiplier_Bits_Selection_Accuracy_Analysis_layout"].update(
            visible=False
        )
        window["ASIC_Adder_Accuracy_Analysis_Layout"].update(
            visible=True,
        )
        window["ASIC_Multiplier_Accuracy_Analysis_Layout"].update(
            visible=False,
        )
        window["ASIC_FPGA_Adder_Actual_Number_Accuracy_Analysis_layout"].update(
            visible=True
        )
        window["ASIC_Multiplier_Actual_Number_Accuracy_Analysis_layout"].update(
            visible=False
        )
    elif event == "Multiplier_Accuracy_Analysis":
        window["ASIC_FPGA_Adder_Bits_Accuracy_Analysis_Selection_layout"].update(
            visible=False
        )
        window["acc_inacc_bits_slider_accuracy_analysis_layout"].update(visible=False)
        window["ASIC_Multiplier_Bits_Selection_Accuracy_Analysis_layout"].update(
            visible=True
        )
        window["ASIC_Adder_Accuracy_Analysis_Layout"].update(visible=False)
        window["ASIC_Multiplier_Accuracy_Analysis_Layout"].update(visible=True)
        window["ASIC_FPGA_Adder_Actual_Number_Accuracy_Analysis_layout"].update(
            visible=False
        )
        window["ASIC_Multiplier_Actual_Number_Accuracy_Analysis_layout"].update(
            visible=True
        )

    # Analyse Accuracy button has been pressed
    if event == "Analyse Accuracy":
        # Populate user_chosen_options dict for
        user_chosen_options = {}
        user_chosen_options["acc_bits"] = acc_bits
        user_chosen_options["inacc_bits"] = inacc_bits
        user_chosen_options["multiplicand_bits"] = multiplicand_bits
        user_chosen_options["multiplier_bits"] = multiplier_bits
        user_chosen_options["total_bits"] = total_bits
        user_chosen_options["type_of_accuracy_analysis"] = type_of_accuracy_analysis
        user_chosen_options['accuracy_analysis_adder_value_error'] = accuracy_analysis_adder_value_error
        user_chosen_options['accuracy_analysis_multiplier_value_error'] = accuracy_analysis_multiplier_value_error
        if type_of_accuracy_analysis == "Adder_Accuracy_Analysis":
            type_of_accuracy_analysis_hardware = values[
                "ASIC_Adder_Accuracy_Analysis_Hardware_Type"
            ][0]
        else:
            type_of_accuracy_analysis_hardware = "MxN AAM01 with V-cut"
        user_chosen_options[
            "type_of_accuracy_analysis_hardware"
        ] = type_of_accuracy_analysis_hardware
        user_chosen_options["v_cut"] = v_cut
        user_chosen_options["adder_first_unsigned_number"] = adder_first_unsigned_number
        user_chosen_options[
            "adder_second_unsigned_number"
        ] = adder_second_unsigned_number
        user_chosen_options[
            "multiplier_first_unsigned_number"
        ] = multiplier_first_unsigned_number
        user_chosen_options[
            "multiplier_second_unsigned_number"
        ] = multiplier_second_unsigned_number

        is_valid, error_message = validate(
            user_chosen_options, "AccuracyAnalysisTabValidator"
        )

        if not is_valid:
            sg.popup_non_blocking(
                error_message,
                title="Please check your input",
            )

            return

        # Perform analysis
        sg.Print("Please wait performing computation...", font="Helvetica 15")

        if type_of_accuracy_analysis == "Adder_Accuracy_Analysis":
            AdderAccuracyAnalyzer.analyze(user_chosen_options)
        else:
            MultiplierAccuracyAnalyzer.analyze(user_chosen_options)
