def perform_operation(num1, num2, operation):
    operations = {
        "add": (num1 + num2, f"The result of adding {num1} and {num2} is: "),
        "subtract": (num1 - num2, f"The result of subtracting {num2} from {num1} is: "),
        "multiply": (num1 * num2, f"The result of multiplying {num1} and {num2} is: "),
    }

    if operation == "divide":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
        return result

    if operation in operations:
        result, message = operations[operation]
        print(f"{message}{result}")
        return result

    print(f"Error: Unsupported operation '{operation}'")
    return None
