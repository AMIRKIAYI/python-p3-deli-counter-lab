def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently: "
        line_str += " ".join(f"{i + 1}. {name}" for i, name in enumerate(katz_deli))
        print(line_str)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        name = katz_deli.pop(0)
        print(f"Currently serving {name}.")
