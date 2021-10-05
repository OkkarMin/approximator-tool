from veriloggen import *

##########################################################################

# Used for ASIC Based Approximate Adder Design
# Using veriloggen
# Veriloggen link for installation and usage (https://pypi.org/project/veriloggen/)

##########################################################################

##Generic Adders

# HEAA


def HEAA_Generic(N, k):

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))

    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(andinp1, andinp2))

    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))

    NotModule = Module("not_1inp")
    notoutp = NotModule.Output("res")
    notinp = NotModule.Input("inp")
    notoutp.assign(Not(notinp))

    AndOrModule = Module("ao21")
    andorinp1 = AndOrModule.Input("a")
    andorinp2 = AndOrModule.Input("b")
    andorinp3 = AndOrModule.Input("c")
    andoroutp = AndOrModule.Output("y")
    andorwire1 = AndOrModule.Wire("net")
    AndOrModule.Instance(AndModule, "t1", ports=[andorwire1, andorinp1, andorinp2])
    AndOrModule.Instance(OrModule, "t2", ports=[andoroutp, andorwire1, andorinp3])

    Add4BitModule = Module("frcla_4b")
    add4bitinpa3 = Add4BitModule.Input("a3")
    add4bitinpa2 = Add4BitModule.Input("a2")
    add4bitinpa1 = Add4BitModule.Input("a1")
    add4bitinpa0 = Add4BitModule.Input("a0")
    add4bitinpb3 = Add4BitModule.Input("b3")
    add4bitinpb2 = Add4BitModule.Input("b2")
    add4bitinpb1 = Add4BitModule.Input("b1")
    add4bitinpb0 = Add4BitModule.Input("b0")
    add4bitinpc0 = Add4BitModule.Input("c0")
    add4bitc4 = Add4BitModule.Output("c4")
    add4bitsum3 = Add4BitModule.Output("sum3")
    add4bitsum2 = Add4BitModule.Output("sum2")
    add4bitsum1 = Add4BitModule.Output("sum1")
    add4bitsum0 = Add4BitModule.Output("sum0")
    add4bitg3 = Add4BitModule.Wire("g3")
    add4bitg2 = Add4BitModule.Wire("g2")
    add4bitg1 = Add4BitModule.Wire("g1")
    add4bitg0 = Add4BitModule.Wire("g0")
    add4bitp3 = Add4BitModule.Wire("p3")
    add4bitp2 = Add4BitModule.Wire("p2")
    add4bitp1 = Add4BitModule.Wire("p1")
    add4bitp0 = Add4BitModule.Wire("p0")
    add4bitc1 = Add4BitModule.Wire("c1")
    add4bitc2 = Add4BitModule.Wire("c2")
    add4bitc3 = Add4BitModule.Wire("c3")
    add4bitm1 = Add4BitModule.Wire("m1")
    add4bitm2 = Add4BitModule.Wire("m2")
    add4bitm3 = Add4BitModule.Wire("m3")
    add4bitm4 = Add4BitModule.Wire("m4")
    add4bitm5 = Add4BitModule.Wire("m5")
    add4bitm6 = Add4BitModule.Wire("m6")

    Add4BitModule.Instance(
        AndModule, "gate1", ports=[add4bitg0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        AndModule, "gate2", ports=[add4bitg1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        AndModule, "gate3", ports=[add4bitg2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        AndModule, "gate4", ports=[add4bitg3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        XorModule, "gate5", ports=[add4bitp0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        XorModule, "gate6", ports=[add4bitp1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        XorModule, "gate7", ports=[add4bitp2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        XorModule, "gate8", ports=[add4bitp3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        AndOrModule, "comp1", ports=[add4bitp1, add4bitg0, add4bitg1, add4bitm1]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp2", ports=[add4bitm1, add4bitp2, add4bitg2, add4bitm2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp3", ports=[add4bitm2, add4bitp3, add4bitg3, add4bitm3]
    )

    Add4BitModule.Instance(AndModule, "and1", ports=[add4bitm4, add4bitp1, add4bitp0])
    Add4BitModule.Instance(AndModule, "and2", ports=[add4bitm5, add4bitp2, add4bitm4])
    Add4BitModule.Instance(AndModule, "and3", ports=[add4bitm6, add4bitp3, add4bitm5])

    Add4BitModule.Instance(
        AndOrModule, "comp4", ports=[add4bitm6, add4bitinpc0, add4bitm3, add4bitc4]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp5", ports=[add4bitm5, add4bitinpc0, add4bitm2, add4bitc3]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp6", ports=[add4bitm4, add4bitinpc0, add4bitm1, add4bitc2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp7", ports=[add4bitp0, add4bitinpc0, add4bitg0, add4bitc1]
    )

    Add4BitModule.Instance(
        XorModule, "xorg1", ports=[add4bitsum0, add4bitp0, add4bitinpc0]
    )
    Add4BitModule.Instance(
        XorModule, "xorg2", ports=[add4bitsum1, add4bitp1, add4bitc1]
    )
    Add4BitModule.Instance(
        XorModule, "xorg3", ports=[add4bitsum2, add4bitp2, add4bitc2]
    )
    Add4BitModule.Instance(
        XorModule, "xorg4", ports=[add4bitsum3, add4bitp3, add4bitc3]
    )

    if ((N - k) % 4) == 3:
        Add3BitModule = Module("frcla_3b")
        add3bitinpa2 = Add3BitModule.Input("a2")
        add3bitinpa1 = Add3BitModule.Input("a1")
        add3bitinpa0 = Add3BitModule.Input("a0")
        add3bitinpb2 = Add3BitModule.Input("b2")
        add3bitinpb1 = Add3BitModule.Input("b1")
        add3bitinpb0 = Add3BitModule.Input("b0")
        add3bitinpc0 = Add3BitModule.Input("c0")
        add3bitc3 = Add3BitModule.Output("c3")
        add3bitsum2 = Add3BitModule.Output("sum2")
        add3bitsum1 = Add3BitModule.Output("sum1")
        add3bitsum0 = Add3BitModule.Output("sum0")

        add3bitg2 = Add3BitModule.Wire("g2")
        add3bitg1 = Add3BitModule.Wire("g1")
        add3bitg0 = Add3BitModule.Wire("g0")

        add3bitp2 = Add3BitModule.Wire("p2")
        add3bitp1 = Add3BitModule.Wire("p1")
        add3bitp0 = Add3BitModule.Wire("p0")
        add3bitc1 = Add3BitModule.Wire("c1")
        add3bitc2 = Add3BitModule.Wire("c2")

        add3bitm1 = Add3BitModule.Wire("m1")
        add3bitm2 = Add3BitModule.Wire("m2")

        add3bitm4 = Add3BitModule.Wire("m4")
        add3bitm5 = Add3BitModule.Wire("m5")

        Add3BitModule.Instance(
            AndModule, "gate1", ports=[add3bitg0, add3bitinpa0, add3bitinpb0]
        )
        Add3BitModule.Instance(
            AndModule, "gate2", ports=[add3bitg1, add3bitinpa1, add3bitinpb1]
        )
        Add3BitModule.Instance(
            AndModule, "gate3", ports=[add3bitg2, add3bitinpa2, add3bitinpb2]
        )

        Add3BitModule.Instance(
            XorModule, "gate5", ports=[add3bitp0, add3bitinpa0, add3bitinpb0]
        )
        Add3BitModule.Instance(
            XorModule, "gate6", ports=[add3bitp1, add3bitinpa1, add3bitinpb1]
        )
        Add3BitModule.Instance(
            XorModule, "gate7", ports=[add3bitp2, add3bitinpa2, add3bitinpb2]
        )

        Add3BitModule.Instance(
            AndOrModule, "comp1", ports=[add3bitp1, add3bitg0, add3bitg1, add3bitm1]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp2", ports=[add3bitm1, add3bitp2, add3bitg2, add3bitm2]
        )

        Add3BitModule.Instance(
            AndModule, "and1", ports=[add3bitm4, add3bitp1, add3bitp0]
        )
        Add3BitModule.Instance(
            AndModule, "and2", ports=[add3bitm5, add3bitp2, add3bitm4]
        )

        Add3BitModule.Instance(
            AndOrModule, "comp5", ports=[add3bitm5, add3bitinpc0, add3bitm2, add3bitc3]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp6", ports=[add3bitm4, add3bitinpc0, add3bitm1, add3bitc2]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp7", ports=[add3bitp0, add3bitinpc0, add3bitg0, add3bitc1]
        )

        Add3BitModule.Instance(
            XorModule, "xorg1", ports=[add3bitsum0, add3bitp0, add3bitinpc0]
        )
        Add3BitModule.Instance(
            XorModule, "xorg2", ports=[add3bitsum1, add3bitp1, add3bitc1]
        )
        Add3BitModule.Instance(
            XorModule, "xorg3", ports=[add3bitsum2, add3bitp2, add3bitc2]
        )

    elif ((N - k) % 4) == 2:
        Add2BitModule = Module("frcla_2b")
        add2bitinpa1 = Add2BitModule.Input("a1")
        add2bitinpa0 = Add2BitModule.Input("a0")
        add2bitinpb1 = Add2BitModule.Input("b1")
        add2bitinpb0 = Add2BitModule.Input("b0")
        add2bitinpc0 = Add2BitModule.Input("c0")
        add2bitc2 = Add2BitModule.Output("c2")
        add2bitsum1 = Add2BitModule.Output("sum1")
        add2bitsum0 = Add2BitModule.Output("sum0")
        add2bitg1 = Add2BitModule.Wire("g1")
        add2bitg0 = Add2BitModule.Wire("g0")
        add2bitp1 = Add2BitModule.Wire("p1")
        add2bitp0 = Add2BitModule.Wire("p0")
        add2bitc1 = Add2BitModule.Wire("c1")
        add2bitm1 = Add2BitModule.Wire("m1")
        add2bitm2 = Add2BitModule.Wire("m2")

        Add2BitModule.Instance(
            AndModule, "gate1", ports=[add2bitg0, add2bitinpa0, add2bitinpb0]
        )
        Add2BitModule.Instance(
            AndModule, "gate2", ports=[add2bitg1, add2bitinpa1, add2bitinpb1]
        )

        Add2BitModule.Instance(
            XorModule, "gate5", ports=[add2bitp0, add2bitinpa0, add2bitinpb0]
        )
        Add2BitModule.Instance(
            XorModule, "gate6", ports=[add2bitp1, add2bitinpa1, add2bitinpb1]
        )

        Add2BitModule.Instance(
            AndOrModule, "comp1", ports=[add2bitp1, add2bitg0, add2bitg1, add2bitm1]
        )

        Add2BitModule.Instance(
            AndModule, "and1", ports=[add2bitm2, add2bitp1, add2bitp0]
        )

        Add2BitModule.Instance(
            AndOrModule, "comp6", ports=[add2bitm2, add2bitinpc0, add2bitm1, add2bitc2]
        )
        Add2BitModule.Instance(
            AndOrModule, "comp7", ports=[add2bitp0, add2bitinpc0, add2bitg0, add2bitc1]
        )

        Add2BitModule.Instance(
            XorModule, "xorg1", ports=[add2bitsum0, add2bitp0, add2bitinpc0]
        )
        Add2BitModule.Instance(
            XorModule, "xorg2", ports=[add2bitsum1, add2bitp1, add2bitc1]
        )

    elif ((N - k) % 4) == 1:
        Add1BitModule = Module("frcla_1b")
        add1bitinpa0 = Add1BitModule.Input("a0")
        add1bitinpb0 = Add1BitModule.Input("b0")
        add1bitinpc0 = Add1BitModule.Input("c0")
        add1bitc1 = Add1BitModule.Output("c1")
        add1bitsum0 = Add1BitModule.Output("sum0")
        add1bitg0 = Add1BitModule.Wire("g0")
        add1bitp0 = Add1BitModule.Wire("p0")
        Add1BitModule.Instance(
            AndModule, "gate1", ports=[add1bitg0, add1bitinpa0, add1bitinpb0]
        )
        Add1BitModule.Instance(
            XorModule, "gate5", ports=[add1bitp0, add1bitinpa0, add1bitinpb0]
        )
        Add1BitModule.Instance(
            AndOrModule, "comp7", ports=[add1bitp0, add1bitinpc0, add1bitg0, add1bitc1]
        )
        Add1BitModule.Instance(
            XorModule, "xorg1", ports=[add1bitsum0, add1bitp0, add1bitinpc0]
        )

    Adder = Module("heaa_" + str(N) + "b" + str(k) + "inacc")
    a = Adder.Input("a", N)
    b = Adder.Input("b", N)
    res = Adder.Output("sum", N + 1)
    w1 = Adder.Wire("w1")
    w2 = Adder.Wire("w2")
    w3 = Adder.Wire("w3")

    temp = k + ((N - k) % 4)
    if (N - k) % 4 == 0:
        k = k + 4

    while temp < N:
        statement1 = "cout" + str(temp) + "=Adder.Wire('cout" + str(temp) + "');"
        exec(statement1)
        temp = temp + 4
    ##    cout12=Adder.Wire('cout12');
    ##    cout16=Adder.Wire('cout16');
    ##    cout20=Adder.Wire('cout20');
    ##    cout24=Adder.Wire('cout24');
    ##    cout28=Adder.Wire('cout28');

    ## Inaccurate Part

    for it1 in range(k - 1):
        Adder.Instance(OrModule, ("t" + str(it1 + 1)), ports=[res[it1], a[it1], b[it1]])

    ##    Adder.Instance(OrModule,'t1',ports=[res[0],a[0],b[0]]);
    ##    Adder.Instance(OrModule,'t2',ports=[res[1],a[1],b[1]]);
    ##    Adder.Instance(OrModule,'t3',ports=[res[2],a[2],b[2]]);
    ##    Adder.Instance(OrModule,'t4',ports=[res[3],a[3],b[3]]);
    ##    Adder.Instance(OrModule,'t5',ports=[res[4],a[4],b[4]]);
    ##    Adder.Instance(OrModule,'t6',ports=[res[5],a[5],b[5]]);
    ##    Adder.Instance(OrModule,'t7',ports=[res[6],a[6],b[6]]);
    ##    Adder.Instance(OrModule,'t8',ports=[res[7],a[7],b[7]]);
    ##    Adder.Instance(OrModule,'t9',ports=[res[8],a[8],b[8]]);

    Adder.Instance(AndModule, ("t" + str(k)), ports=[w1, a[k - 1], b[k - 1]])
    Adder.Instance(NotModule, ("t" + str(k + 1)), ports=[w2, w1])
    Adder.Instance(OrModule, ("t" + str(k + 2)), ports=[w3, a[k - 1], b[k - 1]])
    Adder.Instance(AndModule, ("t" + str(k + 3)), ports=[res[k - 1], w3, w2])

    ##    Adder.Instance(AndModule,'t10',ports=[w1,a[9],b[9]]);
    ##    Adder.Instance(NotModule,'t11',ports=[w2,w1]);
    ##    Adder.Instance(OrModule,'t12',ports=[w3,a[9],b[9]]);
    ##    Adder.Instance(AndModule,'t13',ports=[res[9],w3,w2]);

    ## Accurate Part

    cla_count = 0
    temp = k + ((N - k) % 4)
    if (N - k) % 4 == 0:
        k = k + 4

    if temp < N:
        if (N - k) % 4 == 1:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add1BitModule,'cla%d',ports=[a[k],b[k],w1,cout%d,res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add1BitModule,('cla'+str(cla_count)),ports=[a[k],b[k],w1,cout1,res[k]]);
        elif (N - k) % 4 == 2:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add2BitModule,'cla%d',ports=[a[k+1],a[k],b[k+1],b[k],w1,cout%d,res[k+1],res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add2BitModule,('cla'+str(cla_count)),ports=[a[k+1],a[k],b[k+1],b[k],w1,cout1,res[k+1],res[k]]);
        elif (N - k) % 4 == 3:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add3BitModule,'cla%d',ports=[a[k+2],a[k+1],a[k],b[k+2],b[k+1],b[k],w1,cout%d,res[k+2],res[k+1],res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add3BitModule,('cla'+str(cla_count)),ports=[a[k+2],a[k+1],a[k],b[k+2],b[k+1],b[k],w1,cout1,res[k+2],res[k+1],res[k]]);

        ##    Adder.Instance(Add2BitModule,'cla1',ports=[a[11],a[10],b[11],b[10],w1,cout12,res[11],res[10]]);

        while temp < N:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add4BitModule,'cla%d',ports=[a[temp-1],a[temp-2],a[temp-3],a[temp-4],b[temp-1],b[temp-2], \
                 b[temp-3],b[temp-4],cout%d,cout%d,res[temp-1],res[temp-2],res[temp-3],res[temp-4]]);"
                % (cla_count, (temp - 4), temp)
            )
            temp = temp + 4

        ##    Adder.Instance(Add4BitModule,'cla2',ports=[a[15],a[14],a[13],a[12],b[15],b[14],b[13],b[12],cout12,cout16,res[15],res[14],res[13],res[12]]);
        ##    Adder.Instance(Add4BitModule,'cla3',ports=[a[19],a[18],a[17],a[16],b[19],b[18],b[17],b[16],cout16,cout20,res[19],res[18],res[17],res[16]]);
        ##    Adder.Instance(Add4BitModule,'cla4',ports=[a[23],a[22],a[21],a[20],b[23],b[22],b[21],b[20],cout20,cout24,res[23],res[22],res[21],res[20]]);
        ##    Adder.Instance(Add4BitModule,'cla5',ports=[a[27],a[26],a[25],a[24],b[27],b[26],b[25],b[24],cout24,cout28,res[27],res[26],res[25],res[24]]);
        cla_count = cla_count + 1
        exec(
            "Adder.Instance(Add4BitModule,'cla%d',ports=[a[temp-1],a[temp-2],a[temp-3],a[temp-4],b[temp-1],b[temp-2], \
             b[temp-3],b[temp-4],cout%d,res[temp],res[temp-1],res[temp-2],res[temp-3],res[temp-4]]);"
            % (cla_count, (temp - 4))
        )

    ##    Adder.Instance(Add4BitModule,'cla6',ports=[a[31],a[30],a[29],a[28],b[31],b[30],b[29],b[28],cout28,res[32],res[31],res[30],res[29],res[28]]);
    else:
        if (N - k) % 4 == 1:
            Adder.Instance(
                Add1BitModule, "cla1", ports=[a[k], b[k], w1, res[k + 1], res[k]]
            )
        elif (N - k) % 4 == 2:
            Adder.Instance(
                Add2BitModule,
                "cla1",
                ports=[
                    a[k + 1],
                    a[k],
                    b[k + 1],
                    b[k],
                    w1,
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )
        elif (N - k) % 4 == 3:
            Adder.Instance(
                Add3BitModule,
                "cla1",
                ports=[
                    a[k + 2],
                    a[k + 1],
                    a[k],
                    b[k + 2],
                    b[k + 1],
                    b[k],
                    w1,
                    res[k + 3],
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )
        else:
            Adder.Instance(
                Add4BitModule,
                "cla1",
                ports=[
                    a[k + 3],
                    a[k + 2],
                    a[k + 1],
                    a[k],
                    b[k + 3],
                    b[k + 2],
                    b[k + 1],
                    b[k],
                    w1,
                    res[k + 4],
                    res[k + 3],
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )

    return Adder


# HOERAA


def HOERAA_Generic(N, k):

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))

    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(andinp1, andinp2))

    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))

    NotModule = Module("not_1inp")
    notoutp = NotModule.Output("res")
    notinp = NotModule.Input("inp")
    notoutp.assign(Not(notinp))

    AndOrModule = Module("ao21")
    andorinp1 = AndOrModule.Input("a")
    andorinp2 = AndOrModule.Input("b")
    andorinp3 = AndOrModule.Input("c")
    andoroutp = AndOrModule.Output("y")
    andorwire1 = AndOrModule.Wire("net")
    AndOrModule.Instance(AndModule, "t1", ports=[andorwire1, andorinp1, andorinp2])
    AndOrModule.Instance(OrModule, "t2", ports=[andoroutp, andorwire1, andorinp3])

    Add4BitModule = Module("frcla_4b")
    add4bitinpa3 = Add4BitModule.Input("a3")
    add4bitinpa2 = Add4BitModule.Input("a2")
    add4bitinpa1 = Add4BitModule.Input("a1")
    add4bitinpa0 = Add4BitModule.Input("a0")
    add4bitinpb3 = Add4BitModule.Input("b3")
    add4bitinpb2 = Add4BitModule.Input("b2")
    add4bitinpb1 = Add4BitModule.Input("b1")
    add4bitinpb0 = Add4BitModule.Input("b0")
    add4bitinpc0 = Add4BitModule.Input("c0")
    add4bitc4 = Add4BitModule.Output("c4")
    add4bitsum3 = Add4BitModule.Output("sum3")
    add4bitsum2 = Add4BitModule.Output("sum2")
    add4bitsum1 = Add4BitModule.Output("sum1")
    add4bitsum0 = Add4BitModule.Output("sum0")
    add4bitg3 = Add4BitModule.Wire("g3")
    add4bitg2 = Add4BitModule.Wire("g2")
    add4bitg1 = Add4BitModule.Wire("g1")
    add4bitg0 = Add4BitModule.Wire("g0")
    add4bitp3 = Add4BitModule.Wire("p3")
    add4bitp2 = Add4BitModule.Wire("p2")
    add4bitp1 = Add4BitModule.Wire("p1")
    add4bitp0 = Add4BitModule.Wire("p0")
    add4bitc1 = Add4BitModule.Wire("c1")
    add4bitc2 = Add4BitModule.Wire("c2")
    add4bitc3 = Add4BitModule.Wire("c3")
    add4bitm1 = Add4BitModule.Wire("m1")
    add4bitm2 = Add4BitModule.Wire("m2")
    add4bitm3 = Add4BitModule.Wire("m3")
    add4bitm4 = Add4BitModule.Wire("m4")
    add4bitm5 = Add4BitModule.Wire("m5")
    add4bitm6 = Add4BitModule.Wire("m6")

    Add4BitModule.Instance(
        AndModule, "gate1", ports=[add4bitg0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        AndModule, "gate2", ports=[add4bitg1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        AndModule, "gate3", ports=[add4bitg2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        AndModule, "gate4", ports=[add4bitg3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        XorModule, "gate5", ports=[add4bitp0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        XorModule, "gate6", ports=[add4bitp1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        XorModule, "gate7", ports=[add4bitp2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        XorModule, "gate8", ports=[add4bitp3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        AndOrModule, "comp1", ports=[add4bitp1, add4bitg0, add4bitg1, add4bitm1]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp2", ports=[add4bitm1, add4bitp2, add4bitg2, add4bitm2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp3", ports=[add4bitm2, add4bitp3, add4bitg3, add4bitm3]
    )

    Add4BitModule.Instance(AndModule, "and1", ports=[add4bitm4, add4bitp1, add4bitp0])
    Add4BitModule.Instance(AndModule, "and2", ports=[add4bitm5, add4bitp2, add4bitm4])
    Add4BitModule.Instance(AndModule, "and3", ports=[add4bitm6, add4bitp3, add4bitm5])

    Add4BitModule.Instance(
        AndOrModule, "comp4", ports=[add4bitm6, add4bitinpc0, add4bitm3, add4bitc4]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp5", ports=[add4bitm5, add4bitinpc0, add4bitm2, add4bitc3]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp6", ports=[add4bitm4, add4bitinpc0, add4bitm1, add4bitc2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp7", ports=[add4bitp0, add4bitinpc0, add4bitg0, add4bitc1]
    )

    Add4BitModule.Instance(
        XorModule, "xorg1", ports=[add4bitsum0, add4bitp0, add4bitinpc0]
    )
    Add4BitModule.Instance(
        XorModule, "xorg2", ports=[add4bitsum1, add4bitp1, add4bitc1]
    )
    Add4BitModule.Instance(
        XorModule, "xorg3", ports=[add4bitsum2, add4bitp2, add4bitc2]
    )
    Add4BitModule.Instance(
        XorModule, "xorg4", ports=[add4bitsum3, add4bitp3, add4bitc3]
    )

    if ((N - k) % 4) == 3:
        Add3BitModule = Module("frcla_3b")
        add3bitinpa2 = Add3BitModule.Input("a2")
        add3bitinpa1 = Add3BitModule.Input("a1")
        add3bitinpa0 = Add3BitModule.Input("a0")
        add3bitinpb2 = Add3BitModule.Input("b2")
        add3bitinpb1 = Add3BitModule.Input("b1")
        add3bitinpb0 = Add3BitModule.Input("b0")
        add3bitinpc0 = Add3BitModule.Input("c0")
        add3bitc3 = Add3BitModule.Output("c3")
        add3bitsum2 = Add3BitModule.Output("sum2")
        add3bitsum1 = Add3BitModule.Output("sum1")
        add3bitsum0 = Add3BitModule.Output("sum0")

        add3bitg2 = Add3BitModule.Wire("g2")
        add3bitg1 = Add3BitModule.Wire("g1")
        add3bitg0 = Add3BitModule.Wire("g0")

        add3bitp2 = Add3BitModule.Wire("p2")
        add3bitp1 = Add3BitModule.Wire("p1")
        add3bitp0 = Add3BitModule.Wire("p0")
        add3bitc1 = Add3BitModule.Wire("c1")
        add3bitc2 = Add3BitModule.Wire("c2")

        add3bitm1 = Add3BitModule.Wire("m1")
        add3bitm2 = Add3BitModule.Wire("m2")

        add3bitm4 = Add3BitModule.Wire("m4")
        add3bitm5 = Add3BitModule.Wire("m5")

        Add3BitModule.Instance(
            AndModule, "gate1", ports=[add3bitg0, add3bitinpa0, add3bitinpb0]
        )
        Add3BitModule.Instance(
            AndModule, "gate2", ports=[add3bitg1, add3bitinpa1, add3bitinpb1]
        )
        Add3BitModule.Instance(
            AndModule, "gate3", ports=[add3bitg2, add3bitinpa2, add3bitinpb2]
        )

        Add3BitModule.Instance(
            XorModule, "gate5", ports=[add3bitp0, add3bitinpa0, add3bitinpb0]
        )
        Add3BitModule.Instance(
            XorModule, "gate6", ports=[add3bitp1, add3bitinpa1, add3bitinpb1]
        )
        Add3BitModule.Instance(
            XorModule, "gate7", ports=[add3bitp2, add3bitinpa2, add3bitinpb2]
        )

        Add3BitModule.Instance(
            AndOrModule, "comp1", ports=[add3bitp1, add3bitg0, add3bitg1, add3bitm1]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp2", ports=[add3bitm1, add3bitp2, add3bitg2, add3bitm2]
        )

        Add3BitModule.Instance(
            AndModule, "and1", ports=[add3bitm4, add3bitp1, add3bitp0]
        )
        Add3BitModule.Instance(
            AndModule, "and2", ports=[add3bitm5, add3bitp2, add3bitm4]
        )

        Add3BitModule.Instance(
            AndOrModule, "comp5", ports=[add3bitm5, add3bitinpc0, add3bitm2, add3bitc3]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp6", ports=[add3bitm4, add3bitinpc0, add3bitm1, add3bitc2]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp7", ports=[add3bitp0, add3bitinpc0, add3bitg0, add3bitc1]
        )

        Add3BitModule.Instance(
            XorModule, "xorg1", ports=[add3bitsum0, add3bitp0, add3bitinpc0]
        )
        Add3BitModule.Instance(
            XorModule, "xorg2", ports=[add3bitsum1, add3bitp1, add3bitc1]
        )
        Add3BitModule.Instance(
            XorModule, "xorg3", ports=[add3bitsum2, add3bitp2, add3bitc2]
        )

    elif ((N - k) % 4) == 2:
        Add2BitModule = Module("frcla_2b")
        add2bitinpa1 = Add2BitModule.Input("a1")
        add2bitinpa0 = Add2BitModule.Input("a0")
        add2bitinpb1 = Add2BitModule.Input("b1")
        add2bitinpb0 = Add2BitModule.Input("b0")
        add2bitinpc0 = Add2BitModule.Input("c0")
        add2bitc2 = Add2BitModule.Output("c2")
        add2bitsum1 = Add2BitModule.Output("sum1")
        add2bitsum0 = Add2BitModule.Output("sum0")
        add2bitg1 = Add2BitModule.Wire("g1")
        add2bitg0 = Add2BitModule.Wire("g0")
        add2bitp1 = Add2BitModule.Wire("p1")
        add2bitp0 = Add2BitModule.Wire("p0")
        add2bitc1 = Add2BitModule.Wire("c1")
        add2bitm1 = Add2BitModule.Wire("m1")
        add2bitm2 = Add2BitModule.Wire("m2")

        Add2BitModule.Instance(
            AndModule, "gate1", ports=[add2bitg0, add2bitinpa0, add2bitinpb0]
        )
        Add2BitModule.Instance(
            AndModule, "gate2", ports=[add2bitg1, add2bitinpa1, add2bitinpb1]
        )

        Add2BitModule.Instance(
            XorModule, "gate5", ports=[add2bitp0, add2bitinpa0, add2bitinpb0]
        )
        Add2BitModule.Instance(
            XorModule, "gate6", ports=[add2bitp1, add2bitinpa1, add2bitinpb1]
        )

        Add2BitModule.Instance(
            AndOrModule, "comp1", ports=[add2bitp1, add2bitg0, add2bitg1, add2bitm1]
        )

        Add2BitModule.Instance(
            AndModule, "and1", ports=[add2bitm2, add2bitp1, add2bitp0]
        )

        Add2BitModule.Instance(
            AndOrModule, "comp6", ports=[add2bitm2, add2bitinpc0, add2bitm1, add2bitc2]
        )
        Add2BitModule.Instance(
            AndOrModule, "comp7", ports=[add2bitp0, add2bitinpc0, add2bitg0, add2bitc1]
        )

        Add2BitModule.Instance(
            XorModule, "xorg1", ports=[add2bitsum0, add2bitp0, add2bitinpc0]
        )
        Add2BitModule.Instance(
            XorModule, "xorg2", ports=[add2bitsum1, add2bitp1, add2bitc1]
        )

    elif ((N - k) % 4) == 1:
        Add1BitModule = Module("frcla_1b")
        add1bitinpa0 = Add1BitModule.Input("a0")
        add1bitinpb0 = Add1BitModule.Input("b0")
        add1bitinpc0 = Add1BitModule.Input("c0")
        add1bitc1 = Add1BitModule.Output("c1")
        add1bitsum0 = Add1BitModule.Output("sum0")
        add1bitg0 = Add1BitModule.Wire("g0")
        add1bitp0 = Add1BitModule.Wire("p0")
        Add1BitModule.Instance(
            AndModule, "gate1", ports=[add1bitg0, add1bitinpa0, add1bitinpb0]
        )
        Add1BitModule.Instance(
            XorModule, "gate5", ports=[add1bitp0, add1bitinpa0, add1bitinpb0]
        )
        Add1BitModule.Instance(
            AndOrModule, "comp7", ports=[add1bitp0, add1bitinpc0, add1bitg0, add1bitc1]
        )
        Add1BitModule.Instance(
            XorModule, "xorg1", ports=[add1bitsum0, add1bitp0, add1bitinpc0]
        )

    Adder = Module("hoeraa_" + str(N) + "b" + str(k) + "inacc")
    a = Adder.Input("a", N)
    b = Adder.Input("b", N)
    res = Adder.Output("sum", N + 1)
    n1 = Adder.Wire("n1")
    n2 = Adder.Wire("n2")
    n3 = Adder.Wire("n3")
    n4 = Adder.Wire("n4")
    n5 = Adder.Wire("n5")
    n6 = Adder.Wire("n6")

    temp = k + ((N - k) % 4)
    if (N - k) % 4 == 0:
        k = k + 4

    while temp < N:
        statement1 = "cout" + str(temp) + "=Adder.Wire('cout" + str(temp) + "');"
        exec(statement1)
        temp = temp + 4
    ##    cout12=Adder.Wire('cout12');
    ##    cout16=Adder.Wire('cout16');
    ##    cout20=Adder.Wire('cout20');
    ##    cout24=Adder.Wire('cout24');
    ##    cout28=Adder.Wire('cout28');

    ## Inaccurate Part

    for it1 in range(k - 2):
        res[it1].assign(1)

    ##    res[0].assign(1);
    ##    res[1].assign(1);
    ##    res[2].assign(1);
    ##    res[3].assign(1);
    ##    res[4].assign(1);
    ##    res[5].assign(1);
    ##    res[6].assign(1);
    ##    res[7].assign(1);

    Adder.Instance(OrModule, "t1", ports=[res[k - 2], a[k - 2], b[k - 2]])
    Adder.Instance(AndModule, "t2", ports=[n1, a[k - 1], b[k - 1]])
    Adder.Instance(NotModule, "t3", ports=[n2, n1])
    Adder.Instance(AndModule, "t4", ports=[n3, a[k - 2], b[k - 2]])
    Adder.Instance(OrModule, "t5", ports=[n4, a[k - 1], b[k - 1]])
    Adder.Instance(AndModule, "t6", ports=[n5, n4, n2])
    Adder.Instance(AndModule, "t7", ports=[n6, n3, n1])
    Adder.Instance(OrModule, "t8", ports=[res[k - 1], n5, n6])

    ##    Adder.Instance(OrModule,'t1',ports=[res[8],a[8],b[8]]);
    ##    Adder.Instance(AndModule,'t2',ports=[n1,a[9],b[9]]);
    ##    Adder.Instance(NotModule,'t3',ports=[n2,n1]);
    ##    Adder.Instance(AndModule,'t4',ports=[n3,a[8],b[8]]);
    ##    Adder.Instance(OrModule,'t5',ports=[n4,a[9],b[9]]);
    ##    Adder.Instance(AndModule,'t6',ports=[n5,n4,n2]);
    ##    Adder.Instance(AndModule,'t7',ports=[n6,n3,n1]);
    ##    Adder.Instance(OrModule,'t8',ports=[res[9],n5,n6]);

    ## Accurate Part

    cla_count = 0
    temp = k + ((N - k) % 4)
    if (N - k) % 4 == 0:
        k = k + 4

    if temp < N:
        if (N - k) % 4 == 1:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add1BitModule,'cla%d',ports=[a[k],b[k],n1,cout%d,res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add1BitModule,('cla'+str(cla_count)),ports=[a[k],b[k],n1,cout1,res[k]]);
        elif (N - k) % 4 == 2:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add2BitModule,'cla%d',ports=[a[k+1],a[k],b[k+1],b[k],n1,cout%d,res[k+1],res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add2BitModule,('cla'+str(cla_count)),ports=[a[k+1],a[k],b[k+1],b[k],n1,cout1,res[k+1],res[k]]);
        elif (N - k) % 4 == 3:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add3BitModule,'cla%d',ports=[a[k+2],a[k+1],a[k],b[k+2],b[k+1],b[k],n1,cout%d,res[k+2],res[k+1],res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add3BitModule,('cla'+str(cla_count)),ports=[a[k+2],a[k+1],a[k],b[k+2],b[k+1],b[k],n1,cout1,res[k+2],res[k+1],res[k]]);

        ##    Adder.Instance(Add2BitModule,'cla1',ports=[a[11],a[10],b[11],b[10],n1,cout12,res[11],res[10]]);

        while temp < N:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add4BitModule,'cla%d',ports=[a[temp-1],a[temp-2],a[temp-3],a[temp-4],b[temp-1],b[temp-2], \
                 b[temp-3],b[temp-4],cout%d,cout%d,res[temp-1],res[temp-2],res[temp-3],res[temp-4]]);"
                % (cla_count, (temp - 4), temp)
            )
            temp = temp + 4

        ##    Adder.Instance(Add4BitModule,'cla2',ports=[a[15],a[14],a[13],a[12],b[15],b[14],b[13],b[12],cout12,cout16,res[15],res[14],res[13],res[12]]);
        ##    Adder.Instance(Add4BitModule,'cla3',ports=[a[19],a[18],a[17],a[16],b[19],b[18],b[17],b[16],cout16,cout20,res[19],res[18],res[17],res[16]]);
        ##    Adder.Instance(Add4BitModule,'cla4',ports=[a[23],a[22],a[21],a[20],b[23],b[22],b[21],b[20],cout20,cout24,res[23],res[22],res[21],res[20]]);
        ##    Adder.Instance(Add4BitModule,'cla5',ports=[a[27],a[26],a[25],a[24],b[27],b[26],b[25],b[24],cout24,cout28,res[27],res[26],res[25],res[24]]);
        cla_count = cla_count + 1
        exec(
            "Adder.Instance(Add4BitModule,'cla%d',ports=[a[temp-1],a[temp-2],a[temp-3],a[temp-4],b[temp-1],b[temp-2], \
             b[temp-3],b[temp-4],cout%d,res[temp],res[temp-1],res[temp-2],res[temp-3],res[temp-4]]);"
            % (cla_count, (temp - 4))
        )

    ##    Adder.Instance(Add4BitModule,'cla6',ports=[a[31],a[30],a[29],a[28],b[31],b[30],b[29],b[28],cout28,res[32],res[31],res[30],res[29],res[28]]);
    else:
        if (N - k) % 4 == 1:
            Adder.Instance(
                Add1BitModule, "cla1", ports=[a[k], b[k], n1, res[k + 1], res[k]]
            )
        elif (N - k) % 4 == 2:
            Adder.Instance(
                Add2BitModule,
                "cla1",
                ports=[
                    a[k + 1],
                    a[k],
                    b[k + 1],
                    b[k],
                    n1,
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )
        elif (N - k) % 4 == 3:
            Adder.Instance(
                Add3BitModule,
                "cla1",
                ports=[
                    a[k + 2],
                    a[k + 1],
                    a[k],
                    b[k + 2],
                    b[k + 1],
                    b[k],
                    n1,
                    res[k + 3],
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )
        else:
            Adder.Instance(
                Add4BitModule,
                "cla1",
                ports=[
                    a[k + 3],
                    a[k + 2],
                    a[k + 1],
                    a[k],
                    b[k + 3],
                    b[k + 2],
                    b[k + 1],
                    b[k],
                    n1,
                    res[k + 4],
                    res[k + 3],
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )

    return Adder


# HOAANED


def HOAANED_Generic(N, k):

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))

    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(andinp1, andinp2))

    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))

    NotModule = Module("not_1inp")
    notoutp = NotModule.Output("res")
    notinp = NotModule.Input("inp")
    notoutp.assign(Not(notinp))

    AndOrModule = Module("ao21")
    andorinp1 = AndOrModule.Input("a")
    andorinp2 = AndOrModule.Input("b")
    andorinp3 = AndOrModule.Input("c")
    andoroutp = AndOrModule.Output("y")
    andorwire1 = AndOrModule.Wire("net")
    AndOrModule.Instance(AndModule, "t1", ports=[andorwire1, andorinp1, andorinp2])
    AndOrModule.Instance(OrModule, "t2", ports=[andoroutp, andorwire1, andorinp3])

    Add4BitModule = Module("frcla_4b")
    add4bitinpa3 = Add4BitModule.Input("a3")
    add4bitinpa2 = Add4BitModule.Input("a2")
    add4bitinpa1 = Add4BitModule.Input("a1")
    add4bitinpa0 = Add4BitModule.Input("a0")
    add4bitinpb3 = Add4BitModule.Input("b3")
    add4bitinpb2 = Add4BitModule.Input("b2")
    add4bitinpb1 = Add4BitModule.Input("b1")
    add4bitinpb0 = Add4BitModule.Input("b0")
    add4bitinpc0 = Add4BitModule.Input("c0")
    add4bitc4 = Add4BitModule.Output("c4")
    add4bitsum3 = Add4BitModule.Output("sum3")
    add4bitsum2 = Add4BitModule.Output("sum2")
    add4bitsum1 = Add4BitModule.Output("sum1")
    add4bitsum0 = Add4BitModule.Output("sum0")
    add4bitg3 = Add4BitModule.Wire("g3")
    add4bitg2 = Add4BitModule.Wire("g2")
    add4bitg1 = Add4BitModule.Wire("g1")
    add4bitg0 = Add4BitModule.Wire("g0")
    add4bitp3 = Add4BitModule.Wire("p3")
    add4bitp2 = Add4BitModule.Wire("p2")
    add4bitp1 = Add4BitModule.Wire("p1")
    add4bitp0 = Add4BitModule.Wire("p0")
    add4bitc1 = Add4BitModule.Wire("c1")
    add4bitc2 = Add4BitModule.Wire("c2")
    add4bitc3 = Add4BitModule.Wire("c3")
    add4bitm1 = Add4BitModule.Wire("m1")
    add4bitm2 = Add4BitModule.Wire("m2")
    add4bitm3 = Add4BitModule.Wire("m3")
    add4bitm4 = Add4BitModule.Wire("m4")
    add4bitm5 = Add4BitModule.Wire("m5")
    add4bitm6 = Add4BitModule.Wire("m6")

    Add4BitModule.Instance(
        AndModule, "gate1", ports=[add4bitg0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        AndModule, "gate2", ports=[add4bitg1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        AndModule, "gate3", ports=[add4bitg2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        AndModule, "gate4", ports=[add4bitg3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        XorModule, "gate5", ports=[add4bitp0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        XorModule, "gate6", ports=[add4bitp1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        XorModule, "gate7", ports=[add4bitp2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        XorModule, "gate8", ports=[add4bitp3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        AndOrModule, "comp1", ports=[add4bitp1, add4bitg0, add4bitg1, add4bitm1]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp2", ports=[add4bitm1, add4bitp2, add4bitg2, add4bitm2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp3", ports=[add4bitm2, add4bitp3, add4bitg3, add4bitm3]
    )

    Add4BitModule.Instance(AndModule, "and1", ports=[add4bitm4, add4bitp1, add4bitp0])
    Add4BitModule.Instance(AndModule, "and2", ports=[add4bitm5, add4bitp2, add4bitm4])
    Add4BitModule.Instance(AndModule, "and3", ports=[add4bitm6, add4bitp3, add4bitm5])

    Add4BitModule.Instance(
        AndOrModule, "comp4", ports=[add4bitm6, add4bitinpc0, add4bitm3, add4bitc4]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp5", ports=[add4bitm5, add4bitinpc0, add4bitm2, add4bitc3]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp6", ports=[add4bitm4, add4bitinpc0, add4bitm1, add4bitc2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp7", ports=[add4bitp0, add4bitinpc0, add4bitg0, add4bitc1]
    )

    Add4BitModule.Instance(
        XorModule, "xorg1", ports=[add4bitsum0, add4bitp0, add4bitinpc0]
    )
    Add4BitModule.Instance(
        XorModule, "xorg2", ports=[add4bitsum1, add4bitp1, add4bitc1]
    )
    Add4BitModule.Instance(
        XorModule, "xorg3", ports=[add4bitsum2, add4bitp2, add4bitc2]
    )
    Add4BitModule.Instance(
        XorModule, "xorg4", ports=[add4bitsum3, add4bitp3, add4bitc3]
    )

    if ((N - k) % 4) == 3:
        Add3BitModule = Module("frcla_3b")
        add3bitinpa2 = Add3BitModule.Input("a2")
        add3bitinpa1 = Add3BitModule.Input("a1")
        add3bitinpa0 = Add3BitModule.Input("a0")
        add3bitinpb2 = Add3BitModule.Input("b2")
        add3bitinpb1 = Add3BitModule.Input("b1")
        add3bitinpb0 = Add3BitModule.Input("b0")
        add3bitinpc0 = Add3BitModule.Input("c0")
        add3bitc3 = Add3BitModule.Output("c3")
        add3bitsum2 = Add3BitModule.Output("sum2")
        add3bitsum1 = Add3BitModule.Output("sum1")
        add3bitsum0 = Add3BitModule.Output("sum0")

        add3bitg2 = Add3BitModule.Wire("g2")
        add3bitg1 = Add3BitModule.Wire("g1")
        add3bitg0 = Add3BitModule.Wire("g0")

        add3bitp2 = Add3BitModule.Wire("p2")
        add3bitp1 = Add3BitModule.Wire("p1")
        add3bitp0 = Add3BitModule.Wire("p0")
        add3bitc1 = Add3BitModule.Wire("c1")
        add3bitc2 = Add3BitModule.Wire("c2")

        add3bitm1 = Add3BitModule.Wire("m1")
        add3bitm2 = Add3BitModule.Wire("m2")

        add3bitm4 = Add3BitModule.Wire("m4")
        add3bitm5 = Add3BitModule.Wire("m5")

        Add3BitModule.Instance(
            AndModule, "gate1", ports=[add3bitg0, add3bitinpa0, add3bitinpb0]
        )
        Add3BitModule.Instance(
            AndModule, "gate2", ports=[add3bitg1, add3bitinpa1, add3bitinpb1]
        )
        Add3BitModule.Instance(
            AndModule, "gate3", ports=[add3bitg2, add3bitinpa2, add3bitinpb2]
        )

        Add3BitModule.Instance(
            XorModule, "gate5", ports=[add3bitp0, add3bitinpa0, add3bitinpb0]
        )
        Add3BitModule.Instance(
            XorModule, "gate6", ports=[add3bitp1, add3bitinpa1, add3bitinpb1]
        )
        Add3BitModule.Instance(
            XorModule, "gate7", ports=[add3bitp2, add3bitinpa2, add3bitinpb2]
        )

        Add3BitModule.Instance(
            AndOrModule, "comp1", ports=[add3bitp1, add3bitg0, add3bitg1, add3bitm1]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp2", ports=[add3bitm1, add3bitp2, add3bitg2, add3bitm2]
        )

        Add3BitModule.Instance(
            AndModule, "and1", ports=[add3bitm4, add3bitp1, add3bitp0]
        )
        Add3BitModule.Instance(
            AndModule, "and2", ports=[add3bitm5, add3bitp2, add3bitm4]
        )

        Add3BitModule.Instance(
            AndOrModule, "comp5", ports=[add3bitm5, add3bitinpc0, add3bitm2, add3bitc3]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp6", ports=[add3bitm4, add3bitinpc0, add3bitm1, add3bitc2]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp7", ports=[add3bitp0, add3bitinpc0, add3bitg0, add3bitc1]
        )

        Add3BitModule.Instance(
            XorModule, "xorg1", ports=[add3bitsum0, add3bitp0, add3bitinpc0]
        )
        Add3BitModule.Instance(
            XorModule, "xorg2", ports=[add3bitsum1, add3bitp1, add3bitc1]
        )
        Add3BitModule.Instance(
            XorModule, "xorg3", ports=[add3bitsum2, add3bitp2, add3bitc2]
        )

    elif ((N - k) % 4) == 2:
        Add2BitModule = Module("frcla_2b")
        add2bitinpa1 = Add2BitModule.Input("a1")
        add2bitinpa0 = Add2BitModule.Input("a0")
        add2bitinpb1 = Add2BitModule.Input("b1")
        add2bitinpb0 = Add2BitModule.Input("b0")
        add2bitinpc0 = Add2BitModule.Input("c0")
        add2bitc2 = Add2BitModule.Output("c2")
        add2bitsum1 = Add2BitModule.Output("sum1")
        add2bitsum0 = Add2BitModule.Output("sum0")
        add2bitg1 = Add2BitModule.Wire("g1")
        add2bitg0 = Add2BitModule.Wire("g0")
        add2bitp1 = Add2BitModule.Wire("p1")
        add2bitp0 = Add2BitModule.Wire("p0")
        add2bitc1 = Add2BitModule.Wire("c1")
        add2bitm1 = Add2BitModule.Wire("m1")
        add2bitm2 = Add2BitModule.Wire("m2")

        Add2BitModule.Instance(
            AndModule, "gate1", ports=[add2bitg0, add2bitinpa0, add2bitinpb0]
        )
        Add2BitModule.Instance(
            AndModule, "gate2", ports=[add2bitg1, add2bitinpa1, add2bitinpb1]
        )

        Add2BitModule.Instance(
            XorModule, "gate5", ports=[add2bitp0, add2bitinpa0, add2bitinpb0]
        )
        Add2BitModule.Instance(
            XorModule, "gate6", ports=[add2bitp1, add2bitinpa1, add2bitinpb1]
        )

        Add2BitModule.Instance(
            AndOrModule, "comp1", ports=[add2bitp1, add2bitg0, add2bitg1, add2bitm1]
        )

        Add2BitModule.Instance(
            AndModule, "and1", ports=[add2bitm2, add2bitp1, add2bitp0]
        )

        Add2BitModule.Instance(
            AndOrModule, "comp6", ports=[add2bitm2, add2bitinpc0, add2bitm1, add2bitc2]
        )
        Add2BitModule.Instance(
            AndOrModule, "comp7", ports=[add2bitp0, add2bitinpc0, add2bitg0, add2bitc1]
        )

        Add2BitModule.Instance(
            XorModule, "xorg1", ports=[add2bitsum0, add2bitp0, add2bitinpc0]
        )
        Add2BitModule.Instance(
            XorModule, "xorg2", ports=[add2bitsum1, add2bitp1, add2bitc1]
        )

    elif ((N - k) % 4) == 1:
        Add1BitModule = Module("frcla_1b")
        add1bitinpa0 = Add1BitModule.Input("a0")
        add1bitinpb0 = Add1BitModule.Input("b0")
        add1bitinpc0 = Add1BitModule.Input("c0")
        add1bitc1 = Add1BitModule.Output("c1")
        add1bitsum0 = Add1BitModule.Output("sum0")
        add1bitg0 = Add1BitModule.Wire("g0")
        add1bitp0 = Add1BitModule.Wire("p0")
        Add1BitModule.Instance(
            AndModule, "gate1", ports=[add1bitg0, add1bitinpa0, add1bitinpb0]
        )
        Add1BitModule.Instance(
            XorModule, "gate5", ports=[add1bitp0, add1bitinpa0, add1bitinpb0]
        )
        Add1BitModule.Instance(
            AndOrModule, "comp7", ports=[add1bitp0, add1bitinpc0, add1bitg0, add1bitc1]
        )
        Add1BitModule.Instance(
            XorModule, "xorg1", ports=[add1bitsum0, add1bitp0, add1bitinpc0]
        )

    Adder = Module("hoaaned_" + str(N) + "b" + str(k) + "inacc")
    a = Adder.Input("a", N)
    b = Adder.Input("b", N)
    res = Adder.Output("sum", N + 1)
    n1 = Adder.Wire("n1")
    n2 = Adder.Wire("n2")
    n3 = Adder.Wire("n3")
    n4 = Adder.Wire("n4")
    n5 = Adder.Wire("n5")

    temp = k + ((N - k) % 4)
    if (N - k) % 4 == 0:
        k = k + 4

    while temp < N:
        statement1 = "cout" + str(temp) + "=Adder.Wire('cout" + str(temp) + "');"
        exec(statement1)
        temp = temp + 4
    ##    cout12=Adder.Wire('cout12');
    ##    cout16=Adder.Wire('cout16');
    ##    cout20=Adder.Wire('cout20');
    ##    cout24=Adder.Wire('cout24');
    ##    cout28=Adder.Wire('cout28');

    ## Inaccurate Part

    for it1 in range(k - 2):
        res[it1].assign(1)

    ##    res[0].assign(1);
    ##    res[1].assign(1);
    ##    res[2].assign(1);
    ##    res[3].assign(1);
    ##    res[4].assign(1);
    ##    res[5].assign(1);
    ##    res[6].assign(1);
    ##    res[7].assign(1);

    Adder.Instance(OrModule, "t1", ports=[res[k - 2], a[k - 2], b[k - 2]])
    Adder.Instance(AndModule, "t2", ports=[n1, a[k - 2], b[k - 2]])
    Adder.Instance(AndModule, "t3", ports=[n2, a[k - 1], b[k - 1]])
    Adder.Instance(NotModule, "t4", ports=[n3, n2])
    Adder.Instance(OrModule, "t5", ports=[n4, a[k - 1], b[k - 1]])
    Adder.Instance(AndModule, "t6", ports=[n5, n4, n1])
    Adder.Instance(OrModule, "t7", ports=[res[k - 1], n5, n1])

    ##    Adder.Instance(OrModule,'t1',ports=[res[8],a[8],b[8]]);
    ##    Adder.Instance(AndModule,'t2',ports=[n1,a[8],b[8]]);
    ##    Adder.Instance(AndModule,'t3',ports=[n2,a[9],b[9]]);
    ##    Adder.Instance(NotModule,'t4',ports=[n3,n2]);
    ##    Adder.Instance(OrModule,'t5',ports=[n4,a[9],b[9]]);
    ##    Adder.Instance(AndModule,'t6',ports=[n5,n4,n1]);
    ##    Adder.Instance(OrModule,'t7',ports=[res[9],n5,n1]);

    ## Accurate Part

    cla_count = 0
    temp = k + ((N - k) % 4)
    if (N - k) % 4 == 0:
        k = k + 4

    if temp < N:
        if (N - k) % 4 == 1:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add1BitModule,'cla%d',ports=[a[k],b[k],n2,cout%d,res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add1BitModule,('cla'+str(cla_count)),ports=[a[k],b[k],n2,cout1,res[k]]);
        elif (N - k) % 4 == 2:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add2BitModule,'cla%d',ports=[a[k+1],a[k],b[k+1],b[k],n2,cout%d,res[k+1],res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add2BitModule,('cla'+str(cla_count)),ports=[a[k+1],a[k],b[k+1],b[k],n2,cout1,res[k+1],res[k]]);
        elif (N - k) % 4 == 3:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add3BitModule,'cla%d',ports=[a[k+2],a[k+1],a[k],b[k+2],b[k+1],b[k],n2,cout%d,res[k+2],res[k+1],res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add3BitModule,('cla'+str(cla_count)),ports=[a[k+2],a[k+1],a[k],b[k+2],b[k+1],b[k],n2,cout1,res[k+2],res[k+1],res[k]]);

        ##    Adder.Instance(Add2BitModule,'cla1',ports=[a[11],a[10],b[11],b[10],n2,cout12,res[11],res[10]]);

        while temp < N:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add4BitModule,'cla%d',ports=[a[temp-1],a[temp-2],a[temp-3],a[temp-4],b[temp-1],b[temp-2], \
                 b[temp-3],b[temp-4],cout%d,cout%d,res[temp-1],res[temp-2],res[temp-3],res[temp-4]]);"
                % (cla_count, (temp - 4), temp)
            )
            temp = temp + 4

        ##    Adder.Instance(Add4BitModule,'cla2',ports=[a[15],a[14],a[13],a[12],b[15],b[14],b[13],b[12],cout12,cout16,res[15],res[14],res[13],res[12]]);
        ##    Adder.Instance(Add4BitModule,'cla3',ports=[a[19],a[18],a[17],a[16],b[19],b[18],b[17],b[16],cout16,cout20,res[19],res[18],res[17],res[16]]);
        ##    Adder.Instance(Add4BitModule,'cla4',ports=[a[23],a[22],a[21],a[20],b[23],b[22],b[21],b[20],cout20,cout24,res[23],res[22],res[21],res[20]]);
        ##    Adder.Instance(Add4BitModule,'cla5',ports=[a[27],a[26],a[25],a[24],b[27],b[26],b[25],b[24],cout24,cout28,res[27],res[26],res[25],res[24]]);
        cla_count = cla_count + 1
        exec(
            "Adder.Instance(Add4BitModule,'cla%d',ports=[a[temp-1],a[temp-2],a[temp-3],a[temp-4],b[temp-1],b[temp-2], \
             b[temp-3],b[temp-4],cout%d,res[temp],res[temp-1],res[temp-2],res[temp-3],res[temp-4]]);"
            % (cla_count, (temp - 4))
        )

    ##    Adder.Instance(Add4BitModule,'cla6',ports=[a[31],a[30],a[29],a[28],b[31],b[30],b[29],b[28],cout28,res[32],res[31],res[30],res[29],res[28]]);
    else:
        if (N - k) % 4 == 1:
            Adder.Instance(
                Add1BitModule, "cla1", ports=[a[k], b[k], n2, res[k + 1], res[k]]
            )
        elif (N - k) % 4 == 2:
            Adder.Instance(
                Add2BitModule,
                "cla1",
                ports=[
                    a[k + 1],
                    a[k],
                    b[k + 1],
                    b[k],
                    n2,
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )
        elif (N - k) % 4 == 3:
            Adder.Instance(
                Add3BitModule,
                "cla1",
                ports=[
                    a[k + 2],
                    a[k + 1],
                    a[k],
                    b[k + 2],
                    b[k + 1],
                    b[k],
                    n2,
                    res[k + 3],
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )
        else:
            Adder.Instance(
                Add4BitModule,
                "cla1",
                ports=[
                    a[k + 3],
                    a[k + 2],
                    a[k + 1],
                    a[k],
                    b[k + 3],
                    b[k + 2],
                    b[k + 1],
                    b[k],
                    n2,
                    res[k + 4],
                    res[k + 3],
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )

    return Adder


# M-HERLOA


def M_HERLOA_Generic(N, k):

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))

    NandModule = Module("nand_2inp")
    nandoutp = NandModule.Output("res")
    nandinp1 = NandModule.Input("inp1")
    nandinp2 = NandModule.Input("inp2")
    nandoutp.assign(Not(And(nandinp1, nandinp2)))

    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(andinp1, andinp2))

    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))

    NotModule = Module("not_1inp")
    notoutp = NotModule.Output("res")
    notinp = NotModule.Input("inp")
    notoutp.assign(Not(notinp))

    AndOrModule = Module("ao21")
    andorinp1 = AndOrModule.Input("a")
    andorinp2 = AndOrModule.Input("b")
    andorinp3 = AndOrModule.Input("c")
    andoroutp = AndOrModule.Output("y")
    andorwire1 = AndOrModule.Wire("net")
    AndOrModule.Instance(AndModule, "t1", ports=[andorwire1, andorinp1, andorinp2])
    AndOrModule.Instance(OrModule, "t2", ports=[andoroutp, andorwire1, andorinp3])

    Add4BitModule = Module("frcla_4b")
    add4bitinpa3 = Add4BitModule.Input("a3")
    add4bitinpa2 = Add4BitModule.Input("a2")
    add4bitinpa1 = Add4BitModule.Input("a1")
    add4bitinpa0 = Add4BitModule.Input("a0")
    add4bitinpb3 = Add4BitModule.Input("b3")
    add4bitinpb2 = Add4BitModule.Input("b2")
    add4bitinpb1 = Add4BitModule.Input("b1")
    add4bitinpb0 = Add4BitModule.Input("b0")
    add4bitinpc0 = Add4BitModule.Input("c0")
    add4bitc4 = Add4BitModule.Output("c4")
    add4bitsum3 = Add4BitModule.Output("sum3")
    add4bitsum2 = Add4BitModule.Output("sum2")
    add4bitsum1 = Add4BitModule.Output("sum1")
    add4bitsum0 = Add4BitModule.Output("sum0")
    add4bitg3 = Add4BitModule.Wire("g3")
    add4bitg2 = Add4BitModule.Wire("g2")
    add4bitg1 = Add4BitModule.Wire("g1")
    add4bitg0 = Add4BitModule.Wire("g0")
    add4bitp3 = Add4BitModule.Wire("p3")
    add4bitp2 = Add4BitModule.Wire("p2")
    add4bitp1 = Add4BitModule.Wire("p1")
    add4bitp0 = Add4BitModule.Wire("p0")
    add4bitc1 = Add4BitModule.Wire("c1")
    add4bitc2 = Add4BitModule.Wire("c2")
    add4bitc3 = Add4BitModule.Wire("c3")
    add4bitm1 = Add4BitModule.Wire("m1")
    add4bitm2 = Add4BitModule.Wire("m2")
    add4bitm3 = Add4BitModule.Wire("m3")
    add4bitm4 = Add4BitModule.Wire("m4")
    add4bitm5 = Add4BitModule.Wire("m5")
    add4bitm6 = Add4BitModule.Wire("m6")

    Add4BitModule.Instance(
        AndModule, "gate1", ports=[add4bitg0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        AndModule, "gate2", ports=[add4bitg1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        AndModule, "gate3", ports=[add4bitg2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        AndModule, "gate4", ports=[add4bitg3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        XorModule, "gate5", ports=[add4bitp0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        XorModule, "gate6", ports=[add4bitp1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        XorModule, "gate7", ports=[add4bitp2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        XorModule, "gate8", ports=[add4bitp3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        AndOrModule, "comp1", ports=[add4bitp1, add4bitg0, add4bitg1, add4bitm1]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp2", ports=[add4bitm1, add4bitp2, add4bitg2, add4bitm2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp3", ports=[add4bitm2, add4bitp3, add4bitg3, add4bitm3]
    )

    Add4BitModule.Instance(AndModule, "and1", ports=[add4bitm4, add4bitp1, add4bitp0])
    Add4BitModule.Instance(AndModule, "and2", ports=[add4bitm5, add4bitp2, add4bitm4])
    Add4BitModule.Instance(AndModule, "and3", ports=[add4bitm6, add4bitp3, add4bitm5])

    Add4BitModule.Instance(
        AndOrModule, "comp4", ports=[add4bitm6, add4bitinpc0, add4bitm3, add4bitc4]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp5", ports=[add4bitm5, add4bitinpc0, add4bitm2, add4bitc3]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp6", ports=[add4bitm4, add4bitinpc0, add4bitm1, add4bitc2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp7", ports=[add4bitp0, add4bitinpc0, add4bitg0, add4bitc1]
    )

    Add4BitModule.Instance(
        XorModule, "xorg1", ports=[add4bitsum0, add4bitp0, add4bitinpc0]
    )
    Add4BitModule.Instance(
        XorModule, "xorg2", ports=[add4bitsum1, add4bitp1, add4bitc1]
    )
    Add4BitModule.Instance(
        XorModule, "xorg3", ports=[add4bitsum2, add4bitp2, add4bitc2]
    )
    Add4BitModule.Instance(
        XorModule, "xorg4", ports=[add4bitsum3, add4bitp3, add4bitc3]
    )

    if ((N - k) % 4) == 3:
        Add3BitModule = Module("frcla_3b")
        add3bitinpa2 = Add3BitModule.Input("a2")
        add3bitinpa1 = Add3BitModule.Input("a1")
        add3bitinpa0 = Add3BitModule.Input("a0")
        add3bitinpb2 = Add3BitModule.Input("b2")
        add3bitinpb1 = Add3BitModule.Input("b1")
        add3bitinpb0 = Add3BitModule.Input("b0")
        add3bitinpc0 = Add3BitModule.Input("c0")
        add3bitc3 = Add3BitModule.Output("c3")
        add3bitsum2 = Add3BitModule.Output("sum2")
        add3bitsum1 = Add3BitModule.Output("sum1")
        add3bitsum0 = Add3BitModule.Output("sum0")

        add3bitg2 = Add3BitModule.Wire("g2")
        add3bitg1 = Add3BitModule.Wire("g1")
        add3bitg0 = Add3BitModule.Wire("g0")

        add3bitp2 = Add3BitModule.Wire("p2")
        add3bitp1 = Add3BitModule.Wire("p1")
        add3bitp0 = Add3BitModule.Wire("p0")
        add3bitc1 = Add3BitModule.Wire("c1")
        add3bitc2 = Add3BitModule.Wire("c2")

        add3bitm1 = Add3BitModule.Wire("m1")
        add3bitm2 = Add3BitModule.Wire("m2")

        add3bitm4 = Add3BitModule.Wire("m4")
        add3bitm5 = Add3BitModule.Wire("m5")

        Add3BitModule.Instance(
            AndModule, "gate1", ports=[add3bitg0, add3bitinpa0, add3bitinpb0]
        )
        Add3BitModule.Instance(
            AndModule, "gate2", ports=[add3bitg1, add3bitinpa1, add3bitinpb1]
        )
        Add3BitModule.Instance(
            AndModule, "gate3", ports=[add3bitg2, add3bitinpa2, add3bitinpb2]
        )

        Add3BitModule.Instance(
            XorModule, "gate5", ports=[add3bitp0, add3bitinpa0, add3bitinpb0]
        )
        Add3BitModule.Instance(
            XorModule, "gate6", ports=[add3bitp1, add3bitinpa1, add3bitinpb1]
        )
        Add3BitModule.Instance(
            XorModule, "gate7", ports=[add3bitp2, add3bitinpa2, add3bitinpb2]
        )

        Add3BitModule.Instance(
            AndOrModule, "comp1", ports=[add3bitp1, add3bitg0, add3bitg1, add3bitm1]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp2", ports=[add3bitm1, add3bitp2, add3bitg2, add3bitm2]
        )

        Add3BitModule.Instance(
            AndModule, "and1", ports=[add3bitm4, add3bitp1, add3bitp0]
        )
        Add3BitModule.Instance(
            AndModule, "and2", ports=[add3bitm5, add3bitp2, add3bitm4]
        )

        Add3BitModule.Instance(
            AndOrModule, "comp5", ports=[add3bitm5, add3bitinpc0, add3bitm2, add3bitc3]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp6", ports=[add3bitm4, add3bitinpc0, add3bitm1, add3bitc2]
        )
        Add3BitModule.Instance(
            AndOrModule, "comp7", ports=[add3bitp0, add3bitinpc0, add3bitg0, add3bitc1]
        )

        Add3BitModule.Instance(
            XorModule, "xorg1", ports=[add3bitsum0, add3bitp0, add3bitinpc0]
        )
        Add3BitModule.Instance(
            XorModule, "xorg2", ports=[add3bitsum1, add3bitp1, add3bitc1]
        )
        Add3BitModule.Instance(
            XorModule, "xorg3", ports=[add3bitsum2, add3bitp2, add3bitc2]
        )

    elif ((N - k) % 4) == 2:
        Add2BitModule = Module("frcla_2b")
        add2bitinpa1 = Add2BitModule.Input("a1")
        add2bitinpa0 = Add2BitModule.Input("a0")
        add2bitinpb1 = Add2BitModule.Input("b1")
        add2bitinpb0 = Add2BitModule.Input("b0")
        add2bitinpc0 = Add2BitModule.Input("c0")
        add2bitc2 = Add2BitModule.Output("c2")
        add2bitsum1 = Add2BitModule.Output("sum1")
        add2bitsum0 = Add2BitModule.Output("sum0")
        add2bitg1 = Add2BitModule.Wire("g1")
        add2bitg0 = Add2BitModule.Wire("g0")
        add2bitp1 = Add2BitModule.Wire("p1")
        add2bitp0 = Add2BitModule.Wire("p0")
        add2bitc1 = Add2BitModule.Wire("c1")
        add2bitm1 = Add2BitModule.Wire("m1")
        add2bitm2 = Add2BitModule.Wire("m2")

        Add2BitModule.Instance(
            AndModule, "gate1", ports=[add2bitg0, add2bitinpa0, add2bitinpb0]
        )
        Add2BitModule.Instance(
            AndModule, "gate2", ports=[add2bitg1, add2bitinpa1, add2bitinpb1]
        )

        Add2BitModule.Instance(
            XorModule, "gate5", ports=[add2bitp0, add2bitinpa0, add2bitinpb0]
        )
        Add2BitModule.Instance(
            XorModule, "gate6", ports=[add2bitp1, add2bitinpa1, add2bitinpb1]
        )

        Add2BitModule.Instance(
            AndOrModule, "comp1", ports=[add2bitp1, add2bitg0, add2bitg1, add2bitm1]
        )

        Add2BitModule.Instance(
            AndModule, "and1", ports=[add2bitm2, add2bitp1, add2bitp0]
        )

        Add2BitModule.Instance(
            AndOrModule, "comp6", ports=[add2bitm2, add2bitinpc0, add2bitm1, add2bitc2]
        )
        Add2BitModule.Instance(
            AndOrModule, "comp7", ports=[add2bitp0, add2bitinpc0, add2bitg0, add2bitc1]
        )

        Add2BitModule.Instance(
            XorModule, "xorg1", ports=[add2bitsum0, add2bitp0, add2bitinpc0]
        )
        Add2BitModule.Instance(
            XorModule, "xorg2", ports=[add2bitsum1, add2bitp1, add2bitc1]
        )

    elif ((N - k) % 4) == 1:
        Add1BitModule = Module("frcla_1b")
        add1bitinpa0 = Add1BitModule.Input("a0")
        add1bitinpb0 = Add1BitModule.Input("b0")
        add1bitinpc0 = Add1BitModule.Input("c0")
        add1bitc1 = Add1BitModule.Output("c1")
        add1bitsum0 = Add1BitModule.Output("sum0")
        add1bitg0 = Add1BitModule.Wire("g0")
        add1bitp0 = Add1BitModule.Wire("p0")
        Add1BitModule.Instance(
            AndModule, "gate1", ports=[add1bitg0, add1bitinpa0, add1bitinpb0]
        )
        Add1BitModule.Instance(
            XorModule, "gate5", ports=[add1bitp0, add1bitinpa0, add1bitinpb0]
        )
        Add1BitModule.Instance(
            AndOrModule, "comp7", ports=[add1bitp0, add1bitinpc0, add1bitg0, add1bitc1]
        )
        Add1BitModule.Instance(
            XorModule, "xorg1", ports=[add1bitsum0, add1bitp0, add1bitinpc0]
        )

    Adder = Module("m_herloa_" + str(N) + "b" + str(k) + "inacc")
    a = Adder.Input("a", N)
    b = Adder.Input("b", N)
    res = Adder.Output("sum", N + 1)
    n1 = Adder.Wire("n1")
    n2 = Adder.Wire("n2")
    n3 = Adder.Wire("n3")
    w1 = Adder.Wire("w1")
    if k > 3:
        w2 = Adder.Wire("w2")
        # NOTE- w2 Wire is not used if number of inaccurate bits (k) = 3
        # No need to worry about k<=2 as our tool is used to generate verilog code only for k>=3
    w9 = Adder.Wire("w9")
    w10 = Adder.Wire("w10")
    w11 = Adder.Wire("w11")
    w12 = Adder.Wire("w12")

    temp = k + ((N - k) % 4)
    if (N - k) % 4 == 0:
        k = k + 4

    while temp < N:
        statement1 = "cout" + str(temp) + "=Adder.Wire('cout" + str(temp) + "');"
        exec(statement1)
        temp = temp + 4
    ##    cout12=Adder.Wire('cout12');
    ##    cout16=Adder.Wire('cout16');
    ##    cout20=Adder.Wire('cout20');
    ##    cout24=Adder.Wire('cout24');
    ##    cout28=Adder.Wire('cout28');

    ## Inaccurate Part

    for it1 in range(k - 4):
        res[it1].assign(1)

    ##    res[0].assign(1);
    ##    res[1].assign(1);
    ##    res[2].assign(1);
    ##    res[3].assign(1);
    ##    res[4].assign(1);
    ##    res[5].assign(1);

    Adder.Instance(XorModule, "t1", ports=[n1, a[k - 1], b[k - 1]])
    Adder.Instance(AndModule, "t2", ports=[n2, a[k - 2], b[k - 2]])
    Adder.Instance(OrModule, "t3", ports=[res[k - 1], n1, n2])
    Adder.Instance(AndModule, "t4", ports=[n3, n1, n2])

    Adder.Instance(OrModule, "g1", ports=[w1, a[k - 3], b[k - 3]])
    if k > 3:
        Adder.Instance(OrModule, "g2", ports=[w2, a[k - 4], b[k - 4]])
        # NOTE- Not used if number of inaccurate bits (k) <= 3 as a[k-4]=a[-1] for k=3
        # No need to worry about k<=2 as our tool is used to generate verilog code only for k>=3
    Adder.Instance(OrModule, "e1", ports=[res[k - 3], n3, w1])
    if k > 3:
        Adder.Instance(OrModule, "e2", ports=[res[k - 4], n3, w2])
        # NOTE- Not used if number of inaccurate bits (k) <= 3 as res[k-4]=res[-1] for k=3
        # No need to worry about k<=2 as our tool is used to generate verilog code only for k>=3

    Adder.Instance(OrModule, "t5", ports=[w9, a[k - 2], b[k - 2]])
    Adder.Instance(NotModule, "t6", ports=[w10, n1])
    Adder.Instance(NandModule, "t7", ports=[w11, w10, n2])
    Adder.Instance(AndModule, "t8", ports=[res[k - 2], w11, w9])
    Adder.Instance(AndModule, "t9", ports=[w12, a[k - 1], b[k - 1]])

    ##    Adder.Instance(XorModule,'t1',ports=[n1,a[9],b[9]]);
    ##    Adder.Instance(AndModule,'t2',ports=[n2,a[8],b[8]]);
    ##    Adder.Instance(OrModule,'t3',ports=[res[9],n1,n2]);
    ##    Adder.Instance(AndModule,'t4',ports=[n3,n1,n2]);
    ##
    ##    Adder.Instance(OrModule,'g1',ports=[w1,a[7],b[7]]);
    ##    Adder.Instance(OrModule,'g2',ports=[w2,a[6],b[6]]);
    ##
    ##    Adder.Instance(OrModule,'e1',ports=[res[7],n3,w1]);
    ##    Adder.Instance(OrModule,'e2',ports=[res[6],n3,w2]);
    ##
    ##    Adder.Instance(OrModule,'t5',ports=[w9,a[8],b[8]]);
    ##    Adder.Instance(NotModule,'t6',ports=[w10,n1]);
    ##    Adder.Instance(NandModule,'t7',ports=[w11,w10,n2]);
    ##    Adder.Instance(AndModule,'t8',ports=[res[8],w11,w9]);
    ##    Adder.Instance(AndModule,'t9',ports=[w12,a[9],b[9]]);

    ## Accurate Part

    cla_count = 0
    temp = k + ((N - k) % 4)
    if (N - k) % 4 == 0:
        k = k + 4

    if temp < N:
        if (N - k) % 4 == 1:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add1BitModule,'cla%d',ports=[a[k],b[k],w12,cout%d,res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add1BitModule,('cla'+str(cla_count)),ports=[a[k],b[k],w12,cout1,res[k]]);
        elif (N - k) % 4 == 2:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add2BitModule,'cla%d',ports=[a[k+1],a[k],b[k+1],b[k],w12,cout%d,res[k+1],res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add2BitModule,('cla'+str(cla_count)),ports=[a[k+1],a[k],b[k+1],b[k],w12,cout1,res[k+1],res[k]]);
        elif (N - k) % 4 == 3:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add3BitModule,'cla%d',ports=[a[k+2],a[k+1],a[k],b[k+2],b[k+1],b[k],w12,cout%d,res[k+2],res[k+1],res[k]]);"
                % (cla_count, temp)
            )
            temp = temp + 4
            # Adder.Instance(Add3BitModule,('cla'+str(cla_count)),ports=[a[k+2],a[k+1],a[k],b[k+2],b[k+1],b[k],w12,cout1,res[k+2],res[k+1],res[k]]);

        ##    Adder.Instance(Add2BitModule,'cla1',ports=[a[11],a[10],b[11],b[10],n2,cout12,res[11],res[10]]);

        while temp < N:
            cla_count = cla_count + 1
            exec(
                "Adder.Instance(Add4BitModule,'cla%d',ports=[a[temp-1],a[temp-2],a[temp-3],a[temp-4],b[temp-1],b[temp-2], \
                 b[temp-3],b[temp-4],cout%d,cout%d,res[temp-1],res[temp-2],res[temp-3],res[temp-4]]);"
                % (cla_count, (temp - 4), temp)
            )
            temp = temp + 4

        ##    Adder.Instance(Add4BitModule,'cla2',ports=[a[15],a[14],a[13],a[12],b[15],b[14],b[13],b[12],cout12,cout16,res[15],res[14],res[13],res[12]]);
        ##    Adder.Instance(Add4BitModule,'cla3',ports=[a[19],a[18],a[17],a[16],b[19],b[18],b[17],b[16],cout16,cout20,res[19],res[18],res[17],res[16]]);
        ##    Adder.Instance(Add4BitModule,'cla4',ports=[a[23],a[22],a[21],a[20],b[23],b[22],b[21],b[20],cout20,cout24,res[23],res[22],res[21],res[20]]);
        ##    Adder.Instance(Add4BitModule,'cla5',ports=[a[27],a[26],a[25],a[24],b[27],b[26],b[25],b[24],cout24,cout28,res[27],res[26],res[25],res[24]]);
        cla_count = cla_count + 1
        exec(
            "Adder.Instance(Add4BitModule,'cla%d',ports=[a[temp-1],a[temp-2],a[temp-3],a[temp-4],b[temp-1],b[temp-2], \
             b[temp-3],b[temp-4],cout%d,res[temp],res[temp-1],res[temp-2],res[temp-3],res[temp-4]]);"
            % (cla_count, (temp - 4))
        )

    ##    Adder.Instance(Add4BitModule,'cla6',ports=[a[31],a[30],a[29],a[28],b[31],b[30],b[29],b[28],cout28,res[32],res[31],res[30],res[29],res[28]]);
    else:
        if (N - k) % 4 == 1:
            Adder.Instance(
                Add1BitModule, "cla1", ports=[a[k], b[k], w12, res[k + 1], res[k]]
            )
        elif (N - k) % 4 == 2:
            Adder.Instance(
                Add2BitModule,
                "cla1",
                ports=[
                    a[k + 1],
                    a[k],
                    b[k + 1],
                    b[k],
                    w12,
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )
        elif (N - k) % 4 == 3:
            Adder.Instance(
                Add3BitModule,
                "cla1",
                ports=[
                    a[k + 2],
                    a[k + 1],
                    a[k],
                    b[k + 2],
                    b[k + 1],
                    b[k],
                    w12,
                    res[k + 3],
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )
        else:
            Adder.Instance(
                Add4BitModule,
                "cla1",
                ports=[
                    a[k + 3],
                    a[k + 2],
                    a[k + 1],
                    a[k],
                    b[k + 3],
                    b[k + 2],
                    b[k + 1],
                    b[k],
                    w12,
                    res[k + 4],
                    res[k + 3],
                    res[k + 2],
                    res[k + 1],
                    res[k],
                ],
            )

    return Adder


##############################################################################

## 32 bit adders 10 inaccurate bits (No longer used in code after use of Generic case - For reference purpose only)

# HEAA (32 bit adders 10 inaccurate bits)


def HEAA_32_bits_10_inaccurate():

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))

    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(andinp1, andinp2))

    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))

    NotModule = Module("not_1inp")
    notoutp = NotModule.Output("res")
    notinp = NotModule.Input("inp")
    notoutp.assign(Not(notinp))

    AndOrModule = Module("ao21")
    andorinp1 = AndOrModule.Input("a")
    andorinp2 = AndOrModule.Input("b")
    andorinp3 = AndOrModule.Input("c")
    andoroutp = AndOrModule.Output("y")
    andorwire1 = AndOrModule.Wire("net")
    AndOrModule.Instance(AndModule, "t1", ports=[andorwire1, andorinp1, andorinp2])
    AndOrModule.Instance(OrModule, "t2", ports=[andoroutp, andorwire1, andorinp3])

    Add4BitModule = Module("frcla_4b")
    add4bitinpa3 = Add4BitModule.Input("a3")
    add4bitinpa2 = Add4BitModule.Input("a2")
    add4bitinpa1 = Add4BitModule.Input("a1")
    add4bitinpa0 = Add4BitModule.Input("a0")
    add4bitinpb3 = Add4BitModule.Input("b3")
    add4bitinpb2 = Add4BitModule.Input("b2")
    add4bitinpb1 = Add4BitModule.Input("b1")
    add4bitinpb0 = Add4BitModule.Input("b0")
    add4bitinpc0 = Add4BitModule.Input("c0")
    add4bitc4 = Add4BitModule.Output("c4")
    add4bitsum3 = Add4BitModule.Output("sum3")
    add4bitsum2 = Add4BitModule.Output("sum2")
    add4bitsum1 = Add4BitModule.Output("sum1")
    add4bitsum0 = Add4BitModule.Output("sum0")
    add4bitg3 = Add4BitModule.Wire("g3")
    add4bitg2 = Add4BitModule.Wire("g2")
    add4bitg1 = Add4BitModule.Wire("g1")
    add4bitg0 = Add4BitModule.Wire("g0")
    add4bitp3 = Add4BitModule.Wire("p3")
    add4bitp2 = Add4BitModule.Wire("p2")
    add4bitp1 = Add4BitModule.Wire("p1")
    add4bitp0 = Add4BitModule.Wire("p0")
    add4bitc1 = Add4BitModule.Wire("c1")
    add4bitc2 = Add4BitModule.Wire("c2")
    add4bitc3 = Add4BitModule.Wire("c3")
    add4bitm1 = Add4BitModule.Wire("m1")
    add4bitm2 = Add4BitModule.Wire("m2")
    add4bitm3 = Add4BitModule.Wire("m3")
    add4bitm4 = Add4BitModule.Wire("m4")
    add4bitm5 = Add4BitModule.Wire("m5")
    add4bitm6 = Add4BitModule.Wire("m6")

    Add4BitModule.Instance(
        AndModule, "gate1", ports=[add4bitg0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        AndModule, "gate2", ports=[add4bitg1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        AndModule, "gate3", ports=[add4bitg2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        AndModule, "gate4", ports=[add4bitg3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        XorModule, "gate5", ports=[add4bitp0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        XorModule, "gate6", ports=[add4bitp1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        XorModule, "gate7", ports=[add4bitp2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        XorModule, "gate8", ports=[add4bitp3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        AndOrModule, "comp1", ports=[add4bitp1, add4bitg0, add4bitg1, add4bitm1]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp2", ports=[add4bitm1, add4bitp2, add4bitg2, add4bitm2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp3", ports=[add4bitm2, add4bitp3, add4bitg3, add4bitm3]
    )

    Add4BitModule.Instance(AndModule, "and1", ports=[add4bitm4, add4bitp1, add4bitp0])
    Add4BitModule.Instance(AndModule, "and2", ports=[add4bitm5, add4bitp2, add4bitm4])
    Add4BitModule.Instance(AndModule, "and3", ports=[add4bitm6, add4bitp3, add4bitm5])

    Add4BitModule.Instance(
        AndOrModule, "comp4", ports=[add4bitm6, add4bitinpc0, add4bitm3, add4bitc4]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp5", ports=[add4bitm5, add4bitinpc0, add4bitm2, add4bitc3]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp6", ports=[add4bitm4, add4bitinpc0, add4bitm1, add4bitc2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp7", ports=[add4bitp0, add4bitinpc0, add4bitg0, add4bitc1]
    )

    Add4BitModule.Instance(
        XorModule, "xorg1", ports=[add4bitsum0, add4bitp0, add4bitinpc0]
    )
    Add4BitModule.Instance(
        XorModule, "xorg2", ports=[add4bitsum1, add4bitp1, add4bitc1]
    )
    Add4BitModule.Instance(
        XorModule, "xorg3", ports=[add4bitsum2, add4bitp2, add4bitc2]
    )
    Add4BitModule.Instance(
        XorModule, "xorg4", ports=[add4bitsum3, add4bitp3, add4bitc3]
    )

    Add2BitModule = Module("frcla_2b")
    add2bitinpa1 = Add2BitModule.Input("a1")
    add2bitinpa0 = Add2BitModule.Input("a0")
    add2bitinpb1 = Add2BitModule.Input("b1")
    add2bitinpb0 = Add2BitModule.Input("b0")
    add2bitinpc0 = Add2BitModule.Input("c0")
    add2bitc2 = Add2BitModule.Output("c2")
    add2bitsum1 = Add2BitModule.Output("sum1")
    add2bitsum0 = Add2BitModule.Output("sum0")
    add2bitg1 = Add2BitModule.Wire("g1")
    add2bitg0 = Add2BitModule.Wire("g0")
    add2bitp1 = Add2BitModule.Wire("p1")
    add2bitp0 = Add2BitModule.Wire("p0")
    add2bitc1 = Add2BitModule.Wire("c1")
    add2bitm1 = Add2BitModule.Wire("m1")
    add2bitm2 = Add2BitModule.Wire("m2")

    Add2BitModule.Instance(
        AndModule, "gate1", ports=[add2bitg0, add2bitinpa0, add2bitinpb0]
    )
    Add2BitModule.Instance(
        AndModule, "gate2", ports=[add2bitg1, add2bitinpa1, add2bitinpb1]
    )

    Add2BitModule.Instance(
        XorModule, "gate5", ports=[add2bitp0, add2bitinpa0, add2bitinpb0]
    )
    Add2BitModule.Instance(
        XorModule, "gate6", ports=[add2bitp1, add2bitinpa1, add2bitinpb1]
    )

    Add2BitModule.Instance(
        AndOrModule, "comp1", ports=[add2bitp1, add2bitg0, add2bitg1, add2bitm1]
    )

    Add2BitModule.Instance(AndModule, "and1", ports=[add2bitm2, add2bitp1, add2bitp0])

    Add2BitModule.Instance(
        AndOrModule, "comp6", ports=[add2bitm2, add2bitinpc0, add2bitm1, add2bitc2]
    )
    Add2BitModule.Instance(
        AndOrModule, "comp7", ports=[add2bitp0, add2bitinpc0, add2bitg0, add2bitc1]
    )

    Add2BitModule.Instance(
        XorModule, "xorg1", ports=[add2bitsum0, add2bitp0, add2bitinpc0]
    )
    Add2BitModule.Instance(
        XorModule, "xorg2", ports=[add2bitsum1, add2bitp1, add2bitc1]
    )

    Adder = Module("heaa_32b")
    a = Adder.Input("a", 32)
    b = Adder.Input("b", 32)
    res = Adder.Output("sum", 33)
    w1 = Adder.Wire("w1")
    w2 = Adder.Wire("w2")
    w3 = Adder.Wire("w3")
    cout12 = Adder.Wire("cout12")
    cout16 = Adder.Wire("cout16")
    cout20 = Adder.Wire("cout20")
    cout24 = Adder.Wire("cout24")
    cout28 = Adder.Wire("cout28")

    Adder.Instance(OrModule, "t1", ports=[res[0], a[0], b[0]])
    Adder.Instance(OrModule, "t2", ports=[res[1], a[1], b[1]])
    Adder.Instance(OrModule, "t3", ports=[res[2], a[2], b[2]])
    Adder.Instance(OrModule, "t4", ports=[res[3], a[3], b[3]])
    Adder.Instance(OrModule, "t5", ports=[res[4], a[4], b[4]])
    Adder.Instance(OrModule, "t6", ports=[res[5], a[5], b[5]])
    Adder.Instance(OrModule, "t7", ports=[res[6], a[6], b[6]])
    Adder.Instance(OrModule, "t8", ports=[res[7], a[7], b[7]])
    Adder.Instance(OrModule, "t9", ports=[res[8], a[8], b[8]])

    Adder.Instance(AndModule, "t10", ports=[w1, a[9], b[9]])
    Adder.Instance(NotModule, "t11", ports=[w2, w1])
    Adder.Instance(OrModule, "t12", ports=[w3, a[9], b[9]])
    Adder.Instance(AndModule, "t13", ports=[res[9], w3, w2])

    ## Accurate Part

    Adder.Instance(
        Add2BitModule,
        "cla1",
        ports=[a[11], a[10], b[11], b[10], w1, cout12, res[11], res[10]],
    )
    Adder.Instance(
        Add4BitModule,
        "cla2",
        ports=[
            a[15],
            a[14],
            a[13],
            a[12],
            b[15],
            b[14],
            b[13],
            b[12],
            cout12,
            cout16,
            res[15],
            res[14],
            res[13],
            res[12],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla3",
        ports=[
            a[19],
            a[18],
            a[17],
            a[16],
            b[19],
            b[18],
            b[17],
            b[16],
            cout16,
            cout20,
            res[19],
            res[18],
            res[17],
            res[16],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla4",
        ports=[
            a[23],
            a[22],
            a[21],
            a[20],
            b[23],
            b[22],
            b[21],
            b[20],
            cout20,
            cout24,
            res[23],
            res[22],
            res[21],
            res[20],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla5",
        ports=[
            a[27],
            a[26],
            a[25],
            a[24],
            b[27],
            b[26],
            b[25],
            b[24],
            cout24,
            cout28,
            res[27],
            res[26],
            res[25],
            res[24],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla6",
        ports=[
            a[31],
            a[30],
            a[29],
            a[28],
            b[31],
            b[30],
            b[29],
            b[28],
            cout28,
            res[32],
            res[31],
            res[30],
            res[29],
            res[28],
        ],
    )

    return Adder


# HOAANED (32 bit adders 10 inaccurate bits)


def HOAANED_32_bits_10_inaccurate():

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))

    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(andinp1, andinp2))

    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))

    NotModule = Module("not_1inp")
    notoutp = NotModule.Output("res")
    notinp = NotModule.Input("inp")
    notoutp.assign(Not(notinp))

    AndOrModule = Module("ao21")
    andorinp1 = AndOrModule.Input("a")
    andorinp2 = AndOrModule.Input("b")
    andorinp3 = AndOrModule.Input("c")
    andoroutp = AndOrModule.Output("y")
    andorwire1 = AndOrModule.Wire("net")
    AndOrModule.Instance(AndModule, "t1", ports=[andorwire1, andorinp1, andorinp2])
    AndOrModule.Instance(OrModule, "t2", ports=[andoroutp, andorwire1, andorinp3])

    Add4BitModule = Module("frcla_4b")
    add4bitinpa3 = Add4BitModule.Input("a3")
    add4bitinpa2 = Add4BitModule.Input("a2")
    add4bitinpa1 = Add4BitModule.Input("a1")
    add4bitinpa0 = Add4BitModule.Input("a0")
    add4bitinpb3 = Add4BitModule.Input("b3")
    add4bitinpb2 = Add4BitModule.Input("b2")
    add4bitinpb1 = Add4BitModule.Input("b1")
    add4bitinpb0 = Add4BitModule.Input("b0")
    add4bitinpc0 = Add4BitModule.Input("c0")
    add4bitc4 = Add4BitModule.Output("c4")
    add4bitsum3 = Add4BitModule.Output("sum3")
    add4bitsum2 = Add4BitModule.Output("sum2")
    add4bitsum1 = Add4BitModule.Output("sum1")
    add4bitsum0 = Add4BitModule.Output("sum0")
    add4bitg3 = Add4BitModule.Wire("g3")
    add4bitg2 = Add4BitModule.Wire("g2")
    add4bitg1 = Add4BitModule.Wire("g1")
    add4bitg0 = Add4BitModule.Wire("g0")
    add4bitp3 = Add4BitModule.Wire("p3")
    add4bitp2 = Add4BitModule.Wire("p2")
    add4bitp1 = Add4BitModule.Wire("p1")
    add4bitp0 = Add4BitModule.Wire("p0")
    add4bitc1 = Add4BitModule.Wire("c1")
    add4bitc2 = Add4BitModule.Wire("c2")
    add4bitc3 = Add4BitModule.Wire("c3")
    add4bitm1 = Add4BitModule.Wire("m1")
    add4bitm2 = Add4BitModule.Wire("m2")
    add4bitm3 = Add4BitModule.Wire("m3")
    add4bitm4 = Add4BitModule.Wire("m4")
    add4bitm5 = Add4BitModule.Wire("m5")
    add4bitm6 = Add4BitModule.Wire("m6")

    Add4BitModule.Instance(
        AndModule, "gate1", ports=[add4bitg0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        AndModule, "gate2", ports=[add4bitg1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        AndModule, "gate3", ports=[add4bitg2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        AndModule, "gate4", ports=[add4bitg3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        XorModule, "gate5", ports=[add4bitp0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        XorModule, "gate6", ports=[add4bitp1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        XorModule, "gate7", ports=[add4bitp2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        XorModule, "gate8", ports=[add4bitp3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        AndOrModule, "comp1", ports=[add4bitp1, add4bitg0, add4bitg1, add4bitm1]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp2", ports=[add4bitm1, add4bitp2, add4bitg2, add4bitm2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp3", ports=[add4bitm2, add4bitp3, add4bitg3, add4bitm3]
    )

    Add4BitModule.Instance(AndModule, "and1", ports=[add4bitm4, add4bitp1, add4bitp0])
    Add4BitModule.Instance(AndModule, "and2", ports=[add4bitm5, add4bitp2, add4bitm4])
    Add4BitModule.Instance(AndModule, "and3", ports=[add4bitm6, add4bitp3, add4bitm5])

    Add4BitModule.Instance(
        AndOrModule, "comp4", ports=[add4bitm6, add4bitinpc0, add4bitm3, add4bitc4]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp5", ports=[add4bitm5, add4bitinpc0, add4bitm2, add4bitc3]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp6", ports=[add4bitm4, add4bitinpc0, add4bitm1, add4bitc2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp7", ports=[add4bitp0, add4bitinpc0, add4bitg0, add4bitc1]
    )

    Add4BitModule.Instance(
        XorModule, "xorg1", ports=[add4bitsum0, add4bitp0, add4bitinpc0]
    )
    Add4BitModule.Instance(
        XorModule, "xorg2", ports=[add4bitsum1, add4bitp1, add4bitc1]
    )
    Add4BitModule.Instance(
        XorModule, "xorg3", ports=[add4bitsum2, add4bitp2, add4bitc2]
    )
    Add4BitModule.Instance(
        XorModule, "xorg4", ports=[add4bitsum3, add4bitp3, add4bitc3]
    )

    Add2BitModule = Module("frcla_2b")
    add2bitinpa1 = Add2BitModule.Input("a1")
    add2bitinpa0 = Add2BitModule.Input("a0")
    add2bitinpb1 = Add2BitModule.Input("b1")
    add2bitinpb0 = Add2BitModule.Input("b0")
    add2bitinpc0 = Add2BitModule.Input("c0")
    add2bitc2 = Add2BitModule.Output("c2")
    add2bitsum1 = Add2BitModule.Output("sum1")
    add2bitsum0 = Add2BitModule.Output("sum0")
    add2bitg1 = Add2BitModule.Wire("g1")
    add2bitg0 = Add2BitModule.Wire("g0")
    add2bitp1 = Add2BitModule.Wire("p1")
    add2bitp0 = Add2BitModule.Wire("p0")
    add2bitc1 = Add2BitModule.Wire("c1")
    add2bitm1 = Add2BitModule.Wire("m1")
    add2bitm2 = Add2BitModule.Wire("m2")

    Add2BitModule.Instance(
        AndModule, "gate1", ports=[add2bitg0, add2bitinpa0, add2bitinpb0]
    )
    Add2BitModule.Instance(
        AndModule, "gate2", ports=[add2bitg1, add2bitinpa1, add2bitinpb1]
    )

    Add2BitModule.Instance(
        XorModule, "gate5", ports=[add2bitp0, add2bitinpa0, add2bitinpb0]
    )
    Add2BitModule.Instance(
        XorModule, "gate6", ports=[add2bitp1, add2bitinpa1, add2bitinpb1]
    )

    Add2BitModule.Instance(
        AndOrModule, "comp1", ports=[add2bitp1, add2bitg0, add2bitg1, add2bitm1]
    )

    Add2BitModule.Instance(AndModule, "and1", ports=[add2bitm2, add2bitp1, add2bitp0])

    Add2BitModule.Instance(
        AndOrModule, "comp6", ports=[add2bitm2, add2bitinpc0, add2bitm1, add2bitc2]
    )
    Add2BitModule.Instance(
        AndOrModule, "comp7", ports=[add2bitp0, add2bitinpc0, add2bitg0, add2bitc1]
    )

    Add2BitModule.Instance(
        XorModule, "xorg1", ports=[add2bitsum0, add2bitp0, add2bitinpc0]
    )
    Add2BitModule.Instance(
        XorModule, "xorg2", ports=[add2bitsum1, add2bitp1, add2bitc1]
    )

    Adder = Module("hoaaned_32b")
    a = Adder.Input("a", 32)
    b = Adder.Input("b", 32)
    res = Adder.Output("sum", 33)
    n1 = Adder.Wire("n1")
    n2 = Adder.Wire("n2")
    n3 = Adder.Wire("n3")
    n4 = Adder.Wire("n4")
    n5 = Adder.Wire("n5")
    cout12 = Adder.Wire("cout12")
    cout16 = Adder.Wire("cout16")
    cout20 = Adder.Wire("cout20")
    cout24 = Adder.Wire("cout24")
    cout28 = Adder.Wire("cout28")

    res[0].assign(1)
    res[1].assign(1)
    res[2].assign(1)
    res[3].assign(1)
    res[4].assign(1)
    res[5].assign(1)
    res[6].assign(1)
    res[7].assign(1)

    Adder.Instance(OrModule, "t1", ports=[res[8], a[8], b[8]])
    Adder.Instance(AndModule, "t2", ports=[n1, a[8], b[8]])
    Adder.Instance(AndModule, "t3", ports=[n2, a[9], b[9]])
    Adder.Instance(NotModule, "t4", ports=[n3, n2])
    Adder.Instance(OrModule, "t5", ports=[n4, a[9], b[9]])
    Adder.Instance(AndModule, "t6", ports=[n5, n4, n1])
    Adder.Instance(OrModule, "t7", ports=[res[9], n5, n1])

    ## Accurate Part

    Adder.Instance(
        Add2BitModule,
        "cla1",
        ports=[a[11], a[10], b[11], b[10], n2, cout12, res[11], res[10]],
    )
    Adder.Instance(
        Add4BitModule,
        "cla2",
        ports=[
            a[15],
            a[14],
            a[13],
            a[12],
            b[15],
            b[14],
            b[13],
            b[12],
            cout12,
            cout16,
            res[15],
            res[14],
            res[13],
            res[12],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla3",
        ports=[
            a[19],
            a[18],
            a[17],
            a[16],
            b[19],
            b[18],
            b[17],
            b[16],
            cout16,
            cout20,
            res[19],
            res[18],
            res[17],
            res[16],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla4",
        ports=[
            a[23],
            a[22],
            a[21],
            a[20],
            b[23],
            b[22],
            b[21],
            b[20],
            cout20,
            cout24,
            res[23],
            res[22],
            res[21],
            res[20],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla5",
        ports=[
            a[27],
            a[26],
            a[25],
            a[24],
            b[27],
            b[26],
            b[25],
            b[24],
            cout24,
            cout28,
            res[27],
            res[26],
            res[25],
            res[24],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla6",
        ports=[
            a[31],
            a[30],
            a[29],
            a[28],
            b[31],
            b[30],
            b[29],
            b[28],
            cout28,
            res[32],
            res[31],
            res[30],
            res[29],
            res[28],
        ],
    )

    return Adder


# HOERAA (32 bit adders 10 inaccurate bits)


def HOERAA_32_bits_10_inaccurate():

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))

    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(andinp1, andinp2))

    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))

    NotModule = Module("not_1inp")
    notoutp = NotModule.Output("res")
    notinp = NotModule.Input("inp")
    notoutp.assign(Not(notinp))

    AndOrModule = Module("ao21")
    andorinp1 = AndOrModule.Input("a")
    andorinp2 = AndOrModule.Input("b")
    andorinp3 = AndOrModule.Input("c")
    andoroutp = AndOrModule.Output("y")
    andorwire1 = AndOrModule.Wire("net")
    AndOrModule.Instance(AndModule, "t1", ports=[andorwire1, andorinp1, andorinp2])
    AndOrModule.Instance(OrModule, "t2", ports=[andoroutp, andorwire1, andorinp3])

    Add4BitModule = Module("frcla_4b")
    add4bitinpa3 = Add4BitModule.Input("a3")
    add4bitinpa2 = Add4BitModule.Input("a2")
    add4bitinpa1 = Add4BitModule.Input("a1")
    add4bitinpa0 = Add4BitModule.Input("a0")
    add4bitinpb3 = Add4BitModule.Input("b3")
    add4bitinpb2 = Add4BitModule.Input("b2")
    add4bitinpb1 = Add4BitModule.Input("b1")
    add4bitinpb0 = Add4BitModule.Input("b0")
    add4bitinpc0 = Add4BitModule.Input("c0")
    add4bitc4 = Add4BitModule.Output("c4")
    add4bitsum3 = Add4BitModule.Output("sum3")
    add4bitsum2 = Add4BitModule.Output("sum2")
    add4bitsum1 = Add4BitModule.Output("sum1")
    add4bitsum0 = Add4BitModule.Output("sum0")
    add4bitg3 = Add4BitModule.Wire("g3")
    add4bitg2 = Add4BitModule.Wire("g2")
    add4bitg1 = Add4BitModule.Wire("g1")
    add4bitg0 = Add4BitModule.Wire("g0")
    add4bitp3 = Add4BitModule.Wire("p3")
    add4bitp2 = Add4BitModule.Wire("p2")
    add4bitp1 = Add4BitModule.Wire("p1")
    add4bitp0 = Add4BitModule.Wire("p0")
    add4bitc1 = Add4BitModule.Wire("c1")
    add4bitc2 = Add4BitModule.Wire("c2")
    add4bitc3 = Add4BitModule.Wire("c3")
    add4bitm1 = Add4BitModule.Wire("m1")
    add4bitm2 = Add4BitModule.Wire("m2")
    add4bitm3 = Add4BitModule.Wire("m3")
    add4bitm4 = Add4BitModule.Wire("m4")
    add4bitm5 = Add4BitModule.Wire("m5")
    add4bitm6 = Add4BitModule.Wire("m6")

    Add4BitModule.Instance(
        AndModule, "gate1", ports=[add4bitg0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        AndModule, "gate2", ports=[add4bitg1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        AndModule, "gate3", ports=[add4bitg2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        AndModule, "gate4", ports=[add4bitg3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        XorModule, "gate5", ports=[add4bitp0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        XorModule, "gate6", ports=[add4bitp1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        XorModule, "gate7", ports=[add4bitp2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        XorModule, "gate8", ports=[add4bitp3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        AndOrModule, "comp1", ports=[add4bitp1, add4bitg0, add4bitg1, add4bitm1]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp2", ports=[add4bitm1, add4bitp2, add4bitg2, add4bitm2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp3", ports=[add4bitm2, add4bitp3, add4bitg3, add4bitm3]
    )

    Add4BitModule.Instance(AndModule, "and1", ports=[add4bitm4, add4bitp1, add4bitp0])
    Add4BitModule.Instance(AndModule, "and2", ports=[add4bitm5, add4bitp2, add4bitm4])
    Add4BitModule.Instance(AndModule, "and3", ports=[add4bitm6, add4bitp3, add4bitm5])

    Add4BitModule.Instance(
        AndOrModule, "comp4", ports=[add4bitm6, add4bitinpc0, add4bitm3, add4bitc4]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp5", ports=[add4bitm5, add4bitinpc0, add4bitm2, add4bitc3]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp6", ports=[add4bitm4, add4bitinpc0, add4bitm1, add4bitc2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp7", ports=[add4bitp0, add4bitinpc0, add4bitg0, add4bitc1]
    )

    Add4BitModule.Instance(
        XorModule, "xorg1", ports=[add4bitsum0, add4bitp0, add4bitinpc0]
    )
    Add4BitModule.Instance(
        XorModule, "xorg2", ports=[add4bitsum1, add4bitp1, add4bitc1]
    )
    Add4BitModule.Instance(
        XorModule, "xorg3", ports=[add4bitsum2, add4bitp2, add4bitc2]
    )
    Add4BitModule.Instance(
        XorModule, "xorg4", ports=[add4bitsum3, add4bitp3, add4bitc3]
    )

    Add2BitModule = Module("frcla_2b")
    add2bitinpa1 = Add2BitModule.Input("a1")
    add2bitinpa0 = Add2BitModule.Input("a0")
    add2bitinpb1 = Add2BitModule.Input("b1")
    add2bitinpb0 = Add2BitModule.Input("b0")
    add2bitinpc0 = Add2BitModule.Input("c0")
    add2bitc2 = Add2BitModule.Output("c2")
    add2bitsum1 = Add2BitModule.Output("sum1")
    add2bitsum0 = Add2BitModule.Output("sum0")
    add2bitg1 = Add2BitModule.Wire("g1")
    add2bitg0 = Add2BitModule.Wire("g0")
    add2bitp1 = Add2BitModule.Wire("p1")
    add2bitp0 = Add2BitModule.Wire("p0")
    add2bitc1 = Add2BitModule.Wire("c1")
    add2bitm1 = Add2BitModule.Wire("m1")
    add2bitm2 = Add2BitModule.Wire("m2")

    Add2BitModule.Instance(
        AndModule, "gate1", ports=[add2bitg0, add2bitinpa0, add2bitinpb0]
    )
    Add2BitModule.Instance(
        AndModule, "gate2", ports=[add2bitg1, add2bitinpa1, add2bitinpb1]
    )

    Add2BitModule.Instance(
        XorModule, "gate5", ports=[add2bitp0, add2bitinpa0, add2bitinpb0]
    )
    Add2BitModule.Instance(
        XorModule, "gate6", ports=[add2bitp1, add2bitinpa1, add2bitinpb1]
    )

    Add2BitModule.Instance(
        AndOrModule, "comp1", ports=[add2bitp1, add2bitg0, add2bitg1, add2bitm1]
    )

    Add2BitModule.Instance(AndModule, "and1", ports=[add2bitm2, add2bitp1, add2bitp0])

    Add2BitModule.Instance(
        AndOrModule, "comp6", ports=[add2bitm2, add2bitinpc0, add2bitm1, add2bitc2]
    )
    Add2BitModule.Instance(
        AndOrModule, "comp7", ports=[add2bitp0, add2bitinpc0, add2bitg0, add2bitc1]
    )

    Add2BitModule.Instance(
        XorModule, "xorg1", ports=[add2bitsum0, add2bitp0, add2bitinpc0]
    )
    Add2BitModule.Instance(
        XorModule, "xorg2", ports=[add2bitsum1, add2bitp1, add2bitc1]
    )

    Adder = Module("hoeraa_32b")
    a = Adder.Input("a", 32)
    b = Adder.Input("b", 32)
    res = Adder.Output("sum", 33)
    n1 = Adder.Wire("n1")
    n2 = Adder.Wire("n2")
    n3 = Adder.Wire("n3")
    n4 = Adder.Wire("n4")
    n5 = Adder.Wire("n5")
    n6 = Adder.Wire("n6")
    cout12 = Adder.Wire("cout12")
    cout16 = Adder.Wire("cout16")
    cout20 = Adder.Wire("cout20")
    cout24 = Adder.Wire("cout24")
    cout28 = Adder.Wire("cout28")

    res[0].assign(1)
    res[1].assign(1)
    res[2].assign(1)
    res[3].assign(1)
    res[4].assign(1)
    res[5].assign(1)
    res[6].assign(1)
    res[7].assign(1)

    Adder.Instance(OrModule, "t1", ports=[res[8], a[8], b[8]])
    Adder.Instance(AndModule, "t2", ports=[n1, a[9], b[9]])
    Adder.Instance(NotModule, "t3", ports=[n2, n1])
    Adder.Instance(AndModule, "t4", ports=[n3, a[8], b[8]])
    Adder.Instance(OrModule, "t5", ports=[n4, a[9], b[9]])
    Adder.Instance(AndModule, "t6", ports=[n5, n4, n2])
    Adder.Instance(AndModule, "t7", ports=[n6, n3, n1])
    Adder.Instance(OrModule, "t8", ports=[res[9], n5, n6])

    ## Accurate Part

    Adder.Instance(
        Add2BitModule,
        "cla1",
        ports=[a[11], a[10], b[11], b[10], n1, cout12, res[11], res[10]],
    )
    Adder.Instance(
        Add4BitModule,
        "cla2",
        ports=[
            a[15],
            a[14],
            a[13],
            a[12],
            b[15],
            b[14],
            b[13],
            b[12],
            cout12,
            cout16,
            res[15],
            res[14],
            res[13],
            res[12],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla3",
        ports=[
            a[19],
            a[18],
            a[17],
            a[16],
            b[19],
            b[18],
            b[17],
            b[16],
            cout16,
            cout20,
            res[19],
            res[18],
            res[17],
            res[16],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla4",
        ports=[
            a[23],
            a[22],
            a[21],
            a[20],
            b[23],
            b[22],
            b[21],
            b[20],
            cout20,
            cout24,
            res[23],
            res[22],
            res[21],
            res[20],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla5",
        ports=[
            a[27],
            a[26],
            a[25],
            a[24],
            b[27],
            b[26],
            b[25],
            b[24],
            cout24,
            cout28,
            res[27],
            res[26],
            res[25],
            res[24],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla6",
        ports=[
            a[31],
            a[30],
            a[29],
            a[28],
            b[31],
            b[30],
            b[29],
            b[28],
            cout28,
            res[32],
            res[31],
            res[30],
            res[29],
            res[28],
        ],
    )

    return Adder


# M-HERLOA (32 bit adders 10 inaccurate bits)


def M_HERLOA_32_bits_10_inaccurate():

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))

    NandModule = Module("nand_2inp")
    nandoutp = NandModule.Output("res")
    nandinp1 = NandModule.Input("inp1")
    nandinp2 = NandModule.Input("inp2")
    nandoutp.assign(Not(And(nandinp1, nandinp2)))

    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(andinp1, andinp2))

    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))

    NotModule = Module("not_1inp")
    notoutp = NotModule.Output("res")
    notinp = NotModule.Input("inp")
    notoutp.assign(Not(notinp))

    AndOrModule = Module("ao21")
    andorinp1 = AndOrModule.Input("a")
    andorinp2 = AndOrModule.Input("b")
    andorinp3 = AndOrModule.Input("c")
    andoroutp = AndOrModule.Output("y")
    andorwire1 = AndOrModule.Wire("net")
    AndOrModule.Instance(AndModule, "t1", ports=[andorwire1, andorinp1, andorinp2])
    AndOrModule.Instance(OrModule, "t2", ports=[andoroutp, andorwire1, andorinp3])

    Add4BitModule = Module("frcla_4b")
    add4bitinpa3 = Add4BitModule.Input("a3")
    add4bitinpa2 = Add4BitModule.Input("a2")
    add4bitinpa1 = Add4BitModule.Input("a1")
    add4bitinpa0 = Add4BitModule.Input("a0")
    add4bitinpb3 = Add4BitModule.Input("b3")
    add4bitinpb2 = Add4BitModule.Input("b2")
    add4bitinpb1 = Add4BitModule.Input("b1")
    add4bitinpb0 = Add4BitModule.Input("b0")
    add4bitinpc0 = Add4BitModule.Input("c0")
    add4bitc4 = Add4BitModule.Output("c4")
    add4bitsum3 = Add4BitModule.Output("sum3")
    add4bitsum2 = Add4BitModule.Output("sum2")
    add4bitsum1 = Add4BitModule.Output("sum1")
    add4bitsum0 = Add4BitModule.Output("sum0")
    add4bitg3 = Add4BitModule.Wire("g3")
    add4bitg2 = Add4BitModule.Wire("g2")
    add4bitg1 = Add4BitModule.Wire("g1")
    add4bitg0 = Add4BitModule.Wire("g0")
    add4bitp3 = Add4BitModule.Wire("p3")
    add4bitp2 = Add4BitModule.Wire("p2")
    add4bitp1 = Add4BitModule.Wire("p1")
    add4bitp0 = Add4BitModule.Wire("p0")
    add4bitc1 = Add4BitModule.Wire("c1")
    add4bitc2 = Add4BitModule.Wire("c2")
    add4bitc3 = Add4BitModule.Wire("c3")
    add4bitm1 = Add4BitModule.Wire("m1")
    add4bitm2 = Add4BitModule.Wire("m2")
    add4bitm3 = Add4BitModule.Wire("m3")
    add4bitm4 = Add4BitModule.Wire("m4")
    add4bitm5 = Add4BitModule.Wire("m5")
    add4bitm6 = Add4BitModule.Wire("m6")

    Add4BitModule.Instance(
        AndModule, "gate1", ports=[add4bitg0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        AndModule, "gate2", ports=[add4bitg1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        AndModule, "gate3", ports=[add4bitg2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        AndModule, "gate4", ports=[add4bitg3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        XorModule, "gate5", ports=[add4bitp0, add4bitinpa0, add4bitinpb0]
    )
    Add4BitModule.Instance(
        XorModule, "gate6", ports=[add4bitp1, add4bitinpa1, add4bitinpb1]
    )
    Add4BitModule.Instance(
        XorModule, "gate7", ports=[add4bitp2, add4bitinpa2, add4bitinpb2]
    )
    Add4BitModule.Instance(
        XorModule, "gate8", ports=[add4bitp3, add4bitinpa3, add4bitinpb3]
    )

    Add4BitModule.Instance(
        AndOrModule, "comp1", ports=[add4bitp1, add4bitg0, add4bitg1, add4bitm1]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp2", ports=[add4bitm1, add4bitp2, add4bitg2, add4bitm2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp3", ports=[add4bitm2, add4bitp3, add4bitg3, add4bitm3]
    )

    Add4BitModule.Instance(AndModule, "and1", ports=[add4bitm4, add4bitp1, add4bitp0])
    Add4BitModule.Instance(AndModule, "and2", ports=[add4bitm5, add4bitp2, add4bitm4])
    Add4BitModule.Instance(AndModule, "and3", ports=[add4bitm6, add4bitp3, add4bitm5])

    Add4BitModule.Instance(
        AndOrModule, "comp4", ports=[add4bitm6, add4bitinpc0, add4bitm3, add4bitc4]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp5", ports=[add4bitm5, add4bitinpc0, add4bitm2, add4bitc3]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp6", ports=[add4bitm4, add4bitinpc0, add4bitm1, add4bitc2]
    )
    Add4BitModule.Instance(
        AndOrModule, "comp7", ports=[add4bitp0, add4bitinpc0, add4bitg0, add4bitc1]
    )

    Add4BitModule.Instance(
        XorModule, "xorg1", ports=[add4bitsum0, add4bitp0, add4bitinpc0]
    )
    Add4BitModule.Instance(
        XorModule, "xorg2", ports=[add4bitsum1, add4bitp1, add4bitc1]
    )
    Add4BitModule.Instance(
        XorModule, "xorg3", ports=[add4bitsum2, add4bitp2, add4bitc2]
    )
    Add4BitModule.Instance(
        XorModule, "xorg4", ports=[add4bitsum3, add4bitp3, add4bitc3]
    )

    Add2BitModule = Module("frcla_2b")
    add2bitinpa1 = Add2BitModule.Input("a1")
    add2bitinpa0 = Add2BitModule.Input("a0")
    add2bitinpb1 = Add2BitModule.Input("b1")
    add2bitinpb0 = Add2BitModule.Input("b0")
    add2bitinpc0 = Add2BitModule.Input("c0")
    add2bitc2 = Add2BitModule.Output("c2")
    add2bitsum1 = Add2BitModule.Output("sum1")
    add2bitsum0 = Add2BitModule.Output("sum0")
    add2bitg1 = Add2BitModule.Wire("g1")
    add2bitg0 = Add2BitModule.Wire("g0")
    add2bitp1 = Add2BitModule.Wire("p1")
    add2bitp0 = Add2BitModule.Wire("p0")
    add2bitc1 = Add2BitModule.Wire("c1")
    add2bitm1 = Add2BitModule.Wire("m1")
    add2bitm2 = Add2BitModule.Wire("m2")

    Add2BitModule.Instance(
        AndModule, "gate1", ports=[add2bitg0, add2bitinpa0, add2bitinpb0]
    )
    Add2BitModule.Instance(
        AndModule, "gate2", ports=[add2bitg1, add2bitinpa1, add2bitinpb1]
    )

    Add2BitModule.Instance(
        XorModule, "gate5", ports=[add2bitp0, add2bitinpa0, add2bitinpb0]
    )
    Add2BitModule.Instance(
        XorModule, "gate6", ports=[add2bitp1, add2bitinpa1, add2bitinpb1]
    )

    Add2BitModule.Instance(
        AndOrModule, "comp1", ports=[add2bitp1, add2bitg0, add2bitg1, add2bitm1]
    )

    Add2BitModule.Instance(AndModule, "and1", ports=[add2bitm2, add2bitp1, add2bitp0])

    Add2BitModule.Instance(
        AndOrModule, "comp6", ports=[add2bitm2, add2bitinpc0, add2bitm1, add2bitc2]
    )
    Add2BitModule.Instance(
        AndOrModule, "comp7", ports=[add2bitp0, add2bitinpc0, add2bitg0, add2bitc1]
    )

    Add2BitModule.Instance(
        XorModule, "xorg1", ports=[add2bitsum0, add2bitp0, add2bitinpc0]
    )
    Add2BitModule.Instance(
        XorModule, "xorg2", ports=[add2bitsum1, add2bitp1, add2bitc1]
    )

    Adder = Module("mherloa_32b")
    a = Adder.Input("a", 32)
    b = Adder.Input("b", 32)
    res = Adder.Output("sum", 33)
    n1 = Adder.Wire("n1")
    n2 = Adder.Wire("n2")
    n3 = Adder.Wire("n3")
    w1 = Adder.Wire("w1")
    w2 = Adder.Wire("w2")
    w9 = Adder.Wire("w9")
    w10 = Adder.Wire("w10")
    w11 = Adder.Wire("w11")
    w12 = Adder.Wire("w12")

    cout12 = Adder.Wire("cout12")
    cout16 = Adder.Wire("cout16")
    cout20 = Adder.Wire("cout20")
    cout24 = Adder.Wire("cout24")
    cout28 = Adder.Wire("cout28")

    res[0].assign(1)
    res[1].assign(1)
    res[2].assign(1)
    res[3].assign(1)
    res[4].assign(1)
    res[5].assign(1)

    Adder.Instance(XorModule, "t1", ports=[n1, a[9], b[9]])
    Adder.Instance(AndModule, "t2", ports=[n2, a[8], b[8]])
    Adder.Instance(OrModule, "t3", ports=[res[9], n1, n2])
    Adder.Instance(AndModule, "t4", ports=[n3, n1, n2])

    Adder.Instance(OrModule, "g1", ports=[w1, a[7], b[7]])
    Adder.Instance(OrModule, "g2", ports=[w2, a[6], b[6]])

    Adder.Instance(OrModule, "e1", ports=[res[7], n3, w1])
    Adder.Instance(OrModule, "e2", ports=[res[6], n3, w2])

    Adder.Instance(OrModule, "t5", ports=[w9, a[8], b[8]])
    Adder.Instance(NotModule, "t6", ports=[w10, n1])
    Adder.Instance(NandModule, "t7", ports=[w11, w10, n2])
    Adder.Instance(AndModule, "t8", ports=[res[8], w11, w9])
    Adder.Instance(AndModule, "t9", ports=[w12, a[9], b[9]])

    ## Accurate Part

    Adder.Instance(
        Add2BitModule,
        "cla1",
        ports=[a[11], a[10], b[11], b[10], w12, cout12, res[11], res[10]],
    )
    Adder.Instance(
        Add4BitModule,
        "cla2",
        ports=[
            a[15],
            a[14],
            a[13],
            a[12],
            b[15],
            b[14],
            b[13],
            b[12],
            cout12,
            cout16,
            res[15],
            res[14],
            res[13],
            res[12],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla3",
        ports=[
            a[19],
            a[18],
            a[17],
            a[16],
            b[19],
            b[18],
            b[17],
            b[16],
            cout16,
            cout20,
            res[19],
            res[18],
            res[17],
            res[16],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla4",
        ports=[
            a[23],
            a[22],
            a[21],
            a[20],
            b[23],
            b[22],
            b[21],
            b[20],
            cout20,
            cout24,
            res[23],
            res[22],
            res[21],
            res[20],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla5",
        ports=[
            a[27],
            a[26],
            a[25],
            a[24],
            b[27],
            b[26],
            b[25],
            b[24],
            cout24,
            cout28,
            res[27],
            res[26],
            res[25],
            res[24],
        ],
    )
    Adder.Instance(
        Add4BitModule,
        "cla6",
        ports=[
            a[31],
            a[30],
            a[29],
            a[28],
            b[31],
            b[30],
            b[29],
            b[28],
            cout28,
            res[32],
            res[31],
            res[30],
            res[29],
            res[28],
        ],
    )

    return Adder
