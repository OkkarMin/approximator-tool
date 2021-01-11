import pyverilog.vparser.ast as vast
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

# FPGA Based Adder Calculation (Using Pyverilog) (Pyverilog Link for installation and usage - https://pypi.org/project/pyverilog/) 

def accurate_sum_calc(acc_bits,input_a,input_b,input_clk,output_sum): # accurate sum FPGA based
    num_inacc_bits=0;

    if(acc_bits>1):
        left=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst(ascii(acc_bits)),vast.IntConst('0')));
        right_val = vast.Plus(vast.Partselect(vast.Identifier(input_a),vast.IntConst(ascii(acc_bits-1)),vast.IntConst('0')),
                              vast.Partselect(vast.Identifier(input_b),vast.IntConst(ascii(acc_bits-1)),vast.IntConst('0')));
    elif(acc_bits==1):
        left=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst('1'),vast.IntConst('0')));
        right_val = vast.Plus(vast.Identifier(input_a),
                              vast.Identifier(input_b));             
    right=vast.Rvalue(right_val);
    total_sum=[vast.NonblockingSubstitution(left,right)];

    always_block=vast.Always(vast.Sens(vast.Identifier(input_clk), type='posedge'),vast.Block(total_sum));
    items=[always_block];
    return items;

def HEAA_sum_calc(acc_bits,num_inacc_bits,input_a,input_b,input_clk,output_sum):    # HEAA sum FPGA based

    left=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst(ascii(acc_bits)),vast.IntConst(ascii(num_inacc_bits))));
    right_val_nocarry_in = vast.Plus(vast.Partselect(vast.Identifier(input_a),vast.IntConst(ascii(acc_bits-1)),vast.IntConst(ascii(num_inacc_bits))),
                                     vast.Partselect(vast.Identifier(input_b),vast.IntConst(ascii(acc_bits-1)),vast.IntConst(ascii(num_inacc_bits))))
    right_val_carry_in = vast.And(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                                  vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1))));
    right_val=vast.Plus(right_val_nocarry_in,right_val_carry_in);
    right=vast.Rvalue(right_val);
    accurate_part_sum=[vast.NonblockingSubstitution(left,right)];

    Left_A=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-1))));
    Right_A=vast.Rvalue(
            vast.And(
                vast.Or(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                        vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))),
                vast.Unot(
                    vast.And(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                             vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))))));
            
    inaccurate_part_sum = [vast.NonblockingSubstitution(Left_A,Right_A)];

    if(num_inacc_bits>2):
        Left_B=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-2)),vast.IntConst('0')));
        Right_B=vast.Rvalue(vast.Or(vast.Partselect(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2)),vast.IntConst('0')),
                                    vast.Partselect(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2)),vast.IntConst('0'))));
    elif(num_inacc_bits==2):
        Left_B=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst('0')));
        Right_B=vast.Rvalue(vast.Or(vast.Pointer(vast.Identifier(input_a),vast.IntConst('0')),
                                    vast.Pointer(vast.Identifier(input_b),vast.IntConst('0'))));      

    inaccurate_part_sum = inaccurate_part_sum  + [vast.NonblockingSubstitution(Left_B,Right_B)];

    total_sum = accurate_part_sum + inaccurate_part_sum;

    always_block=vast.Always(vast.Sens(vast.Identifier(input_clk), type='posedge'),vast.Block(total_sum));
    items=[always_block];
    return items;



def HOERAA_sum_calc(acc_bits,num_inacc_bits,input_a,input_b,input_clk,output_sum):      # HOERAA sum FPGA based

    left=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst(ascii(acc_bits)),vast.IntConst(ascii(num_inacc_bits))));
    right_val_nocarry_in = vast.Plus(vast.Partselect(vast.Identifier(input_a),vast.IntConst(ascii(acc_bits-1)),vast.IntConst(ascii(num_inacc_bits))),
                                     vast.Partselect(vast.Identifier(input_b),vast.IntConst(ascii(acc_bits-1)),vast.IntConst(ascii(num_inacc_bits))))
    right_val_carry_in = vast.And(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                                  vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1))));
    right_val=vast.Plus(right_val_nocarry_in,right_val_carry_in);
    right=vast.Rvalue(right_val);
    accurate_part_sum=[vast.NonblockingSubstitution(left,right)];

    Left_A=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-1))));
    Right_A=vast.Rvalue(
        vast.Or(
            vast.And(
                vast.Or(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                        vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))),
                vast.Unot(
                    vast.And(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                             vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))))),
            vast.And(
                vast.And(
                    vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                    vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))),
                vast.And(
                    vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                    vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2)))))));
    inaccurate_part_sum = [vast.NonblockingSubstitution(Left_A,Right_A)];

    Left_B=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-2))));
    Right_B=vast.Or(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                    vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2))));
    inaccurate_part_sum = inaccurate_part_sum  + [vast.NonblockingSubstitution(Left_B,Right_B)];

    if(num_inacc_bits>2):
        if(num_inacc_bits>3):
            Left_C=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-3)),vast.IntConst('0')));
        elif(num_inacc_bits==3):
            Left_C=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst('0')));
        
        #Right_C=vast.Rvalue(vast.IntConst(ascii(2**(num_inacc_bits-2)-1)));
        Right_C=vast.Rvalue(vast.IntConst(ascii(num_inacc_bits-2)+"'b"+('1'*(num_inacc_bits-2))));
        inaccurate_part_sum = inaccurate_part_sum  + [vast.NonblockingSubstitution(Left_C,Right_C)];

    total_sum = accurate_part_sum + inaccurate_part_sum;

    always_block=vast.Always(vast.Sens(vast.Identifier(input_clk), type='posedge'),vast.Block(total_sum));
    items=[always_block];
    return items;


