import cal_art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculation():
    print(cal_art.logo)
    should_accumulate = True
    n1 = float(input("Enter the first number: "))
    while should_accumulate is True:
        for symbol in calculator:
            print(symbol)
        operation = input("What operation do you want to perform: ")
        n2 = float(input("Enter the second number: "))

        answer = calculator[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            should_accumulate = True
            n1 = answer
        else:
            should_accumulate = False
            print("\n" * 100)
            calculation()

calculation()