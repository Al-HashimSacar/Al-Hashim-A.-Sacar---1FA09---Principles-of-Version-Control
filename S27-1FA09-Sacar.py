import math

"""
Distance Calculator
Calculates the 2D Euclidean distance between two points (x1, y1) and (x2, y2).
"""

def main():
    # Get coordinate inputs from the user
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    # Calculate distance using the Euclidean distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    delta_x = x2 - x1
    delta_y = y2 - y1
    distance = math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))

    # Display the formatted result
    print(f"\nThe distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")

if __name__ == "__main__":
    main()

# Answers to Guide Questions

#1. What comments did you add, and why?
# Removed the top reflection comment from the code file to clean up clutter and moved the relevant context to the `README.md` file.
# Added a clear top-level docstring describing the program purpose.
# Clarified inline comments to explain intermediate distance calculations (`delta_x` and `delta_y`).

#2. What variable names or formatting did you improve?
# Encapsulated the logic inside a structured `main()` function block.
# Added intermediate variables `delta_x` and `delta_y` to reduce formula length and make the math standard easier to read.
# Added spacing around input prompts and formatting for printed output.

#3. What did you include in your README.md file?
# Project Title, Description, and How to Run

#4. How did your changes make the program easier to understand?
# Breaking down long single-line standard library calls into intermediate variables prevents cognitive overload.
# Moving non-essential reflection text out of the source code keeps the program clean and focused on code implementation.

#5. If you worked with a partner or group, how did your team divide the work?
# Worked individually to perform code cleanup, structure the Python script, and draft the Markdown documentation.
