

module heaa_32b12inacc
(
  input [32-1:0] a,
  input [32-1:0] b,
  output [33-1:0] sum
);

  wire w1;
  wire w2;
  wire w3;
  wire cout12;
  wire cout16;
  wire cout20;
  wire cout24;
  wire cout28;

  or_2inp
  t1
  (
    .res(sum[0]),
    .inp1(a[0]),
    .inp2(b[0])
  );


  or_2inp
  t2
  (
    .res(sum[1]),
    .inp1(a[1]),
    .inp2(b[1])
  );


  or_2inp
  t3
  (
    .res(sum[2]),
    .inp1(a[2]),
    .inp2(b[2])
  );


  or_2inp
  t4
  (
    .res(sum[3]),
    .inp1(a[3]),
    .inp2(b[3])
  );


  or_2inp
  t5
  (
    .res(sum[4]),
    .inp1(a[4]),
    .inp2(b[4])
  );


  or_2inp
  t6
  (
    .res(sum[5]),
    .inp1(a[5]),
    .inp2(b[5])
  );


  or_2inp
  t7
  (
    .res(sum[6]),
    .inp1(a[6]),
    .inp2(b[6])
  );


  or_2inp
  t8
  (
    .res(sum[7]),
    .inp1(a[7]),
    .inp2(b[7])
  );


  or_2inp
  t9
  (
    .res(sum[8]),
    .inp1(a[8]),
    .inp2(b[8])
  );


  or_2inp
  t10
  (
    .res(sum[9]),
    .inp1(a[9]),
    .inp2(b[9])
  );


  or_2inp
  t11
  (
    .res(sum[10]),
    .inp1(a[10]),
    .inp2(b[10])
  );


  or_2inp
  t12
  (
    .res(sum[11]),
    .inp1(a[11]),
    .inp2(b[11])
  );


  or_2inp
  t13
  (
    .res(sum[12]),
    .inp1(a[12]),
    .inp2(b[12])
  );


  or_2inp
  t14
  (
    .res(sum[13]),
    .inp1(a[13]),
    .inp2(b[13])
  );


  or_2inp
  t15
  (
    .res(sum[14]),
    .inp1(a[14]),
    .inp2(b[14])
  );


  and_2inp
  t16
  (
    .res(w1),
    .inp1(a[15]),
    .inp2(b[15])
  );


  not_1inp
  t17
  (
    .res(w2),
    .inp(w1)
  );


  or_2inp
  t18
  (
    .res(w3),
    .inp1(a[15]),
    .inp2(b[15])
  );


  and_2inp
  t19
  (
    .res(sum[15]),
    .inp1(w3),
    .inp2(w2)
  );


  frcla_4b
  cla1
  (
    .a3(a[15]),
    .a2(a[14]),
    .a1(a[13]),
    .a0(a[12]),
    .b3(b[15]),
    .b2(b[14]),
    .b1(b[13]),
    .b0(b[12]),
    .c0(cout12),
    .c4(cout16),
    .sum3(sum[15]),
    .sum2(sum[14]),
    .sum1(sum[13]),
    .sum0(sum[12])
  );


  frcla_4b
  cla2
  (
    .a3(a[19]),
    .a2(a[18]),
    .a1(a[17]),
    .a0(a[16]),
    .b3(b[19]),
    .b2(b[18]),
    .b1(b[17]),
    .b0(b[16]),
    .c0(cout16),
    .c4(cout20),
    .sum3(sum[19]),
    .sum2(sum[18]),
    .sum1(sum[17]),
    .sum0(sum[16])
  );


  frcla_4b
  cla3
  (
    .a3(a[23]),
    .a2(a[22]),
    .a1(a[21]),
    .a0(a[20]),
    .b3(b[23]),
    .b2(b[22]),
    .b1(b[21]),
    .b0(b[20]),
    .c0(cout20),
    .c4(cout24),
    .sum3(sum[23]),
    .sum2(sum[22]),
    .sum1(sum[21]),
    .sum0(sum[20])
  );


  frcla_4b
  cla4
  (
    .a3(a[27]),
    .a2(a[26]),
    .a1(a[25]),
    .a0(a[24]),
    .b3(b[27]),
    .b2(b[26]),
    .b1(b[25]),
    .b0(b[24]),
    .c0(cout24),
    .c4(cout28),
    .sum3(sum[27]),
    .sum2(sum[26]),
    .sum1(sum[25]),
    .sum0(sum[24])
  );


  frcla_4b
  cla5
  (
    .a3(a[31]),
    .a2(a[30]),
    .a1(a[29]),
    .a0(a[28]),
    .b3(b[31]),
    .b2(b[30]),
    .b1(b[29]),
    .b0(b[28]),
    .c0(cout28),
    .c4(sum[32]),
    .sum3(sum[31]),
    .sum2(sum[30]),
    .sum1(sum[29]),
    .sum0(sum[28])
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



module and_2inp
(
  output res,
  input inp1,
  input inp2
);

  assign res = inp1 & inp2;

endmodule



module not_1inp
(
  output res,
  input inp
);

  assign res = !inp;

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



module xor_2inp
(
  output res,
  input inp1,
  input inp2
);

  assign res = inp1 ^ inp2;

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

