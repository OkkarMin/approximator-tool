import adder;
import numpy as np;


# Accurate Multiplier Product
def accurate(num1,num2,N1,N2):
    num1=num1%(2**N1);
    num2=num2%(2**N2);
    return num1*num2;

# Accurate Binary Array Multiplier Product
def accurate_array_multiplier(num1,num2,N1,N2):
    num1=num1%(2**N1);
    num2=num2%(2**N2);
    result=0;
#    N1=8;
#    N2=6;
    A=np.zeros(N1, dtype='int');
    B=np.zeros(N2, dtype='int');
    AND_Gate=np.zeros((N1,N2),dtype='int');
    res=np.zeros((N1,N2),dtype='int');
    carry=np.zeros((N1,N2),dtype='int');
    sum_bit=np.zeros(N1+N2,dtype='int');
    carry_final=np.zeros(N1-1,dtype='int');
    for i in range(N1):
        A[i]=((num1//(2**i))%2);
    for i in range(N2):
        B[i]=((num2//(2**i))%2);
        
    for j in range(N2):
        for i in range(N1):
            AND_Gate[i][j]=(A[i] & B [j]);
            if(j==0):
                res[i][j]=AND_Gate[i][j];
                carry[i][j]=0;
            elif(j==1):
                if(i!=(N1-1)):
                    (res[i][j],carry[i][j])=adder.HalfAdder(AND_Gate[i][j],res[i+1][j-1]);
                    
                else:
                    temp=AND_Gate[i][j];
                    res[i][j]=temp;
                    carry[i][j]=0;
            else:
                if(i!=(N1-1)):
                    (res[i][j], carry[i][j])= adder.FullAdder(AND_Gate[i][j],res[i+1][j-1],carry[i][j-1]);
                else:
                    res[i][j]=AND_Gate[i][j];
                    carry[i][j]=0;
        sum_bit[j]=res[0][j];
        

    
    for i in range(N2,N1+N2-1):
        if(i==N2):
            (sum_bit[i],carry_final[i-N2])=adder.HalfAdder(res[i+1-N2][N2-1],carry[i-N2][N2-1]);
        else:
            (sum_bit[i],carry_final[i-N2])=adder.FullAdder(res[i+1-N2][N2-1],carry[i-N2][N2-1],carry_final[i-N2-1]);
    sum_bit[N1+N2-1]=carry_final[N1-2];

    for k in range(N1+N2):
        result = result + sum_bit[k]*(2**(k));

    return result;

# Approximate PAAM01 multiplier product with different V-cuts

def PAAM01(num1,num2,N1,N2,V_val):
    num1=num1%(2**N1);
    num2=num2%(2**N2);
    result=0;
#    N1=8;
#    N2=6;
    A=np.zeros(N1, dtype='int');
    B=np.zeros(N2, dtype='int');
    AND_Gate=np.zeros((N1,N2),dtype='int');
    res=np.zeros((N1,N2),dtype='int');
    carry=np.zeros((N1,N2),dtype='int');
    sum_bit=np.zeros(N1+N2,dtype='int');
    carry_final=np.zeros(N1-1,dtype='int');
    for i in range(N1):
        A[i]=((num1//(2**i))%2);
    for i in range(N2):
        B[i]=((num2//(2**i))%2);
        
    for j in range(N2):
        for i in range(N1):
            AND_Gate[i][j]=(A[i] & B [j]);
            if((i+j)<=V_val):
                res[i][j]=1;
                carry[i][j]=0;
            else:
                if(j==0):
                    res[i][j]=AND_Gate[i][j];
                    carry[i][j]=0;
                elif(j==1):
                    if(i!=(N1-1)):
                        (res[i][j],carry[i][j])=adder.HalfAdder(AND_Gate[i][j],res[i+1][j-1]);
                    
                    else:
                        temp=AND_Gate[i][j];
                        res[i][j]=temp;
                        carry[i][j]=0;
                else:
                    if(i!=(N1-1)):
                        (res[i][j], carry[i][j])= adder.FullAdder(AND_Gate[i][j],res[i+1][j-1],carry[i][j-1]);
                    else:
                        res[i][j]=AND_Gate[i][j];
                        carry[i][j]=0;
        sum_bit[j]=res[0][j];
        

    
    for i in range(N2,N1+N2-1):
        if(i==N2):
            (sum_bit[i],carry_final[i-N2])=adder.HalfAdder(res[i+1-N2][N2-1],carry[i-N2][N2-1]);
        else:
            (sum_bit[i],carry_final[i-N2])=adder.FullAdder(res[i+1-N2][N2-1],carry[i-N2][N2-1],carry_final[i-N2-1]);
    sum_bit[N1+N2-1]=carry_final[N1-2];

    for k in range(N1+N2):
        result = result + sum_bit[k]*(2**(k));

    return result;