def HOAANED_sum_calc(acc_bits,num_inacc_bits,input_a,input_b,input_clk,output_sum):         # HOAANED sum FPGA based

    left=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst(ascii(acc_bits)),vast.IntConst(ascii(num_inacc_bits))));
    right_val_nocarry_in = vast.Plus(vast.Partselect(vast.Identifier(input_a),vast.IntConst(ascii(acc_bits-1)),vast.IntConst(ascii(num_inacc_bits))),
                                     vast.Partselect(vast.Identifier(input_b),vast.IntConst(ascii(acc_bits-1)),vast.IntConst(ascii(num_inacc_bits))))
    right_val_carry_in = vast.And(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                                  vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1))));
    right_val=vast.Plus(right_val_nocarry_in,right_val_carry_in);
    right=vast.Rvalue(right_val);
    accurate_part_sum=[vast.NonblockingSubstitution(left,right)];

    Left_A=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-1))));
    Right_A=vast.Rvalue(
        vast.Or(
            vast.And(
                vast.Or(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                        vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))),
                vast.Unot(
                    vast.And(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                             vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))))),
                vast.And(
                    vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                    vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2))))));
    inaccurate_part_sum = [vast.NonblockingSubstitution(Left_A,Right_A)];

    Left_B=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-2))));
    Right_B=vast.Or(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                    vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2))));
    inaccurate_part_sum = inaccurate_part_sum  + [vast.NonblockingSubstitution(Left_B,Right_B)];

    if(num_inacc_bits>2):
        if(num_inacc_bits>3):
            Left_C=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-3)),vast.IntConst('0')));
        elif(num_inacc_bits==3):
            Left_C=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst('0')));            
        #Right_C=vast.Rvalue(vast.IntConst(ascii(2**(num_inacc_bits-2)-1)));
        Right_C=vast.Rvalue(vast.IntConst(ascii(num_inacc_bits-2)+"'b"+('1'*(num_inacc_bits-2))));
        inaccurate_part_sum = inaccurate_part_sum  + [vast.NonblockingSubstitution(Left_C,Right_C)];

    total_sum = accurate_part_sum + inaccurate_part_sum;

    always_block=vast.Always(vast.Sens(vast.Identifier(input_clk), type='posedge'),vast.Block(total_sum));
    items=[always_block];
    return items;



def HERLOA_sum_calc(acc_bits,num_inacc_bits,input_a,input_b,input_clk,output_sum):      # HERLOA sum FPGA Based

    left=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst(ascii(acc_bits)),vast.IntConst(ascii(num_inacc_bits))));
    right_val_nocarry_in = vast.Plus(vast.Partselect(vast.Identifier(input_a),vast.IntConst(ascii(acc_bits-1)),vast.IntConst(ascii(num_inacc_bits))),
                                     vast.Partselect(vast.Identifier(input_b),vast.IntConst(ascii(acc_bits-1)),vast.IntConst(ascii(num_inacc_bits))))
    right_val_carry_in = vast.And(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                                  vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1))));
    right_val=vast.Plus(right_val_nocarry_in,right_val_carry_in);
    right=vast.Rvalue(right_val);
    accurate_part_sum=[vast.NonblockingSubstitution(left,right)];

    Left_A=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-1))));
    Right_A=vast.Rvalue(
        vast.Or(
                vast.Xor(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                        vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))),
                vast.And(
                    vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                    vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2))))));
    
    inaccurate_part_sum = [vast.NonblockingSubstitution(Left_A,Right_A)];

    Left_B=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-2))));
    Right_B=vast.Rvalue(
        vast.And(
            vast.Or(
                vast.Xor(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                         vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))),
                vast.Unot(vast.And(
                    vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                    vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2)))))),
            vast.Or(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                    vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2))))));
    inaccurate_part_sum = inaccurate_part_sum  + [vast.NonblockingSubstitution(Left_B,Right_B)];

    if(num_inacc_bits>2):
        if(num_inacc_bits>3):
            Left_C=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-3)),vast.IntConst('0')));
            #Right_C=vast.Rvalue(vast.IntConst(ascii(2**(num_inacc_bits-2)-1)));
            Right_C1=vast.Rvalue(vast.IntConst(ascii(num_inacc_bits-2)+"'b"+('1'*(num_inacc_bits-2))));
            Right_C2=vast.Rvalue(vast.Or(vast.Partselect(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-3)),vast.IntConst('0')),
                                         vast.Partselect(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-3)),vast.IntConst('0'))));
        elif(num_inacc_bits==3):
            Left_C=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst('0')));
            #Right_C=vast.Rvalue(vast.IntConst(ascii(2**(num_inacc_bits-2)-1)));
            Right_C1=vast.Rvalue(vast.IntConst(ascii(num_inacc_bits-2)+"'b"+('1'*(num_inacc_bits-2))));
            Right_C2=vast.Rvalue(vast.Or(vast.Pointer(vast.Identifier(input_a),vast.IntConst('0')),
                                         vast.Pointer(vast.Identifier(input_b),vast.IntConst('0'))));

        Statement_C = vast.IfStatement(
            vast.Eq(
                vast.And(
                    vast.Xor(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                            vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))),
                    vast.And(
                        vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                        vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2))))) ,
                vast.IntConst('1') ),
            vast.NonblockingSubstitution(Left_C,Right_C1) ,
            vast.NonblockingSubstitution(Left_C,Right_C2));

        inaccurate_part_sum = inaccurate_part_sum  + [Statement_C];

    total_sum = accurate_part_sum + inaccurate_part_sum;

    always_block=vast.Always(vast.Sens(vast.Identifier(input_clk), type='posedge'),vast.Block(total_sum));
    items=[always_block];
    return items;



