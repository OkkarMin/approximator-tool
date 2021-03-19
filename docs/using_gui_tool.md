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

Insert a GIF of using verilog code generator here

![Verilog Code Generator](_images/verilog_code_generator.png)

| No. | Description                                                                                                             |        Default Option(s)        |            Constraint(s)            |
| :-: | ----------------------------------------------------------------------------------------------------------------------- | :-----------------------------: | :---------------------------------: |
|  1  | Type of Verilog Code to generate, choose one of <br>`[ASIC Verilog Adder, ASIC Verilog Multiplier, FPGA Verilog Adder]` |      `ASIC Verilog Adder`       |                  -                  |
|  2  | Total number of bits for the module verilog code generation                                                             |               `4`               |       `4 <= total_bits <= 32`       |
|  3  | Accurate bits and Inaccurate bits selection. Move slider to adjust.                                                     | `acc_bits = 1` `inacc_bits = 3` | `3 <= inacc_bits <= total_bits - 1` |
|  4  | Type of hardware module to generate, chose one of <br>`[HEAA, HOERAA, HOAANED, M-HERLOA]`                               |             `HEAA`              |                  -                  |
|  5  | Choose location in computer to save generated verilog file                                                              |            `Desktop`            |                  -                  |
|  6  | Generate verilog code or exit                                                                                           |                -                |                  -                  |

!> As of 4 Mar 2021 (GMT+8), you will need to modify a tiny portion of generated verilog code. [Click here to find out more](link-to-how-to-edit). We are working to fix it

## Error Analysis

Insert a GIF of using error analysis here

![Error Analysis](_images/error_analysis.png)

| No. | Description                                                                                            |        Default Option(s)        |            Constraint(s)            |
| :-: | ------------------------------------------------------------------------------------------------------ | :-----------------------------: | :---------------------------------: |
|  1  | Type of Error Analysis to carry out, choose one of `[Adder Error Analysis, Multiplier Error Analysis]` |     `Adder Error Analysis`      |                  -                  |
|  2  | Total number of bits for approximate computing module                                                  |               `4`               |       `4 <= total_bits <= 32`       |
|  3  | Accurate bits and Inaccurate bits selection. Move slider to adjust.                                    | `acc_bits = 1` `inacc_bits = 3` | `3 <= inacc_bits <= total_bits - 1` |
|  4  | Type of hardware module to analyze error, chose one of `[HEAA, HOERAA, HOAANED, M-HERLOA]`             |             `HEAA`              |                  -                  |
|  5  | Analyse Error                                                                                          |                -                |                  -                  |

## Accuracy Analysis

Insert a GIF of using accuracy analysis here

![Accuracy Analysis](_images/accuracy_analysis.png)

| No. | Description                                                                                                            |        Default Option(s)        |               Constraint(s)                |
| :-: | ---------------------------------------------------------------------------------------------------------------------- | :-----------------------------: | :----------------------------------------: |
|  1  | Type of Accuracy Analysis to carry out, choose one of `[Adder Accuracy Analysis, Multiplier Accuracy Analysis]`        |    `Adder Accuracy Analysis`    |                     -                      |
|  2  | Total number of bits for approximate computing module                                                                  |               `4`               |          `4 <= total_bits <= 32`           |
|  3  | Accurate bits and Inaccurate bits selection. Move slider to adjust.                                                    | `acc_bits = 1` `inacc_bits = 3` |    `3 <= inacc_bits <= total_bits - 1`     |
|  4  | Two unsigned decimal numbers to be added using accurate adder and to be compared against inaccurate adder for accuracy |              `12`               | `0 <= decimal_number <= 2^(total_bits) -1` |
|  5  | Type of hardware module to analyze error, chose one of `[HEAA, HOERAA, HOAANED, M-HERLOA]`                             |             `HEAA`              |                     -                      |
|  6  | Analyse Accuracy                                                                                                       |                -                |                     -                      |
