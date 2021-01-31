from GUI.Validator.VerilogCodeGeneratorTabValidator import VerilogCodeGeneratorTabValidator
from GUI.Validator.ErrorAnalysisTabValidator import ErrorAnalysisTabValidator


def validate(user_chosen_options, validation_strategy):
    strategy = {
        'VerilogCodeGeneratorTabValidator': VerilogCodeGeneratorTabValidator,
        'ErrorAnalysisTabValidator': ErrorAnalysisTabValidator
    }

    execute_validation = None

    execute_validation = getattr(strategy[validation_strategy],
                                 'execute_validation')

    return execute_validation(user_chosen_options)
