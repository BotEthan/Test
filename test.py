def Start():
    numberOne = input("What is the first number? ")
    sign = input("What is the sign? ")
    numberTwo = input("What is the second number? ")
    match sign:
        case "+":
            print(f'{numberOne} + {numberTwo} = {int(numberOne) + int(numberTwo)}')
        case "-":
            print(f'{numberOne} - {numberTwo} = {int(numberOne) - int(numberTwo)}')
        case "*":
            print(f'{numberOne} * {numberTwo} = {int(numberOne) * int(numberTwo)}')
        case "/":
            print(f'{numberOne} / {numberTwo} = {int(numberOne) / int(numberTwo)}')

if __name__ == "__main__":
    Start()