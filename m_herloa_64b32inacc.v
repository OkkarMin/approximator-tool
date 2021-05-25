

module m_herloa_64b32inacc
(
  input [64-1:0] a,
  input [64-1:0] b,
  output [65-1:0] sum
);

  wire n1;
  wire n2;
  wire n3;
  wire w1;
  wire w2;
  wire w9;
  wire w10;
  wire w11;
  wire w12;
  wire cout32;
  wire cout36;
  wire cout40;
  wire cout44;
  wire cout48;
  wire cout52;
  wire cout56;
  wire cout60;
  assign sum[0] = 1;
  assign sum[1] = 1;
  assign sum[2] = 1;
  assign sum[3] = 1;
  assign sum[4] = 1;
  assign sum[5] = 1;
  assign sum[6] = 1;
  assign sum[7] = 1;
  assign sum[8] = 1;
  assign sum[9] = 1;
  assign sum[10] = 1;
  assign sum[11] = 1;
  assign sum[12] = 1;
  assign sum[13] = 1;
  assign sum[14] = 1;
  assign sum[15] = 1;
  assign sum[16] = 1;
  assign sum[17] = 1;
  assign sum[18] = 1;
  assign sum[19] = 1;
  assign sum[20] = 1;
  assign sum[21] = 1;
  assign sum[22] = 1;
  assign sum[23] = 1;
  assign sum[24] = 1;
  assign sum[25] = 1;
  assign sum[26] = 1;
  assign sum[27] = 1;
  assign sum[28] = 1;
  assign sum[29] = 1;
  assign sum[30] = 1;
  assign sum[31] = 1;

  xor_2inp
  t1
  (
    .res(n1),
    .inp1(a[35]),
    .inp2(b[35])
  );


  and_2inp
  t2
  (
    .res(n2),
    .inp1(a[34]),
    .inp2(b[34])
  );


  or_2inp
  t3
  (
    .res(sum[35]),
    .inp1(n1),
    .inp2(n2)
  );


  and_2inp
  t4
  (
    .res(n3),
    .inp1(n1),
    .inp2(n2)
  );


  or_2inp
  g1
  (
    .res(w1),
    .inp1(a[33]),
    .inp2(b[33])
  );


  or_2inp
  g2
  (
    .res(w2),
    .inp1(a[32]),
    .inp2(b[32])
  );


  or_2inp
  e1
  (
    .res(sum[33]),
    .inp1(n3),
    .inp2(w1)
  );


  or_2inp
  e2
  (
    .res(sum[32]),
    .inp1(n3),
    .inp2(w2)
  );


  or_2inp
  t5
  (
    .res(w9),
    .inp1(a[34]),
    .inp2(b[34])
  );


  not_1inp
  t6
  (
    .res(w10),
    .inp(n1)
  );


  nand_2inp
  t7
  (
    .res(w11),
    .inp1(w10),
    .inp2(n2)
  );


  and_2inp
  t8
  (
    .res(sum[34]),
    .inp1(w11),
    .inp2(w9)
  );


  and_2inp
  t9
  (
    .res(w12),
    .inp1(a[35]),
    .inp2(b[35])
  );


  frcla_4b
  cla1
  (
    .a3(a[35]),
    .a2(a[34]),
    .a1(a[33]),
    .a0(a[32]),
    .b3(b[35]),
    .b2(b[34]),
    .b1(b[33]),
    .b0(b[32]),
    .c0(cout32),
    .c4(cout36),
    .sum3(sum[35]),
    .sum2(sum[34]),
    .sum1(sum[33]),
    .sum0(sum[32])
  );


  frcla_4b
  cla2
  (
    .a3(a[39]),
    .a2(a[38]),
    .a1(a[37]),
    .a0(a[36]),
    .b3(b[39]),
    .b2(b[38]),
    .b1(b[37]),
    .b0(b[36]),
    .c0(cout36),
    .c4(cout40),
    .sum3(sum[39]),
    .sum2(sum[38]),
    .sum1(sum[37]),
    .sum0(sum[36])
  );


  frcla_4b
  cla3
  (
    .a3(a[43]),
    .a2(a[42]),
    .a1(a[41]),
    .a0(a[40]),
    .b3(b[43]),
    .b2(b[42]),
    .b1(b[41]),
    .b0(b[40]),
    .c0(cout40),
    .c4(cout44),
    .sum3(sum[43]),
    .sum2(sum[42]),
    .sum1(sum[41]),
    .sum0(sum[40])
  );


  frcla_4b
  cla4
  (
    .a3(a[47]),
    .a2(a[46]),
    .a1(a[45]),
    .a0(a[44]),
    .b3(b[47]),
    .b2(b[46]),
    .b1(b[45]),
    .b0(b[44]),
    .c0(cout44),
    .c4(cout48),
    .sum3(sum[47]),
    .sum2(sum[46]),
    .sum1(sum[45]),
    .sum0(sum[44])
  );


  frcla_4b
  cla5
  (
    .a3(a[51]),
    .a2(a[50]),
    .a1(a[49]),
    .a0(a[48]),
    .b3(b[51]),
    .b2(b[50]),
    .b1(b[49]),
    .b0(b[48]),
    .c0(cout48),
    .c4(cout52),
    .sum3(sum[51]),
    .sum2(sum[50]),
    .sum1(sum[49]),
    .sum0(sum[48])
  );


  frcla_4b
  cla6
  (
    .a3(a[55]),
    .a2(a[54]),
    .a1(a[53]),
    .a0(a[52]),
    .b3(b[55]),
    .b2(b[54]),
    .b1(b[53]),
    .b0(b[52]),
    .c0(cout52),
    .c4(cout56),
    .sum3(sum[55]),
    .sum2(sum[54]),
    .sum1(sum[53]),
    .sum0(sum[52])
  );


  frcla_4b
  cla7
  (
    .a3(a[59]),
    .a2(a[58]),
    .a1(a[57]),
    .a0(a[56]),
    .b3(b[59]),
    .b2(b[58]),
    .b1(b[57]),
    .b0(b[56]),
    .c0(cout56),
    .c4(cout60),
    .sum3(sum[59]),
    .sum2(sum[58]),
    .sum1(sum[57]),
    .sum0(sum[56])
  );


  frcla_4b
  cla8
  (
    .a3(a[63]),
    .a2(a[62]),
    .a1(a[61]),
    .a0(a[60]),
    .b3(b[63]),
    .b2(b[62]),
    .b1(b[61]),
    .b0(b[60]),
    .c0(cout60),
    .c4(sum[64]),
    .sum3(sum[63]),
    .sum2(sum[62]),
    .sum1(sum[61]),
    .sum0(sum[60])
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



module and_2inp
(
  output res,
  input inp1,
  input inp2
);

  assign res = inp1 & inp2;

endmodule



module or_2inp
(
  output res,
  input inp1,
  input inp2
);

  assign res = inp1 | inp2;

endmodule



module not_1inp
(
  output res,
  input inp
);

  assign res = !inp;

endmodule



module nand_2inp
(
  output res,
  input inp1,
  input inp2
);

  assign res = !(inp1 & inp2);

endmodule



module frcla_4b
(
  input a3,
  input a2,
  input a1,
  input a0,
  input b3,
  input b2,
  input b1,
  input b0,
  input c0,
  output c4,
  output sum3,
  output sum2,
  output sum1,
  output sum0
);

  wire g3;
  wire g2;
  wire g1;
  wire g0;
  wire p3;
  wire p2;
  wire p1;
  wire p0;
  wire c1;
  wire c2;
  wire c3;
  wire m1;
  wire m2;
  wire m3;
  wire m4;
  wire m5;
  wire m6;

  and_2inp
  gate1
  (
    .res(g0),
    .inp1(a0),
    .inp2(b0)
  );


  and_2inp
  gate2
  (
    .res(g1),
    .inp1(a1),
    .inp2(b1)
  );


  and_2inp
  gate3
  (
    .res(g2),
    .inp1(a2),
    .inp2(b2)
  );


  and_2inp
  gate4
  (
    .res(g3),
    .inp1(a3),
    .inp2(b3)
  );


  xor_2inp
  gate5
  (
    .res(p0),
    .inp1(a0),
    .inp2(b0)
  );


  xor_2inp
  gate6
  (
    .res(p1),
    .inp1(a1),
    .inp2(b1)
  );


  xor_2inp
  gate7
  (
    .res(p2),
    .inp1(a2),
    .inp2(b2)
  );


  xor_2inp
  gate8
  (
    .res(p3),
    .inp1(a3),
    .inp2(b3)
  );


  ao21
  comp1
  (
    .a(p1),
    .b(g0),
    .c(g1),
    .y(m1)
  );


  ao21
  comp2
  (
    .a(m1),
    .b(p2),
    .c(g2),
    .y(m2)
  );


  ao21
  comp3
  (
    .a(m2),
    .b(p3),
    .c(g3),
    .y(m3)
  );


  and_2inp
  and1
  (
    .res(m4),
    .inp1(p1),
    .inp2(p0)
  );


  and_2inp
  and2
  (
    .res(m5),
    .inp1(p2),
    .inp2(m4)
  );


  and_2inp
  and3
  (
    .res(m6),
    .inp1(p3),
    .inp2(m5)
  );


  ao21
  comp4
  (
    .a(m6),
    .b(c0),
    .c(m3),
    .y(c4)
  );


  ao21
  comp5
  (
    .a(m5),
    .b(c0),
    .c(m2),
    .y(c3)
  );


  ao21
  comp6
  (
    .a(m4),
    .b(c0),
    .c(m1),
    .y(c2)
  );


  ao21
  comp7
  (
    .a(p0),
    .b(c0),
    .c(g0),
    .y(c1)
  );


  xor_2inp
  xorg1
  (
    .res(sum0),
    .inp1(p0),
    .inp2(c0)
  );


  xor_2inp
  xorg2
  (
    .res(sum1),
    .inp1(p1),
    .inp2(c1)
  );


  xor_2inp
  xorg3
  (
    .res(sum2),
    .inp1(p2),
    .inp2(c2)
  );


  xor_2inp
  xorg4
  (
    .res(sum3),
    .inp1(p3),
    .inp2(c3)
  );


endmodule



module ao21
(
  input a,
  input b,
  input c,
  output y
);

  wire net;

  and_2inp
  t1
  (
    .res(net),
    .inp1(a),
    .inp2(b)
  );


  or_2inp
  t2
  (
    .res(y),
    .inp1(net),
    .inp2(c)
  );


endmodule

