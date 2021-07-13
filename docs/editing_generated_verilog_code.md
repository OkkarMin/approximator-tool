# Editing Generated Verilog Code

## Inaccurate-adder Generated Verilog Code Manual Change

[Adder verilog code generated using the tool](using_gui_tool.md#verilog-code-generator) will look like below (width and size depends upon chosen options)

```verilog
module hoaaned_32b10inacc
(
  input [32-1:0] a,      // to change
  input [32-1:0] b,      // to change
  output [33-1:0] sum    // to change
);

  wire n1;
  wire n2;
  wire n3;
  wire n4;
  wire n5;
  wire cout12;
  wire cout16;
  wire cout20;
  wire cout24;
  wire cout28;
  assign sum[0] = 1;    // to change
  assign sum[1] = 1;    // to change
  assign sum[2] = 1;    // to change
  assign sum[3] = 1;    // to change
  assign sum[4] = 1;    // to change
  assign sum[5] = 1;    // to change
  assign sum[6] = 1;    // to change
  assign sum[7] = 1;    // to change
```

you would need to modify the code accordingly to look like the one below.

```verilog
module hoaaned_32b10inacc
(
  a,                            // changed
  b,                            // changed
  sum                           // changed
);
  input [31:0] a;               // changed
  input [31:0] b;               // changed
  output [32:0] sum;            // changed

  wire n1;
  wire n2;
  wire n3;
  wire n4;
  wire n5;
  wire cout12;
  wire cout16;
  wire cout20;
  wire cout24;
  wire cout28;
  wire net[7:0];                // changed
  TIEL_HVT gate1(net[0]);       // changed
  TIEL_HVT gate2(net[1]);       // changed
  TIEL_HVT gate3(net[2]);       // changed
  TIEL_HVT gate4(net[3]);       // changed
  TIEL_HVT gate5(net[4]);       // changed
  TIEL_HVT gate6(net[5]);       // changed
  TIEL_HVT gate7(net[6]);       // changed
  TIEL_HVT gate8(net[7]);       // changed
  assign sum[7:0] = net[7:0];   // changed
```

<!-- ![Adder Verilog Generated Code After](_image/../_images/adder-code-gen-after.png) -->

## Inaccurate-multiplier Generated Verilog Code Manual Change

[Multiplier verilog code generated using the tool](using_gui_tool.md#verilog-code-generator) will look like below (width and size depends upon chosen options)

```verilog
module paam_01_V_7_8x6
(
  input [8-1:0] a,      // to change
  input [6-1:0] b,      // to change
  output [14-1:0] p     // to change
);

  wire w71;
  wire w62;
  wire w72;
  wire w53;
  wire w63;
  wire w73;
  wire w44;
  wire w54;
  wire w64;
  wire w74;
  wire w35;
  wire w45;
  wire w55;
  wire w65;
  wire w75;
  wire s_26;
  wire c_26;
  wire s_35;
  wire c_35;
  wire s_36;
  wire c_36;
  wire s_44;
  wire c_44;
  wire s_45;
  wire c_45;
  wire s_46;
  wire c_46;
  wire s_53;
  wire c_53;
  wire s_54;
  wire c_54;
  wire s_55;
  wire c_55;
  wire s_56;
  wire c_56;
  wire c_63;
  wire c_64;
  wire c_65;
  assign p[0] = 1;      // to change
  assign p[1] = 1;      // to change
  assign p[2] = 1;      // to change
  assign p[3] = 1;      // to change
  assign p[4] = 1;      // to change
  assign p[5] = 1;      // to change
  assign p[6] = 1;      // to change
  assign p[7] = 1;      // to change
  .
  .
  .
```

you would need to modify the code accordingly to look like the one below.

```verilog
module paam_01_V_7_8x6
(
  a,                    // changed
  b,                    // changed
  p                     // changed
);
  input [7:0] a;        // changed
  input [5:0] b;        // changed
  output [13:0] p;      // changed
  wire w71;
  wire w62;
  wire w72;
  wire w53;
  wire w63;
  wire w73;
  wire w44;
  wire w54;
  wire w64;
  wire w74;
  wire w35;
  wire w45;
  wire w55;
  wire w65;
  wire w75;
  wire s_26;
  wire c_26;
  wire s_35;
  wire c_35;
  wire s_36;
  wire c_36;
  wire s_44;
  wire c_44;
  wire s_45;
  wire c_45;
  wire s_46;
  wire c_46;
  wire s_53;
  wire c_53;
  wire s_54;
  wire c_54;
  wire s_55;
  wire c_55;
  wire s_56;
  wire c_56;
  wire c_63;
  wire c_64;
  wire c_65;
  wire net[7:0];            // changed
  TIEL_HVT gate1(net[0]);   // changed
  TIEL_HVT gate2(net[1]);   // changed
  TIEL_HVT gate3(net[2]);   // changed
  TIEL_HVT gate4(net[3]);   // changed
  TIEL_HVT gate5(net[4]);   // changed
  TIEL_HVT gate6(net[5]);   // changed
  TIEL_HVT gate7(net[6]);   // changed
  TIEL_HVT gate8(net[7]);   // changed
  assign p[7:0] = net[7:0]; // changed
  .
  .
  .
```
