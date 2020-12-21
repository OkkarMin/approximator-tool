

module m_herloa_15b12inacc
(
  input [15-1:0] a,
  input [15-1:0] b,
  output [16-1:0] sum
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
  assign sum[0] = 1;
  assign sum[1] = 1;
  assign sum[2] = 1;
  assign sum[3] = 1;
  assign sum[4] = 1;
  assign sum[5] = 1;
  assign sum[6] = 1;
  assign sum[7] = 1;

  xor_2inp
  t1
  (
    .res(n1),
    .inp1(a[11]),
    .inp2(b[11])
  );


  and_2inp
  t2
  (
    .res(n2),
    .inp1(a[10]),
    .inp2(b[10])
  );


  or_2inp
  t3
  (
    .res(sum[11]),
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
    .inp1(a[9]),
    .inp2(b[9])
  );


  or_2inp
  g2
  (
    .res(w2),
    .inp1(a[8]),
    .inp2(b[8])
  );


  or_2inp
  e1
  (
    .res(sum[9]),
    .inp1(n3),
    .inp2(w1)
  );


  or_2inp
  e2
  (
    .res(sum[8]),
    .inp1(n3),
    .inp2(w2)
  );


  or_2inp
  t5
  (
    .res(w9),
    .inp1(a[10]),
    .inp2(b[10])
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
    .res(sum[10]),
    .inp1(w11),
    .inp2(w9)
  );


  and_2inp
  t9
  (
    .res(w12),
    .inp1(a[11]),
    .inp2(b[11])
  );


  frcla_3b
  cla1
  (
    .a2(a[14]),
    .a1(a[13]),
    .a0(a[12]),
    .b2(b[14]),
    .b1(b[13]),
    .b0(b[12]),
    .c0(w12),
    .c3(sum[15]),
    .sum2(sum[14]),
    .sum1(sum[13]),
    .sum0(sum[12])
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

