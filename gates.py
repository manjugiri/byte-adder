def or_gate(r1,r2):
    return r1|r2


def and_gate(r1,r2):
    return r1&r2



def xor_gate(r1,r2):
    return r1^r2


def not_gate(r1):
    return (~r1)+2


def nand_gate(r1,r2):
    return not_gate(and_gate(r1,r2))


def nor_gate(r1,r2):
    return not_gate(or_gate(r1,r2))

