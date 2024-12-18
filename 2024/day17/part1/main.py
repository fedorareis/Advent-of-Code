import pprint

ex = {"A": 729, "B": 0, "C": 0, "Program": [(0, 1), (5, 4), (3, 0)]}
input = {
    "A": 21539243,
    "B": 0,
    "C": 0,
    "Program": [(2, 4), (1, 3), (7, 5), (1, 5), (0, 3), (4, 1), (5, 5), (3, 0)],
}

result = []
# a = ex["A"]
# b = ex["B"]
# c = ex["C"]
# program = ex["Program"]

a = input["A"]
b = input["B"]
c = input["C"]
program = input["Program"]


# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.
# Combo operand 7 is reserved and will not appear in valid programs.
def getCombo(val):
    global a
    global b
    global c
    match val:
        case 0:
            return val
        case 1:
            return val
        case 2:
            return val
        case 3:
            return val
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c


# The adv instruction (opcode 0) performs division.
# The numerator is the value in the A register.
# The denominator is found by raising 2 to the power of the
# instruction's combo operand.
# (So, an operand of 2 would divide A by 4 (2^2);
#  an operand of 5 would divide A by 2^B.)
# The result of the division operation is truncated
# to an integer and then written to the A register.
def adv(val):
    global a
    global b
    global c
    val = getCombo(val)
    val = 2**val
    a = int(a / val)


# The bxl instruction (opcode 1) calculates the
# bitwise XOR of register B and the instruction's
# literal operand, then stores the result in register B.
def bxl(val):
    global a
    global b
    global c
    b = b ^ val


# The bst instruction (opcode 2) calculates the value of
# its combo operand modulo 8 (thereby keeping only its
# lowest 3 bits), then writes that value to the B register.
def bst(val):
    global a
    global b
    global c
    val = getCombo(val)
    b = val % 8


# The jnz instruction (opcode 3) does nothing if the
# A register is 0. However, if the A register is not zero,
# it jumps by setting the instruction pointer to the
# value of its literal operand; if this instruction jumps,
# the instruction pointer is not increased by 2 after this
# instruction.
def jnz(val):
    global a
    global b
    global c
    if a != 0:
        return val


# The bxc instruction (opcode 4) calculates the
# bitwise XOR of register B and register C,
# then stores the result in register B.
# (For legacy reasons, this instruction reads an operand
# but ignores it.)
def bxc(val):
    global a
    global b
    global c
    b = b ^ c


# The out instruction (opcode 5) calculates the value
# of its combo operand modulo 8, then outputs that value.
# (If a program outputs multiple values, they are separated
# by commas.)
def out(val):
    global a
    global b
    global c
    return str(int(getCombo(val) % 8))


# The bdv instruction (opcode 6) works exactly like
# the adv instruction except that the result is stored
# in the B register. (The numerator is still read from
# the A register.)
def bdv(val):
    global a
    global b
    global c
    val = getCombo(val)
    val = 2**val
    b = int(a / val)


# The cdv instruction (opcode 7) works exactly like
# the adv instruction except that the result is
# stored in the C register. (The numerator is still read
# from the A register.)
def cdv(val):
    global a
    global b
    global c
    val = getCombo(val)
    val = 2**val
    c = int(a / val)


ptr = 0
while ptr < len(program):
    com = program[ptr]
    op = com[0]
    val = com[1]
    # print(com, op, val, a, b, c)

    match op:
        case 0:
            adv(val)
        case 1:
            bxl(val)
        case 2:
            bst(val)
        case 3:
            tmp = jnz(val)
            if tmp != None:
                ptr = tmp
                continue
        case 4:
            bxc(val)
        case 5:
            result.append(out(val))
        case 6:
            bdv(val)
        case 7:
            cdv(val)
    ptr += 1
    # print(ptr)

print(",".join(result))
