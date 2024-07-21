#Building a calculator using concepts of dictionaries.

#calculator
def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

#dictionary
operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
}

num1 = eval(input("What's the first number? "))
num2 = eval(input("What's the second number? "))
for keys in operations:
    print(keys)
operand = input("Which operation would you choose? ")

math = operations[operand]
answer = math(num1, num2)

print(f"{num1} {operand} {num2} = {answer}")
