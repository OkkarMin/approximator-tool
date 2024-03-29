import PySimpleGUI as sg
from GUI.Analyzers.ErrorAnalyzers import AdderErrorAnalyzer, MultiplierErrorAnalyzer
from GUI.Validator import validate


def ErrorAnalysisTabLogic(window, event, values):
    # Extract user chosen options
    # When text input is not number, set an error flag
    # to make sure GUI keep running without crashing
    # input validation is performed when 'Generate' button is pressed
    try:
        total_bits = int(values["total_bits_error_analysis"])
        error_analysis_adder_value_error=0
    except ValueError:
        total_bits = 4
        error_analysis_adder_value_error=1
    try:
        multiplicand_bits = int(values["multiplicand_bits_error_analysis"])
        multiplier_bits = int(values["multiplier_bits_error_analysis"])
        v_cut = int(values["v_cut_error_analysis"])
        error_analysis_multiplier_value_error=0
    except ValueError:
        multiplicand_bits = 4
        multiplier_bits = 4
        v_cut = 4
        error_analysis_multiplier_value_error=1
    acc_bits = int(values["acc_inacc_bits_slider_error_analysis"])
    inacc_bits = total_bits - acc_bits
    type_of_error_analysis = (
        "Adder_Error_Analysis"
        if values["Adder_Error_Analysis"]
        else "Multiplier_Error_Analysis"
    )

    # Update GUI with respective chosen options
    window["acc_inacc_bits_slider_error_analysis"].update(range=(1, total_bits))
    window["acc_bits_error_analysis"].update(acc_bits)
    window["inacc_bits_error_analysis"].update(total_bits - acc_bits)

    if event == "Adder_Error_Analysis":
        window["ASIC_FPGA_Adder_Bits_Error_Analysis_Selection_layout"].update(
            visible=True
        )
        window["acc_inacc_bits_slider_error_analysis_layout"].update(visible=True)
        window["ASIC_Multiplier_Bits_Selection_Error_Analysis_layout"].update(
            visible=False
        )
        window["ASIC_Adder_Error_Analysis_Layout"].update(visible=True)
        window["ASIC_Multiplier_Error_Analysis_Layout"].update(visible=False)
    elif event == "Multiplier_Error_Analysis":
        window["ASIC_FPGA_Adder_Bits_Error_Analysis_Selection_layout"].update(
            visible=False
        )
        window["acc_inacc_bits_slider_error_analysis_layout"].update(visible=False)
        window["ASIC_Multiplier_Bits_Selection_Error_Analysis_layout"].update(
            visible=True
        )
        window["ASIC_Adder_Error_Analysis_Layout"].update(visible=False)
        window["ASIC_Multiplier_Error_Analysis_Layout"].update(visible=True)

    # Analyse Error button has been pressed
    if event == "Analyse Error":
        # Populate user_chosen_options dict for
        # validation and verilog code generation
        user_chosen_options = {}
        user_chosen_options["acc_bits"] = acc_bits
        user_chosen_options["inacc_bits"] = inacc_bits
        user_chosen_options["multiplicand_bits"] = multiplicand_bits
        user_chosen_options["multiplier_bits"] = multiplier_bits
        user_chosen_options["total_bits"] = total_bits
        user_chosen_options["type_of_error_analysis"] = type_of_error_analysis
        user_chosen_options["error_analysis_adder_value_error"] = error_analysis_adder_value_error
        user_chosen_options["error_analysis_multiplier_value_error"] = error_analysis_multiplier_value_error
        if type_of_error_analysis == "Adder_Error_Analysis":
            type_of_error_analysis_hardware = values[
                "ASIC_Adder_Error_Analysis_Hardware_Type"
            ][0]
        else:
            type_of_error_analysis_hardware = "MxN AAM01 with V-cut"
        user_chosen_options[
            "type_of_error_analysis_hardware"
        ] = type_of_error_analysis_hardware
        user_chosen_options["v_cut"] = v_cut

        is_valid, error_message = validate(
            user_chosen_options, "ErrorAnalysisTabValidator"
        )

        if not is_valid:
            sg.popup_non_blocking(
                error_message,
                title="Please check your input",
            )

            return

        # Perform analysis
        sg.Print("Please wait performing computation...", font="Helvetica 15")

        if type_of_error_analysis == "Adder_Error_Analysis":
            getattr(AdderErrorAnalyzer, type_of_error_analysis_hardware)(
                total_bits, inacc_bits
            )
        else:  # MxN AAM01 with V-cut
            MultiplierErrorAnalyzer.AAM01_VCut(
                multiplicand_bits, multiplier_bits, v_cut
            )
