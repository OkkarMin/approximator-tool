import PySimpleGUI as sg
from .CommonElements import horizontal_line


def get_error_analysis_layout():
    return [
        [sg.T('Type of Error Analysis')],
        [
            sg.R('Adder Error Analysis',
                 'error_analysis_type',
                 enable_events=True,
                 default=True,
                 key='Adder_Error_Analysis'),
            sg.R(
                'Multiplier Error Analysis',
                'error_analysis_type',
                enable_events=True,
                key='Multiplier_Error_Analysis',
            )
        ],
        horizontal_line(), [sg.T('Number of bits')],
        [
            sg.Column(
                ASIC_FPGA_Adder_Bits_Selection_layout(),
                key='ASIC_FPGA_Adder_Bits_Error_Analysis_Selection_layout'),
            sg.Column(Accurate_Inaccurate_Bits_Slider_layout(),
                      key='acc_inacc_bits_slider_error_analysis_layout'),
            sg.Column(
                ASIC_Multiplier_Bits_Selection_layout(),
                visible=False,
                key='ASIC_Multiplier_Bits_Selection_Error_Analysis_layout')
        ],
        horizontal_line(), [sg.T('Type of hardware module')],
        [
            sg.Column(ASIC_Adder_Error_Analysis_layout(),
                      key='ASIC_Adder_Error_Analysis_Layout'),
            sg.Column(ASIC_Multiplier_Error_Analysis_layout(),
                      visible=False,
                      key='ASIC_Multiplier_Error_Analysis_Layout'),
        ],
        horizontal_line(), [sg.B('Analyse Error')]
    ]


def ASIC_FPGA_Adder_Bits_Selection_layout():
    return [
        [
            sg.T('Total bits'),
            sg.Input(default_text='4',
                     enable_events=True,
                     size=(4, 1),
                     key='total_bits_error_analysis')
        ],
    ]


def Accurate_Inaccurate_Bits_Slider_layout():
    return [
        [sg.T('Accurate bits', size=(25, 1)),
         sg.T('Inaccurate bits')],
        [
            sg.T('1',
                 size=(3, 1),
                 pad=((40, 0), (0, 0)),
                 key='acc_bits_error_analysis'),
            sg.Slider(range=(1, 4),
                      default_value=1,
                      enable_events=True,
                      disable_number_display=True,
                      orientation='h',
                      key='acc_inacc_bits_slider_error_analysis'),
            sg.T('3', size=(3, 1), key='inacc_bits_error_analysis')
        ],
    ]


def ASIC_Multiplier_Bits_Selection_layout():
    return [
        [
            sg.T('Total Multiplicand bits'),
            sg.Input(default_text='4',
                     size=(4, 1),
                     enable_events=True,
                     key='multiplicand_bits_error_analysis'),
            sg.T('V-cut', visible=True, key='v_cut_text_error_analysis'),
            sg.Input(default_text='3',
                     enable_events=True,
                     size=(4, 1),
                     visible=True,
                     key='v_cut_error_analysis')
        ],
        [
            sg.T('Total Multiplier bits'),
            sg.Input(default_text='4',
                     enable_events=True,
                     size=(4, 1),
                     key='multiplier_bits_error_analysis'),
        ],
    ]


### Layout for type of error analysis module selection
def ASIC_Adder_Error_Analysis_layout():
    return [[
        sg.Listbox(values=('HEAA', 'HOERAA', 'HOAANED', 'M-HERLOA'),
                   default_values=('HEAA'),
                   size=(30, 4),
                   auto_size_text=True,
                   key='ASIC_Adder_Error_Analysis_Hardware_Type')
    ]]


def ASIC_Multiplier_Error_Analysis_layout():
    return [[
        sg.R('MxN PAAM01 with V-cut',
             '_',
             default=True,
             key='ASIC_Multiplier_Error_Analysis_Hardware_Type')
    ]]