def M_HERLOA_sum_calc(acc_bits,num_inacc_bits,input_a,input_b,input_clk,output_sum):        # M-HERLOA sum FPGA Based

    left=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst(ascii(acc_bits)),vast.IntConst(ascii(num_inacc_bits))));
    right_val_nocarry_in = vast.Plus(vast.Partselect(vast.Identifier(input_a),vast.IntConst(ascii(acc_bits-1)),vast.IntConst(ascii(num_inacc_bits))),
                                     vast.Partselect(vast.Identifier(input_b),vast.IntConst(ascii(acc_bits-1)),vast.IntConst(ascii(num_inacc_bits))))
    right_val_carry_in = vast.And(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                                  vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1))));
    right_val=vast.Plus(right_val_nocarry_in,right_val_carry_in);
    right=vast.Rvalue(right_val);
    accurate_part_sum=[vast.NonblockingSubstitution(left,right)];

    Left_A=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-1))));
    Right_A=vast.Rvalue(
        vast.Or(
                vast.Xor(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                        vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))),
                vast.And(
                    vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                    vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2))))));
    
    inaccurate_part_sum = [vast.NonblockingSubstitution(Left_A,Right_A)];

    Left_B=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-2))));
    Right_B=vast.Rvalue(
        vast.And(
            vast.Or(
                vast.Xor(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                         vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))),
                vast.Unot(vast.And(
                    vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                    vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2)))))),
            vast.Or(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                    vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2))))));
    inaccurate_part_sum = inaccurate_part_sum  + [vast.NonblockingSubstitution(Left_B,Right_B)];

    if(num_inacc_bits>2):
        Left_C=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-3))));
        Right_C=vast.Rvalue(
            vast.Or(
                vast.And(
                    vast.Xor(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                             vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))),
                    vast.And(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                             vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2))))),
                vast.Or(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-3))),
                        vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-3))))));
        inaccurate_part_sum = inaccurate_part_sum  + [vast.NonblockingSubstitution(Left_C,Right_C)];

    if (num_inacc_bits>3):
        Left_D=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-4))));
        Right_D=vast.Rvalue(
            vast.Or(
                vast.And(
                    vast.Xor(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-1))),
                             vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-1)))),
                    vast.And(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-2))),
                             vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-2))))),
                vast.Or(vast.Pointer(vast.Identifier(input_a),vast.IntConst(ascii(num_inacc_bits-4))),
                        vast.Pointer(vast.Identifier(input_b),vast.IntConst(ascii(num_inacc_bits-4))))));
        inaccurate_part_sum = inaccurate_part_sum  + [vast.NonblockingSubstitution(Left_D,Right_D)];

    if (num_inacc_bits>5):
        Left_E=vast.Lvalue(vast.Partselect(vast.Identifier(output_sum),vast.IntConst(ascii(num_inacc_bits-5)),vast.IntConst('0')));
        Right_E=vast.Rvalue(vast.IntConst(ascii(num_inacc_bits-4)+"'b"+('1'*(num_inacc_bits-4))));
        inaccurate_part_sum = inaccurate_part_sum  + [vast.NonblockingSubstitution(Left_E,Right_E)];
    elif (num_inacc_bits==5):
        Left_E=vast.Lvalue(vast.Pointer(vast.Identifier(output_sum),vast.IntConst('0')));
        Right_E=vast.Rvalue(vast.IntConst(ascii(num_inacc_bits-4)+"'b"+('1'*(num_inacc_bits-4))));
        inaccurate_part_sum = inaccurate_part_sum  + [vast.NonblockingSubstitution(Left_E,Right_E)];


    total_sum = accurate_part_sum + inaccurate_part_sum;

    always_block=vast.Always(vast.Sens(vast.Identifier(input_clk), type='posedge'),vast.Block(total_sum));
    items=[always_block];
    return items;
