from typing import Sized
import PySimpleGUI as sg


def get_layout():
    layout = [
        [sg.T("Type of Verilog Code")],
        [
            sg.R(
                "ASIC Verilog Adder",
                "type",
                enable_events=True,
                default=True,
                key="ASIC_Based_VerilogAdder",
            ),
            sg.R(
                "ASIC Verilog Multiplier",
                "type",
                key="ASIC_Based_VerilogMultiplier",
                enable_events=True,
            ),
        ],
        [
            sg.R(
                "FPGA Verilog Adder",
                "type",
                enable_events=True,
                key="FPGA_Based_VerilogAdder",
            )
        ],
        horizontal_line(),
        [sg.T("Number of bits")],
        [
            sg.Column(
                ASIC_FPGA_Adder_Bits_Selection_layout(),
                key="ASIC_FPGA_Adder_Bits_Selection_layout",
            ),
            sg.Column(
                Accurate_Inaccurate_Bits_Slider_layout(),
                key="acc_inacc_bits_slider_layout",
            ),
            sg.Column(
                ASIC_Multiplier_Bits_Selection_layout(),
                visible=False,
                key="ASIC_Multiplier_Bits_Selection_layout",
            ),
        ],
        horizontal_line(),
        [sg.T("Type of hardware module")],
        [
            sg.Column(ASIC_Verilog_Adder_layout(), key="ASIC_Verilog_Adder_Layout"),
            sg.Column(
                ASIC_Verilog_Multiplier_layout(),
                visible=False,
                key="ASIC_Verilog_Multiplier_Layout",
            ),
            sg.Column(
                FPGA_Verilog_Adder_layout(),
                visible=False,
                key="FPGA_Verilog_Adder_Layout",
            ),
        ],
        horizontal_line(),
        [
            sg.FolderBrowse(
                "Select a folder to save generated file",
                enable_events=True,
                key="folder_to_save_file",
            )
        ],
        [
            sg.T(
                'by default will save in "Desktop"',
                size=(65, 2),
                key="folder_to_save_file_text",
            )
        ],
        horizontal_line(),
        [sg.B("Generate"), sg.B("Exit")],
    ]

    return layout


def horizontal_line():
    return [sg.T("_" * 100, size=(65, 1))]


### Layout for number of bits selection
def ASIC_FPGA_Adder_Bits_Selection_layout():
    return [
        [
            sg.T("Total bits"),
            sg.Input(
                default_text="4", enable_events=True, size=(4, 1), key="total_bits"
            ),
        ],
    ]


def Accurate_Inaccurate_Bits_Slider_layout():
    return [
        [sg.T("Accurate bits", size=(25, 1)), sg.T("Inaccurate bits")],
        [
            sg.T("1", size=(3, 1), pad=((40, 0), (0, 0)), key="acc_bits"),
            sg.Slider(
                range=(1, 4),
                default_value=1,
                enable_events=True,
                disable_number_display=True,
                orientation="h",
                key="acc_inacc_bits_slider",
            ),
            sg.T("3", size=(3, 1), key="inacc_bits"),
        ],
    ]


def ASIC_Multiplier_Bits_Selection_layout():
    return [
        [
            sg.T("Total Multiplicand bits"),
            sg.Input(
                default_text="4",
                size=(4, 1),
                enable_events=True,
                key="multiplicand_bits",
            ),
            sg.T("V-cut", visible=False, key="v_cut_text"),
            sg.Input(
                default_text="3",
                enable_events=True,
                size=(4, 1),
                visible=False,
                key="v_cut",
            ),
        ],
        [
            sg.T("Total Multiplier bits"),
            sg.Input(
                default_text="4", enable_events=True, size=(4, 1), key="multiplier_bits"
            ),
        ],
    ]


### Layout for type of hardware modules selection
def ASIC_Verilog_Adder_layout():
    return [
        [
            sg.Listbox(
                values=("HEAA", "HOERAA", "HOAANED", "M-HERLOA"),
                default_values=("HEAA"),
                size=(30, 4),
                auto_size_text=True,
                key="ASIC_Based_VerilogAdder_Hardware_Type",
            )
        ]
    ]


def ASIC_Verilog_Multiplier_layout():
    return [
        [
            sg.Listbox(
                values=(
                    "MxN Accurate Multiplier",
                    "MxN Accurate Binary Array Multiplier",
                    "MxN AAM01 with V-cut",
                ),
                default_values=("MxN Accurate Multiplier"),
                size=(30, 3),
                auto_size_text=True,
                enable_events=True,
                key="ASIC_Based_VerilogMultiplier_Hardware_Type",
            )
        ]
    ]


def FPGA_Verilog_Adder_layout():
    return [
        [
            sg.Listbox(
                values=("Accurate Adder", "HEAA", "HOERAA", "HOAANED", "M-HERLOA"),
                default_values=("HEAA"),
                size=(30, 5),
                auto_size_text=True,
                enable_events=True,
                key="FPGA_Based_VerilogAdder_Hardware_Type",
            )
        ]
    ]
