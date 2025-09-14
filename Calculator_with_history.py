HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
        if len(lines) == 0:
            print("No history found!")
        else:
            for line in reversed(lines):
                print(line.strip())
    except FileNotFoundError:
        print("No history file found!")


def clear_history():
    with open(HISTORY_FILE, 'w') as file:
        pass
    print("History cleared.")


def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")


def calculate(expression):
    try:
        parts = expression.split()
        if len(parts) != 3:
            print("Invalid input. Use format: numberoperatornumber (e.g. 6+5)")
            return

        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("You cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operator.")
            return

        if int(result) == result:
            result = int(result)

        print("Result:", result)
        save_to_history(expression, result)

    except ValueError:
        print("Invalid numbers entered.")


def main():
    print("--- Simple Calculator (type history, clear, exit) ---")
    while True:
        user_input = input("Enter calculation (* / + -) or command (history, clear, exit): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)


main()
