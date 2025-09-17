from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

if __name__ == "__main__":
    print("Simple Python Calculator 🚀")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))

