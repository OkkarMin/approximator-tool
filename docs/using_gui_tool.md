# Using GUI Tool <!-- {docsify-ignore} -->

!> Before running please check that you have installed required requirements [listed here](/README.md#requirements)

## Steps to run the GUI Tool

1. Clone repository/download the source code from [here](link-to-repository)
2. Extract files if downloaded in zip format
3. Install requirements
4. Run GUIMainToolCode.py
   
```bash
git clone link-to-repository
cd ApproximateComputingTool 
pip install -r requirements.txt
python3 GUIMainToolCode.py
```

## Verilog Code Generator

![Verilog Code Generator](_images/verilog_code_generator.png)

| No. | Description | Default Option(s) | Constraint(s) |
|:-:|-|:-:|:-:|
| 1 | Type of Verilog Code to generate, choose one of <br>`[ASIC Verilog Adder, ASIC Verilog Multiplier, FPGA Verilog Adder]` | `ASIC Verilog Adder` | - |
| 2 | Total number of bits for the module verilog code generation | `4` | `4 <= total_bits <= 32` |
| 3 | Accurate bits and Inaccurate bits selection. Move slider to adjust. | `acc_bits = 1` `inacc_bits = 3` | `3 <= inacc_bits <= total_bits - 1` |
| 4 | Type of hardware module to generate, chose one of <br>`[HEAA, HOERAA, HOAANED, M-HERLOA]` | `HEAA` | - |
| 5 | Choose location in computer to save generated verilog file | `Desktop` | - |
| 6 | Generate verilog code or exit | - | - |

## Error Analzyer

## Accuracy Analzyer