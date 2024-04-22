import matplotlib.pyplot as plt
import math

numbers = [x for x in range(-10, 11)]

unique_functions = {
    1: lambda: [x**2 - 5 for x in numbers],
    2: lambda: [x**2 + x - 90 for x in numbers],
    3: lambda: [x**10 - x**8 + x**2 - 9 for x in numbers],
    4: lambda: [x**4 + x**3 + x**2 + x + 2 for x in numbers],
    5: lambda: [(x**2 + x + 12) / (2*x+1) for x in numbers],
    6: lambda: [math.sin(x) / (4*x+1) for x in numbers],
    7: lambda: [x**3 + 3*x**2 - 10*x + 4 for x in numbers],
    8: lambda: [math.cos(x) / (6*x+1) for x in numbers],
    9: lambda: [(x**3 / (3*x)) - 10*x+1 for x in numbers],
    10: lambda: [(x+3)*(x+4)*(x-5) for x in numbers]
}

while True:
    problem_num = int(input("Enter a problem number (1-10): "))
    if problem_num in unique_functions:
        result = unique_functions[problem_num]()
        break
    else:
        print("Oops! Please enter a number between 1 and 10.")

plt.plot(numbers, result, label=f'Unique Problem {problem_num}')
plt.xlabel('Input Numbers')
plt.ylabel('Result')
plt.legend()
plt.show()
