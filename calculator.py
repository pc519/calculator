while True:
    try:
        x = float(input("\nNum 1: "))
        z = input("z (+,-,*,/): ")
        y = float(input("Num 2: "))

        if z == '+': print(f"= {x + y}")
        elif z == '-': print(f"= {x - y}")
        elif z == '*': print(f"= {x * y}")
        elif z == '/': print(f"= {x / y}") if y != 0 else print("Error: / 0")
    except ValueError:
        print("Error")
