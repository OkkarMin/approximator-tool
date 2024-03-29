class ErrorAnalysisTabValidator:
    def execute_validation(user_chosen_options):
        is_valid = True
        error_message = ""

        # Extract variables from user_chosen_options dict
        inacc_bits = user_chosen_options["inacc_bits"]
        multiplicand_bits = user_chosen_options["multiplicand_bits"]
        multiplier_bits = user_chosen_options["multiplier_bits"]
        total_bits = user_chosen_options["total_bits"]
        v_cut = user_chosen_options["v_cut"]
        type_of_error_analysis = user_chosen_options["type_of_error_analysis"]
        error_analysis_adder_value_error = user_chosen_options["error_analysis_adder_value_error"]
        error_analysis_multiplier_value_error = user_chosen_options["error_analysis_multiplier_value_error"]
        if type_of_error_analysis == "Adder_Error_Analysis":
            # Adder inputs filled by the user must be integer
            if error_analysis_adder_value_error==1:
                is_valid = False
                error_message = "Inputs filled by the user must be integer"
            # Inaccurate Adders should have total_bits >= 4
            elif not total_bits >= 4:
                is_valid = False
                error_message = "Total bits should be >= 4 for Inaccurate Adders"

            # Inaccurate Adders should have inacc_bits >=3 but <= total_bits - 1
            elif not (3 <= inacc_bits <= total_bits - 1):
                is_valid = False
                error_message = "Inaccurate bits should be >= 3 but <= Total bits-1"

        if type_of_error_analysis == "Multiplier_Error_Analysis":
            # Multiplier inputs filled by the user must be integer
            if error_analysis_multiplier_value_error==1:
                is_valid = False
                error_message = "Inputs filled by the user must be integer"
            # Total multiplicand bits and multiplier bits should be >=3
            elif not (multiplicand_bits >= 3 and multiplier_bits >= 3):
                is_valid = False
                error_message = (
                    "Total Multiplicand bits and Total Multiplier bits should be >= 3"
                )

            # V-cut should be > 0 but <= (multiplicand_bits + multiplier_bits - 3)
            elif not (0 < v_cut <= (multiplicand_bits + multiplier_bits - 3)):
                is_valid = False
                error_message = "V-cut should be > 0 but <= (Total Multiplicand bits + Total Multiplier bits -3)"

        return is_valid, error_message
