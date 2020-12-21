

module bam_8x8
(
  input [8-1:0] a,
  input [8-1:0] b,
  output [16-1:0] p
);

  wire w10;
  wire w20;
  wire w30;
  wire w40;
  wire w50;
  wire w60;
  wire w70;
  wire w01;
  wire w11;
  wire w21;
  wire w31;
  wire w41;
  wire w51;
  wire w61;
  wire w71;
  wire w02;
  wire w12;
  wire w22;
  wire w32;
  wire w42;
  wire w52;
  wire w62;
  wire w72;
  wire w03;
  wire w13;
  wire w23;
  wire w33;
  wire w43;
  wire w53;
  wire w63;
  wire w73;
  wire w04;
  wire w14;
  wire w24;
  wire w34;
  wire w44;
  wire w54;
  wire w64;
  wire w74;
  wire w05;
  wire w15;
  wire w25;
  wire w35;
  wire w45;
  wire w55;
  wire w65;
  wire w75;
  wire w06;
  wire w16;
  wire w26;
  wire w36;
  wire w46;
  wire w56;
  wire w66;
  wire w76;
  wire w07;
  wire w17;
  wire w27;
  wire w37;
  wire w47;
  wire w57;
  wire w67;
  wire w77;
  wire c_10;
  wire s_11;
  wire c_11;
  wire s_12;
  wire c_12;
  wire s_13;
  wire c_13;
  wire s_14;
  wire c_14;
  wire s_15;
  wire c_15;
  wire s_16;
  wire c_16;
  wire c_20;
  wire s_21;
  wire c_21;
  wire s_22;
  wire c_22;
  wire s_23;
  wire c_23;
  wire s_24;
  wire c_24;
  wire s_25;
  wire c_25;
  wire s_26;
  wire c_26;
  wire c_30;
  wire s_31;
  wire c_31;
  wire s_32;
  wire c_32;
  wire s_33;
  wire c_33;
  wire s_34;
  wire c_34;
  wire s_35;
  wire c_35;
  wire s_36;
  wire c_36;
  wire c_40;
  wire s_41;
  wire c_41;
  wire s_42;
  wire c_42;
  wire s_43;
  wire c_43;
  wire s_44;
  wire c_44;
  wire s_45;
  wire c_45;
  wire s_46;
  wire c_46;
  wire c_50;
  wire s_51;
  wire c_51;
  wire s_52;
  wire c_52;
  wire s_53;
  wire c_53;
  wire s_54;
  wire c_54;
  wire s_55;
  wire c_55;
  wire s_56;
  wire c_56;
  wire c_60;
  wire s_61;
  wire c_61;
  wire s_62;
  wire c_62;
  wire s_63;
  wire c_63;
  wire s_64;
  wire c_64;
  wire s_65;
  wire c_65;
  wire s_66;
  wire c_66;
  wire c_70;
  wire s_71;
  wire c_71;
  wire s_72;
  wire c_72;
  wire s_73;
  wire c_73;
  wire s_74;
  wire c_74;
  wire s_75;
  wire c_75;
  wire s_76;
  wire c_76;
  wire c_80;
  wire c_81;
  wire c_82;
  wire c_83;
  wire c_84;
  wire c_85;

  and_2inp
  and_00
  (
    .res(p[0]),
    .inp1(a[0]),
    .inp2(b[0])
  );


  and_2inp
  and_01
  (
    .res(w01),
    .inp1(a[0]),
    .inp2(b[1])
  );


  and_2inp
  and_02
  (
    .res(w02),
    .inp1(a[0]),
    .inp2(b[2])
  );


  and_2inp
  and_03
  (
    .res(w03),
    .inp1(a[0]),
    .inp2(b[3])
  );


  and_2inp
  and_04
  (
    .res(w04),
    .inp1(a[0]),
    .inp2(b[4])
  );


  and_2inp
  and_05
  (
    .res(w05),
    .inp1(a[0]),
    .inp2(b[5])
  );


  and_2inp
  and_06
  (
    .res(w06),
    .inp1(a[0]),
    .inp2(b[6])
  );


  and_2inp
  and_07
  (
    .res(w07),
    .inp1(a[0]),
    .inp2(b[7])
  );


  and_2inp
  and_10
  (
    .res(w10),
    .inp1(a[1]),
    .inp2(b[0])
  );


  and_2inp
  and_11
  (
    .res(w11),
    .inp1(a[1]),
    .inp2(b[1])
  );


  and_2inp
  and_12
  (
    .res(w12),
    .inp1(a[1]),
    .inp2(b[2])
  );


  and_2inp
  and_13
  (
    .res(w13),
    .inp1(a[1]),
    .inp2(b[3])
  );


  and_2inp
  and_14
  (
    .res(w14),
    .inp1(a[1]),
    .inp2(b[4])
  );


  and_2inp
  and_15
  (
    .res(w15),
    .inp1(a[1]),
    .inp2(b[5])
  );


  and_2inp
  and_16
  (
    .res(w16),
    .inp1(a[1]),
    .inp2(b[6])
  );


  and_2inp
  and_17
  (
    .res(w17),
    .inp1(a[1]),
    .inp2(b[7])
  );


  and_2inp
  and_20
  (
    .res(w20),
    .inp1(a[2]),
    .inp2(b[0])
  );


  and_2inp
  and_21
  (
    .res(w21),
    .inp1(a[2]),
    .inp2(b[1])
  );


  and_2inp
  and_22
  (
    .res(w22),
    .inp1(a[2]),
    .inp2(b[2])
  );


  and_2inp
  and_23
  (
    .res(w23),
    .inp1(a[2]),
    .inp2(b[3])
  );


  and_2inp
  and_24
  (
    .res(w24),
    .inp1(a[2]),
    .inp2(b[4])
  );


  and_2inp
  and_25
  (
    .res(w25),
    .inp1(a[2]),
    .inp2(b[5])
  );


  and_2inp
  and_26
  (
    .res(w26),
    .inp1(a[2]),
    .inp2(b[6])
  );


  and_2inp
  and_27
  (
    .res(w27),
    .inp1(a[2]),
    .inp2(b[7])
  );


  and_2inp
  and_30
  (
    .res(w30),
    .inp1(a[3]),
    .inp2(b[0])
  );


  and_2inp
  and_31
  (
    .res(w31),
    .inp1(a[3]),
    .inp2(b[1])
  );


  and_2inp
  and_32
  (
    .res(w32),
    .inp1(a[3]),
    .inp2(b[2])
  );


  and_2inp
  and_33
  (
    .res(w33),
    .inp1(a[3]),
    .inp2(b[3])
  );


  and_2inp
  and_34
  (
    .res(w34),
    .inp1(a[3]),
    .inp2(b[4])
  );


  and_2inp
  and_35
  (
    .res(w35),
    .inp1(a[3]),
    .inp2(b[5])
  );


  and_2inp
  and_36
  (
    .res(w36),
    .inp1(a[3]),
    .inp2(b[6])
  );


  and_2inp
  and_37
  (
    .res(w37),
    .inp1(a[3]),
    .inp2(b[7])
  );


  and_2inp
  and_40
  (
    .res(w40),
    .inp1(a[4]),
    .inp2(b[0])
  );


  and_2inp
  and_41
  (
    .res(w41),
    .inp1(a[4]),
    .inp2(b[1])
  );


  and_2inp
  and_42
  (
    .res(w42),
    .inp1(a[4]),
    .inp2(b[2])
  );


  and_2inp
  and_43
  (
    .res(w43),
    .inp1(a[4]),
    .inp2(b[3])
  );


  and_2inp
  and_44
  (
    .res(w44),
    .inp1(a[4]),
    .inp2(b[4])
  );


  and_2inp
  and_45
  (
    .res(w45),
    .inp1(a[4]),
    .inp2(b[5])
  );


  and_2inp
  and_46
  (
    .res(w46),
    .inp1(a[4]),
    .inp2(b[6])
  );


  and_2inp
  and_47
  (
    .res(w47),
    .inp1(a[4]),
    .inp2(b[7])
  );


  and_2inp
  and_50
  (
    .res(w50),
    .inp1(a[5]),
    .inp2(b[0])
  );


  and_2inp
  and_51
  (
    .res(w51),
    .inp1(a[5]),
    .inp2(b[1])
  );


  and_2inp
  and_52
  (
    .res(w52),
    .inp1(a[5]),
    .inp2(b[2])
  );


  and_2inp
  and_53
  (
    .res(w53),
    .inp1(a[5]),
    .inp2(b[3])
  );


  and_2inp
  and_54
  (
    .res(w54),
    .inp1(a[5]),
    .inp2(b[4])
  );


  and_2inp
  and_55
  (
    .res(w55),
    .inp1(a[5]),
    .inp2(b[5])
  );


  and_2inp
  and_56
  (
    .res(w56),
    .inp1(a[5]),
    .inp2(b[6])
  );


  and_2inp
  and_57
  (
    .res(w57),
    .inp1(a[5]),
    .inp2(b[7])
  );


  and_2inp
  and_60
  (
    .res(w60),
    .inp1(a[6]),
    .inp2(b[0])
  );


  and_2inp
  and_61
  (
    .res(w61),
    .inp1(a[6]),
    .inp2(b[1])
  );


  and_2inp
  and_62
  (
    .res(w62),
    .inp1(a[6]),
    .inp2(b[2])
  );


  and_2inp
  and_63
  (
    .res(w63),
    .inp1(a[6]),
    .inp2(b[3])
  );


  and_2inp
  and_64
  (
    .res(w64),
    .inp1(a[6]),
    .inp2(b[4])
  );


  and_2inp
  and_65
  (
    .res(w65),
    .inp1(a[6]),
    .inp2(b[5])
  );


  and_2inp
  and_66
  (
    .res(w66),
    .inp1(a[6]),
    .inp2(b[6])
  );


  and_2inp
  and_67
  (
    .res(w67),
    .inp1(a[6]),
    .inp2(b[7])
  );


  and_2inp
  and_70
  (
    .res(w70),
    .inp1(a[7]),
    .inp2(b[0])
  );


  and_2inp
  and_71
  (
    .res(w71),
    .inp1(a[7]),
    .inp2(b[1])
  );


  and_2inp
  and_72
  (
    .res(w72),
    .inp1(a[7]),
    .inp2(b[2])
  );


  and_2inp
  and_73
  (
    .res(w73),
    .inp1(a[7]),
    .inp2(b[3])
  );


  and_2inp
  and_74
  (
    .res(w74),
    .inp1(a[7]),
    .inp2(b[4])
  );


  and_2inp
  and_75
  (
    .res(w75),
    .inp1(a[7]),
    .inp2(b[5])
  );


  and_2inp
  and_76
  (
    .res(w76),
    .inp1(a[7]),
    .inp2(b[6])
  );


  and_2inp
  and_77
  (
    .res(w77),
    .inp1(a[7]),
    .inp2(b[7])
  );


  halfadder
  ha1
  (
    .a(w10),
    .b(w01),
    .sum(p[1]),
    .cout(c_10)
  );


  halfadder
  ha2
  (
    .a(w20),
    .b(w11),
    .sum(s_11),
    .cout(c_11)
  );


  halfadder
  ha3
  (
    .a(w30),
    .b(w21),
    .sum(s_12),
    .cout(c_12)
  );


  halfadder
  ha4
  (
    .a(w40),
    .b(w31),
    .sum(s_13),
    .cout(c_13)
  );


  halfadder
  ha5
  (
    .a(w50),
    .b(w41),
    .sum(s_14),
    .cout(c_14)
  );


  halfadder
  ha6
  (
    .a(w60),
    .b(w51),
    .sum(s_15),
    .cout(c_15)
  );


  halfadder
  ha7
  (
    .a(w70),
    .b(w61),
    .sum(s_16),
    .cout(c_16)
  );


  fulladder
  fa12
  (
    .a(c_10),
    .b(s_11),
    .cin(w02),
    .sum(p[2]),
    .cout(c_20)
  );


  fulladder
  fa22
  (
    .a(c_11),
    .b(s_12),
    .cin(w12),
    .sum(s_21),
    .cout(c_21)
  );


  fulladder
  fa32
  (
    .a(c_12),
    .b(s_13),
    .cin(w22),
    .sum(s_22),
    .cout(c_22)
  );


  fulladder
  fa42
  (
    .a(c_13),
    .b(s_14),
    .cin(w32),
    .sum(s_23),
    .cout(c_23)
  );


  fulladder
  fa52
  (
    .a(c_14),
    .b(s_15),
    .cin(w42),
    .sum(s_24),
    .cout(c_24)
  );


  fulladder
  fa62
  (
    .a(c_15),
    .b(s_16),
    .cin(w52),
    .sum(s_25),
    .cout(c_25)
  );


  fulladder
  fa72
  (
    .a(c_16),
    .b(w71),
    .cin(w62),
    .sum(s_26),
    .cout(c_26)
  );


  fulladder
  fa13
  (
    .a(c_20),
    .b(s_21),
    .cin(w03),
    .sum(p[3]),
    .cout(c_30)
  );


  fulladder
  fa23
  (
    .a(c_21),
    .b(s_22),
    .cin(w13),
    .sum(s_31),
    .cout(c_31)
  );


  fulladder
  fa33
  (
    .a(c_22),
    .b(s_23),
    .cin(w23),
    .sum(s_32),
    .cout(c_32)
  );


  fulladder
  fa43
  (
    .a(c_23),
    .b(s_24),
    .cin(w33),
    .sum(s_33),
    .cout(c_33)
  );


  fulladder
  fa53
  (
    .a(c_24),
    .b(s_25),
    .cin(w43),
    .sum(s_34),
    .cout(c_34)
  );


  fulladder
  fa63
  (
    .a(c_25),
    .b(s_26),
    .cin(w53),
    .sum(s_35),
    .cout(c_35)
  );


  fulladder
  fa73
  (
    .a(c_26),
    .b(w72),
    .cin(w63),
    .sum(s_36),
    .cout(c_36)
  );


  fulladder
  fa14
  (
    .a(c_30),
    .b(s_31),
    .cin(w04),
    .sum(p[4]),
    .cout(c_40)
  );


  fulladder
  fa24
  (
    .a(c_31),
    .b(s_32),
    .cin(w14),
    .sum(s_41),
    .cout(c_41)
  );


  fulladder
  fa34
  (
    .a(c_32),
    .b(s_33),
    .cin(w24),
    .sum(s_42),
    .cout(c_42)
  );


  fulladder
  fa44
  (
    .a(c_33),
    .b(s_34),
    .cin(w34),
    .sum(s_43),
    .cout(c_43)
  );


  fulladder
  fa54
  (
    .a(c_34),
    .b(s_35),
    .cin(w44),
    .sum(s_44),
    .cout(c_44)
  );


  fulladder
  fa64
  (
    .a(c_35),
    .b(s_36),
    .cin(w54),
    .sum(s_45),
    .cout(c_45)
  );


  fulladder
  fa74
  (
    .a(c_36),
    .b(w73),
    .cin(w64),
    .sum(s_46),
    .cout(c_46)
  );


  fulladder
  fa15
  (
    .a(c_40),
    .b(s_41),
    .cin(w05),
    .sum(p[5]),
    .cout(c_50)
  );


  fulladder
  fa25
  (
    .a(c_41),
    .b(s_42),
    .cin(w15),
    .sum(s_51),
    .cout(c_51)
  );


  fulladder
  fa35
  (
    .a(c_42),
    .b(s_43),
    .cin(w25),
    .sum(s_52),
    .cout(c_52)
  );


  fulladder
  fa45
  (
    .a(c_43),
    .b(s_44),
    .cin(w35),
    .sum(s_53),
    .cout(c_53)
  );


  fulladder
  fa55
  (
    .a(c_44),
    .b(s_45),
    .cin(w45),
    .sum(s_54),
    .cout(c_54)
  );


  fulladder
  fa65
  (
    .a(c_45),
    .b(s_46),
    .cin(w55),
    .sum(s_55),
    .cout(c_55)
  );


  fulladder
  fa75
  (
    .a(c_46),
    .b(w74),
    .cin(w65),
    .sum(s_56),
    .cout(c_56)
  );


  fulladder
  fa16
  (
    .a(c_50),
    .b(s_51),
    .cin(w06),
    .sum(p[6]),
    .cout(c_60)
  );


  fulladder
  fa26
  (
    .a(c_51),
    .b(s_52),
    .cin(w16),
    .sum(s_61),
    .cout(c_61)
  );


  fulladder
  fa36
  (
    .a(c_52),
    .b(s_53),
    .cin(w26),
    .sum(s_62),
    .cout(c_62)
  );


  fulladder
  fa46
  (
    .a(c_53),
    .b(s_54),
    .cin(w36),
    .sum(s_63),
    .cout(c_63)
  );


  fulladder
  fa56
  (
    .a(c_54),
    .b(s_55),
    .cin(w46),
    .sum(s_64),
    .cout(c_64)
  );


  fulladder
  fa66
  (
    .a(c_55),
    .b(s_56),
    .cin(w56),
    .sum(s_65),
    .cout(c_65)
  );


  fulladder
  fa76
  (
    .a(c_56),
    .b(w75),
    .cin(w66),
    .sum(s_66),
    .cout(c_66)
  );


  fulladder
  fa17
  (
    .a(c_60),
    .b(s_61),
    .cin(w07),
    .sum(p[7]),
    .cout(c_70)
  );


  fulladder
  fa27
  (
    .a(c_61),
    .b(s_62),
    .cin(w17),
    .sum(s_71),
    .cout(c_71)
  );


  fulladder
  fa37
  (
    .a(c_62),
    .b(s_63),
    .cin(w27),
    .sum(s_72),
    .cout(c_72)
  );


  fulladder
  fa47
  (
    .a(c_63),
    .b(s_64),
    .cin(w37),
    .sum(s_73),
    .cout(c_73)
  );


  fulladder
  fa57
  (
    .a(c_64),
    .b(s_65),
    .cin(w47),
    .sum(s_74),
    .cout(c_74)
  );


  fulladder
  fa67
  (
    .a(c_65),
    .b(s_66),
    .cin(w57),
    .sum(s_75),
    .cout(c_75)
  );


  fulladder
  fa77
  (
    .a(c_66),
    .b(w76),
    .cin(w67),
    .sum(s_76),
    .cout(c_76)
  );


  halfadder
  hadd
  (
    .a(c_70),
    .b(s_71),
    .sum(p[8]),
    .cout(c_80)
  );


  fulladder
  fadd1
  (
    .a(c_71),
    .b(s_72),
    .cin(c_80),
    .sum(p[9]),
    .cout(c_81)
  );


  fulladder
  fadd2
  (
    .a(c_72),
    .b(s_73),
    .cin(c_81),
    .sum(p[10]),
    .cout(c_82)
  );


  fulladder
  fadd3
  (
    .a(c_73),
    .b(s_74),
    .cin(c_82),
    .sum(p[11]),
    .cout(c_83)
  );


  fulladder
  fadd4
  (
    .a(c_74),
    .b(s_75),
    .cin(c_83),
    .sum(p[12]),
    .cout(c_84)
  );


  fulladder
  fadd5
  (
    .a(c_75),
    .b(s_76),
    .cin(c_84),
    .sum(p[13]),
    .cout(c_85)
  );


  fulladder
  fadd6
  (
    .a(c_76),
    .b(w77),
    .cin(c_85),
    .sum(p[14]),
    .cout(p[15])
  );


