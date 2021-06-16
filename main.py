from inputGet import *
from adder import *
from conversion import *

def main_Function():
    flag = False
    while(not flag):
        Num = get_input()

        sum = byteAdder(Num)
        print()
        print("Here is the final result:")
        print("Binary Number                     Decimal Number")
        print(" " , Num[0] ,"                ", binaryToDecimal(Num[0]))
        print("+" , Num[1] ,"                ", binaryToDecimal(Num[1]))
        print("___________________            ____________________")
        
        print(sum ,"                          ", binaryToDecimal (Num[0]) + binaryToDecimal(Num[1]))
        
        
        CorrectInput = False
        print()
        print("____________________________________________________________________________________________________")
        print()
        while not CorrectInput:
            DoContinue = input("do you want to continue!choose c if you want to continue or choose e if you want to exit:")
            if DoContinue == "c":
                CorrectInput = True
            elif DoContinue == "e":
                CorrectInput = True
                flag = True
            else:
                print("Give correct input")
                CorrectInput = False
print("******************************************************************************")                
print("*||||||||       ||                    |          ||      ||                   *")
print("*||    ||       ||                   |||         ||      ||                   *")
print("*||    ||     |||||||               || ||        ||      ||                   *")
print("*||    || || || ||     |||||\      ||   ||       ||      || ||||||\  ||  ||   *")
print("*|||||||  || || ||     ||   ||    ||     ||      ||      || ||    || || ||    *")
print("*||    ||  \|/  ||     ||||||/    ||||||||| ||||||| ||||||| |||||||| ||||/    *")
print("*||    ||  ||   ||     ||         ||     || ||   || ||   || ||       ||       *")
print("*||    ||  ||   ||  || ||   ||    ||     || ||   || ||   || ||   ||  ||       *")
print("*||||||||  ||   |||||/ |||||/     ||     || ||||||| ||||||| ||||||/  ||       *")
print("*                                                                             *")
print("*                               WELCOME to byte adder!!                       *")
print("******************************************************************************")
main_Function()

