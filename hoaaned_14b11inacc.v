

module hoaaned_14b11inacc
(
  input [14-1:0] a,
  input [14-1:0] b,
  output [15-1:0] sum
);

  wire n1;
  wire n2;
  wire n3;
  wire n4;
  wire n5;
  assign sum[0] = 1;
  assign sum[1] = 1;
  assign sum[2] = 1;
  assign sum[3] = 1;
  assign sum[4] = 1;
  assign sum[5] = 1;
  assign sum[6] = 1;
  assign sum[7] = 1;
  assign sum[8] = 1;

  or_2inp
  t1
  (
    .res(sum[9]),
    .inp1(a[9]),
    .inp2(b[9])
  );


  and_2inp
  t2
  (
    .res(n1),
    .inp1(a[9]),
    .inp2(b[9])
  );


  and_2inp
  t3
  (
    .res(n2),
    .inp1(a[10]),
    .inp2(b[10])
  );


  not_1inp
  t4
  (
    .res(n3),
    .inp(n2)
  );


  or_2inp
  t5
  (
    .res(n4),
    .inp1(a[10]),
    .inp2(b[10])
  );


  and_2inp
  t6
  (
    .res(n5),
    .inp1(n4),
    .inp2(n1)
  );


  or_2inp
  t7
  (
    .res(sum[10]),
    .inp1(n5),
    .inp2(n1)
  );


  frcla_3b
  cla1
  (
    .a2(a[13]),
    .a1(a[12]),
    .a0(a[11]),
    .b2(b[13]),
    .b1(b[12]),
    .b0(b[11]),
    .c0(n2),
    .c3(sum[14]),
    .sum2(sum[13]),
    .sum1(sum[12]),
    .sum0(sum[11])
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



module frcla_3b
(
  input a2,
  input a1,
  input a0,
  input b2,
  input b1,
  input b0,
  input c0,
  output c3,
  output sum2,
  output sum1,
  output sum0
);

  wire g2;
  wire g1;
  wire g0;
  wire p2;
  wire p1;
  wire p0;
  wire c1;
  wire c2;
  wire m1;
  wire m2;
  wire m4;
  wire m5;

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

