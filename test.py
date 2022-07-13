def Start():
    #Collect the numbers and signs
    numberOne = input("What is the first number? ")
    sign = input("What is the sign? ")
    numberTwo = input("What is the second number? ")
    #Figure out what sign is used
    match sign:
        case "+":
            print(f'{numberOne} + {numberTwo} = {int(numberOne) + int(numberTwo)}')
        case "-":
            print(f'{numberOne} - {numberTwo} = {int(numberOne) - int(numberTwo)}')
        case "*":
            print(f'{numberOne} * {numberTwo} = {int(numberOne) * int(numberTwo)}')
        case "/":                                                                       #Print calculation
            print(f'{numberOne} / {numberTwo} = {int(numberOne) / int(numberTwo)}')
        case "%":
            print(f'{numberOne} % {numberTwo} = {int(numberOne) % int(numberTwo)}')

if __name__ == "__main__":
    Start()