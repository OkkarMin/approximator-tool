from GUI.Validator.VerilogCodeGeneratorTabValidator import VerilogCodeGeneratorTabValidator
from GUI.Validator.ErrorAnalysisTabValidator import ErrorAnalysisTabValidator
from GUI.Validator.AccuracyAnalysisTabValidator import AccuracyAnalysisTabValidator


def validate(user_chosen_options, validation_strategy):
    strategy = {
        'VerilogCodeGeneratorTabValidator': VerilogCodeGeneratorTabValidator,
        'ErrorAnalysisTabValidator': ErrorAnalysisTabValidator,
        'AccuracyAnalysisTabValidator': AccuracyAnalysisTabValidator,
    }

    execute_validation = None

    execute_validation = getattr(strategy[validation_strategy],
                                 'execute_validation')

    return execute_validation(user_chosen_options)
