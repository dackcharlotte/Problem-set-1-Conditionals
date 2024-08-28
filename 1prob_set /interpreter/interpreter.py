expression = input("Expression: ") # collect the input

x, y, z = expression.split(" ")

x_float = float(x)
z_float = float(z)

match y:
    case "+":
        print(x_float + z_float)
    case "-":
        print(x_float - z_float)
    case "*":
        print(x_float * z_float)
    case _:
        print(x_float / z_float)
