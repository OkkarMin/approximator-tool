

module paam_01_V_5_8x6
(
  input [8-1:0] a,
  input [6-1:0] b,
  output [14-1:0] p
);

  wire w60;
  wire w70;
  wire w51;
  wire w61;
  wire w71;
  wire w42;
  wire w52;
  wire w62;
  wire w72;
  wire w33;
  wire w43;
  wire w53;
  wire w63;
  wire w73;
  wire w24;
  wire w34;
  wire w44;
  wire w54;
  wire w64;
  wire w74;
  wire w15;
  wire w25;
  wire w35;
  wire w45;
  wire w55;
  wire w65;
  wire w75;
  wire s_15;
  wire c_15;
  wire s_16;
  wire c_16;
  wire s_24;
  wire c_24;
  wire s_25;
  wire c_25;
  wire s_26;
  wire c_26;
  wire s_33;
  wire c_33;
  wire s_34;
  wire c_34;
  wire s_35;
  wire c_35;
  wire s_36;
  wire c_36;
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
  wire c_61;
  wire c_62;
  wire c_63;
  wire c_64;
  wire c_65;
  assign p[0] = 1;
  assign p[1] = 1;
  assign p[2] = 1;
  assign p[3] = 1;
  assign p[4] = 1;
  assign p[5] = 1;

  and_2inp
  and_15
  (
    .res(w15),
    .inp1(a[1]),
    .inp2(b[5])
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


  halfadder
  ha52
  (
    .a(s_15),
    .b(w42),
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


  halfadder
  ha43
  (
    .a(s_24),
    .b(w33),
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


  halfadder
  ha34
  (
    .a(s_33),
    .b(w24),
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


  halfadder
  ha25
  (
    .a(s_42),
    .b(w15),
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

  assign p[6] = s_51;

  halfadder
  hadd1
  (
    .a(c_51),
    .b(s_52),
    .sum(p[7]),
    .cout(c_61)
  );


  fulladder
  fadd2
  (
    .a(c_52),
    .b(s_53),
    .cin(c_61),
    .sum(p[8]),
    .cout(c_62)
  );


  fulladder
  fadd3
  (
    .a(c_53),
    .b(s_54),
    .cin(c_62),
    .sum(p[9]),
    .cout(c_63)
  );


  fulladder
  fadd4
  (
    .a(c_54),
    .b(s_55),
    .cin(c_63),
    .sum(p[10]),
    .cout(c_64)
  );


  fulladder
  fadd5
  (
    .a(c_55),
    .b(s_56),
    .cin(c_64),
    .sum(p[11]),
    .cout(c_65)
  );


  fulladder
  fadd6
  (
    .a(c_56),
    .b(w75),
    .cin(c_65),
    .sum(p[12]),
    .cout(p[13])
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

