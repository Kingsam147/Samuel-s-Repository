import math

def stringToFloat(x: str):
    part1: str = x.split('.')[0]
    part2: str = x.split('.')[1]
    return float(part1 + '.' + part2)

print("\"l\" for list of operations")

while True: 
    
    # works like a regular calculator you type in the numbers and operations like normal with spaces inbetween

    equation = input()

    # do the one variable operations first, like the square root and trig functions
    if(equation.count('(') == 1 and equation.count(')') == 1): 
        equation = equation.split('(')
        operation = equation[0]
        firstNum = equation[1]
        firstNum = firstNum.split(')')[0]

        # convert first and second nums to ints or floats
        if(firstNum.isdigit()):
            firstNum = int(firstNum)
        elif(firstNum.count('.') == 1): 
            firstNum = stringToFloat(firstNum) # method at top
        else:
            print("\nEnter a valid equation\n")
            continue

        match operation:
            case 'sqrt':
                print("Solution: ", end="") 
                print(round(math.sqrt(firstNum), 7))
                continue
            case 'cbrt': 
                print("Solution: ", end="") 
                print(round(math.cbrt(firstNum), 7))
                continue
            case 'sin': 
                print("Solution: ", end="") 
                print(round(math.sin(math.radians(firstNum)), 7))
                continue
            case 'cos': 
                print("Solution: ", end="") 
                print(round(math.cos(math.radians(firstNum)), 7))
                continue
            case 'tan': 
                print("Solution: ", end="") 
                print(round(math.tan(math.radians(firstNum)), 7))
                continue
            case 'arcsin': 
                print("Solution: ", end="") 
                print(round(math.asin(math.radians(firstNum)), 7))
                continue
            case 'arccos':
                print("Solution: ", end="") 
                print(round(math.acos(math.radians(firstNum)), 7))
                continue
            case 'arctan': 
                print("Solution: ", end="") 
                print(round(math.atan(math.radians(firstNum)), 7)) 
                continue
            case 'exit':
                break
            case default:
                print("\nplease enter a valid operation")
                print("resetting calculator...\n")
                continue
    
    match equation:
        case "l":
            print("List of operations")
            print("+: addition")
            print("-: subtraction")
            print("*: multiplication")
            print("/: division")
            print("%: mod")
            print("^: exponent")
            print("log: log(x)")
            print("sqrt: square root")
            print("cbrt: cube root")
            print("sin: sin(x)")
            print("cos: cos(x)")
            print("tan: tan(x)")
            print("arcsin: arcsin(x)")
            print("arccos: arccos(x)")
            print("arctan: arctan(x)")
            print("exit: terminate calculator")
            continue
        case 'exit':
            break 

    equation = equation.split() 
    firstNum = equation[0]
    operation = equation[1]
    secondNum = equation[2]

    # convert first and second nums to ints or floats
    if(firstNum.isdigit()):
        firstNum = int(firstNum)
    elif(firstNum.count('.') == 1): 
        firstNum = stringToFloat(firstNum) # method at top
    else:
        print("\nEnter a valid equation\n")
        continue

    if(secondNum.isdigit()):
        secondNum = int(secondNum)
    elif(secondNum.count('.') == 1): 
        secondNum = stringToFloat(secondNum) # method at top
    else:
        print("\nEnter a valid equation\n")
        continue 

    # recognize the operation and deal with it accordingly
    match operation:
        case '+': 
            print("Solution: ", end="") 
            print(round(firstNum + secondNum, 7))
            print()
        case '-': 
            print("Solution: ", end="") 
            print(round(firstNum - secondNum, 7))
            print()
        case '*': 
            print("Solution: ", end="")  
            print(round(firstNum * secondNum, 7))
            print()
        case '/': 
            print("Solution: ", end = "")
            if (secondNum == 0):
                print("cannot divide by 0")
                continue
            else: 
                print(round(firstNum/secondNum, 7))  
                print()        
        case '%': 
            print("Solution: ", end = "")
            print(firstNum % secondNum)
            print()
        case '^': 
            print("Solution: ", end = "")
            print(round(firstNum ** secondNum, 7))
            print()
        case 'log':
            print("Solution: ", end = "")
            print(round(math.log(firstNum, secondNum), 7))
            print()
        case 'exit':
            break
        case default:
            print("\nplease enter a valid operation")
            print("resetting calculator...\n")
            continue
        
    # after everything loop back to restart the function        
    continue

