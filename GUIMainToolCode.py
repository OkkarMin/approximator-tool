import PySimpleGUI as sg
from GUI.Layout import get_layout
from GUI.Logic.VerilogCodeGeneratorTabLogic import VerilogCodeGeneratorTabLogic

sg.theme('SystemDefault')
sg.SetOptions(font=('Helvetica', 15))

window = sg.Window(
    'Approximate Computing Tool',
    get_layout(),
)

while True:
    event, values = window.read()

    print(event)

    # If user closed window with X or if user clicked "Exit" button then exit
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # Reacts to user inputs in Verilog Code Generator Tab
    VerilogCodeGeneratorTabLogic(window, event, values)

window.close()