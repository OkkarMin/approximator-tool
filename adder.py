def HalfAdder(a, b):
    sum_ha = a ^ b
    carry_ha = a & b
    return (sum_ha, carry_ha)


def FullAdder(a, b, cin):
    sum_fa = a ^ b ^ cin
    carry_fa = (a & b) | (b & cin) | (cin & a)
    return (sum_fa, carry_fa)


def EstimateFullAdder1(a, b, cin):
    sum_fa = a ^ (b | cin)
    carry_fa = a | (b & cin)
    return (sum_fa, carry_fa)


def EstimateFullAdder2(a, b, cin):
    sum_fa = (a ^ b) & (not (cin))
    carry_fa = cin
    return (sum_fa, carry_fa)


def EstimateFullAdder3(a, b, cin):
    carry_fa = (a & b) | (b & cin) | (cin & a)
    if carry_fa == 0:
        sum_fa = 1
    else:
        sum_fa = 0
    return (sum_fa, carry_fa)


def EstimateFullAdder4(a, b, cin):
    carry_fa = a & (b | cin)
    sum_fa = (~(carry_fa) & (a | b | cin)) | (carry_fa & b & cin)
    return (sum_fa, carry_fa)
