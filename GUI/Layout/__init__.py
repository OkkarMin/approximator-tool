import PySimpleGUI as sg
from .VerilogCodeGeneratorLayout import get_verilog_code_generator_layout
from .ErrorAnalysisLayout import get_error_analysis_layout
from .AccuracyAnalysisLayout import get_accuracy_analysis_layout


def get_layout():
    return [[
        sg.TabGroup([[
            sg.Tab(
                'Verilog Code Generator',
                get_verilog_code_generator_layout(),
                key='first_tab',
            ),
            sg.Tab(
                'Error Analysis',
                get_error_analysis_layout(),
                key='second_tab',
            ),
            sg.Tab(
                'Accuracy Analysis',
                get_accuracy_analysis_layout(),
                key='third_tab',
            ),
        ]],
                    enable_events=True,
                    key='tab')
    ]]
