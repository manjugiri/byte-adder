from gates import *

def byteAdder (binaryNumberList):
    BinaryNumber1 = binaryNumberList[0]
    BinaryNumber2 = binaryNumberList[1]

    BinarySum = ""

    print("Adding in binary number system")

    for i in BinaryNumber1:
        print(i,end="")
    print()
    print("+")
    
    for i in BinaryNumber2:
        print(i,end="")
    print()

    for i in range(len(BinaryNumber1)-1,-1,-1):
        
        carry = 0
        c = ["0","0","0","0","0","0","0","0"]
        for i in range(len(BinaryNumber1)-1,-1,-1):
            FirstBit = int(BinaryNumber1[i])
            SecondBit = int(BinaryNumber2[i])
            
            xor = xor_gate(FirstBit,SecondBit)
            nand = nand_gate(xor,carry)
            orgate = or_gate(xor,carry)
            sum_ = and_gate(orgate,nand)
            c[i] = str(sum_)

           
            and1 = and_gate(FirstBit,SecondBit)
            and2 = and_gate(xor,carry)
            nor  = nor_gate(and1,and2)
            carry = not_gate(nor)
            BinarySum = "".join(c)
    return BinarySum


    
