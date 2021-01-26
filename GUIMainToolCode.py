import PySimpleGUI as sg
from GUI.Layout import get_layout
from GUI.Logic.VerilogCodeGeneratorTabLogic import VerilogCodeGeneratorTabLogic
from GUI.Logic.ErrorAnalysisTabLogic import ErrorAnalysisTabLogic

sg.theme('SystemDefault')
sg.SetOptions(font=('Helvetica', 15))

window = sg.Window(
    'Approximate Computing Tool',
    get_layout(),
)

while True:
    event, values = window.read()

    # If user closed window with X or if user clicked "Exit" button then exit
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # Reacts to user inputs in respective tabs
    if values['tab'] == 'first_tab':
        VerilogCodeGeneratorTabLogic(window, event, values)
    elif values['tab'] == 'second_tab':
        ErrorAnalysisTabLogic(window, event, values)

window.close()