

module hoeraa_12b7inacc
(
  input [12-1:0] a,
  input [12-1:0] b,
  output [13-1:0] sum
);

  wire n1;
  wire n2;
  wire n3;
  wire n4;
  wire n5;
  wire n6;
  wire cout8;
  assign sum[0] = 1;
  assign sum[1] = 1;
  assign sum[2] = 1;
  assign sum[3] = 1;
  assign sum[4] = 1;

  or_2inp
  t1
  (
    .res(sum[5]),
    .inp1(a[5]),
    .inp2(b[5])
  );


  and_2inp
  t2
  (
    .res(n1),
    .inp1(a[6]),
    .inp2(b[6])
  );


  not_1inp
  t3
  (
    .res(n2),
    .inp(n1)
  );


  and_2inp
  t4
  (
    .res(n3),
    .inp1(a[5]),
    .inp2(b[5])
  );


  or_2inp
  t5
  (
    .res(n4),
    .inp1(a[6]),
    .inp2(b[6])
  );


  and_2inp
  t6
  (
    .res(n5),
    .inp1(n4),
    .inp2(n2)
  );


  and_2inp
  t7
  (
    .res(n6),
    .inp1(n3),
    .inp2(n1)
  );


  or_2inp
  t8
  (
    .res(sum[6]),
    .inp1(n5),
    .inp2(n6)
  );


  frcla_1b
  cla1
  (
    .a0(a[7]),
    .b0(b[7]),
    .c0(n1),
    .c1(cout8),
    .sum0(sum[7])
  );


  frcla_4b
  cla2
  (
    .a3(a[11]),
    .a2(a[10]),
    .a1(a[9]),
    .a0(a[8]),
    .b3(b[11]),
    .b2(b[10]),
    .b1(b[9]),
    .b0(b[8]),
    .c0(cout8),
    .c4(sum[12]),
    .sum3(sum[11]),
    .sum2(sum[10]),
    .sum1(sum[9]),
    .sum0(sum[8])
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



module frcla_1b
(
  input a0,
  input b0,
  input c0,
  output c1,
  output sum0
);

  wire g0;
  wire p0;

  and_2inp
  gate1
  (
    .res(g0),
    .inp1(a0),
    .inp2(b0)
  );


  xor_2inp
  gate5
  (
    .res(p0),
    .inp1(a0),
    .inp2(b0)
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

