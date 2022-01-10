# Approximate Computing Tool <!-- {docsify-ignore} -->

# What is Approximator

Approximator is an open-source software tool that can be used to automatically generate Verilog HDL codes of approximate arithmetic circuits proposed by our research team. Approximator can be used to generate Verilog codes of approximate adders and approximate multiplier of any specified size, corresponding to FPGA and ASIC (standard cell) based implementations. The approximate adder architectures include HEAA [1], HOERAA [2], HOAANED [3] and M-HERLOA [4]. The approximate multiplier architecture includes AAM01/PAAM01 [5,6]

# Approximator - Publication

If you use Approximator in your research, please cite the following publication to acknowledge our effort.
P. Balasubramanian, R. Nayar, O. Min, D.L. Maskell, "Approximator: A Software Tool for Automatic Generation of Approximate Arithmetic Circuits", Computers, vol. 11, no. 1, Article #11, pp. 1-32, January 2022.

#### Citations

1. HEAA

   P. Balasubramanian, D.L. Maskell, “Hardware Efficient Approximate Adder Design”, Proceedings of IEEE Region 10 Conference (TENCON), pp. 806-810, 2018, Jeju, South Korea.

2. HOERAA

   P. Balasubramanian, D.L. Maskell, “Hardware Optimized and Error Reduced Approximate Adder”, Electronics, vol. 8, no. 11, Article #1212, pp. 1-15, October 2019.

3. HOAANED

   P. Balasubramanian, R. Nayar, D.L. Maskell, N.E. Mastorakis, “An Approximate Adder with a Near-Normal Error Distribution: Design, Error Analysis and Practical Application”, IEEE Access, vol. 9, pp. 4518-4530, January 2021.

4. M-HERLOA

   P. Balasubramanian, R. Nayar, D.L. Maskell, "An Approximate Adder with Reduced Error and Optimized Design Metrics", Accepted for presentation and publication in the Proceedings of the 17th IEEE Asia Pacific Conference on Circuits and Systems (APCCAS 2021), November 22-26, 2021, Penang, Malaysia.

5. Approximate Array Multipliers (Image Denoising application)

   P. Balasubramanian, R. Nayar, D.L. Maskell, “Approximate Array Multipliers”, Electronics, (Special Issue: Circuits and Systems for Approximate Computing), vol. 10, no. 5, Article #630, pp. 1-20, March 2021.

6. Approximate Array Multiplier (Image Blending application)

   P. Balasubramanian, R. Nayar, O. Min, D.L. Maskell, "Image Blending using Approximate Multiplication", Proceedings of IEEE 32nd International Conference on Microelectronics (MIEL 2021), pp. 305-310, 2021, Niš, Serbia.

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
