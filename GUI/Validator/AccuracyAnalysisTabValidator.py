class AccuracyAnalysisTabValidator:
    def execute_validation(user_chosen_options):
        is_valid = True
        error_message = ''

        # Extract variables from user_chosen_options dict
        inacc_bits = user_chosen_options['inacc_bits']
        multiplicand_bits = user_chosen_options['multiplicand_bits']
        multiplier_bits = user_chosen_options['multiplier_bits']
        total_bits = user_chosen_options['total_bits']
        v_cut = user_chosen_options['v_cut']
        type_of_accuracy_analysis = user_chosen_options[
            'type_of_accuracy_analysis']
        adder_first_unsigned_number = user_chosen_options[
            'adder_first_unsigned_number']
        adder_second_unsigned_number = user_chosen_options[
            'adder_second_unsigned_number']
        multiplier_first_unsigned_number = user_chosen_options[
            'multiplier_first_unsigned_number']
        multiplier_second_unsigned_number = user_chosen_options[
            'multiplier_second_unsigned_number']

        if type_of_accuracy_analysis == 'Adder_Accuracy_Analysis':
            # Inaccurate Adders should have total_bits >= 4
            if not total_bits >= 4:
                is_valid = False
                error_message = 'Total bits should be >= 4 for Inaccurate Adders'

            # Both unsigned numbers cannot be 0
            if adder_first_unsigned_number == adder_second_unsigned_number == 0:
                is_valid = False
                error_message = 'Both unsigned numbers cannot be 0'

            # Unsigned first and second number should have >= 1 but <= 2^total_bits - 1
            if not 0 <= adder_first_unsigned_number <= (2**total_bits) - 1:
                is_valid = False
                error_message = 'Unsigned number should be >= 0 but <= (2^Total bits) - 1'

            if not 0 <= adder_second_unsigned_number <= (2**total_bits) - 1:
                is_valid = False
                error_message = 'Unsigned number should be >= 0 but <= (2^Total bits) - 1'

            # Inaccurate Adders should have inacc_bits >=3 but <= total_bits - 1
            if not (3 <= inacc_bits <= total_bits - 1):
                is_valid = False
                error_message = 'Inaccurate bits should be >= 3 but <= Total bits-1'

        if type_of_accuracy_analysis == 'Multiplier_Accuracy_Analysis':
            # V-cut should be > 0 but <= multiplicand_bits
            if not (0 < v_cut <= multiplicand_bits):
                is_valid = False
                error_message = 'V-cut should be > 0 but <= Total Multiplicand bits'

            # Unsigned first and second number should have >= 1 but <= 2^total_bits - 1
            if not (1 <= multiplier_first_unsigned_number <=
                    (2**multiplicand_bits) - 1):
                is_valid = False
                error_message = 'Unsigned number should be >= 1 but <= (2^Multiplicand bits) - 1'

            if not (1 <= multiplier_second_unsigned_number <=
                    (2**multiplier_bits) - 1):
                is_valid = False
                error_message = 'Unsigned number should be >= 1 but <= (2^Multiplier bits) - 1'

            # Total multiplicand bits and multiplier bits should be >=3
            if not (multiplicand_bits >= 3 and multiplier_bits >= 3):
                is_valid = False
                error_message = 'Total Multiplicand bits and Total Multiplier bits should be >= 3'

        return is_valid, error_message