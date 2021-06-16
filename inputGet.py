from conversion import *
def get_input():
    flag = False
    while(not flag):
        inputData = []
        choice =input("Enter 'd' for decimal and 'b' for binary : ")
        if choice=='b':
            correctInput = False
            while(not correctInput):            
                firstNCorrect =False
                while(not firstNCorrect):
                    firstNum=input("Enter First Binary Number : ")
                    if validation(firstNum):
                        print(" first number is correct:")
                        firstNCorrect=True
                    else:
                        print("Error!! please enter the correct numbers")
                secondNCorrect =False
                while(not secondNCorrect):
                    secondNum= input("Enter the second binary number : ")
                    if validation(secondNum):
                        print("second binary number is correct")
                        secondNCorrect=True
                    else:
                        print("please enter the correct numbers : ")
                if(binaryToDecimal(firstNum)+binaryToDecimal(secondNum)>255):
                    print("Please enter number which sum is less than 255")
                else:
                    correctInput = True
            inputData.append(binaryToEightBit(firstNum))
            inputData.append(binaryToEightBit(secondNum))
            flag = True
            return inputData


        elif choice == 'd':
            
            correctInput = False
            while(not correctInput):            
                
                firstNCorrect= False
                while(not firstNCorrect):
                    firstNum= input(" Enter first Decimal Number:")
                    if validationToDecimal(firstNum):
                        print("The first decimal Number is correct")
                        firstNCorrect=True
                    else:
                        print("Error!! please enter the correct decimal numbers")

                secondNCorrect =False
                while(not secondNCorrect):          
                    secondNum= input("Enter the second decimal number:")
                    if validationToDecimal(secondNum):
                        print(" The second decimal number is correct")
                        secondNCorrect=True
                    else:
                        print("Error!! please enter the correct decimal numbers")
                if(int(firstNum)+int(secondNum)>255):
                    print("Please insert the number which sums less than 255")
   
                else:
                    correctInput = True
            
            inputData.append(decimalToBinary(int(firstNum))) 
            inputData.append(decimalToBinary(int(secondNum)))
            flag = True
            return inputData


        

def validation(num):
    if num == "":
        print("empty field found, please enter binary number")
        return False
    try:
        checkNum = int(num)
    except:
        print("No special alphabets or character allowed here! please enter the correct binary number")
        return False
    for digit in num:
        if digit not in['0', '1']:
            print("error! Digits must be either 0 or 1")
            return False
    if binaryToDecimal(num)<0:
        print("found negative number , Negetive values are not allowed.")
        return False
    
    return True
def validationToDecimal(num):
    if num == "":
        print("found empty field, please enter decimal number")
        return False
    try:
        checkNum = int(num)
    except:
        print("No special character or alphabets allowed! please enter the correct decimal number")
        return False
    if int(num)<0:
        print("negative number found, Negetive values are not allowed.")
        return False
    for digit in num:
        if digit not in['0','1','2','3','4','5','6','7','8','9']:
            print("error!! Digits must be 0 to 9")
            return False
    if(int(num) <0 or int(num) >255):
        print("The number must be in between 0-255")
        return False
        
    return True
    

            
