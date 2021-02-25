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

        # Inaccurate Adders should have total_bits >= 4
        if not total_bits >= 4:
            is_valid = False
            error_message = 'Total bits should be >= 4 for Inaccurate Adders'

        # Inaccurate Adders should have inacc_bits >=3 but <= total_bits - 1
        if not (3 <= inacc_bits <= total_bits - 1):
            is_valid = False
            error_message = 'Inaccurate bits should be >= 3 but <= Total bits-1'

        # Total multiplicand bits and multiplier bits should be >=3
        if not (multiplicand_bits >= 3 and multiplier_bits >= 3):
            is_valid = False
            error_message = 'Total Multiplicand bits and Total Multiplier bits should be >= 3'

        # V-cut should be > 0 but <= multiplicand_bits
        if not (0 < v_cut <= multiplicand_bits):
            is_valid = False
            error_message = 'V-cut should be > 0 but <= Total Multiplicand bits'

        return is_valid, error_message
