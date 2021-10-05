import ApproximateComputingVerilog
import ApproximateComputingError
import ApproximateComputingAccuracy

exit_flag = 0

while True:
    print("Types of Tasks:\t")
    print("1. Verilog Code Generator ")
    print("2. Error Analysis ( MAE and RMSE Calculation ) ")
    print("3. Accuracy Analysis Based on user inputs")
    print("q. Quit")
    print()
    user_inp = input("Enter your choice - \t")

    if user_inp == "1":
        exit_flag = ApproximateComputingVerilog.runVerilog()
        # Verilog Code Generator
    elif user_inp == "2":
        exit_flag = ApproximateComputingError.runError()
        # Error Analysis ( MAE and RMSE Calculation )
    elif user_inp == "3":
        exit_flag = ApproximateComputingAccuracy.runAccuracy()
        # Accuracy Analysis Based on user inputs

    elif user_inp == "q" or user_inp == "Q":  # Quit
        exit_flag = 1
        break
    else:
        print("\nWARNING: Wrong choice. Enter Valid Choice\n")

    if exit_flag == 1:
        break

if exit_flag == 1:
    print("\nEXITING THE TOOL!")
