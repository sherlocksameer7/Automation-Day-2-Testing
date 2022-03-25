def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

if __name__ == "__main__":

    a = int(input("Enter 1st Number= "))
    b = int(input("Enter 2nd Number= "))

    Addition = add(a, b)
    print(Addition)

    Subtraction = sub(a, b)
    print(Subtraction)

    Multiplication = mul(a, b)
    print(Multiplication)

    Division = div(a, b)
    print(Division)
