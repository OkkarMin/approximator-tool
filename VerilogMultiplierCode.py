from veriloggen import *

##########################################################################

# Used for ASIC Based Approximate Multiplier Design
# Using veriloggen
# Veriloggen link for installation and usage (https://pypi.org/project/veriloggen/)

##########################################################################

## 8x6 and 8x8 Multipliers


def accurate_8x6_multiplier():  # Accurate 8x6 Multiplier
    Mult = Module("multiplier_8x6")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 6)
    res = Mult.Output("p", 14)
    res.assign(a * b)
    return Mult


def accurate_8x8_multiplier():  # Accurate 8x8 Multiplier
    Mult = Module("multiplier_8x8")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 8)
    res = Mult.Output("p", 16)
    res.assign(a * b)
    return Mult


def accurate_MxN_multiplier(M, N):  # Accurate MxN Multiplier
    Mult = Module("multiplier_" + str(M) + "x" + str(N))
    a = Mult.Input("a", M)
    b = Mult.Input("b", N)
    res = Mult.Output("p", M + N)
    res.assign(a * b)
    return Mult


def accurate_8x6_binary_array_multiplier():  # Accurate 8x6 Binary Array Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("bam_8x6")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 6)
    res = Mult.Output("p", 14)

    w10 = Mult.Wire("w10")
    w20 = Mult.Wire("w20")
    w30 = Mult.Wire("w30")
    w40 = Mult.Wire("w40")
    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w01 = Mult.Wire("w01")
    w11 = Mult.Wire("w11")
    w21 = Mult.Wire("w21")
    w31 = Mult.Wire("w31")
    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w02 = Mult.Wire("w02")
    w12 = Mult.Wire("w12")
    w22 = Mult.Wire("w22")
    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w03 = Mult.Wire("w03")
    w13 = Mult.Wire("w13")
    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w04 = Mult.Wire("w04")
    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    a1 = Mult.Wire("a1")
    a2 = Mult.Wire("a2")
    a3 = Mult.Wire("a3")
    a4 = Mult.Wire("a4")
    a5 = Mult.Wire("a5")
    a6 = Mult.Wire("a6")
    a7 = Mult.Wire("a7")
    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b1 = Mult.Wire("b1")
    b2 = Mult.Wire("b2")
    b3 = Mult.Wire("b3")
    b4 = Mult.Wire("b4")
    b5 = Mult.Wire("b5")
    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c1 = Mult.Wire("c1")
    c2 = Mult.Wire("c2")
    c3 = Mult.Wire("c3")
    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d1 = Mult.Wire("d1")
    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")

    Mult.Instance(AndModule, "i1", ports=[w01, a[0], b[1]])
    Mult.Instance(AndModule, "i2", ports=[w10, a[1], b[0]])
    Mult.Instance(AndModule, "i3", ports=[w11, a[1], b[1]])
    Mult.Instance(AndModule, "i4", ports=[w20, a[2], b[0]])
    Mult.Instance(AndModule, "i5", ports=[w21, a[2], b[1]])
    Mult.Instance(AndModule, "i6", ports=[w30, a[3], b[0]])
    Mult.Instance(AndModule, "i7", ports=[w31, a[3], b[1]])
    Mult.Instance(AndModule, "i8", ports=[w40, a[4], b[0]])
    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li1", ports=[w02, a[0], b[2]])
    Mult.Instance(AndModule, "li2", ports=[w12, a[1], b[2]])
    Mult.Instance(AndModule, "li3", ports=[w22, a[2], b[2]])
    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi1", ports=[w03, a[0], b[3]])
    Mult.Instance(AndModule, "gi2", ports=[w13, a[1], b[3]])
    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi1", ports=[w04, a[0], b[4]])
    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "mi1", ports=[w75, a[7], b[5]])
    Mult.Instance(AndModule, "mi2", ports=[res[0], a[0], b[0]])

    Mult.Instance(HalfAdderModule, "ha1", ports=[w10, w01, res[1], a1])
    Mult.Instance(HalfAdderModule, "ha2", ports=[w20, w11, a2, a3])
    Mult.Instance(HalfAdderModule, "ha3", ports=[w30, w21, a4, a5])
    Mult.Instance(HalfAdderModule, "ha4", ports=[w40, w31, a6, a7])
    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(FullAdderModule, "afa1", ports=[a1, a2, w02, res[2], b1])
    Mult.Instance(FullAdderModule, "afa2", ports=[a3, a4, w12, b2, b3])
    Mult.Instance(FullAdderModule, "afa3", ports=[a5, a6, w22, b4, b5])
    Mult.Instance(FullAdderModule, "afa4", ports=[a7, a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(FullAdderModule, "bfa1", ports=[b1, b2, w03, res[3], c1])
    Mult.Instance(FullAdderModule, "bfa2", ports=[b3, b4, w13, c2, c3])
    Mult.Instance(FullAdderModule, "bfa3", ports=[b5, b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(FullAdderModule, "cfa1", ports=[c1, c2, w04, res[4], d1])
    Mult.Instance(FullAdderModule, "cfa2", ports=[c3, c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(FullAdderModule, "dfa1", ports=[d1, d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    Mult.Instance(HalfAdderModule, "had1", ports=[e1, e2, res[6], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[e3, e4, h1, res[7], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[e5, e6, h2, res[8], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[e7, e8, h3, res[9], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[e9, e10, h4, res[10], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[e11, e12, h5, res[11], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w75, e13, h6, res[12], res[13]])

    return Mult


def accurate_8x8_binary_array_multiplier():  # Accurate 8x8 Binary Array Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("bam_8x8")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 8)
    res = Mult.Output("p", 16)

    w10 = Mult.Wire("w10")
    w20 = Mult.Wire("w20")
    w30 = Mult.Wire("w30")
    w40 = Mult.Wire("w40")
    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w01 = Mult.Wire("w01")
    w11 = Mult.Wire("w11")
    w21 = Mult.Wire("w21")
    w31 = Mult.Wire("w31")
    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w02 = Mult.Wire("w02")
    w12 = Mult.Wire("w12")
    w22 = Mult.Wire("w22")
    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w03 = Mult.Wire("w03")
    w13 = Mult.Wire("w13")
    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w04 = Mult.Wire("w04")
    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    w06 = Mult.Wire("w06")
    w16 = Mult.Wire("w16")
    w26 = Mult.Wire("w26")
    w36 = Mult.Wire("w36")
    w46 = Mult.Wire("w46")
    w56 = Mult.Wire("w56")
    w66 = Mult.Wire("w66")
    w76 = Mult.Wire("w76")

    w07 = Mult.Wire("w07")
    w17 = Mult.Wire("w17")
    w27 = Mult.Wire("w27")
    w37 = Mult.Wire("w37")
    w47 = Mult.Wire("w47")
    w57 = Mult.Wire("w57")
    w67 = Mult.Wire("w67")
    w77 = Mult.Wire("w77")

    a1 = Mult.Wire("a1")
    a2 = Mult.Wire("a2")
    a3 = Mult.Wire("a3")
    a4 = Mult.Wire("a4")
    a5 = Mult.Wire("a5")
    a6 = Mult.Wire("a6")
    a7 = Mult.Wire("a7")
    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b1 = Mult.Wire("b1")
    b2 = Mult.Wire("b2")
    b3 = Mult.Wire("b3")
    b4 = Mult.Wire("b4")
    b5 = Mult.Wire("b5")
    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c1 = Mult.Wire("c1")
    c2 = Mult.Wire("c2")
    c3 = Mult.Wire("c3")
    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d1 = Mult.Wire("d1")
    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    f1 = Mult.Wire("f1")
    f2 = Mult.Wire("f2")
    f3 = Mult.Wire("f3")
    f4 = Mult.Wire("f4")
    f5 = Mult.Wire("f5")
    f6 = Mult.Wire("f6")
    f7 = Mult.Wire("f7")
    f8 = Mult.Wire("f8")
    f9 = Mult.Wire("f9")
    f10 = Mult.Wire("f10")
    f11 = Mult.Wire("f11")
    f12 = Mult.Wire("f12")
    f13 = Mult.Wire("f13")

    g1 = Mult.Wire("g1")
    g2 = Mult.Wire("g2")
    g3 = Mult.Wire("g3")
    g4 = Mult.Wire("g4")
    g5 = Mult.Wire("g5")
    g6 = Mult.Wire("g6")
    g7 = Mult.Wire("g7")
    g8 = Mult.Wire("g8")
    g9 = Mult.Wire("g9")
    g10 = Mult.Wire("g10")
    g11 = Mult.Wire("g11")
    g12 = Mult.Wire("g12")
    g13 = Mult.Wire("g13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")

    Mult.Instance(AndModule, "i1", ports=[w01, a[0], b[1]])
    Mult.Instance(AndModule, "i2", ports=[w10, a[1], b[0]])
    Mult.Instance(AndModule, "i3", ports=[w11, a[1], b[1]])
    Mult.Instance(AndModule, "i4", ports=[w20, a[2], b[0]])
    Mult.Instance(AndModule, "i5", ports=[w21, a[2], b[1]])
    Mult.Instance(AndModule, "i6", ports=[w30, a[3], b[0]])
    Mult.Instance(AndModule, "i7", ports=[w31, a[3], b[1]])
    Mult.Instance(AndModule, "i8", ports=[w40, a[4], b[0]])
    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li1", ports=[w02, a[0], b[2]])
    Mult.Instance(AndModule, "li2", ports=[w12, a[1], b[2]])
    Mult.Instance(AndModule, "li3", ports=[w22, a[2], b[2]])
    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi1", ports=[w03, a[0], b[3]])
    Mult.Instance(AndModule, "gi2", ports=[w13, a[1], b[3]])
    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi1", ports=[w04, a[0], b[4]])
    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "ji1", ports=[w06, a[0], b[6]])
    Mult.Instance(AndModule, "ji2", ports=[w16, a[1], b[6]])
    Mult.Instance(AndModule, "ji3", ports=[w26, a[2], b[6]])
    Mult.Instance(AndModule, "ji4", ports=[w36, a[3], b[6]])
    Mult.Instance(AndModule, "ji5", ports=[w46, a[4], b[6]])
    Mult.Instance(AndModule, "ji6", ports=[w56, a[5], b[6]])
    Mult.Instance(AndModule, "ji7", ports=[w66, a[6], b[6]])
    Mult.Instance(AndModule, "ji8", ports=[w75, a[7], b[5]])

    Mult.Instance(AndModule, "ki1", ports=[w07, a[0], b[7]])
    Mult.Instance(AndModule, "ki2", ports=[w17, a[1], b[7]])
    Mult.Instance(AndModule, "ki3", ports=[w27, a[2], b[7]])
    Mult.Instance(AndModule, "ki4", ports=[w37, a[3], b[7]])
    Mult.Instance(AndModule, "ki5", ports=[w47, a[4], b[7]])
    Mult.Instance(AndModule, "ki6", ports=[w57, a[5], b[7]])
    Mult.Instance(AndModule, "ki7", ports=[w67, a[6], b[7]])
    Mult.Instance(AndModule, "ki8", ports=[w76, a[7], b[6]])

    Mult.Instance(AndModule, "mi1", ports=[w77, a[7], b[7]])
    Mult.Instance(AndModule, "mi2", ports=[res[0], a[0], b[0]])

    Mult.Instance(HalfAdderModule, "ha1", ports=[w10, w01, res[1], a1])
    Mult.Instance(HalfAdderModule, "ha2", ports=[w20, w11, a2, a3])
    Mult.Instance(HalfAdderModule, "ha3", ports=[w30, w21, a4, a5])
    Mult.Instance(HalfAdderModule, "ha4", ports=[w40, w31, a6, a7])
    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(FullAdderModule, "afa1", ports=[a1, a2, w02, res[2], b1])
    Mult.Instance(FullAdderModule, "afa2", ports=[a3, a4, w12, b2, b3])
    Mult.Instance(FullAdderModule, "afa3", ports=[a5, a6, w22, b4, b5])
    Mult.Instance(FullAdderModule, "afa4", ports=[a7, a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(FullAdderModule, "bfa1", ports=[b1, b2, w03, res[3], c1])
    Mult.Instance(FullAdderModule, "bfa2", ports=[b3, b4, w13, c2, c3])
    Mult.Instance(FullAdderModule, "bfa3", ports=[b5, b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(FullAdderModule, "cfa1", ports=[c1, c2, w04, res[4], d1])
    Mult.Instance(FullAdderModule, "cfa2", ports=[c3, c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(FullAdderModule, "dfa1", ports=[d1, d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    Mult.Instance(FullAdderModule, "efa1", ports=[e1, e2, w06, res[6], f1])
    Mult.Instance(FullAdderModule, "efa2", ports=[e3, e4, w16, f2, f3])
    Mult.Instance(FullAdderModule, "efa3", ports=[e5, e6, w26, f4, f5])
    Mult.Instance(FullAdderModule, "efa4", ports=[e7, e8, w36, f6, f7])
    Mult.Instance(FullAdderModule, "efa5", ports=[e9, e10, w46, f8, f9])
    Mult.Instance(FullAdderModule, "efa6", ports=[e11, e12, w56, f10, f11])
    Mult.Instance(FullAdderModule, "efa7", ports=[e13, w75, w66, f12, f13])

    Mult.Instance(FullAdderModule, "ffa1", ports=[f1, f2, w07, res[7], g1])
    Mult.Instance(FullAdderModule, "ffa2", ports=[f3, f4, w17, g2, g3])
    Mult.Instance(FullAdderModule, "ffa3", ports=[f5, f6, w27, g4, g5])
    Mult.Instance(FullAdderModule, "ffa4", ports=[f7, f8, w37, g6, g7])
    Mult.Instance(FullAdderModule, "ffa5", ports=[f9, f10, w47, g8, g9])
    Mult.Instance(FullAdderModule, "ffa6", ports=[f11, f12, w57, g10, g11])
    Mult.Instance(FullAdderModule, "ffa7", ports=[f13, w76, w67, g12, g13])

    Mult.Instance(HalfAdderModule, "had1", ports=[g1, g2, res[8], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[g3, g4, h1, res[9], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[g5, g6, h2, res[10], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[g7, g8, h3, res[11], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[g9, g10, h4, res[12], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[g11, g12, h5, res[13], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w77, g13, h6, res[14], res[15]])

    return Mult


def accurate_MxN_binary_array_multiplier(M, N):  # Accurate MxN Binary Array Multiplier
    # Remember to use constraint M>=3 and N>=3

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("bam_" + str(M) + "x" + str(N))
    a = Mult.Input("a", M)
    b = Mult.Input("b", N)
    res = Mult.Output("p", M + N)

    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                continue
            else:
                exec("w%d_%d = Mult.Wire('w%d_%d');" % (j, i, j, i))

    ##    w10=Mult.Wire('w10');
    ##    w20=Mult.Wire('w20');
    ##    w30=Mult.Wire('w30');
    ##    w40=Mult.Wire('w40');
    ##    w50=Mult.Wire('w50');
    ##    w60=Mult.Wire('w60');
    ##    w70=Mult.Wire('w70');
    ##
    ##    w01=Mult.Wire('w01');
    ##    w11=Mult.Wire('w11');
    ##    w21=Mult.Wire('w21');
    ##    w31=Mult.Wire('w31');
    ##    w41=Mult.Wire('w41');
    ##    w51=Mult.Wire('w51');
    ##    w61=Mult.Wire('w61');
    ##    w71=Mult.Wire('w71');
    ##
    ##    w02=Mult.Wire('w02');
    ##    w12=Mult.Wire('w12');
    ##    w22=Mult.Wire('w22');
    ##    w32=Mult.Wire('w32');
    ##    w42=Mult.Wire('w42');
    ##    w52=Mult.Wire('w52');
    ##    w62=Mult.Wire('w62');
    ##    w72=Mult.Wire('w72');
    ##
    ##    w03=Mult.Wire('w03');
    ##    w13=Mult.Wire('w13');
    ##    w23=Mult.Wire('w23');
    ##    w33=Mult.Wire('w33');
    ##    w43=Mult.Wire('w43');
    ##    w53=Mult.Wire('w53');
    ##    w63=Mult.Wire('w63');
    ##    w73=Mult.Wire('w73');
    ##
    ##    w04=Mult.Wire('w04');
    ##    w14=Mult.Wire('w14');
    ##    w24=Mult.Wire('w24');
    ##    w34=Mult.Wire('w34');
    ##    w44=Mult.Wire('w44');
    ##    w54=Mult.Wire('w54');
    ##    w64=Mult.Wire('w64');
    ##    w74=Mult.Wire('w74');
    ##
    ##    w05=Mult.Wire('w05');
    ##    w15=Mult.Wire('w15');
    ##    w25=Mult.Wire('w25');
    ##    w35=Mult.Wire('w35');
    ##    w45=Mult.Wire('w45');
    ##    w55=Mult.Wire('w55');
    ##    w65=Mult.Wire('w65');
    ##    w75=Mult.Wire('w75');
    ##
    ##    w06=Mult.Wire('w06');
    ##    w16=Mult.Wire('w16');
    ##    w26=Mult.Wire('w26');
    ##    w36=Mult.Wire('w36');
    ##    w46=Mult.Wire('w46');
    ##    w56=Mult.Wire('w56');
    ##    w66=Mult.Wire('w66');
    ##    w76=Mult.Wire('w76');
    ##
    ##    w07=Mult.Wire('w07');
    ##    w17=Mult.Wire('w17');
    ##    w27=Mult.Wire('w27');
    ##    w37=Mult.Wire('w37');
    ##    w47=Mult.Wire('w47');
    ##    w57=Mult.Wire('w57');
    ##    w67=Mult.Wire('w67');
    ##    w77=Mult.Wire('w77');

    for i in range(N - 1):
        for j in range(M - 1):
            if j != 0:
                exec("s_%d_%d=Mult.Wire('s_%d_%d');" % ((i + 1), j, (i + 1), j))

            exec("c_%d_%d=Mult.Wire('c_%d_%d');" % ((i + 1), j, (i + 1), j))

    for j in range(M - 2):
        exec("c_%d_%d=Mult.Wire('c_%d_%d');" % (N, j, N, j))

    ##    a1=Mult.Wire('a1');
    ##    a2=Mult.Wire('a2');
    ##    a3=Mult.Wire('a3');
    ##    a4=Mult.Wire('a4');
    ##    a5=Mult.Wire('a5');
    ##    a6=Mult.Wire('a6');
    ##    a7=Mult.Wire('a7');
    ##    a8=Mult.Wire('a8');
    ##    a9=Mult.Wire('a9');
    ##    a10=Mult.Wire('a10');
    ##    a11=Mult.Wire('a11');
    ##    a12=Mult.Wire('a12');
    ##    a13=Mult.Wire('a13');
    ##
    ##    b1=Mult.Wire('b1');
    ##    b2=Mult.Wire('b2');
    ##    b3=Mult.Wire('b3');
    ##    b4=Mult.Wire('b4');
    ##    b5=Mult.Wire('b5');
    ##    b6=Mult.Wire('b6');
    ##    b7=Mult.Wire('b7');
    ##    b8=Mult.Wire('b8');
    ##    b9=Mult.Wire('b9');
    ##    b10=Mult.Wire('b10');
    ##    b11=Mult.Wire('b11');
    ##    b12=Mult.Wire('b12');
    ##    b13=Mult.Wire('b13');
    ##
    ##    c1=Mult.Wire('c1');
    ##    c2=Mult.Wire('c2');
    ##    c3=Mult.Wire('c3');
    ##    c4=Mult.Wire('c4');
    ##    c5=Mult.Wire('c5');
    ##    c6=Mult.Wire('c6');
    ##    c7=Mult.Wire('c7');
    ##    c8=Mult.Wire('c8');
    ##    c9=Mult.Wire('c9');
    ##    c10=Mult.Wire('c10');
    ##    c11=Mult.Wire('c11');
    ##    c12=Mult.Wire('c12');
    ##    c13=Mult.Wire('c13');
    ##
    ##    d1=Mult.Wire('d1');
    ##    d2=Mult.Wire('d2');
    ##    d3=Mult.Wire('d3');
    ##    d4=Mult.Wire('d4');
    ##    d5=Mult.Wire('d5');
    ##    d6=Mult.Wire('d6');
    ##    d7=Mult.Wire('d7');
    ##    d8=Mult.Wire('d8');
    ##    d9=Mult.Wire('d9');
    ##    d10=Mult.Wire('d10');
    ##    d11=Mult.Wire('d11');
    ##    d12=Mult.Wire('d12');
    ##    d13=Mult.Wire('d13');
    ##
    ##    e1=Mult.Wire('e1');
    ##    e2=Mult.Wire('e2');
    ##    e3=Mult.Wire('e3');
    ##    e4=Mult.Wire('e4');
    ##    e5=Mult.Wire('e5');
    ##    e6=Mult.Wire('e6');
    ##    e7=Mult.Wire('e7');
    ##    e8=Mult.Wire('e8');
    ##    e9=Mult.Wire('e9');
    ##    e10=Mult.Wire('e10');
    ##    e11=Mult.Wire('e11');
    ##    e12=Mult.Wire('e12');
    ##    e13=Mult.Wire('e13');
    ##
    ##    f1=Mult.Wire('f1');
    ##    f2=Mult.Wire('f2');
    ##    f3=Mult.Wire('f3');
    ##    f4=Mult.Wire('f4');
    ##    f5=Mult.Wire('f5');
    ##    f6=Mult.Wire('f6');
    ##    f7=Mult.Wire('f7');
    ##    f8=Mult.Wire('f8');
    ##    f9=Mult.Wire('f9');
    ##    f10=Mult.Wire('f10');
    ##    f11=Mult.Wire('f11');
    ##    f12=Mult.Wire('f12');
    ##    f13=Mult.Wire('f13');
    ##
    ##    g1=Mult.Wire('g1');
    ##    g2=Mult.Wire('g2');
    ##    g3=Mult.Wire('g3');
    ##    g4=Mult.Wire('g4');
    ##    g5=Mult.Wire('g5');
    ##    g6=Mult.Wire('g6');
    ##    g7=Mult.Wire('g7');
    ##    g8=Mult.Wire('g8');
    ##    g9=Mult.Wire('g9');
    ##    g10=Mult.Wire('g10');
    ##    g11=Mult.Wire('g11');
    ##    g12=Mult.Wire('g12');
    ##    g13=Mult.Wire('g13');
    ##
    ##    h1=Mult.Wire('h1');
    ##    h2=Mult.Wire('h2');
    ##    h3=Mult.Wire('h3');
    ##    h4=Mult.Wire('h4');
    ##    h5=Mult.Wire('h5');
    ##    h6=Mult.Wire('h6');

    for i in range(M):
        for j in range(N):
            if i == 0 and j == 0:
                Mult.Instance(AndModule, "and_0_0", ports=[res[0], a[0], b[0]])
            else:
                exec(
                    "Mult.Instance(AndModule,'and_%d_%d',ports=[w%d_%d,a[%d],b[%d]]);"
                    % (i, j, i, j, i, j)
                )

    ##    Mult.Instance(AndModule,'i1',ports=[w01,a[0],b[1]]);
    ##    Mult.Instance(AndModule,'i2',ports=[w10,a[1],b[0]]);
    ##    Mult.Instance(AndModule,'i3',ports=[w11,a[1],b[1]]);
    ##    Mult.Instance(AndModule,'i4',ports=[w20,a[2],b[0]]);
    ##    Mult.Instance(AndModule,'i5',ports=[w21,a[2],b[1]]);
    ##    Mult.Instance(AndModule,'i6',ports=[w30,a[3],b[0]]);
    ##    Mult.Instance(AndModule,'i7',ports=[w31,a[3],b[1]]);
    ##    Mult.Instance(AndModule,'i8',ports=[w40,a[4],b[0]]);
    ##    Mult.Instance(AndModule,'i9',ports=[w41,a[4],b[1]]);
    ##    Mult.Instance(AndModule,'i10',ports=[w50,a[5],b[0]]);
    ##    Mult.Instance(AndModule,'i11',ports=[w51,a[5],b[1]]);
    ##    Mult.Instance(AndModule,'i12',ports=[w60,a[6],b[0]]);
    ##    Mult.Instance(AndModule,'i13',ports=[w61,a[6],b[1]]);
    ##    Mult.Instance(AndModule,'i14',ports=[w70,a[7],b[0]]);
    ##
    ##    Mult.Instance(AndModule,'li1',ports=[w02,a[0],b[2]]);
    ##    Mult.Instance(AndModule,'li2',ports=[w12,a[1],b[2]]);
    ##    Mult.Instance(AndModule,'li3',ports=[w22,a[2],b[2]]);
    ##    Mult.Instance(AndModule,'li4',ports=[w32,a[3],b[2]]);
    ##    Mult.Instance(AndModule,'li5',ports=[w42,a[4],b[2]]);
    ##    Mult.Instance(AndModule,'li6',ports=[w52,a[5],b[2]]);
    ##    Mult.Instance(AndModule,'li7',ports=[w62,a[6],b[2]]);
    ##    Mult.Instance(AndModule,'li8',ports=[w71,a[7],b[1]]);
    ##
    ##    Mult.Instance(AndModule,'gi1',ports=[w03,a[0],b[3]]);
    ##    Mult.Instance(AndModule,'gi2',ports=[w13,a[1],b[3]]);
    ##    Mult.Instance(AndModule,'gi3',ports=[w23,a[2],b[3]]);
    ##    Mult.Instance(AndModule,'gi4',ports=[w33,a[3],b[3]]);
    ##    Mult.Instance(AndModule,'gi5',ports=[w43,a[4],b[3]]);
    ##    Mult.Instance(AndModule,'gi6',ports=[w53,a[5],b[3]]);
    ##    Mult.Instance(AndModule,'gi7',ports=[w63,a[6],b[3]]);
    ##    Mult.Instance(AndModule,'gi8',ports=[w72,a[7],b[2]]);
    ##
    ##    Mult.Instance(AndModule,'hi1',ports=[w04,a[0],b[4]]);
    ##    Mult.Instance(AndModule,'hi2',ports=[w14,a[1],b[4]]);
    ##    Mult.Instance(AndModule,'hi3',ports=[w24,a[2],b[4]]);
    ##    Mult.Instance(AndModule,'hi4',ports=[w34,a[3],b[4]]);
    ##    Mult.Instance(AndModule,'hi5',ports=[w44,a[4],b[4]]);
    ##    Mult.Instance(AndModule,'hi6',ports=[w54,a[5],b[4]]);
    ##    Mult.Instance(AndModule,'hi7',ports=[w64,a[6],b[4]]);
    ##    Mult.Instance(AndModule,'hi8',ports=[w73,a[7],b[3]]);
    ##
    ##    Mult.Instance(AndModule,'ii1',ports=[w05,a[0],b[5]]);
    ##    Mult.Instance(AndModule,'ii2',ports=[w15,a[1],b[5]]);
    ##    Mult.Instance(AndModule,'ii3',ports=[w25,a[2],b[5]]);
    ##    Mult.Instance(AndModule,'ii4',ports=[w35,a[3],b[5]]);
    ##    Mult.Instance(AndModule,'ii5',ports=[w45,a[4],b[5]]);
    ##    Mult.Instance(AndModule,'ii6',ports=[w55,a[5],b[5]]);
    ##    Mult.Instance(AndModule,'ii7',ports=[w65,a[6],b[5]]);
    ##    Mult.Instance(AndModule,'ii8',ports=[w74,a[7],b[4]]);
    ##
    ##    Mult.Instance(AndModule,'ji1',ports=[w06,a[0],b[6]]);
    ##    Mult.Instance(AndModule,'ji2',ports=[w16,a[1],b[6]]);
    ##    Mult.Instance(AndModule,'ji3',ports=[w26,a[2],b[6]]);
    ##    Mult.Instance(AndModule,'ji4',ports=[w36,a[3],b[6]]);
    ##    Mult.Instance(AndModule,'ji5',ports=[w46,a[4],b[6]]);
    ##    Mult.Instance(AndModule,'ji6',ports=[w56,a[5],b[6]]);
    ##    Mult.Instance(AndModule,'ji7',ports=[w66,a[6],b[6]]);
    ##    Mult.Instance(AndModule,'ji8',ports=[w75,a[7],b[5]]);
    ##
    ##    Mult.Instance(AndModule,'ki1',ports=[w07,a[0],b[7]]);
    ##    Mult.Instance(AndModule,'ki2',ports=[w17,a[1],b[7]]);
    ##    Mult.Instance(AndModule,'ki3',ports=[w27,a[2],b[7]]);
    ##    Mult.Instance(AndModule,'ki4',ports=[w37,a[3],b[7]]);
    ##    Mult.Instance(AndModule,'ki5',ports=[w47,a[4],b[7]]);
    ##    Mult.Instance(AndModule,'ki6',ports=[w57,a[5],b[7]]);
    ##    Mult.Instance(AndModule,'ki7',ports=[w67,a[6],b[7]]);
    ##    Mult.Instance(AndModule,'ki8',ports=[w76,a[7],b[6]]);
    ##
    ##
    ##    Mult.Instance(AndModule,'mi1',ports=[w77,a[7],b[7]]);
    ##    Mult.Instance(AndModule,'mi2',ports=[res[0],a[0],b[0]]);

    for j in range(1, N + 1):
        for i in range(1, M):
            if j == 1:
                if i == 1:
                    exec(
                        "Mult.Instance(HalfAdderModule,'ha%d',ports=[w%d_0,w%d_1,res[1],c_1_%d]);"
                        % (i, i, i - 1, i - 1)
                    )
                else:
                    exec(
                        "Mult.Instance(HalfAdderModule,'ha%d',ports=[w%d_0,w%d_1,s_1_%d,c_1_%d]);"
                        % (i, i, i - 1, i - 1, i - 1)
                    )
            elif j != N:
                if i == 1:
                    exec(
                        "Mult.Instance(FullAdderModule,'fa%d_%d',ports=[c_%d_%d,s_%d_%d,w%d_%d,res[%d],c_%d_%d]);"
                        % (i, j, j - 1, i - 1, j - 1, i, i - 1, j, j, j, i - 1)
                    )
                elif i != (M - 1):
                    exec(
                        "Mult.Instance(FullAdderModule,'fa%d_%d',ports=[c_%d_%d,s_%d_%d,w%d_%d,s_%d_%d,c_%d_%d]);"
                        % (i, j, j - 1, i - 1, j - 1, i, i - 1, j, j, i - 1, j, i - 1)
                    )
                else:
                    exec(
                        "Mult.Instance(FullAdderModule,'fa%d_%d',ports=[c_%d_%d,w%d_%d,w%d_%d,s_%d_%d,c_%d_%d]);"
                        % (i, j, j - 1, i - 1, i, j - 1, i - 1, j, j, i - 1, j, i - 1)
                    )
            else:
                if i == 1:
                    exec(
                        "Mult.Instance(HalfAdderModule,'hadd',ports=[c_%d_%d,s_%d_%d,res[%d],c_%d_%d]);"
                        % (j - 1, i - 1, j - 1, i, j + i - 1, j, i - 1)
                    )
                elif i != (M - 1):
                    exec(
                        "Mult.Instance(FullAdderModule,'fadd%d',ports=[c_%d_%d,s_%d_%d,c_%d_%d,res[%d],c_%d_%d]);"
                        % (i - 1, j - 1, i - 1, j - 1, i, j, i - 2, j + i - 1, j, i - 1)
                    )
                else:
                    exec(
                        "Mult.Instance(FullAdderModule,'fadd%d',ports=[c_%d_%d,w%d_%d,c_%d_%d,res[%d],res[%d]]);"
                        % (i - 1, j - 1, i - 1, i, j - 1, j, i - 2, j + i - 1, j + i)
                    )

    ##    Mult.Instance(HalfAdderModule,'ha1',ports=[w10,w01,res[1],a1]);
    ##    Mult.Instance(HalfAdderModule,'ha2',ports=[w20,w11,a2,a3]);
    ##    Mult.Instance(HalfAdderModule,'ha3',ports=[w30,w21,a4,a5]);
    ##    Mult.Instance(HalfAdderModule,'ha4',ports=[w40,w31,a6,a7]);
    ##    Mult.Instance(HalfAdderModule,'ha5',ports=[w50,w41,a8,a9]);
    ##    Mult.Instance(HalfAdderModule,'ha6',ports=[w60,w51,a10,a11]);
    ##    Mult.Instance(HalfAdderModule,'ha7',ports=[w70,w61,a12,a13]);
    ##
    ##    Mult.Instance(FullAdderModule,'afa1',ports=[a1,a2,w02,res[2],b1]);
    ##    Mult.Instance(FullAdderModule,'afa2',ports=[a3,a4,w12,b2,b3]);
    ##    Mult.Instance(FullAdderModule,'afa3',ports=[a5,a6,w22,b4,b5]);
    ##    Mult.Instance(FullAdderModule,'afa4',ports=[a7,a8,w32,b6,b7]);
    ##    Mult.Instance(FullAdderModule,'afa5',ports=[a9,a10,w42,b8,b9]);
    ##    Mult.Instance(FullAdderModule,'afa6',ports=[a11,a12,w52,b10,b11]);
    ##    Mult.Instance(FullAdderModule,'afa7',ports=[a13,w71,w62,b12,b13]);
    ##
    ##    Mult.Instance(FullAdderModule,'bfa1',ports=[b1,b2,w03,res[3],c1]);
    ##    Mult.Instance(FullAdderModule,'bfa2',ports=[b3,b4,w13,c2,c3]);
    ##    Mult.Instance(FullAdderModule,'bfa3',ports=[b5,b6,w23,c4,c5]);
    ##    Mult.Instance(FullAdderModule,'bfa4',ports=[b7,b8,w33,c6,c7]);
    ##    Mult.Instance(FullAdderModule,'bfa5',ports=[b9,b10,w43,c8,c9]);
    ##    Mult.Instance(FullAdderModule,'bfa6',ports=[b11,b12,w53,c10,c11]);
    ##    Mult.Instance(FullAdderModule,'bfa7',ports=[b13,w72,w63,c12,c13]);
    ##
    ##    Mult.Instance(FullAdderModule,'cfa1',ports=[c1,c2,w04,res[4],d1]);
    ##    Mult.Instance(FullAdderModule,'cfa2',ports=[c3,c4,w14,d2,d3]);
    ##    Mult.Instance(FullAdderModule,'cfa3',ports=[c5,c6,w24,d4,d5]);
    ##    Mult.Instance(FullAdderModule,'cfa4',ports=[c7,c8,w34,d6,d7]);
    ##    Mult.Instance(FullAdderModule,'cfa5',ports=[c9,c10,w44,d8,d9]);
    ##    Mult.Instance(FullAdderModule,'cfa6',ports=[c11,c12,w54,d10,d11]);
    ##    Mult.Instance(FullAdderModule,'cfa7',ports=[c13,w73,w64,d12,d13]);
    ##
    ##    Mult.Instance(FullAdderModule,'dfa1',ports=[d1,d2,w05,res[5],e1]);
    ##    Mult.Instance(FullAdderModule,'dfa2',ports=[d3,d4,w15,e2,e3]);
    ##    Mult.Instance(FullAdderModule,'dfa3',ports=[d5,d6,w25,e4,e5]);
    ##    Mult.Instance(FullAdderModule,'dfa4',ports=[d7,d8,w35,e6,e7]);
    ##    Mult.Instance(FullAdderModule,'dfa5',ports=[d9,d10,w45,e8,e9]);
    ##    Mult.Instance(FullAdderModule,'dfa6',ports=[d11,d12,w55,e10,e11]);
    ##    Mult.Instance(FullAdderModule,'dfa7',ports=[d13,w74,w65,e12,e13]);
    ##
    ##    Mult.Instance(FullAdderModule,'efa1',ports=[e1,e2,w06,res[6],f1]);
    ##    Mult.Instance(FullAdderModule,'efa2',ports=[e3,e4,w16,f2,f3]);
    ##    Mult.Instance(FullAdderModule,'efa3',ports=[e5,e6,w26,f4,f5]);
    ##    Mult.Instance(FullAdderModule,'efa4',ports=[e7,e8,w36,f6,f7]);
    ##    Mult.Instance(FullAdderModule,'efa5',ports=[e9,e10,w46,f8,f9]);
    ##    Mult.Instance(FullAdderModule,'efa6',ports=[e11,e12,w56,f10,f11]);
    ##    Mult.Instance(FullAdderModule,'efa7',ports=[e13,w75,w66,f12,f13]);
    ##
    ##    Mult.Instance(FullAdderModule,'ffa1',ports=[f1,f2,w07,res[7],g1]);
    ##    Mult.Instance(FullAdderModule,'ffa2',ports=[f3,f4,w17,g2,g3]);
    ##    Mult.Instance(FullAdderModule,'ffa3',ports=[f5,f6,w27,g4,g5]);
    ##    Mult.Instance(FullAdderModule,'ffa4',ports=[f7,f8,w37,g6,g7]);
    ##    Mult.Instance(FullAdderModule,'ffa5',ports=[f9,f10,w47,g8,g9]);
    ##    Mult.Instance(FullAdderModule,'ffa6',ports=[f11,f12,w57,g10,g11]);
    ##    Mult.Instance(FullAdderModule,'ffa7',ports=[f13,w76,w67,g12,g13]);
    ##
    ##    Mult.Instance(HalfAdderModule,'had1',ports=[g1,g2,res[8],h1]);
    ##    Mult.Instance(FullAdderModule,'fad1',ports=[g3,g4,h1,res[9],h2]);
    ##    Mult.Instance(FullAdderModule,'fad2',ports=[g5,g6,h2,res[10],h3]);
    ##    Mult.Instance(FullAdderModule,'fad3',ports=[g7,g8,h3,res[11],h4]);
    ##    Mult.Instance(FullAdderModule,'fad4',ports=[g9,g10,h4,res[12],h5]);
    ##    Mult.Instance(FullAdderModule,'fad5',ports=[g11,g12,h5,res[13],h6]);
    ##    Mult.Instance(FullAdderModule,'fad6',ports=[w77,g13,h6,res[14],res[15]]);

    return Mult


def PAAM01_V_cut_MxN_binary_array_multiplier(
    M, N, V_cut
):  # Accurate MxN Binary Array Multiplier
    # Remember to use constraint M>=3 and N>=3
    # V_cut should be integer between 0 and M inclusive

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam_01_V_" + str(V_cut) + "_" + str(M) + "x" + str(N))
    a = Mult.Input("a", M)
    b = Mult.Input("b", N)
    res = Mult.Output("p", M + N)

    for i in range(N):
        for j in range(M):
            if i + j > V_cut:
                exec("w%d_%d = Mult.Wire('w%d_%d');" % (j, i, j, i))

    ##    w10=Mult.Wire('w10');
    ##    w20=Mult.Wire('w20');
    ##    w30=Mult.Wire('w30');
    ##    w40=Mult.Wire('w40');
    ##    w50=Mult.Wire('w50');
    ##    w60=Mult.Wire('w60');
    ##    w70=Mult.Wire('w70');
    ##
    ##    w01=Mult.Wire('w01');
    ##    w11=Mult.Wire('w11');
    ##    w21=Mult.Wire('w21');
    ##    w31=Mult.Wire('w31');
    ##    w41=Mult.Wire('w41');
    ##    w51=Mult.Wire('w51');
    ##    w61=Mult.Wire('w61');
    ##    w71=Mult.Wire('w71');
    ##
    ##    w02=Mult.Wire('w02');
    ##    w12=Mult.Wire('w12');
    ##    w22=Mult.Wire('w22');
    ##    w32=Mult.Wire('w32');
    ##    w42=Mult.Wire('w42');
    ##    w52=Mult.Wire('w52');
    ##    w62=Mult.Wire('w62');
    ##    w72=Mult.Wire('w72');
    ##
    ##    w03=Mult.Wire('w03');
    ##    w13=Mult.Wire('w13');
    ##    w23=Mult.Wire('w23');
    ##    w33=Mult.Wire('w33');
    ##    w43=Mult.Wire('w43');
    ##    w53=Mult.Wire('w53');
    ##    w63=Mult.Wire('w63');
    ##    w73=Mult.Wire('w73');
    ##
    ##    w04=Mult.Wire('w04');
    ##    w14=Mult.Wire('w14');
    ##    w24=Mult.Wire('w24');
    ##    w34=Mult.Wire('w34');
    ##    w44=Mult.Wire('w44');
    ##    w54=Mult.Wire('w54');
    ##    w64=Mult.Wire('w64');
    ##    w74=Mult.Wire('w74');
    ##
    ##    w05=Mult.Wire('w05');
    ##    w15=Mult.Wire('w15');
    ##    w25=Mult.Wire('w25');
    ##    w35=Mult.Wire('w35');
    ##    w45=Mult.Wire('w45');
    ##    w55=Mult.Wire('w55');
    ##    w65=Mult.Wire('w65');
    ##    w75=Mult.Wire('w75');
    ##
    ##    w06=Mult.Wire('w06');
    ##    w16=Mult.Wire('w16');
    ##    w26=Mult.Wire('w26');
    ##    w36=Mult.Wire('w36');
    ##    w46=Mult.Wire('w46');
    ##    w56=Mult.Wire('w56');
    ##    w66=Mult.Wire('w66');
    ##    w76=Mult.Wire('w76');
    ##
    ##    w07=Mult.Wire('w07');
    ##    w17=Mult.Wire('w17');
    ##    w27=Mult.Wire('w27');
    ##    w37=Mult.Wire('w37');
    ##    w47=Mult.Wire('w47');
    ##    w57=Mult.Wire('w57');
    ##    w67=Mult.Wire('w67');
    ##    w77=Mult.Wire('w77');

    for i in range(N - 1):
        for j in range(M - 1):
            if (i + 1 + j) > V_cut:
                if j != 0:
                    exec("s_%d_%d=Mult.Wire('s_%d_%d');" % ((i + 1), j, (i + 1), j))

                exec("c_%d_%d=Mult.Wire('c_%d_%d');" % ((i + 1), j, (i + 1), j))

    for j in range(M - 2):
        if (N + j) > V_cut + 1:  # Final layer of Multiplier reacts differently to V_cut
            exec("c_%d_%d=Mult.Wire('c_%d_%d');" % (N, j, N, j))

    ##    a1=Mult.Wire('a1');
    ##    a2=Mult.Wire('a2');
    ##    a3=Mult.Wire('a3');
    ##    a4=Mult.Wire('a4');
    ##    a5=Mult.Wire('a5');
    ##    a6=Mult.Wire('a6');
    ##    a7=Mult.Wire('a7');
    ##    a8=Mult.Wire('a8');
    ##    a9=Mult.Wire('a9');
    ##    a10=Mult.Wire('a10');
    ##    a11=Mult.Wire('a11');
    ##    a12=Mult.Wire('a12');
    ##    a13=Mult.Wire('a13');
    ##
    ##    b1=Mult.Wire('b1');
    ##    b2=Mult.Wire('b2');
    ##    b3=Mult.Wire('b3');
    ##    b4=Mult.Wire('b4');
    ##    b5=Mult.Wire('b5');
    ##    b6=Mult.Wire('b6');
    ##    b7=Mult.Wire('b7');
    ##    b8=Mult.Wire('b8');
    ##    b9=Mult.Wire('b9');
    ##    b10=Mult.Wire('b10');
    ##    b11=Mult.Wire('b11');
    ##    b12=Mult.Wire('b12');
    ##    b13=Mult.Wire('b13');
    ##
    ##    c1=Mult.Wire('c1');
    ##    c2=Mult.Wire('c2');
    ##    c3=Mult.Wire('c3');
    ##    c4=Mult.Wire('c4');
    ##    c5=Mult.Wire('c5');
    ##    c6=Mult.Wire('c6');
    ##    c7=Mult.Wire('c7');
    ##    c8=Mult.Wire('c8');
    ##    c9=Mult.Wire('c9');
    ##    c10=Mult.Wire('c10');
    ##    c11=Mult.Wire('c11');
    ##    c12=Mult.Wire('c12');
    ##    c13=Mult.Wire('c13');
    ##
    ##    d1=Mult.Wire('d1');
    ##    d2=Mult.Wire('d2');
    ##    d3=Mult.Wire('d3');
    ##    d4=Mult.Wire('d4');
    ##    d5=Mult.Wire('d5');
    ##    d6=Mult.Wire('d6');
    ##    d7=Mult.Wire('d7');
    ##    d8=Mult.Wire('d8');
    ##    d9=Mult.Wire('d9');
    ##    d10=Mult.Wire('d10');
    ##    d11=Mult.Wire('d11');
    ##    d12=Mult.Wire('d12');
    ##    d13=Mult.Wire('d13');
    ##
    ##    e1=Mult.Wire('e1');
    ##    e2=Mult.Wire('e2');
    ##    e3=Mult.Wire('e3');
    ##    e4=Mult.Wire('e4');
    ##    e5=Mult.Wire('e5');
    ##    e6=Mult.Wire('e6');
    ##    e7=Mult.Wire('e7');
    ##    e8=Mult.Wire('e8');
    ##    e9=Mult.Wire('e9');
    ##    e10=Mult.Wire('e10');
    ##    e11=Mult.Wire('e11');
    ##    e12=Mult.Wire('e12');
    ##    e13=Mult.Wire('e13');
    ##
    ##    f1=Mult.Wire('f1');
    ##    f2=Mult.Wire('f2');
    ##    f3=Mult.Wire('f3');
    ##    f4=Mult.Wire('f4');
    ##    f5=Mult.Wire('f5');
    ##    f6=Mult.Wire('f6');
    ##    f7=Mult.Wire('f7');
    ##    f8=Mult.Wire('f8');
    ##    f9=Mult.Wire('f9');
    ##    f10=Mult.Wire('f10');
    ##    f11=Mult.Wire('f11');
    ##    f12=Mult.Wire('f12');
    ##    f13=Mult.Wire('f13');
    ##
    ##    g1=Mult.Wire('g1');
    ##    g2=Mult.Wire('g2');
    ##    g3=Mult.Wire('g3');
    ##    g4=Mult.Wire('g4');
    ##    g5=Mult.Wire('g5');
    ##    g6=Mult.Wire('g6');
    ##    g7=Mult.Wire('g7');
    ##    g8=Mult.Wire('g8');
    ##    g9=Mult.Wire('g9');
    ##    g10=Mult.Wire('g10');
    ##    g11=Mult.Wire('g11');
    ##    g12=Mult.Wire('g12');
    ##    g13=Mult.Wire('g13');
    ##
    ##    h1=Mult.Wire('h1');
    ##    h2=Mult.Wire('h2');
    ##    h3=Mult.Wire('h3');
    ##    h4=Mult.Wire('h4');
    ##    h5=Mult.Wire('h5');
    ##    h6=Mult.Wire('h6');

    for i in range(V_cut + 1):
        res[i].assign(1)
    ##    res[0].assign(1);

    for i in range(M):
        for j in range(N):
            if (i + j) > V_cut:
                exec(
                    "Mult.Instance(AndModule,'and_%d_%d',ports=[w%d_%d,a[%d],b[%d]]);"
                    % (i, j, i, j, i, j)
                )

    ##    Mult.Instance(AndModule,'i1',ports=[w01,a[0],b[1]]);
    ##    Mult.Instance(AndModule,'i2',ports=[w10,a[1],b[0]]);
    ##    Mult.Instance(AndModule,'i3',ports=[w11,a[1],b[1]]);
    ##    Mult.Instance(AndModule,'i4',ports=[w20,a[2],b[0]]);
    ##    Mult.Instance(AndModule,'i5',ports=[w21,a[2],b[1]]);
    ##    Mult.Instance(AndModule,'i6',ports=[w30,a[3],b[0]]);
    ##    Mult.Instance(AndModule,'i7',ports=[w31,a[3],b[1]]);
    ##    Mult.Instance(AndModule,'i8',ports=[w40,a[4],b[0]]);
    ##    Mult.Instance(AndModule,'i9',ports=[w41,a[4],b[1]]);
    ##    Mult.Instance(AndModule,'i10',ports=[w50,a[5],b[0]]);
    ##    Mult.Instance(AndModule,'i11',ports=[w51,a[5],b[1]]);
    ##    Mult.Instance(AndModule,'i12',ports=[w60,a[6],b[0]]);
    ##    Mult.Instance(AndModule,'i13',ports=[w61,a[6],b[1]]);
    ##    Mult.Instance(AndModule,'i14',ports=[w70,a[7],b[0]]);
    ##
    ##    Mult.Instance(AndModule,'li1',ports=[w02,a[0],b[2]]);
    ##    Mult.Instance(AndModule,'li2',ports=[w12,a[1],b[2]]);
    ##    Mult.Instance(AndModule,'li3',ports=[w22,a[2],b[2]]);
    ##    Mult.Instance(AndModule,'li4',ports=[w32,a[3],b[2]]);
    ##    Mult.Instance(AndModule,'li5',ports=[w42,a[4],b[2]]);
    ##    Mult.Instance(AndModule,'li6',ports=[w52,a[5],b[2]]);
    ##    Mult.Instance(AndModule,'li7',ports=[w62,a[6],b[2]]);
    ##    Mult.Instance(AndModule,'li8',ports=[w71,a[7],b[1]]);
    ##
    ##    Mult.Instance(AndModule,'gi1',ports=[w03,a[0],b[3]]);
    ##    Mult.Instance(AndModule,'gi2',ports=[w13,a[1],b[3]]);
    ##    Mult.Instance(AndModule,'gi3',ports=[w23,a[2],b[3]]);
    ##    Mult.Instance(AndModule,'gi4',ports=[w33,a[3],b[3]]);
    ##    Mult.Instance(AndModule,'gi5',ports=[w43,a[4],b[3]]);
    ##    Mult.Instance(AndModule,'gi6',ports=[w53,a[5],b[3]]);
    ##    Mult.Instance(AndModule,'gi7',ports=[w63,a[6],b[3]]);
    ##    Mult.Instance(AndModule,'gi8',ports=[w72,a[7],b[2]]);
    ##
    ##    Mult.Instance(AndModule,'hi1',ports=[w04,a[0],b[4]]);
    ##    Mult.Instance(AndModule,'hi2',ports=[w14,a[1],b[4]]);
    ##    Mult.Instance(AndModule,'hi3',ports=[w24,a[2],b[4]]);
    ##    Mult.Instance(AndModule,'hi4',ports=[w34,a[3],b[4]]);
    ##    Mult.Instance(AndModule,'hi5',ports=[w44,a[4],b[4]]);
    ##    Mult.Instance(AndModule,'hi6',ports=[w54,a[5],b[4]]);
    ##    Mult.Instance(AndModule,'hi7',ports=[w64,a[6],b[4]]);
    ##    Mult.Instance(AndModule,'hi8',ports=[w73,a[7],b[3]]);
    ##
    ##    Mult.Instance(AndModule,'ii1',ports=[w05,a[0],b[5]]);
    ##    Mult.Instance(AndModule,'ii2',ports=[w15,a[1],b[5]]);
    ##    Mult.Instance(AndModule,'ii3',ports=[w25,a[2],b[5]]);
    ##    Mult.Instance(AndModule,'ii4',ports=[w35,a[3],b[5]]);
    ##    Mult.Instance(AndModule,'ii5',ports=[w45,a[4],b[5]]);
    ##    Mult.Instance(AndModule,'ii6',ports=[w55,a[5],b[5]]);
    ##    Mult.Instance(AndModule,'ii7',ports=[w65,a[6],b[5]]);
    ##    Mult.Instance(AndModule,'ii8',ports=[w74,a[7],b[4]]);
    ##
    ##    Mult.Instance(AndModule,'ji1',ports=[w06,a[0],b[6]]);
    ##    Mult.Instance(AndModule,'ji2',ports=[w16,a[1],b[6]]);
    ##    Mult.Instance(AndModule,'ji3',ports=[w26,a[2],b[6]]);
    ##    Mult.Instance(AndModule,'ji4',ports=[w36,a[3],b[6]]);
    ##    Mult.Instance(AndModule,'ji5',ports=[w46,a[4],b[6]]);
    ##    Mult.Instance(AndModule,'ji6',ports=[w56,a[5],b[6]]);
    ##    Mult.Instance(AndModule,'ji7',ports=[w66,a[6],b[6]]);
    ##    Mult.Instance(AndModule,'ji8',ports=[w75,a[7],b[5]]);
    ##
    ##    Mult.Instance(AndModule,'ki1',ports=[w07,a[0],b[7]]);
    ##    Mult.Instance(AndModule,'ki2',ports=[w17,a[1],b[7]]);
    ##    Mult.Instance(AndModule,'ki3',ports=[w27,a[2],b[7]]);
    ##    Mult.Instance(AndModule,'ki4',ports=[w37,a[3],b[7]]);
    ##    Mult.Instance(AndModule,'ki5',ports=[w47,a[4],b[7]]);
    ##    Mult.Instance(AndModule,'ki6',ports=[w57,a[5],b[7]]);
    ##    Mult.Instance(AndModule,'ki7',ports=[w67,a[6],b[7]]);
    ##    Mult.Instance(AndModule,'ki8',ports=[w76,a[7],b[6]]);
    ##
    ##
    ##    Mult.Instance(AndModule,'mi1',ports=[w77,a[7],b[7]]);
    ##    Mult.Instance(AndModule,'mi2',ports=[res[0],a[0],b[0]]);
    V_cut_flag = 0
    for j in range(1, N + 1):
        for i in range(1, M):
            if (i + j - 1) > V_cut:
                if j == 1:
                    if i == 1:
                        exec(
                            "Mult.Instance(HalfAdderModule,'ha%d',ports=[w%d_0,w%d_1,res[1],c_1_%d]);"
                            % (i, i, i - 1, i - 1)
                        )
                    else:
                        exec(
                            "Mult.Instance(HalfAdderModule,'ha%d',ports=[w%d_0,w%d_1,s_1_%d,c_1_%d]);"
                            % (i, i, i - 1, i - 1, i - 1)
                        )
                elif j != N:
                    if (i + j - 2) == V_cut:
                        if i == 1:
                            exec(
                                "Mult.Instance(HalfAdderModule,'ha%d_%d',ports=[s_%d_%d,w%d_%d,res[%d],c_%d_%d]);"
                                % (i, j, j - 1, i, i - 1, j, j, j, i - 1)
                            )
                        elif i != (M - 1):
                            exec(
                                "Mult.Instance(HalfAdderModule,'ha%d_%d',ports=[s_%d_%d,w%d_%d,s_%d_%d,c_%d_%d]);"
                                % (i, j, j - 1, i, i - 1, j, j, i - 1, j, i - 1)
                            )
                        else:
                            exec(
                                "Mult.Instance(HalfAdderModule,'ha%d_%d',ports=[w%d_%d,w%d_%d,s_%d_%d,c_%d_%d]);"
                                % (i, j, i, j - 1, i - 1, j, j, i - 1, j, i - 1)
                            )
                    else:
                        if i == 1:
                            exec(
                                "Mult.Instance(FullAdderModule,'fa%d_%d',ports=[c_%d_%d,s_%d_%d,w%d_%d,res[%d],c_%d_%d]);"
                                % (i, j, j - 1, i - 1, j - 1, i, i - 1, j, j, j, i - 1)
                            )
                        elif i != (M - 1):
                            exec(
                                "Mult.Instance(FullAdderModule,'fa%d_%d',ports=[c_%d_%d,s_%d_%d,w%d_%d,s_%d_%d,c_%d_%d]);"
                                % (
                                    i,
                                    j,
                                    j - 1,
                                    i - 1,
                                    j - 1,
                                    i,
                                    i - 1,
                                    j,
                                    j,
                                    i - 1,
                                    j,
                                    i - 1,
                                )
                            )
                        else:
                            exec(
                                "Mult.Instance(FullAdderModule,'fa%d_%d',ports=[c_%d_%d,w%d_%d,w%d_%d,s_%d_%d,c_%d_%d]);"
                                % (
                                    i,
                                    j,
                                    j - 1,
                                    i - 1,
                                    i,
                                    j - 1,
                                    i - 1,
                                    j,
                                    j,
                                    i - 1,
                                    j,
                                    i - 1,
                                )
                            )
                else:
                    if (i + j - 2) == V_cut:
                        V_cut_flag = 1
                        if i == 1:
                            exec("res[%d].assign(s_%d_%d);" % (j + i - 1, j - 1, i))
                            # exec("Mult.Instance(HalfAdderModule,'hadd',ports=[c_%d%d,s_%d%d,res[%d],c_%d%d]);" %(j-1,i-1,j-1,i,j+i-1,j,i-1));
                        elif i != (M - 1):
                            exec("res[%d].assign(s_%d_%d);" % (j + i - 1, j - 1, i))
                            # exec("Mult.Instance(FullAdderModule,'fadd%d',ports=[c_%d%d,s_%d%d,c_%d%d,res[%d],c_%d%d]);" %(i-1,j-1,i-1,j-1,i,j,i-2,j+i-1,j,i-1));
                        else:
                            exec("res[%d].assign(w%d_%d);" % (j + i - 1, i, j - 1))
                            exec("res[%d].assign(0);" % (j + i))
                            # exec("Mult.Instance(FullAdderModule,'fadd%d',ports=[c_%d%d,w%d%d,c_%d%d,res[%d],res[%d]]);" %(i-1,j-1,i-1,i,j-1,j,i-2,j+i-1,j+i));
                    elif V_cut_flag == 1:
                        V_cut_flag = 0
                        if i != (M - 1):
                            exec(
                                "Mult.Instance(HalfAdderModule,'hadd%d',ports=[c_%d_%d,s_%d_%d,res[%d],c_%d_%d]);"
                                % (i - 1, j - 1, i - 1, j - 1, i, j + i - 1, j, i - 1)
                            )
                        else:
                            exec(
                                "Mult.Instance(HalfAdderModule,'hadd%d',ports=[c_%d_%d,w%d_%d,res[%d],res[%d]]);"
                                % (i - 1, j - 1, i - 1, i, j - 1, j + i - 1, j + i)
                            )
                    else:
                        if i == 1:
                            exec(
                                "Mult.Instance(HalfAdderModule,'hadd',ports=[c_%d_%d,s_%d_%d,res[%d],c_%d_%d]);"
                                % (j - 1, i - 1, j - 1, i, j + i - 1, j, i - 1)
                            )
                        elif i != (M - 1):
                            exec(
                                "Mult.Instance(FullAdderModule,'fadd%d',ports=[c_%d_%d,s_%d_%d,c_%d_%d,res[%d],c_%d_%d]);"
                                % (
                                    i - 1,
                                    j - 1,
                                    i - 1,
                                    j - 1,
                                    i,
                                    j,
                                    i - 2,
                                    j + i - 1,
                                    j,
                                    i - 1,
                                )
                            )
                        else:
                            exec(
                                "Mult.Instance(FullAdderModule,'fadd%d',ports=[c_%d_%d,w%d_%d,c_%d_%d,res[%d],res[%d]]);"
                                % (
                                    i - 1,
                                    j - 1,
                                    i - 1,
                                    i,
                                    j - 1,
                                    j,
                                    i - 2,
                                    j + i - 1,
                                    j + i,
                                )
                            )

    ##    Mult.Instance(HalfAdderModule,'ha1',ports=[w10,w01,res[1],a1]);
    ##    Mult.Instance(HalfAdderModule,'ha2',ports=[w20,w11,a2,a3]);
    ##    Mult.Instance(HalfAdderModule,'ha3',ports=[w30,w21,a4,a5]);
    ##    Mult.Instance(HalfAdderModule,'ha4',ports=[w40,w31,a6,a7]);
    ##    Mult.Instance(HalfAdderModule,'ha5',ports=[w50,w41,a8,a9]);
    ##    Mult.Instance(HalfAdderModule,'ha6',ports=[w60,w51,a10,a11]);
    ##    Mult.Instance(HalfAdderModule,'ha7',ports=[w70,w61,a12,a13]);
    ##
    ##    Mult.Instance(FullAdderModule,'afa1',ports=[a1,a2,w02,res[2],b1]);
    ##    Mult.Instance(FullAdderModule,'afa2',ports=[a3,a4,w12,b2,b3]);
    ##    Mult.Instance(FullAdderModule,'afa3',ports=[a5,a6,w22,b4,b5]);
    ##    Mult.Instance(FullAdderModule,'afa4',ports=[a7,a8,w32,b6,b7]);
    ##    Mult.Instance(FullAdderModule,'afa5',ports=[a9,a10,w42,b8,b9]);
    ##    Mult.Instance(FullAdderModule,'afa6',ports=[a11,a12,w52,b10,b11]);
    ##    Mult.Instance(FullAdderModule,'afa7',ports=[a13,w71,w62,b12,b13]);
    ##
    ##    Mult.Instance(FullAdderModule,'bfa1',ports=[b1,b2,w03,res[3],c1]);
    ##    Mult.Instance(FullAdderModule,'bfa2',ports=[b3,b4,w13,c2,c3]);
    ##    Mult.Instance(FullAdderModule,'bfa3',ports=[b5,b6,w23,c4,c5]);
    ##    Mult.Instance(FullAdderModule,'bfa4',ports=[b7,b8,w33,c6,c7]);
    ##    Mult.Instance(FullAdderModule,'bfa5',ports=[b9,b10,w43,c8,c9]);
    ##    Mult.Instance(FullAdderModule,'bfa6',ports=[b11,b12,w53,c10,c11]);
    ##    Mult.Instance(FullAdderModule,'bfa7',ports=[b13,w72,w63,c12,c13]);
    ##
    ##    Mult.Instance(FullAdderModule,'cfa1',ports=[c1,c2,w04,res[4],d1]);
    ##    Mult.Instance(FullAdderModule,'cfa2',ports=[c3,c4,w14,d2,d3]);
    ##    Mult.Instance(FullAdderModule,'cfa3',ports=[c5,c6,w24,d4,d5]);
    ##    Mult.Instance(FullAdderModule,'cfa4',ports=[c7,c8,w34,d6,d7]);
    ##    Mult.Instance(FullAdderModule,'cfa5',ports=[c9,c10,w44,d8,d9]);
    ##    Mult.Instance(FullAdderModule,'cfa6',ports=[c11,c12,w54,d10,d11]);
    ##    Mult.Instance(FullAdderModule,'cfa7',ports=[c13,w73,w64,d12,d13]);
    ##
    ##    Mult.Instance(FullAdderModule,'dfa1',ports=[d1,d2,w05,res[5],e1]);
    ##    Mult.Instance(FullAdderModule,'dfa2',ports=[d3,d4,w15,e2,e3]);
    ##    Mult.Instance(FullAdderModule,'dfa3',ports=[d5,d6,w25,e4,e5]);
    ##    Mult.Instance(FullAdderModule,'dfa4',ports=[d7,d8,w35,e6,e7]);
    ##    Mult.Instance(FullAdderModule,'dfa5',ports=[d9,d10,w45,e8,e9]);
    ##    Mult.Instance(FullAdderModule,'dfa6',ports=[d11,d12,w55,e10,e11]);
    ##    Mult.Instance(FullAdderModule,'dfa7',ports=[d13,w74,w65,e12,e13]);
    ##
    ##    Mult.Instance(FullAdderModule,'efa1',ports=[e1,e2,w06,res[6],f1]);
    ##    Mult.Instance(FullAdderModule,'efa2',ports=[e3,e4,w16,f2,f3]);
    ##    Mult.Instance(FullAdderModule,'efa3',ports=[e5,e6,w26,f4,f5]);
    ##    Mult.Instance(FullAdderModule,'efa4',ports=[e7,e8,w36,f6,f7]);
    ##    Mult.Instance(FullAdderModule,'efa5',ports=[e9,e10,w46,f8,f9]);
    ##    Mult.Instance(FullAdderModule,'efa6',ports=[e11,e12,w56,f10,f11]);
    ##    Mult.Instance(FullAdderModule,'efa7',ports=[e13,w75,w66,f12,f13]);
    ##
    ##    Mult.Instance(FullAdderModule,'ffa1',ports=[f1,f2,w07,res[7],g1]);
    ##    Mult.Instance(FullAdderModule,'ffa2',ports=[f3,f4,w17,g2,g3]);
    ##    Mult.Instance(FullAdderModule,'ffa3',ports=[f5,f6,w27,g4,g5]);
    ##    Mult.Instance(FullAdderModule,'ffa4',ports=[f7,f8,w37,g6,g7]);
    ##    Mult.Instance(FullAdderModule,'ffa5',ports=[f9,f10,w47,g8,g9]);
    ##    Mult.Instance(FullAdderModule,'ffa6',ports=[f11,f12,w57,g10,g11]);
    ##    Mult.Instance(FullAdderModule,'ffa7',ports=[f13,w76,w67,g12,g13]);
    ##
    ##    Mult.Instance(HalfAdderModule,'had1',ports=[g1,g2,res[8],h1]);
    ##    Mult.Instance(FullAdderModule,'fad1',ports=[g3,g4,h1,res[9],h2]);
    ##    Mult.Instance(FullAdderModule,'fad2',ports=[g5,g6,h2,res[10],h3]);
    ##    Mult.Instance(FullAdderModule,'fad3',ports=[g7,g8,h3,res[11],h4]);
    ##    Mult.Instance(FullAdderModule,'fad4',ports=[g9,g10,h4,res[12],h5]);
    ##    Mult.Instance(FullAdderModule,'fad5',ports=[g11,g12,h5,res[13],h6]);
    ##    Mult.Instance(FullAdderModule,'fad6',ports=[w77,g13,h6,res[14],res[15]]);

    return Mult


def paam01_v0_8x6_multiplier():  # 8x6 PAAM01-V0 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    ##    HighModule=Module('Logic_High');
    ##    high_out=HighModule.Output('a');
    ##    high_out.assign(1);
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v0_8x6")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 6)
    res = Mult.Output("p", 14)

    w10 = Mult.Wire("w10")
    w20 = Mult.Wire("w20")
    w30 = Mult.Wire("w30")
    w40 = Mult.Wire("w40")
    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w01 = Mult.Wire("w01")
    w11 = Mult.Wire("w11")
    w21 = Mult.Wire("w21")
    w31 = Mult.Wire("w31")
    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w02 = Mult.Wire("w02")
    w12 = Mult.Wire("w12")
    w22 = Mult.Wire("w22")
    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w03 = Mult.Wire("w03")
    w13 = Mult.Wire("w13")
    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w04 = Mult.Wire("w04")
    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    a1 = Mult.Wire("a1")
    a2 = Mult.Wire("a2")
    a3 = Mult.Wire("a3")
    a4 = Mult.Wire("a4")
    a5 = Mult.Wire("a5")
    a6 = Mult.Wire("a6")
    a7 = Mult.Wire("a7")
    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b1 = Mult.Wire("b1")
    b2 = Mult.Wire("b2")
    b3 = Mult.Wire("b3")
    b4 = Mult.Wire("b4")
    b5 = Mult.Wire("b5")
    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c1 = Mult.Wire("c1")
    c2 = Mult.Wire("c2")
    c3 = Mult.Wire("c3")
    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d1 = Mult.Wire("d1")
    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")
    ##    net=Mult.Wire('net');
    ##    Mult.Instance(HighModule,'G1',ports=[net]);

    Mult.Instance(AndModule, "i1", ports=[w01, a[0], b[1]])
    Mult.Instance(AndModule, "i2", ports=[w10, a[1], b[0]])
    Mult.Instance(AndModule, "i3", ports=[w11, a[1], b[1]])
    Mult.Instance(AndModule, "i4", ports=[w20, a[2], b[0]])
    Mult.Instance(AndModule, "i5", ports=[w21, a[2], b[1]])
    Mult.Instance(AndModule, "i6", ports=[w30, a[3], b[0]])
    Mult.Instance(AndModule, "i7", ports=[w31, a[3], b[1]])
    Mult.Instance(AndModule, "i8", ports=[w40, a[4], b[0]])
    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li1", ports=[w02, a[0], b[2]])
    Mult.Instance(AndModule, "li2", ports=[w12, a[1], b[2]])
    Mult.Instance(AndModule, "li3", ports=[w22, a[2], b[2]])
    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi1", ports=[w03, a[0], b[3]])
    Mult.Instance(AndModule, "gi2", ports=[w13, a[1], b[3]])
    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi1", ports=[w04, a[0], b[4]])
    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "mi1", ports=[w75, a[7], b[5]])

    Mult.Instance(HalfAdderModule, "ha1", ports=[w10, w01, res[1], a1])
    Mult.Instance(HalfAdderModule, "ha2", ports=[w20, w11, a2, a3])
    Mult.Instance(HalfAdderModule, "ha3", ports=[w30, w21, a4, a5])
    Mult.Instance(HalfAdderModule, "ha4", ports=[w40, w31, a6, a7])
    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(FullAdderModule, "afa1", ports=[a1, a2, w02, res[2], b1])
    Mult.Instance(FullAdderModule, "afa2", ports=[a3, a4, w12, b2, b3])
    Mult.Instance(FullAdderModule, "afa3", ports=[a5, a6, w22, b4, b5])
    Mult.Instance(FullAdderModule, "afa4", ports=[a7, a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(FullAdderModule, "bfa1", ports=[b1, b2, w03, res[3], c1])
    Mult.Instance(FullAdderModule, "bfa2", ports=[b3, b4, w13, c2, c3])
    Mult.Instance(FullAdderModule, "bfa3", ports=[b5, b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(FullAdderModule, "cfa1", ports=[c1, c2, w04, res[4], d1])
    Mult.Instance(FullAdderModule, "cfa2", ports=[c3, c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(FullAdderModule, "dfa1", ports=[d1, d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[e1, e2, res[6], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[e3, e4, h1, res[7], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[e5, e6, h2, res[8], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[e7, e8, h3, res[9], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[e9, e10, h4, res[10], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[e11, e12, h5, res[11], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w75, e13, h6, res[12], res[13]])

    return Mult


def paam01_v0_8x8_multiplier():  # 8x8 PAAM01-V0 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v0_8x8")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 8)
    res = Mult.Output("p", 16)

    w10 = Mult.Wire("w10")
    w20 = Mult.Wire("w20")
    w30 = Mult.Wire("w30")
    w40 = Mult.Wire("w40")
    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w01 = Mult.Wire("w01")
    w11 = Mult.Wire("w11")
    w21 = Mult.Wire("w21")
    w31 = Mult.Wire("w31")
    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w02 = Mult.Wire("w02")
    w12 = Mult.Wire("w12")
    w22 = Mult.Wire("w22")
    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w03 = Mult.Wire("w03")
    w13 = Mult.Wire("w13")
    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w04 = Mult.Wire("w04")
    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    w06 = Mult.Wire("w06")
    w16 = Mult.Wire("w16")
    w26 = Mult.Wire("w26")
    w36 = Mult.Wire("w36")
    w46 = Mult.Wire("w46")
    w56 = Mult.Wire("w56")
    w66 = Mult.Wire("w66")
    w76 = Mult.Wire("w76")

    w07 = Mult.Wire("w07")
    w17 = Mult.Wire("w17")
    w27 = Mult.Wire("w27")
    w37 = Mult.Wire("w37")
    w47 = Mult.Wire("w47")
    w57 = Mult.Wire("w57")
    w67 = Mult.Wire("w67")
    w77 = Mult.Wire("w77")

    a1 = Mult.Wire("a1")
    a2 = Mult.Wire("a2")
    a3 = Mult.Wire("a3")
    a4 = Mult.Wire("a4")
    a5 = Mult.Wire("a5")
    a6 = Mult.Wire("a6")
    a7 = Mult.Wire("a7")
    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b1 = Mult.Wire("b1")
    b2 = Mult.Wire("b2")
    b3 = Mult.Wire("b3")
    b4 = Mult.Wire("b4")
    b5 = Mult.Wire("b5")
    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c1 = Mult.Wire("c1")
    c2 = Mult.Wire("c2")
    c3 = Mult.Wire("c3")
    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d1 = Mult.Wire("d1")
    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    f1 = Mult.Wire("f1")
    f2 = Mult.Wire("f2")
    f3 = Mult.Wire("f3")
    f4 = Mult.Wire("f4")
    f5 = Mult.Wire("f5")
    f6 = Mult.Wire("f6")
    f7 = Mult.Wire("f7")
    f8 = Mult.Wire("f8")
    f9 = Mult.Wire("f9")
    f10 = Mult.Wire("f10")
    f11 = Mult.Wire("f11")
    f12 = Mult.Wire("f12")
    f13 = Mult.Wire("f13")

    g1 = Mult.Wire("g1")
    g2 = Mult.Wire("g2")
    g3 = Mult.Wire("g3")
    g4 = Mult.Wire("g4")
    g5 = Mult.Wire("g5")
    g6 = Mult.Wire("g6")
    g7 = Mult.Wire("g7")
    g8 = Mult.Wire("g8")
    g9 = Mult.Wire("g9")
    g10 = Mult.Wire("g10")
    g11 = Mult.Wire("g11")
    g12 = Mult.Wire("g12")
    g13 = Mult.Wire("g13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")

    Mult.Instance(AndModule, "i1", ports=[w01, a[0], b[1]])
    Mult.Instance(AndModule, "i2", ports=[w10, a[1], b[0]])
    Mult.Instance(AndModule, "i3", ports=[w11, a[1], b[1]])
    Mult.Instance(AndModule, "i4", ports=[w20, a[2], b[0]])
    Mult.Instance(AndModule, "i5", ports=[w21, a[2], b[1]])
    Mult.Instance(AndModule, "i6", ports=[w30, a[3], b[0]])
    Mult.Instance(AndModule, "i7", ports=[w31, a[3], b[1]])
    Mult.Instance(AndModule, "i8", ports=[w40, a[4], b[0]])
    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li1", ports=[w02, a[0], b[2]])
    Mult.Instance(AndModule, "li2", ports=[w12, a[1], b[2]])
    Mult.Instance(AndModule, "li3", ports=[w22, a[2], b[2]])
    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi1", ports=[w03, a[0], b[3]])
    Mult.Instance(AndModule, "gi2", ports=[w13, a[1], b[3]])
    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi1", ports=[w04, a[0], b[4]])
    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "ji1", ports=[w06, a[0], b[6]])
    Mult.Instance(AndModule, "ji2", ports=[w16, a[1], b[6]])
    Mult.Instance(AndModule, "ji3", ports=[w26, a[2], b[6]])
    Mult.Instance(AndModule, "ji4", ports=[w36, a[3], b[6]])
    Mult.Instance(AndModule, "ji5", ports=[w46, a[4], b[6]])
    Mult.Instance(AndModule, "ji6", ports=[w56, a[5], b[6]])
    Mult.Instance(AndModule, "ji7", ports=[w66, a[6], b[6]])
    Mult.Instance(AndModule, "ji8", ports=[w75, a[7], b[5]])

    Mult.Instance(AndModule, "ki1", ports=[w07, a[0], b[7]])
    Mult.Instance(AndModule, "ki2", ports=[w17, a[1], b[7]])
    Mult.Instance(AndModule, "ki3", ports=[w27, a[2], b[7]])
    Mult.Instance(AndModule, "ki4", ports=[w37, a[3], b[7]])
    Mult.Instance(AndModule, "ki5", ports=[w47, a[4], b[7]])
    Mult.Instance(AndModule, "ki6", ports=[w57, a[5], b[7]])
    Mult.Instance(AndModule, "ki7", ports=[w67, a[6], b[7]])
    Mult.Instance(AndModule, "ki8", ports=[w76, a[7], b[6]])

    Mult.Instance(AndModule, "mi1", ports=[w77, a[7], b[7]])

    Mult.Instance(HalfAdderModule, "ha1", ports=[w10, w01, res[1], a1])
    Mult.Instance(HalfAdderModule, "ha2", ports=[w20, w11, a2, a3])
    Mult.Instance(HalfAdderModule, "ha3", ports=[w30, w21, a4, a5])
    Mult.Instance(HalfAdderModule, "ha4", ports=[w40, w31, a6, a7])
    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(FullAdderModule, "afa1", ports=[a1, a2, w02, res[2], b1])
    Mult.Instance(FullAdderModule, "afa2", ports=[a3, a4, w12, b2, b3])
    Mult.Instance(FullAdderModule, "afa3", ports=[a5, a6, w22, b4, b5])
    Mult.Instance(FullAdderModule, "afa4", ports=[a7, a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(FullAdderModule, "bfa1", ports=[b1, b2, w03, res[3], c1])
    Mult.Instance(FullAdderModule, "bfa2", ports=[b3, b4, w13, c2, c3])
    Mult.Instance(FullAdderModule, "bfa3", ports=[b5, b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(FullAdderModule, "cfa1", ports=[c1, c2, w04, res[4], d1])
    Mult.Instance(FullAdderModule, "cfa2", ports=[c3, c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(FullAdderModule, "dfa1", ports=[d1, d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    Mult.Instance(FullAdderModule, "efa1", ports=[e1, e2, w06, res[6], f1])
    Mult.Instance(FullAdderModule, "efa2", ports=[e3, e4, w16, f2, f3])
    Mult.Instance(FullAdderModule, "efa3", ports=[e5, e6, w26, f4, f5])
    Mult.Instance(FullAdderModule, "efa4", ports=[e7, e8, w36, f6, f7])
    Mult.Instance(FullAdderModule, "efa5", ports=[e9, e10, w46, f8, f9])
    Mult.Instance(FullAdderModule, "efa6", ports=[e11, e12, w56, f10, f11])
    Mult.Instance(FullAdderModule, "efa7", ports=[e13, w75, w66, f12, f13])

    Mult.Instance(FullAdderModule, "ffa1", ports=[f1, f2, w07, res[7], g1])
    Mult.Instance(FullAdderModule, "ffa2", ports=[f3, f4, w17, g2, g3])
    Mult.Instance(FullAdderModule, "ffa3", ports=[f5, f6, w27, g4, g5])
    Mult.Instance(FullAdderModule, "ffa4", ports=[f7, f8, w37, g6, g7])
    Mult.Instance(FullAdderModule, "ffa5", ports=[f9, f10, w47, g8, g9])
    Mult.Instance(FullAdderModule, "ffa6", ports=[f11, f12, w57, g10, g11])
    Mult.Instance(FullAdderModule, "ffa7", ports=[f13, w76, w67, g12, g13])

    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[g1, g2, res[8], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[g3, g4, h1, res[9], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[g5, g6, h2, res[10], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[g7, g8, h3, res[11], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[g9, g10, h4, res[12], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[g11, g12, h5, res[13], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w77, g13, h6, res[14], res[15]])

    return Mult


def paam01_v1_8x6_multiplier():  # 8x6 PAAM01-V1 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    ##    HighModule=Module('Logic_High');
    ##    high_out=HighModule.Output('a');
    ##    high_out.assign(1);
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v1_8x6")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 6)
    res = Mult.Output("p", 14)

    w20 = Mult.Wire("w20")
    w30 = Mult.Wire("w30")
    w40 = Mult.Wire("w40")
    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w11 = Mult.Wire("w11")
    w21 = Mult.Wire("w21")
    w31 = Mult.Wire("w31")
    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w02 = Mult.Wire("w02")
    w12 = Mult.Wire("w12")
    w22 = Mult.Wire("w22")
    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w03 = Mult.Wire("w03")
    w13 = Mult.Wire("w13")
    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w04 = Mult.Wire("w04")
    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    a2 = Mult.Wire("a2")
    a3 = Mult.Wire("a3")
    a4 = Mult.Wire("a4")
    a5 = Mult.Wire("a5")
    a6 = Mult.Wire("a6")
    a7 = Mult.Wire("a7")
    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b1 = Mult.Wire("b1")
    b2 = Mult.Wire("b2")
    b3 = Mult.Wire("b3")
    b4 = Mult.Wire("b4")
    b5 = Mult.Wire("b5")
    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c1 = Mult.Wire("c1")
    c2 = Mult.Wire("c2")
    c3 = Mult.Wire("c3")
    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d1 = Mult.Wire("d1")
    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")
    ##    net=Mult.Wire('net',2);
    ##    Mult.Instance(HighModule,'G1',ports=[net[0]]);
    ##    Mult.Instance(HighModule,'G2',ports=[net[1]]);

    Mult.Instance(AndModule, "i3", ports=[w11, a[1], b[1]])
    Mult.Instance(AndModule, "i4", ports=[w20, a[2], b[0]])
    Mult.Instance(AndModule, "i5", ports=[w21, a[2], b[1]])
    Mult.Instance(AndModule, "i6", ports=[w30, a[3], b[0]])
    Mult.Instance(AndModule, "i7", ports=[w31, a[3], b[1]])
    Mult.Instance(AndModule, "i8", ports=[w40, a[4], b[0]])
    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li1", ports=[w02, a[0], b[2]])
    Mult.Instance(AndModule, "li2", ports=[w12, a[1], b[2]])
    Mult.Instance(AndModule, "li3", ports=[w22, a[2], b[2]])
    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi1", ports=[w03, a[0], b[3]])
    Mult.Instance(AndModule, "gi2", ports=[w13, a[1], b[3]])
    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi1", ports=[w04, a[0], b[4]])
    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "mi1", ports=[w75, a[7], b[5]])

    Mult.Instance(HalfAdderModule, "ha2", ports=[w20, w11, a2, a3])
    Mult.Instance(HalfAdderModule, "ha3", ports=[w30, w21, a4, a5])
    Mult.Instance(HalfAdderModule, "ha4", ports=[w40, w31, a6, a7])
    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa1", ports=[a2, w02, res[2], b1])
    Mult.Instance(FullAdderModule, "afa2", ports=[a3, a4, w12, b2, b3])
    Mult.Instance(FullAdderModule, "afa3", ports=[a5, a6, w22, b4, b5])
    Mult.Instance(FullAdderModule, "afa4", ports=[a7, a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(FullAdderModule, "bfa1", ports=[b1, b2, w03, res[3], c1])
    Mult.Instance(FullAdderModule, "bfa2", ports=[b3, b4, w13, c2, c3])
    Mult.Instance(FullAdderModule, "bfa3", ports=[b5, b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(FullAdderModule, "cfa1", ports=[c1, c2, w04, res[4], d1])
    Mult.Instance(FullAdderModule, "cfa2", ports=[c3, c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(FullAdderModule, "dfa1", ports=[d1, d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[e1, e2, res[6], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[e3, e4, h1, res[7], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[e5, e6, h2, res[8], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[e7, e8, h3, res[9], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[e9, e10, h4, res[10], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[e11, e12, h5, res[11], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w75, e13, h6, res[12], res[13]])

    return Mult


def paam01_v1_8x8_multiplier():  # 8x8 PAAM01-V1 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v1_8x8")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 8)
    res = Mult.Output("p", 16)

    w20 = Mult.Wire("w20")
    w30 = Mult.Wire("w30")
    w40 = Mult.Wire("w40")
    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w11 = Mult.Wire("w11")
    w21 = Mult.Wire("w21")
    w31 = Mult.Wire("w31")
    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w02 = Mult.Wire("w02")
    w12 = Mult.Wire("w12")
    w22 = Mult.Wire("w22")
    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w03 = Mult.Wire("w03")
    w13 = Mult.Wire("w13")
    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w04 = Mult.Wire("w04")
    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    w06 = Mult.Wire("w06")
    w16 = Mult.Wire("w16")
    w26 = Mult.Wire("w26")
    w36 = Mult.Wire("w36")
    w46 = Mult.Wire("w46")
    w56 = Mult.Wire("w56")
    w66 = Mult.Wire("w66")
    w76 = Mult.Wire("w76")

    w07 = Mult.Wire("w07")
    w17 = Mult.Wire("w17")
    w27 = Mult.Wire("w27")
    w37 = Mult.Wire("w37")
    w47 = Mult.Wire("w47")
    w57 = Mult.Wire("w57")
    w67 = Mult.Wire("w67")
    w77 = Mult.Wire("w77")

    a2 = Mult.Wire("a2")
    a3 = Mult.Wire("a3")
    a4 = Mult.Wire("a4")
    a5 = Mult.Wire("a5")
    a6 = Mult.Wire("a6")
    a7 = Mult.Wire("a7")
    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b1 = Mult.Wire("b1")
    b2 = Mult.Wire("b2")
    b3 = Mult.Wire("b3")
    b4 = Mult.Wire("b4")
    b5 = Mult.Wire("b5")
    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c1 = Mult.Wire("c1")
    c2 = Mult.Wire("c2")
    c3 = Mult.Wire("c3")
    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d1 = Mult.Wire("d1")
    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    f1 = Mult.Wire("f1")
    f2 = Mult.Wire("f2")
    f3 = Mult.Wire("f3")
    f4 = Mult.Wire("f4")
    f5 = Mult.Wire("f5")
    f6 = Mult.Wire("f6")
    f7 = Mult.Wire("f7")
    f8 = Mult.Wire("f8")
    f9 = Mult.Wire("f9")
    f10 = Mult.Wire("f10")
    f11 = Mult.Wire("f11")
    f12 = Mult.Wire("f12")
    f13 = Mult.Wire("f13")

    g1 = Mult.Wire("g1")
    g2 = Mult.Wire("g2")
    g3 = Mult.Wire("g3")
    g4 = Mult.Wire("g4")
    g5 = Mult.Wire("g5")
    g6 = Mult.Wire("g6")
    g7 = Mult.Wire("g7")
    g8 = Mult.Wire("g8")
    g9 = Mult.Wire("g9")
    g10 = Mult.Wire("g10")
    g11 = Mult.Wire("g11")
    g12 = Mult.Wire("g12")
    g13 = Mult.Wire("g13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")

    Mult.Instance(AndModule, "i3", ports=[w11, a[1], b[1]])
    Mult.Instance(AndModule, "i4", ports=[w20, a[2], b[0]])
    Mult.Instance(AndModule, "i5", ports=[w21, a[2], b[1]])
    Mult.Instance(AndModule, "i6", ports=[w30, a[3], b[0]])
    Mult.Instance(AndModule, "i7", ports=[w31, a[3], b[1]])
    Mult.Instance(AndModule, "i8", ports=[w40, a[4], b[0]])
    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li1", ports=[w02, a[0], b[2]])
    Mult.Instance(AndModule, "li2", ports=[w12, a[1], b[2]])
    Mult.Instance(AndModule, "li3", ports=[w22, a[2], b[2]])
    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi1", ports=[w03, a[0], b[3]])
    Mult.Instance(AndModule, "gi2", ports=[w13, a[1], b[3]])
    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi1", ports=[w04, a[0], b[4]])
    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "ji1", ports=[w06, a[0], b[6]])
    Mult.Instance(AndModule, "ji2", ports=[w16, a[1], b[6]])
    Mult.Instance(AndModule, "ji3", ports=[w26, a[2], b[6]])
    Mult.Instance(AndModule, "ji4", ports=[w36, a[3], b[6]])
    Mult.Instance(AndModule, "ji5", ports=[w46, a[4], b[6]])
    Mult.Instance(AndModule, "ji6", ports=[w56, a[5], b[6]])
    Mult.Instance(AndModule, "ji7", ports=[w66, a[6], b[6]])
    Mult.Instance(AndModule, "ji8", ports=[w75, a[7], b[5]])

    Mult.Instance(AndModule, "ki1", ports=[w07, a[0], b[7]])
    Mult.Instance(AndModule, "ki2", ports=[w17, a[1], b[7]])
    Mult.Instance(AndModule, "ki3", ports=[w27, a[2], b[7]])
    Mult.Instance(AndModule, "ki4", ports=[w37, a[3], b[7]])
    Mult.Instance(AndModule, "ki5", ports=[w47, a[4], b[7]])
    Mult.Instance(AndModule, "ki6", ports=[w57, a[5], b[7]])
    Mult.Instance(AndModule, "ki7", ports=[w67, a[6], b[7]])
    Mult.Instance(AndModule, "ki8", ports=[w76, a[7], b[6]])

    Mult.Instance(AndModule, "mi1", ports=[w77, a[7], b[7]])

    Mult.Instance(HalfAdderModule, "ha2", ports=[w20, w11, a2, a3])
    Mult.Instance(HalfAdderModule, "ha3", ports=[w30, w21, a4, a5])
    Mult.Instance(HalfAdderModule, "ha4", ports=[w40, w31, a6, a7])
    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa1", ports=[a2, w02, res[2], b1])
    Mult.Instance(FullAdderModule, "afa2", ports=[a3, a4, w12, b2, b3])
    Mult.Instance(FullAdderModule, "afa3", ports=[a5, a6, w22, b4, b5])
    Mult.Instance(FullAdderModule, "afa4", ports=[a7, a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(FullAdderModule, "bfa1", ports=[b1, b2, w03, res[3], c1])
    Mult.Instance(FullAdderModule, "bfa2", ports=[b3, b4, w13, c2, c3])
    Mult.Instance(FullAdderModule, "bfa3", ports=[b5, b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(FullAdderModule, "cfa1", ports=[c1, c2, w04, res[4], d1])
    Mult.Instance(FullAdderModule, "cfa2", ports=[c3, c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(FullAdderModule, "dfa1", ports=[d1, d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    Mult.Instance(FullAdderModule, "efa1", ports=[e1, e2, w06, res[6], f1])
    Mult.Instance(FullAdderModule, "efa2", ports=[e3, e4, w16, f2, f3])
    Mult.Instance(FullAdderModule, "efa3", ports=[e5, e6, w26, f4, f5])
    Mult.Instance(FullAdderModule, "efa4", ports=[e7, e8, w36, f6, f7])
    Mult.Instance(FullAdderModule, "efa5", ports=[e9, e10, w46, f8, f9])
    Mult.Instance(FullAdderModule, "efa6", ports=[e11, e12, w56, f10, f11])
    Mult.Instance(FullAdderModule, "efa7", ports=[e13, w75, w66, f12, f13])

    Mult.Instance(FullAdderModule, "ffa1", ports=[f1, f2, w07, res[7], g1])
    Mult.Instance(FullAdderModule, "ffa2", ports=[f3, f4, w17, g2, g3])
    Mult.Instance(FullAdderModule, "ffa3", ports=[f5, f6, w27, g4, g5])
    Mult.Instance(FullAdderModule, "ffa4", ports=[f7, f8, w37, g6, g7])
    Mult.Instance(FullAdderModule, "ffa5", ports=[f9, f10, w47, g8, g9])
    Mult.Instance(FullAdderModule, "ffa6", ports=[f11, f12, w57, g10, g11])
    Mult.Instance(FullAdderModule, "ffa7", ports=[f13, w76, w67, g12, g13])

    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[g1, g2, res[8], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[g3, g4, h1, res[9], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[g5, g6, h2, res[10], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[g7, g8, h3, res[11], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[g9, g10, h4, res[12], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[g11, g12, h5, res[13], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w77, g13, h6, res[14], res[15]])

    return Mult


def paam01_v2_8x6_multiplier():  # 8x6 PAAM01-V2 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    ##    HighModule=Module('Logic_High');
    ##    high_out=HighModule.Output('a');
    ##    high_out.assign(1);
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v2_8x6")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 6)
    res = Mult.Output("p", 14)

    w30 = Mult.Wire("w30")
    w40 = Mult.Wire("w40")
    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w21 = Mult.Wire("w21")
    w31 = Mult.Wire("w31")
    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w12 = Mult.Wire("w12")
    w22 = Mult.Wire("w22")
    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w03 = Mult.Wire("w03")
    w13 = Mult.Wire("w13")
    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w04 = Mult.Wire("w04")
    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    a4 = Mult.Wire("a4")
    a5 = Mult.Wire("a5")
    a6 = Mult.Wire("a6")
    a7 = Mult.Wire("a7")
    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b2 = Mult.Wire("b2")
    b3 = Mult.Wire("b3")
    b4 = Mult.Wire("b4")
    b5 = Mult.Wire("b5")
    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c1 = Mult.Wire("c1")
    c2 = Mult.Wire("c2")
    c3 = Mult.Wire("c3")
    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d1 = Mult.Wire("d1")
    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")
    ##    net=Mult.Wire('net',3);
    ##    Mult.Instance(HighModule,'G1',ports=[net[0]]);
    ##    Mult.Instance(HighModule,'G2',ports=[net[1]]);
    ##    Mult.Instance(HighModule,'G3',ports=[net[2]]);

    Mult.Instance(AndModule, "i5", ports=[w21, a[2], b[1]])
    Mult.Instance(AndModule, "i6", ports=[w30, a[3], b[0]])
    Mult.Instance(AndModule, "i7", ports=[w31, a[3], b[1]])
    Mult.Instance(AndModule, "i8", ports=[w40, a[4], b[0]])
    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li2", ports=[w12, a[1], b[2]])
    Mult.Instance(AndModule, "li3", ports=[w22, a[2], b[2]])
    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi1", ports=[w03, a[0], b[3]])
    Mult.Instance(AndModule, "gi2", ports=[w13, a[1], b[3]])
    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi1", ports=[w04, a[0], b[4]])
    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "mi1", ports=[w75, a[7], b[5]])

    Mult.Instance(HalfAdderModule, "ha3", ports=[w30, w21, a4, a5])
    Mult.Instance(HalfAdderModule, "ha4", ports=[w40, w31, a6, a7])
    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa2", ports=[a4, w12, b2, b3])
    Mult.Instance(FullAdderModule, "afa3", ports=[a5, a6, w22, b4, b5])
    Mult.Instance(FullAdderModule, "afa4", ports=[a7, a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(HalfAdderModule, "bfa1", ports=[b2, w03, res[3], c1])
    Mult.Instance(FullAdderModule, "bfa2", ports=[b3, b4, w13, c2, c3])
    Mult.Instance(FullAdderModule, "bfa3", ports=[b5, b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(FullAdderModule, "cfa1", ports=[c1, c2, w04, res[4], d1])
    Mult.Instance(FullAdderModule, "cfa2", ports=[c3, c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(FullAdderModule, "dfa1", ports=[d1, d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[e1, e2, res[6], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[e3, e4, h1, res[7], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[e5, e6, h2, res[8], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[e7, e8, h3, res[9], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[e9, e10, h4, res[10], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[e11, e12, h5, res[11], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w75, e13, h6, res[12], res[13]])

    return Mult


def paam01_v2_8x8_multiplier():  # 8x8 PAAM01-V2 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v2_8x8")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 8)
    res = Mult.Output("p", 16)

    w30 = Mult.Wire("w30")
    w40 = Mult.Wire("w40")
    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w21 = Mult.Wire("w21")
    w31 = Mult.Wire("w31")
    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w12 = Mult.Wire("w12")
    w22 = Mult.Wire("w22")
    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w03 = Mult.Wire("w03")
    w13 = Mult.Wire("w13")
    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w04 = Mult.Wire("w04")
    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    w06 = Mult.Wire("w06")
    w16 = Mult.Wire("w16")
    w26 = Mult.Wire("w26")
    w36 = Mult.Wire("w36")
    w46 = Mult.Wire("w46")
    w56 = Mult.Wire("w56")
    w66 = Mult.Wire("w66")
    w76 = Mult.Wire("w76")

    w07 = Mult.Wire("w07")
    w17 = Mult.Wire("w17")
    w27 = Mult.Wire("w27")
    w37 = Mult.Wire("w37")
    w47 = Mult.Wire("w47")
    w57 = Mult.Wire("w57")
    w67 = Mult.Wire("w67")
    w77 = Mult.Wire("w77")

    a4 = Mult.Wire("a4")
    a5 = Mult.Wire("a5")
    a6 = Mult.Wire("a6")
    a7 = Mult.Wire("a7")
    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b2 = Mult.Wire("b2")
    b3 = Mult.Wire("b3")
    b4 = Mult.Wire("b4")
    b5 = Mult.Wire("b5")
    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c1 = Mult.Wire("c1")
    c2 = Mult.Wire("c2")
    c3 = Mult.Wire("c3")
    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d1 = Mult.Wire("d1")
    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    f1 = Mult.Wire("f1")
    f2 = Mult.Wire("f2")
    f3 = Mult.Wire("f3")
    f4 = Mult.Wire("f4")
    f5 = Mult.Wire("f5")
    f6 = Mult.Wire("f6")
    f7 = Mult.Wire("f7")
    f8 = Mult.Wire("f8")
    f9 = Mult.Wire("f9")
    f10 = Mult.Wire("f10")
    f11 = Mult.Wire("f11")
    f12 = Mult.Wire("f12")
    f13 = Mult.Wire("f13")

    g1 = Mult.Wire("g1")
    g2 = Mult.Wire("g2")
    g3 = Mult.Wire("g3")
    g4 = Mult.Wire("g4")
    g5 = Mult.Wire("g5")
    g6 = Mult.Wire("g6")
    g7 = Mult.Wire("g7")
    g8 = Mult.Wire("g8")
    g9 = Mult.Wire("g9")
    g10 = Mult.Wire("g10")
    g11 = Mult.Wire("g11")
    g12 = Mult.Wire("g12")
    g13 = Mult.Wire("g13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")

    Mult.Instance(AndModule, "i5", ports=[w21, a[2], b[1]])
    Mult.Instance(AndModule, "i6", ports=[w30, a[3], b[0]])
    Mult.Instance(AndModule, "i7", ports=[w31, a[3], b[1]])
    Mult.Instance(AndModule, "i8", ports=[w40, a[4], b[0]])
    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li2", ports=[w12, a[1], b[2]])
    Mult.Instance(AndModule, "li3", ports=[w22, a[2], b[2]])
    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi1", ports=[w03, a[0], b[3]])
    Mult.Instance(AndModule, "gi2", ports=[w13, a[1], b[3]])
    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi1", ports=[w04, a[0], b[4]])
    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "ji1", ports=[w06, a[0], b[6]])
    Mult.Instance(AndModule, "ji2", ports=[w16, a[1], b[6]])
    Mult.Instance(AndModule, "ji3", ports=[w26, a[2], b[6]])
    Mult.Instance(AndModule, "ji4", ports=[w36, a[3], b[6]])
    Mult.Instance(AndModule, "ji5", ports=[w46, a[4], b[6]])
    Mult.Instance(AndModule, "ji6", ports=[w56, a[5], b[6]])
    Mult.Instance(AndModule, "ji7", ports=[w66, a[6], b[6]])
    Mult.Instance(AndModule, "ji8", ports=[w75, a[7], b[5]])

    Mult.Instance(AndModule, "ki1", ports=[w07, a[0], b[7]])
    Mult.Instance(AndModule, "ki2", ports=[w17, a[1], b[7]])
    Mult.Instance(AndModule, "ki3", ports=[w27, a[2], b[7]])
    Mult.Instance(AndModule, "ki4", ports=[w37, a[3], b[7]])
    Mult.Instance(AndModule, "ki5", ports=[w47, a[4], b[7]])
    Mult.Instance(AndModule, "ki6", ports=[w57, a[5], b[7]])
    Mult.Instance(AndModule, "ki7", ports=[w67, a[6], b[7]])
    Mult.Instance(AndModule, "ki8", ports=[w76, a[7], b[6]])

    Mult.Instance(AndModule, "mi1", ports=[w77, a[7], b[7]])

    Mult.Instance(HalfAdderModule, "ha3", ports=[w30, w21, a4, a5])
    Mult.Instance(HalfAdderModule, "ha4", ports=[w40, w31, a6, a7])
    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa2", ports=[a4, w12, b2, b3])
    Mult.Instance(FullAdderModule, "afa3", ports=[a5, a6, w22, b4, b5])
    Mult.Instance(FullAdderModule, "afa4", ports=[a7, a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(HalfAdderModule, "bfa1", ports=[b2, w03, res[3], c1])
    Mult.Instance(FullAdderModule, "bfa2", ports=[b3, b4, w13, c2, c3])
    Mult.Instance(FullAdderModule, "bfa3", ports=[b5, b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(FullAdderModule, "cfa1", ports=[c1, c2, w04, res[4], d1])
    Mult.Instance(FullAdderModule, "cfa2", ports=[c3, c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(FullAdderModule, "dfa1", ports=[d1, d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    Mult.Instance(FullAdderModule, "efa1", ports=[e1, e2, w06, res[6], f1])
    Mult.Instance(FullAdderModule, "efa2", ports=[e3, e4, w16, f2, f3])
    Mult.Instance(FullAdderModule, "efa3", ports=[e5, e6, w26, f4, f5])
    Mult.Instance(FullAdderModule, "efa4", ports=[e7, e8, w36, f6, f7])
    Mult.Instance(FullAdderModule, "efa5", ports=[e9, e10, w46, f8, f9])
    Mult.Instance(FullAdderModule, "efa6", ports=[e11, e12, w56, f10, f11])
    Mult.Instance(FullAdderModule, "efa7", ports=[e13, w75, w66, f12, f13])

    Mult.Instance(FullAdderModule, "ffa1", ports=[f1, f2, w07, res[7], g1])
    Mult.Instance(FullAdderModule, "ffa2", ports=[f3, f4, w17, g2, g3])
    Mult.Instance(FullAdderModule, "ffa3", ports=[f5, f6, w27, g4, g5])
    Mult.Instance(FullAdderModule, "ffa4", ports=[f7, f8, w37, g6, g7])
    Mult.Instance(FullAdderModule, "ffa5", ports=[f9, f10, w47, g8, g9])
    Mult.Instance(FullAdderModule, "ffa6", ports=[f11, f12, w57, g10, g11])
    Mult.Instance(FullAdderModule, "ffa7", ports=[f13, w76, w67, g12, g13])

    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[g1, g2, res[8], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[g3, g4, h1, res[9], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[g5, g6, h2, res[10], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[g7, g8, h3, res[11], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[g9, g10, h4, res[12], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[g11, g12, h5, res[13], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w77, g13, h6, res[14], res[15]])

    return Mult


def paam01_v3_8x6_multiplier():  # 8x6 PAAM01-V3 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    ##    HighModule=Module('Logic_High');
    ##    high_out=HighModule.Output('a');
    ##    high_out.assign(1);
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v3_8x6")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 6)
    res = Mult.Output("p", 14)

    w40 = Mult.Wire("w40")
    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w31 = Mult.Wire("w31")
    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w22 = Mult.Wire("w22")
    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w13 = Mult.Wire("w13")
    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w04 = Mult.Wire("w04")
    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    a6 = Mult.Wire("a6")
    a7 = Mult.Wire("a7")
    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b4 = Mult.Wire("b4")
    b5 = Mult.Wire("b5")
    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c2 = Mult.Wire("c2")
    c3 = Mult.Wire("c3")
    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d1 = Mult.Wire("d1")
    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")
    ##    net=Mult.Wire('net',4);
    ##    Mult.Instance(HighModule,'G1',ports=[net[0]]);
    ##    Mult.Instance(HighModule,'G2',ports=[net[1]]);
    ##    Mult.Instance(HighModule,'G3',ports=[net[2]]);
    ##    Mult.Instance(HighModule,'G4',ports=[net[3]]);

    Mult.Instance(AndModule, "i7", ports=[w31, a[3], b[1]])
    Mult.Instance(AndModule, "i8", ports=[w40, a[4], b[0]])
    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li3", ports=[w22, a[2], b[2]])
    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi2", ports=[w13, a[1], b[3]])
    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi1", ports=[w04, a[0], b[4]])
    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "mi1", ports=[w75, a[7], b[5]])

    Mult.Instance(HalfAdderModule, "ha4", ports=[w40, w31, a6, a7])
    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa3", ports=[a6, w22, b4, b5])
    Mult.Instance(FullAdderModule, "afa4", ports=[a7, a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(HalfAdderModule, "bfa2", ports=[b4, w13, c2, c3])
    Mult.Instance(FullAdderModule, "bfa3", ports=[b5, b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(HalfAdderModule, "cfa1", ports=[c2, w04, res[4], d1])
    Mult.Instance(FullAdderModule, "cfa2", ports=[c3, c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(FullAdderModule, "dfa1", ports=[d1, d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    res[3].assign(1)
    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[e1, e2, res[6], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[e3, e4, h1, res[7], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[e5, e6, h2, res[8], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[e7, e8, h3, res[9], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[e9, e10, h4, res[10], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[e11, e12, h5, res[11], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w75, e13, h6, res[12], res[13]])

    return Mult


def paam01_v3_8x8_multiplier():  # 8x8 PAAM01-V3 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v3_8x8")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 8)
    res = Mult.Output("p", 16)

    w40 = Mult.Wire("w40")
    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w31 = Mult.Wire("w31")
    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w22 = Mult.Wire("w22")
    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w13 = Mult.Wire("w13")
    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w04 = Mult.Wire("w04")
    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    w06 = Mult.Wire("w06")
    w16 = Mult.Wire("w16")
    w26 = Mult.Wire("w26")
    w36 = Mult.Wire("w36")
    w46 = Mult.Wire("w46")
    w56 = Mult.Wire("w56")
    w66 = Mult.Wire("w66")
    w76 = Mult.Wire("w76")

    w07 = Mult.Wire("w07")
    w17 = Mult.Wire("w17")
    w27 = Mult.Wire("w27")
    w37 = Mult.Wire("w37")
    w47 = Mult.Wire("w47")
    w57 = Mult.Wire("w57")
    w67 = Mult.Wire("w67")
    w77 = Mult.Wire("w77")

    a6 = Mult.Wire("a6")
    a7 = Mult.Wire("a7")
    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b4 = Mult.Wire("b4")
    b5 = Mult.Wire("b5")
    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c2 = Mult.Wire("c2")
    c3 = Mult.Wire("c3")
    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d1 = Mult.Wire("d1")
    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    f1 = Mult.Wire("f1")
    f2 = Mult.Wire("f2")
    f3 = Mult.Wire("f3")
    f4 = Mult.Wire("f4")
    f5 = Mult.Wire("f5")
    f6 = Mult.Wire("f6")
    f7 = Mult.Wire("f7")
    f8 = Mult.Wire("f8")
    f9 = Mult.Wire("f9")
    f10 = Mult.Wire("f10")
    f11 = Mult.Wire("f11")
    f12 = Mult.Wire("f12")
    f13 = Mult.Wire("f13")

    g1 = Mult.Wire("g1")
    g2 = Mult.Wire("g2")
    g3 = Mult.Wire("g3")
    g4 = Mult.Wire("g4")
    g5 = Mult.Wire("g5")
    g6 = Mult.Wire("g6")
    g7 = Mult.Wire("g7")
    g8 = Mult.Wire("g8")
    g9 = Mult.Wire("g9")
    g10 = Mult.Wire("g10")
    g11 = Mult.Wire("g11")
    g12 = Mult.Wire("g12")
    g13 = Mult.Wire("g13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")

    Mult.Instance(AndModule, "i7", ports=[w31, a[3], b[1]])
    Mult.Instance(AndModule, "i8", ports=[w40, a[4], b[0]])
    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li3", ports=[w22, a[2], b[2]])
    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi2", ports=[w13, a[1], b[3]])
    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi1", ports=[w04, a[0], b[4]])
    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "ji1", ports=[w06, a[0], b[6]])
    Mult.Instance(AndModule, "ji2", ports=[w16, a[1], b[6]])
    Mult.Instance(AndModule, "ji3", ports=[w26, a[2], b[6]])
    Mult.Instance(AndModule, "ji4", ports=[w36, a[3], b[6]])
    Mult.Instance(AndModule, "ji5", ports=[w46, a[4], b[6]])
    Mult.Instance(AndModule, "ji6", ports=[w56, a[5], b[6]])
    Mult.Instance(AndModule, "ji7", ports=[w66, a[6], b[6]])
    Mult.Instance(AndModule, "ji8", ports=[w75, a[7], b[5]])

    Mult.Instance(AndModule, "ki1", ports=[w07, a[0], b[7]])
    Mult.Instance(AndModule, "ki2", ports=[w17, a[1], b[7]])
    Mult.Instance(AndModule, "ki3", ports=[w27, a[2], b[7]])
    Mult.Instance(AndModule, "ki4", ports=[w37, a[3], b[7]])
    Mult.Instance(AndModule, "ki5", ports=[w47, a[4], b[7]])
    Mult.Instance(AndModule, "ki6", ports=[w57, a[5], b[7]])
    Mult.Instance(AndModule, "ki7", ports=[w67, a[6], b[7]])
    Mult.Instance(AndModule, "ki8", ports=[w76, a[7], b[6]])

    Mult.Instance(AndModule, "mi1", ports=[w77, a[7], b[7]])

    Mult.Instance(HalfAdderModule, "ha4", ports=[w40, w31, a6, a7])
    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa3", ports=[a6, w22, b4, b5])
    Mult.Instance(FullAdderModule, "afa4", ports=[a7, a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(HalfAdderModule, "bfa2", ports=[b4, w13, c2, c3])
    Mult.Instance(FullAdderModule, "bfa3", ports=[b5, b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(HalfAdderModule, "cfa1", ports=[c2, w04, res[4], d1])
    Mult.Instance(FullAdderModule, "cfa2", ports=[c3, c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(FullAdderModule, "dfa1", ports=[d1, d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    Mult.Instance(FullAdderModule, "efa1", ports=[e1, e2, w06, res[6], f1])
    Mult.Instance(FullAdderModule, "efa2", ports=[e3, e4, w16, f2, f3])
    Mult.Instance(FullAdderModule, "efa3", ports=[e5, e6, w26, f4, f5])
    Mult.Instance(FullAdderModule, "efa4", ports=[e7, e8, w36, f6, f7])
    Mult.Instance(FullAdderModule, "efa5", ports=[e9, e10, w46, f8, f9])
    Mult.Instance(FullAdderModule, "efa6", ports=[e11, e12, w56, f10, f11])
    Mult.Instance(FullAdderModule, "efa7", ports=[e13, w75, w66, f12, f13])

    Mult.Instance(FullAdderModule, "ffa1", ports=[f1, f2, w07, res[7], g1])
    Mult.Instance(FullAdderModule, "ffa2", ports=[f3, f4, w17, g2, g3])
    Mult.Instance(FullAdderModule, "ffa3", ports=[f5, f6, w27, g4, g5])
    Mult.Instance(FullAdderModule, "ffa4", ports=[f7, f8, w37, g6, g7])
    Mult.Instance(FullAdderModule, "ffa5", ports=[f9, f10, w47, g8, g9])
    Mult.Instance(FullAdderModule, "ffa6", ports=[f11, f12, w57, g10, g11])
    Mult.Instance(FullAdderModule, "ffa7", ports=[f13, w76, w67, g12, g13])

    res[3].assign(1)
    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[g1, g2, res[8], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[g3, g4, h1, res[9], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[g5, g6, h2, res[10], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[g7, g8, h3, res[11], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[g9, g10, h4, res[12], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[g11, g12, h5, res[13], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w77, g13, h6, res[14], res[15]])

    return Mult


def paam01_v4_8x6_multiplier():  # 8x6 PAAM01-V4 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    ##    HighModule=Module('Logic_High');
    ##    high_out=HighModule.Output('a');
    ##    high_out.assign(1);
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v4_8x6")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 6)
    res = Mult.Output("p", 14)

    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")
    ##    net=Mult.Wire('net',5);
    ##    Mult.Instance(HighModule,'G1',ports=[net[0]]);
    ##    Mult.Instance(HighModule,'G2',ports=[net[1]]);
    ##    Mult.Instance(HighModule,'G3',ports=[net[2]]);
    ##    Mult.Instance(HighModule,'G4',ports=[net[3]]);
    ##    Mult.Instance(HighModule,'G5',ports=[net[4]]);

    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "mi1", ports=[w75, a[7], b[5]])

    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa4", ports=[a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(HalfAdderModule, "bfa3", ports=[b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(HalfAdderModule, "cfa2", ports=[c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(HalfAdderModule, "dfa1", ports=[d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    res[4].assign(1)
    res[3].assign(1)
    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[e1, e2, res[6], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[e3, e4, h1, res[7], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[e5, e6, h2, res[8], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[e7, e8, h3, res[9], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[e9, e10, h4, res[10], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[e11, e12, h5, res[11], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w75, e13, h6, res[12], res[13]])

    return Mult


def paam01_v4_8x8_multiplier():  # 8x8 PAAM01-V4 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v4_8x8")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 8)
    res = Mult.Output("p", 16)

    w50 = Mult.Wire("w50")
    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w41 = Mult.Wire("w41")
    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w32 = Mult.Wire("w32")
    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w23 = Mult.Wire("w23")
    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w14 = Mult.Wire("w14")
    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w05 = Mult.Wire("w05")
    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    w06 = Mult.Wire("w06")
    w16 = Mult.Wire("w16")
    w26 = Mult.Wire("w26")
    w36 = Mult.Wire("w36")
    w46 = Mult.Wire("w46")
    w56 = Mult.Wire("w56")
    w66 = Mult.Wire("w66")
    w76 = Mult.Wire("w76")

    w07 = Mult.Wire("w07")
    w17 = Mult.Wire("w17")
    w27 = Mult.Wire("w27")
    w37 = Mult.Wire("w37")
    w47 = Mult.Wire("w47")
    w57 = Mult.Wire("w57")
    w67 = Mult.Wire("w67")
    w77 = Mult.Wire("w77")

    a8 = Mult.Wire("a8")
    a9 = Mult.Wire("a9")
    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b6 = Mult.Wire("b6")
    b7 = Mult.Wire("b7")
    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c4 = Mult.Wire("c4")
    c5 = Mult.Wire("c5")
    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d2 = Mult.Wire("d2")
    d3 = Mult.Wire("d3")
    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e1 = Mult.Wire("e1")
    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    f1 = Mult.Wire("f1")
    f2 = Mult.Wire("f2")
    f3 = Mult.Wire("f3")
    f4 = Mult.Wire("f4")
    f5 = Mult.Wire("f5")
    f6 = Mult.Wire("f6")
    f7 = Mult.Wire("f7")
    f8 = Mult.Wire("f8")
    f9 = Mult.Wire("f9")
    f10 = Mult.Wire("f10")
    f11 = Mult.Wire("f11")
    f12 = Mult.Wire("f12")
    f13 = Mult.Wire("f13")

    g1 = Mult.Wire("g1")
    g2 = Mult.Wire("g2")
    g3 = Mult.Wire("g3")
    g4 = Mult.Wire("g4")
    g5 = Mult.Wire("g5")
    g6 = Mult.Wire("g6")
    g7 = Mult.Wire("g7")
    g8 = Mult.Wire("g8")
    g9 = Mult.Wire("g9")
    g10 = Mult.Wire("g10")
    g11 = Mult.Wire("g11")
    g12 = Mult.Wire("g12")
    g13 = Mult.Wire("g13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")

    Mult.Instance(AndModule, "i9", ports=[w41, a[4], b[1]])
    Mult.Instance(AndModule, "i10", ports=[w50, a[5], b[0]])
    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li4", ports=[w32, a[3], b[2]])
    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi3", ports=[w23, a[2], b[3]])
    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi2", ports=[w14, a[1], b[4]])
    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii1", ports=[w05, a[0], b[5]])
    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "ji1", ports=[w06, a[0], b[6]])
    Mult.Instance(AndModule, "ji2", ports=[w16, a[1], b[6]])
    Mult.Instance(AndModule, "ji3", ports=[w26, a[2], b[6]])
    Mult.Instance(AndModule, "ji4", ports=[w36, a[3], b[6]])
    Mult.Instance(AndModule, "ji5", ports=[w46, a[4], b[6]])
    Mult.Instance(AndModule, "ji6", ports=[w56, a[5], b[6]])
    Mult.Instance(AndModule, "ji7", ports=[w66, a[6], b[6]])
    Mult.Instance(AndModule, "ji8", ports=[w75, a[7], b[5]])

    Mult.Instance(AndModule, "ki1", ports=[w07, a[0], b[7]])
    Mult.Instance(AndModule, "ki2", ports=[w17, a[1], b[7]])
    Mult.Instance(AndModule, "ki3", ports=[w27, a[2], b[7]])
    Mult.Instance(AndModule, "ki4", ports=[w37, a[3], b[7]])
    Mult.Instance(AndModule, "ki5", ports=[w47, a[4], b[7]])
    Mult.Instance(AndModule, "ki6", ports=[w57, a[5], b[7]])
    Mult.Instance(AndModule, "ki7", ports=[w67, a[6], b[7]])
    Mult.Instance(AndModule, "ki8", ports=[w76, a[7], b[6]])

    Mult.Instance(AndModule, "mi1", ports=[w77, a[7], b[7]])

    Mult.Instance(HalfAdderModule, "ha5", ports=[w50, w41, a8, a9])
    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa4", ports=[a8, w32, b6, b7])
    Mult.Instance(FullAdderModule, "afa5", ports=[a9, a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(HalfAdderModule, "bfa3", ports=[b6, w23, c4, c5])
    Mult.Instance(FullAdderModule, "bfa4", ports=[b7, b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(HalfAdderModule, "cfa2", ports=[c4, w14, d2, d3])
    Mult.Instance(FullAdderModule, "cfa3", ports=[c5, c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(HalfAdderModule, "dfa1", ports=[d2, w05, res[5], e1])
    Mult.Instance(FullAdderModule, "dfa2", ports=[d3, d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    Mult.Instance(FullAdderModule, "efa1", ports=[e1, e2, w06, res[6], f1])
    Mult.Instance(FullAdderModule, "efa2", ports=[e3, e4, w16, f2, f3])
    Mult.Instance(FullAdderModule, "efa3", ports=[e5, e6, w26, f4, f5])
    Mult.Instance(FullAdderModule, "efa4", ports=[e7, e8, w36, f6, f7])
    Mult.Instance(FullAdderModule, "efa5", ports=[e9, e10, w46, f8, f9])
    Mult.Instance(FullAdderModule, "efa6", ports=[e11, e12, w56, f10, f11])
    Mult.Instance(FullAdderModule, "efa7", ports=[e13, w75, w66, f12, f13])

    Mult.Instance(FullAdderModule, "ffa1", ports=[f1, f2, w07, res[7], g1])
    Mult.Instance(FullAdderModule, "ffa2", ports=[f3, f4, w17, g2, g3])
    Mult.Instance(FullAdderModule, "ffa3", ports=[f5, f6, w27, g4, g5])
    Mult.Instance(FullAdderModule, "ffa4", ports=[f7, f8, w37, g6, g7])
    Mult.Instance(FullAdderModule, "ffa5", ports=[f9, f10, w47, g8, g9])
    Mult.Instance(FullAdderModule, "ffa6", ports=[f11, f12, w57, g10, g11])
    Mult.Instance(FullAdderModule, "ffa7", ports=[f13, w76, w67, g12, g13])

    res[4].assign(1)
    res[3].assign(1)
    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[g1, g2, res[8], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[g3, g4, h1, res[9], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[g5, g6, h2, res[10], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[g7, g8, h3, res[11], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[g9, g10, h4, res[12], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[g11, g12, h5, res[13], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w77, g13, h6, res[14], res[15]])

    return Mult


def paam01_v5_8x6_multiplier():  # 8x6 PAAM01-V5 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    ##    HighModule=Module('Logic_High');
    ##    high_out=HighModule.Output('a');
    ##    high_out.assign(1);
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v5_8x6")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 6)
    res = Mult.Output("p", 14)

    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")
    ##    net=Mult.Wire('net',6);
    ##    Mult.Instance(HighModule,'G1',ports=[net[0]]);
    ##    Mult.Instance(HighModule,'G2',ports=[net[1]]);
    ##    Mult.Instance(HighModule,'G3',ports=[net[2]]);
    ##    Mult.Instance(HighModule,'G4',ports=[net[3]]);
    ##    Mult.Instance(HighModule,'G5',ports=[net[4]]);
    ##    Mult.Instance(HighModule,'G6',ports=[net[5]]);

    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "mi1", ports=[w75, a[7], b[5]])

    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa5", ports=[a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(FullAdderModule, "bfa4", ports=[b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(HalfAdderModule, "cfa3", ports=[c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(HalfAdderModule, "dfa2", ports=[d4, w15, res[6], e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    res[5].assign(1)
    res[4].assign(1)
    res[3].assign(1)
    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[e3, e4, res[7], h2])
    Mult.Instance(FullAdderModule, "fad1", ports=[e5, e6, h2, res[8], h3])
    Mult.Instance(FullAdderModule, "fad2", ports=[e7, e8, h3, res[9], h4])
    Mult.Instance(FullAdderModule, "fad3", ports=[e9, e10, h4, res[10], h5])
    Mult.Instance(FullAdderModule, "fad4", ports=[e11, e12, h5, res[11], h6])
    Mult.Instance(FullAdderModule, "fad5", ports=[w75, e13, h6, res[12], res[13]])

    return Mult


def paam01_v5_8x8_multiplier():  # 8x8 PAAM01-V5 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v5_8x8")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 8)
    res = Mult.Output("p", 16)

    w60 = Mult.Wire("w60")
    w70 = Mult.Wire("w70")

    w51 = Mult.Wire("w51")
    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w42 = Mult.Wire("w42")
    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w33 = Mult.Wire("w33")
    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w24 = Mult.Wire("w24")
    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w15 = Mult.Wire("w15")
    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    w06 = Mult.Wire("w06")
    w16 = Mult.Wire("w16")
    w26 = Mult.Wire("w26")
    w36 = Mult.Wire("w36")
    w46 = Mult.Wire("w46")
    w56 = Mult.Wire("w56")
    w66 = Mult.Wire("w66")
    w76 = Mult.Wire("w76")

    w07 = Mult.Wire("w07")
    w17 = Mult.Wire("w17")
    w27 = Mult.Wire("w27")
    w37 = Mult.Wire("w37")
    w47 = Mult.Wire("w47")
    w57 = Mult.Wire("w57")
    w67 = Mult.Wire("w67")
    w77 = Mult.Wire("w77")

    a10 = Mult.Wire("a10")
    a11 = Mult.Wire("a11")
    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b8 = Mult.Wire("b8")
    b9 = Mult.Wire("b9")
    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c6 = Mult.Wire("c6")
    c7 = Mult.Wire("c7")
    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d4 = Mult.Wire("d4")
    d5 = Mult.Wire("d5")
    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e2 = Mult.Wire("e2")
    e3 = Mult.Wire("e3")
    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    f1 = Mult.Wire("f1")
    f2 = Mult.Wire("f2")
    f3 = Mult.Wire("f3")
    f4 = Mult.Wire("f4")
    f5 = Mult.Wire("f5")
    f6 = Mult.Wire("f6")
    f7 = Mult.Wire("f7")
    f8 = Mult.Wire("f8")
    f9 = Mult.Wire("f9")
    f10 = Mult.Wire("f10")
    f11 = Mult.Wire("f11")
    f12 = Mult.Wire("f12")
    f13 = Mult.Wire("f13")

    g1 = Mult.Wire("g1")
    g2 = Mult.Wire("g2")
    g3 = Mult.Wire("g3")
    g4 = Mult.Wire("g4")
    g5 = Mult.Wire("g5")
    g6 = Mult.Wire("g6")
    g7 = Mult.Wire("g7")
    g8 = Mult.Wire("g8")
    g9 = Mult.Wire("g9")
    g10 = Mult.Wire("g10")
    g11 = Mult.Wire("g11")
    g12 = Mult.Wire("g12")
    g13 = Mult.Wire("g13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")

    Mult.Instance(AndModule, "i11", ports=[w51, a[5], b[1]])
    Mult.Instance(AndModule, "i12", ports=[w60, a[6], b[0]])
    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li5", ports=[w42, a[4], b[2]])
    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi4", ports=[w33, a[3], b[3]])
    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi3", ports=[w24, a[2], b[4]])
    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii2", ports=[w15, a[1], b[5]])
    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "ji1", ports=[w06, a[0], b[6]])
    Mult.Instance(AndModule, "ji2", ports=[w16, a[1], b[6]])
    Mult.Instance(AndModule, "ji3", ports=[w26, a[2], b[6]])
    Mult.Instance(AndModule, "ji4", ports=[w36, a[3], b[6]])
    Mult.Instance(AndModule, "ji5", ports=[w46, a[4], b[6]])
    Mult.Instance(AndModule, "ji6", ports=[w56, a[5], b[6]])
    Mult.Instance(AndModule, "ji7", ports=[w66, a[6], b[6]])
    Mult.Instance(AndModule, "ji8", ports=[w75, a[7], b[5]])

    Mult.Instance(AndModule, "ki1", ports=[w07, a[0], b[7]])
    Mult.Instance(AndModule, "ki2", ports=[w17, a[1], b[7]])
    Mult.Instance(AndModule, "ki3", ports=[w27, a[2], b[7]])
    Mult.Instance(AndModule, "ki4", ports=[w37, a[3], b[7]])
    Mult.Instance(AndModule, "ki5", ports=[w47, a[4], b[7]])
    Mult.Instance(AndModule, "ki6", ports=[w57, a[5], b[7]])
    Mult.Instance(AndModule, "ki7", ports=[w67, a[6], b[7]])
    Mult.Instance(AndModule, "ki8", ports=[w76, a[7], b[6]])

    Mult.Instance(AndModule, "mi1", ports=[w77, a[7], b[7]])

    Mult.Instance(HalfAdderModule, "ha6", ports=[w60, w51, a10, a11])
    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa5", ports=[a10, w42, b8, b9])
    Mult.Instance(FullAdderModule, "afa6", ports=[a11, a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(HalfAdderModule, "bfa4", ports=[b8, w33, c6, c7])
    Mult.Instance(FullAdderModule, "bfa5", ports=[b9, b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(HalfAdderModule, "cfa3", ports=[c6, w24, d4, d5])
    Mult.Instance(FullAdderModule, "cfa4", ports=[c7, c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(HalfAdderModule, "dfa2", ports=[d4, w15, e2, e3])
    Mult.Instance(FullAdderModule, "dfa3", ports=[d5, d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    Mult.Instance(HalfAdderModule, "efa1", ports=[e2, w06, res[6], f1])
    Mult.Instance(FullAdderModule, "efa2", ports=[e3, e4, w16, f2, f3])
    Mult.Instance(FullAdderModule, "efa3", ports=[e5, e6, w26, f4, f5])
    Mult.Instance(FullAdderModule, "efa4", ports=[e7, e8, w36, f6, f7])
    Mult.Instance(FullAdderModule, "efa5", ports=[e9, e10, w46, f8, f9])
    Mult.Instance(FullAdderModule, "efa6", ports=[e11, e12, w56, f10, f11])
    Mult.Instance(FullAdderModule, "efa7", ports=[e13, w75, w66, f12, f13])

    Mult.Instance(FullAdderModule, "ffa1", ports=[f1, f2, w07, res[7], g1])
    Mult.Instance(FullAdderModule, "ffa2", ports=[f3, f4, w17, g2, g3])
    Mult.Instance(FullAdderModule, "ffa3", ports=[f5, f6, w27, g4, g5])
    Mult.Instance(FullAdderModule, "ffa4", ports=[f7, f8, w37, g6, g7])
    Mult.Instance(FullAdderModule, "ffa5", ports=[f9, f10, w47, g8, g9])
    Mult.Instance(FullAdderModule, "ffa6", ports=[f11, f12, w57, g10, g11])
    Mult.Instance(FullAdderModule, "ffa7", ports=[f13, w76, w67, g12, g13])

    res[5].assign(1)
    res[4].assign(1)
    res[3].assign(1)
    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[g1, g2, res[8], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[g3, g4, h1, res[9], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[g5, g6, h2, res[10], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[g7, g8, h3, res[11], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[g9, g10, h4, res[12], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[g11, g12, h5, res[13], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w77, g13, h6, res[14], res[15]])

    return Mult


def paam01_v6_8x6_multiplier():  # 8x6 PAAM01-V6 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    ##    HighModule=Module('Logic_High');
    ##    high_out=HighModule.Output('a');
    ##    high_out.assign(1);
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v6_8x6")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 6)
    res = Mult.Output("p", 14)

    w70 = Mult.Wire("w70")

    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")
    ##    net=Mult.Wire('net',7);
    ##    Mult.Instance(HighModule,'G1',ports=[net[0]]);
    ##    Mult.Instance(HighModule,'G2',ports=[net[1]]);
    ##    Mult.Instance(HighModule,'G3',ports=[net[2]]);
    ##    Mult.Instance(HighModule,'G4',ports=[net[3]]);
    ##    Mult.Instance(HighModule,'G5',ports=[net[4]]);
    ##    Mult.Instance(HighModule,'G6',ports=[net[5]]);
    ##    Mult.Instance(HighModule,'G7',ports=[net[6]]);

    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "mi1", ports=[w75, a[7], b[5]])

    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa6", ports=[a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(HalfAdderModule, "bfa5", ports=[b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(HalfAdderModule, "cfa4", ports=[c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(HalfAdderModule, "dfa3", ports=[d6, w25, res[7], e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    res[6].assign(1)
    res[5].assign(1)
    res[4].assign(1)
    res[3].assign(1)
    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[e5, e6, res[8], h3])
    Mult.Instance(FullAdderModule, "fad1", ports=[e7, e8, h3, res[9], h4])
    Mult.Instance(FullAdderModule, "fad2", ports=[e9, e10, h4, res[10], h5])
    Mult.Instance(FullAdderModule, "fad3", ports=[e11, e12, h5, res[11], h6])
    Mult.Instance(FullAdderModule, "fad4", ports=[w75, e13, h6, res[12], res[13]])

    return Mult


def paam01_v6_8x8_multiplier():  # 8x8 PAAM01-V6 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v6_8x8")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 8)
    res = Mult.Output("p", 16)

    w70 = Mult.Wire("w70")

    w61 = Mult.Wire("w61")
    w71 = Mult.Wire("w71")

    w52 = Mult.Wire("w52")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w43 = Mult.Wire("w43")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w34 = Mult.Wire("w34")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w25 = Mult.Wire("w25")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    w16 = Mult.Wire("w16")
    w26 = Mult.Wire("w26")
    w36 = Mult.Wire("w36")
    w46 = Mult.Wire("w46")
    w56 = Mult.Wire("w56")
    w66 = Mult.Wire("w66")
    w76 = Mult.Wire("w76")

    w07 = Mult.Wire("w07")
    w17 = Mult.Wire("w17")
    w27 = Mult.Wire("w27")
    w37 = Mult.Wire("w37")
    w47 = Mult.Wire("w47")
    w57 = Mult.Wire("w57")
    w67 = Mult.Wire("w67")
    w77 = Mult.Wire("w77")

    a12 = Mult.Wire("a12")
    a13 = Mult.Wire("a13")

    b10 = Mult.Wire("b10")
    b11 = Mult.Wire("b11")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c8 = Mult.Wire("c8")
    c9 = Mult.Wire("c9")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d6 = Mult.Wire("d6")
    d7 = Mult.Wire("d7")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e4 = Mult.Wire("e4")
    e5 = Mult.Wire("e5")
    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    f2 = Mult.Wire("f2")
    f3 = Mult.Wire("f3")
    f4 = Mult.Wire("f4")
    f5 = Mult.Wire("f5")
    f6 = Mult.Wire("f6")
    f7 = Mult.Wire("f7")
    f8 = Mult.Wire("f8")
    f9 = Mult.Wire("f9")
    f10 = Mult.Wire("f10")
    f11 = Mult.Wire("f11")
    f12 = Mult.Wire("f12")
    f13 = Mult.Wire("f13")

    g1 = Mult.Wire("g1")
    g2 = Mult.Wire("g2")
    g3 = Mult.Wire("g3")
    g4 = Mult.Wire("g4")
    g5 = Mult.Wire("g5")
    g6 = Mult.Wire("g6")
    g7 = Mult.Wire("g7")
    g8 = Mult.Wire("g8")
    g9 = Mult.Wire("g9")
    g10 = Mult.Wire("g10")
    g11 = Mult.Wire("g11")
    g12 = Mult.Wire("g12")
    g13 = Mult.Wire("g13")

    h1 = Mult.Wire("h1")
    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")

    Mult.Instance(AndModule, "i13", ports=[w61, a[6], b[1]])
    Mult.Instance(AndModule, "i14", ports=[w70, a[7], b[0]])

    Mult.Instance(AndModule, "li6", ports=[w52, a[5], b[2]])
    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi5", ports=[w43, a[4], b[3]])
    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi4", ports=[w34, a[3], b[4]])
    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii3", ports=[w25, a[2], b[5]])
    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "ji2", ports=[w16, a[1], b[6]])
    Mult.Instance(AndModule, "ji3", ports=[w26, a[2], b[6]])
    Mult.Instance(AndModule, "ji4", ports=[w36, a[3], b[6]])
    Mult.Instance(AndModule, "ji5", ports=[w46, a[4], b[6]])
    Mult.Instance(AndModule, "ji6", ports=[w56, a[5], b[6]])
    Mult.Instance(AndModule, "ji7", ports=[w66, a[6], b[6]])
    Mult.Instance(AndModule, "ji8", ports=[w75, a[7], b[5]])

    Mult.Instance(AndModule, "ki1", ports=[w07, a[0], b[7]])
    Mult.Instance(AndModule, "ki2", ports=[w17, a[1], b[7]])
    Mult.Instance(AndModule, "ki3", ports=[w27, a[2], b[7]])
    Mult.Instance(AndModule, "ki4", ports=[w37, a[3], b[7]])
    Mult.Instance(AndModule, "ki5", ports=[w47, a[4], b[7]])
    Mult.Instance(AndModule, "ki6", ports=[w57, a[5], b[7]])
    Mult.Instance(AndModule, "ki7", ports=[w67, a[6], b[7]])
    Mult.Instance(AndModule, "ki8", ports=[w76, a[7], b[6]])

    Mult.Instance(AndModule, "mi1", ports=[w77, a[7], b[7]])

    Mult.Instance(HalfAdderModule, "ha7", ports=[w70, w61, a12, a13])

    Mult.Instance(HalfAdderModule, "afa6", ports=[a12, w52, b10, b11])
    Mult.Instance(FullAdderModule, "afa7", ports=[a13, w71, w62, b12, b13])

    Mult.Instance(HalfAdderModule, "bfa5", ports=[b10, w43, c8, c9])
    Mult.Instance(FullAdderModule, "bfa6", ports=[b11, b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(HalfAdderModule, "cfa4", ports=[c8, w34, d6, d7])
    Mult.Instance(FullAdderModule, "cfa5", ports=[c9, c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(HalfAdderModule, "dfa3", ports=[d6, w25, e4, e5])
    Mult.Instance(FullAdderModule, "dfa4", ports=[d7, d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    Mult.Instance(HalfAdderModule, "efa2", ports=[e4, w16, f2, f3])
    Mult.Instance(FullAdderModule, "efa3", ports=[e5, e6, w26, f4, f5])
    Mult.Instance(FullAdderModule, "efa4", ports=[e7, e8, w36, f6, f7])
    Mult.Instance(FullAdderModule, "efa5", ports=[e9, e10, w46, f8, f9])
    Mult.Instance(FullAdderModule, "efa6", ports=[e11, e12, w56, f10, f11])
    Mult.Instance(FullAdderModule, "efa7", ports=[e13, w75, w66, f12, f13])

    Mult.Instance(HalfAdderModule, "ffa1", ports=[f2, w07, res[7], g1])
    Mult.Instance(FullAdderModule, "ffa2", ports=[f3, f4, w17, g2, g3])
    Mult.Instance(FullAdderModule, "ffa3", ports=[f5, f6, w27, g4, g5])
    Mult.Instance(FullAdderModule, "ffa4", ports=[f7, f8, w37, g6, g7])
    Mult.Instance(FullAdderModule, "ffa5", ports=[f9, f10, w47, g8, g9])
    Mult.Instance(FullAdderModule, "ffa6", ports=[f11, f12, w57, g10, g11])
    Mult.Instance(FullAdderModule, "ffa7", ports=[f13, w76, w67, g12, g13])

    res[6].assign(1)
    res[5].assign(1)
    res[4].assign(1)
    res[3].assign(1)
    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[g1, g2, res[8], h1])
    Mult.Instance(FullAdderModule, "fad1", ports=[g3, g4, h1, res[9], h2])
    Mult.Instance(FullAdderModule, "fad2", ports=[g5, g6, h2, res[10], h3])
    Mult.Instance(FullAdderModule, "fad3", ports=[g7, g8, h3, res[11], h4])
    Mult.Instance(FullAdderModule, "fad4", ports=[g9, g10, h4, res[12], h5])
    Mult.Instance(FullAdderModule, "fad5", ports=[g11, g12, h5, res[13], h6])
    Mult.Instance(FullAdderModule, "fad6", ports=[w77, g13, h6, res[14], res[15]])

    return Mult


def paam01_v7_8x6_multiplier():  # 8x6 PAAM01-V7 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    ##    AndModule.Instance('and','and1',ports=[res,inp1,inp2]);
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    ##    OrModule.Instance('or','or1',ports=[res,inp1,inp2]);
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    ##    XorModule.Instance('xor','xor1',ports=[res,inp1,inp2]);
    ##    HighModule=Module('Logic_High');
    ##    high_out=HighModule.Output('a');
    ##    high_out.assign(1);
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v7_8x6")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 6)
    res = Mult.Output("p", 14)
    w71 = Mult.Wire("w71")
    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")
    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")
    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")
    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")
    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")
    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")
    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")
    ##    net=Mult.Wire('net',8);
    ##    Mult.Instance(HighModule,'G1',ports=[net[0]]);
    ##    Mult.Instance(HighModule,'G2',ports=[net[1]]);
    ##    Mult.Instance(HighModule,'G3',ports=[net[2]]);
    ##    Mult.Instance(HighModule,'G4',ports=[net[3]]);
    ##    Mult.Instance(HighModule,'G5',ports=[net[4]]);
    ##    Mult.Instance(HighModule,'G6',ports=[net[5]]);
    ##    Mult.Instance(HighModule,'G7',ports=[net[6]]);
    ##    Mult.Instance(HighModule,'G8',ports=[net[7]]);

    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "mi1", ports=[w75, a[7], b[5]])

    Mult.Instance(HalfAdderModule, "afa7", ports=[w71, w62, b12, b13])

    Mult.Instance(HalfAdderModule, "bfa6", ports=[b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(HalfAdderModule, "cfa5", ports=[c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(HalfAdderModule, "dfa4", ports=[d8, w35, res[8], e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    res[7].assign(1)
    res[6].assign(1)
    res[5].assign(1)
    res[4].assign(1)
    res[3].assign(1)
    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[e7, e8, res[9], h4])
    Mult.Instance(FullAdderModule, "fad1", ports=[e9, e10, h4, res[10], h5])
    Mult.Instance(FullAdderModule, "fad2", ports=[e11, e12, h5, res[11], h6])
    Mult.Instance(FullAdderModule, "fad3", ports=[w75, e13, h6, res[12], res[13]])

    return Mult


def paam01_v7_8x8_multiplier():  # 8x8 PAAM01-V7 Approximate Multiplier

    AndModule = Module("and_2inp")
    andoutp = AndModule.Output("res")
    andinp1 = AndModule.Input("inp1")
    andinp2 = AndModule.Input("inp2")
    andoutp.assign(And(andinp1, andinp2))
    OrModule = Module("or_2inp")
    oroutp = OrModule.Output("res")
    orinp1 = OrModule.Input("inp1")
    orinp2 = OrModule.Input("inp2")
    oroutp.assign(Or(orinp1, orinp2))
    XorModule = Module("xor_2inp")
    xoroutp = XorModule.Output("res")
    xorinp1 = XorModule.Input("inp1")
    xorinp2 = XorModule.Input("inp2")
    xoroutp.assign(Xor(xorinp1, xorinp2))
    HalfAdderModule = Module("halfadder")
    HA_inp1 = HalfAdderModule.Input("a")
    HA_inp2 = HalfAdderModule.Input("b")
    HA_sum = HalfAdderModule.Output("sum")
    HA_carry_out = HalfAdderModule.Output("cout")
    HalfAdderModule.Instance(XorModule, "g1", ports=[HA_sum, HA_inp1, HA_inp2])
    HalfAdderModule.Instance(AndModule, "g2", ports=[HA_carry_out, HA_inp1, HA_inp2])

    FullAdderModule = Module("fulladder")
    FA_inp1 = FullAdderModule.Input("a")
    FA_inp2 = FullAdderModule.Input("b")
    FA_cin = FullAdderModule.Input("cin")
    FA_sum = FullAdderModule.Output("sum")
    w1 = FullAdderModule.Wire("w1")
    w2 = FullAdderModule.Wire("w2")
    w3 = FullAdderModule.Wire("w3")
    FA_carry_out = FullAdderModule.Output("cout")
    FullAdderModule.Instance(XorModule, "g1", ports=[w1, FA_inp1, FA_inp2])
    FullAdderModule.Instance(XorModule, "g2", ports=[FA_sum, w1, FA_cin])
    FullAdderModule.Instance(AndModule, "g3", ports=[w2, FA_inp1, FA_inp2])
    FullAdderModule.Instance(AndModule, "g4", ports=[w3, w1, FA_cin])
    FullAdderModule.Instance(OrModule, "g5", ports=[FA_carry_out, w3, w2])

    Mult = Module("paam01_v7_8x8")
    a = Mult.Input("a", 8)
    b = Mult.Input("b", 8)
    res = Mult.Output("p", 16)

    w71 = Mult.Wire("w71")

    w62 = Mult.Wire("w62")
    w72 = Mult.Wire("w72")

    w53 = Mult.Wire("w53")
    w63 = Mult.Wire("w63")
    w73 = Mult.Wire("w73")

    w44 = Mult.Wire("w44")
    w54 = Mult.Wire("w54")
    w64 = Mult.Wire("w64")
    w74 = Mult.Wire("w74")

    w35 = Mult.Wire("w35")
    w45 = Mult.Wire("w45")
    w55 = Mult.Wire("w55")
    w65 = Mult.Wire("w65")
    w75 = Mult.Wire("w75")

    w26 = Mult.Wire("w26")
    w36 = Mult.Wire("w36")
    w46 = Mult.Wire("w46")
    w56 = Mult.Wire("w56")
    w66 = Mult.Wire("w66")
    w76 = Mult.Wire("w76")

    w17 = Mult.Wire("w17")
    w27 = Mult.Wire("w27")
    w37 = Mult.Wire("w37")
    w47 = Mult.Wire("w47")
    w57 = Mult.Wire("w57")
    w67 = Mult.Wire("w67")
    w77 = Mult.Wire("w77")

    b12 = Mult.Wire("b12")
    b13 = Mult.Wire("b13")

    c10 = Mult.Wire("c10")
    c11 = Mult.Wire("c11")
    c12 = Mult.Wire("c12")
    c13 = Mult.Wire("c13")

    d8 = Mult.Wire("d8")
    d9 = Mult.Wire("d9")
    d10 = Mult.Wire("d10")
    d11 = Mult.Wire("d11")
    d12 = Mult.Wire("d12")
    d13 = Mult.Wire("d13")

    e6 = Mult.Wire("e6")
    e7 = Mult.Wire("e7")
    e8 = Mult.Wire("e8")
    e9 = Mult.Wire("e9")
    e10 = Mult.Wire("e10")
    e11 = Mult.Wire("e11")
    e12 = Mult.Wire("e12")
    e13 = Mult.Wire("e13")

    f4 = Mult.Wire("f4")
    f5 = Mult.Wire("f5")
    f6 = Mult.Wire("f6")
    f7 = Mult.Wire("f7")
    f8 = Mult.Wire("f8")
    f9 = Mult.Wire("f9")
    f10 = Mult.Wire("f10")
    f11 = Mult.Wire("f11")
    f12 = Mult.Wire("f12")
    f13 = Mult.Wire("f13")

    g3 = Mult.Wire("g3")
    g4 = Mult.Wire("g4")
    g5 = Mult.Wire("g5")
    g6 = Mult.Wire("g6")
    g7 = Mult.Wire("g7")
    g8 = Mult.Wire("g8")
    g9 = Mult.Wire("g9")
    g10 = Mult.Wire("g10")
    g11 = Mult.Wire("g11")
    g12 = Mult.Wire("g12")
    g13 = Mult.Wire("g13")

    h2 = Mult.Wire("h2")
    h3 = Mult.Wire("h3")
    h4 = Mult.Wire("h4")
    h5 = Mult.Wire("h5")
    h6 = Mult.Wire("h6")

    Mult.Instance(AndModule, "li7", ports=[w62, a[6], b[2]])
    Mult.Instance(AndModule, "li8", ports=[w71, a[7], b[1]])

    Mult.Instance(AndModule, "gi6", ports=[w53, a[5], b[3]])
    Mult.Instance(AndModule, "gi7", ports=[w63, a[6], b[3]])
    Mult.Instance(AndModule, "gi8", ports=[w72, a[7], b[2]])

    Mult.Instance(AndModule, "hi5", ports=[w44, a[4], b[4]])
    Mult.Instance(AndModule, "hi6", ports=[w54, a[5], b[4]])
    Mult.Instance(AndModule, "hi7", ports=[w64, a[6], b[4]])
    Mult.Instance(AndModule, "hi8", ports=[w73, a[7], b[3]])

    Mult.Instance(AndModule, "ii4", ports=[w35, a[3], b[5]])
    Mult.Instance(AndModule, "ii5", ports=[w45, a[4], b[5]])
    Mult.Instance(AndModule, "ii6", ports=[w55, a[5], b[5]])
    Mult.Instance(AndModule, "ii7", ports=[w65, a[6], b[5]])
    Mult.Instance(AndModule, "ii8", ports=[w74, a[7], b[4]])

    Mult.Instance(AndModule, "ji3", ports=[w26, a[2], b[6]])
    Mult.Instance(AndModule, "ji4", ports=[w36, a[3], b[6]])
    Mult.Instance(AndModule, "ji5", ports=[w46, a[4], b[6]])
    Mult.Instance(AndModule, "ji6", ports=[w56, a[5], b[6]])
    Mult.Instance(AndModule, "ji7", ports=[w66, a[6], b[6]])
    Mult.Instance(AndModule, "ji8", ports=[w75, a[7], b[5]])

    Mult.Instance(AndModule, "ki2", ports=[w17, a[1], b[7]])
    Mult.Instance(AndModule, "ki3", ports=[w27, a[2], b[7]])
    Mult.Instance(AndModule, "ki4", ports=[w37, a[3], b[7]])
    Mult.Instance(AndModule, "ki5", ports=[w47, a[4], b[7]])
    Mult.Instance(AndModule, "ki6", ports=[w57, a[5], b[7]])
    Mult.Instance(AndModule, "ki7", ports=[w67, a[6], b[7]])
    Mult.Instance(AndModule, "ki8", ports=[w76, a[7], b[6]])

    Mult.Instance(AndModule, "mi1", ports=[w77, a[7], b[7]])

    Mult.Instance(HalfAdderModule, "afa7", ports=[w71, w62, b12, b13])

    Mult.Instance(HalfAdderModule, "bfa6", ports=[b12, w53, c10, c11])
    Mult.Instance(FullAdderModule, "bfa7", ports=[b13, w72, w63, c12, c13])

    Mult.Instance(HalfAdderModule, "cfa5", ports=[c10, w44, d8, d9])
    Mult.Instance(FullAdderModule, "cfa6", ports=[c11, c12, w54, d10, d11])
    Mult.Instance(FullAdderModule, "cfa7", ports=[c13, w73, w64, d12, d13])

    Mult.Instance(HalfAdderModule, "dfa4", ports=[d8, w35, e6, e7])
    Mult.Instance(FullAdderModule, "dfa5", ports=[d9, d10, w45, e8, e9])
    Mult.Instance(FullAdderModule, "dfa6", ports=[d11, d12, w55, e10, e11])
    Mult.Instance(FullAdderModule, "dfa7", ports=[d13, w74, w65, e12, e13])

    Mult.Instance(HalfAdderModule, "efa3", ports=[e6, w26, f4, f5])
    Mult.Instance(FullAdderModule, "efa4", ports=[e7, e8, w36, f6, f7])
    Mult.Instance(FullAdderModule, "efa5", ports=[e9, e10, w46, f8, f9])
    Mult.Instance(FullAdderModule, "efa6", ports=[e11, e12, w56, f10, f11])
    Mult.Instance(FullAdderModule, "efa7", ports=[e13, w75, w66, f12, f13])

    Mult.Instance(HalfAdderModule, "ffa2", ports=[f4, w17, res[8], g3])
    Mult.Instance(FullAdderModule, "ffa3", ports=[f5, f6, w27, g4, g5])
    Mult.Instance(FullAdderModule, "ffa4", ports=[f7, f8, w37, g6, g7])
    Mult.Instance(FullAdderModule, "ffa5", ports=[f9, f10, w47, g8, g9])
    Mult.Instance(FullAdderModule, "ffa6", ports=[f11, f12, w57, g10, g11])
    Mult.Instance(FullAdderModule, "ffa7", ports=[f13, w76, w67, g12, g13])

    res[7].assign(1)
    res[6].assign(1)
    res[5].assign(1)
    res[4].assign(1)
    res[3].assign(1)
    res[2].assign(1)
    res[1].assign(1)
    res[0].assign(1)

    Mult.Instance(HalfAdderModule, "had1", ports=[g3, g4, res[9], h2])
    Mult.Instance(FullAdderModule, "fad1", ports=[g5, g6, h2, res[10], h3])
    Mult.Instance(FullAdderModule, "fad2", ports=[g7, g8, h3, res[11], h4])
    Mult.Instance(FullAdderModule, "fad3", ports=[g9, g10, h4, res[12], h5])
    Mult.Instance(FullAdderModule, "fad4", ports=[g11, g12, h5, res[13], h6])
    Mult.Instance(FullAdderModule, "fad5", ports=[w77, g13, h6, res[14], res[15]])

    return Mult
