# Approximate Computing Tool <!-- {docsify-ignore} -->

## What it is
Command Line Tool and GUI Tool that have 3 features:

- [Verilog Code Generator](using_gui_tool.md#verilog-code-generator)
    - Generate verilog code (.v file) of inaccurate adder/inaccurate multiplier based on user chosen options
- [Error Analyzers](using_gui_tool.md#error-analzyer)
    - Analyzer Error rates of inaccurate adders and multipliers
- [Accuracy Analzyer](using_gui_tool.md#accuracy-analzyer)
    - Analyze accuracy of inaccurate adder/inaccurate multiplier by comparint it with accurate adder/accurate multiplier


## Requirements

!> Be mindful of version numbers, the tools were developed and tested with the versions listed below

?> It is highly recommended to install requirements and run the tools in a [virtual enviornment](https://docs.python.org/3/tutorial/venv.html)

?> You can also install all the requirements using `pip install -r requirements.txt`

- GUI Tool Requirements
    - [Python 3.7.3](https://www.python.org/downloads/release/python-373)
    - [Pyverilog 1.3.0](https://github.com/PyHDI/Pyverilog)
    - [Veriloggen 1.9.0](https://github.com/PyHDI/veriloggen)
    - [NumPy 1.19.3](https://numpy.org)
    - [PySimpleGUI 4.33.0](https://pysimplegui.readthedocs.io/en/latest)

```bash
pip install pyverilog==1.3.0 veriloggen==1.9.0 numpy==1.19.3 PySimpleGUI==4.33.0
```

- Command Line Tool Requirements
    - [Python 3.7.3](https://www.python.org/downloads/release/python-373)
    - [Pyverilog 1.3.0](https://github.com/PyHDI/Pyverilog)
    - [Veriloggen 1.9.0](https://github.com/PyHDI/veriloggen)
    - [NumPy 1.19.3](https://numpy.org)

```bash
pip install pyverilog==1.3.0 veriloggen==1.9.0 numpy==1.19.3 
```