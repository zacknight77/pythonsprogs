
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
print("Select operation.")
print("1.Add")
print("2.Subtract")
while True:
    choice = input("Enter choice 1 or 2: ")
    if choice in ('1', '2'):
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))
        elif choice == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))   
    else:
        print("Invalid Input")
    