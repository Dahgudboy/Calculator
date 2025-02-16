# Simple Python Calculator

This is a basic Python calculator that allows users to perform simple arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Addition
- Subtraction
- Multiplication
- Division

## Requirements

- Python 3.x or higher

## How to Use

### Running the Program

1. Clone or download the repository to your local machine.
2. Navigate to the project folder.
3. Run the program by executing the following command in the terminal:

```bash
python calculator.py
```

### Operations

After running the program, you will be prompted to input two numbers and an operator. The available operators are:

- `+` for addition
- `-` for subtraction
- `*` for multiplication
- `/` for division

### Example

```
Enter first number: 5
Enter operator (+, -, *, /): +
Enter second number: 3
Result: 8
```

## Code Explanation

The program defines a function `calculator()` to handle the arithmetic operations. It prompts the user to input two numbers and choose an operator. Based on the operator input, it performs the corresponding calculation and displays the result.

## Sample Code

```python
def calculator():
    # Input the first number
    num1 = float(input("Enter first number: "))
    
    # Input the operator
    operator = input("Enter operator (+, -, *, /): ")
    
    # Input the second number
    num2 = float(input("Enter second number: "))
    
    # Perform the calculation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operator!"

    # Display the result
    print(f"Result: {result}")

# Call the calculator function to run the program
calculator()
```

## License

This project is open-source and free to use. You can modify, distribute, and contribute to it.