endmodule



module and_2inp
(
  output res,
  input inp1,
  input inp2
);

  assign res = inp1 & inp2;

endmodule



module halfadder
(
  input a,
  input b,
  output sum,
  output cout
);


  xor_2inp
  g1
  (
    .res(sum),
    .inp1(a),
    .inp2(b)
  );


  and_2inp
  g2
  (
    .res(cout),
    .inp1(a),
    .inp2(b)
  );


endmodule



module xor_2inp
(
  output res,
  input inp1,
  input inp2
);

  assign res = inp1 ^ inp2;

endmodule



module fulladder
(
  input a,
  input b,
  input cin,
  output sum,
  output cout
);

  wire w1;
  wire w2;
  wire w3;

  xor_2inp
  g1
  (
    .res(w1),
    .inp1(a),
    .inp2(b)
  );


  xor_2inp
  g2
  (
    .res(sum),
    .inp1(w1),
    .inp2(cin)
  );


  and_2inp
  g3
  (
    .res(w2),
    .inp1(a),
    .inp2(b)
  );


  and_2inp
  g4
  (
    .res(w3),
    .inp1(w1),
    .inp2(cin)
  );


  or_2inp
  g5
  (
    .res(cout),
    .inp1(w3),
    .inp2(w2)
  );


endmodule



module or_2inp
(
  output res,
  input inp1,
  input inp2
);

  assign res = inp1 | inp2;

endmodule

