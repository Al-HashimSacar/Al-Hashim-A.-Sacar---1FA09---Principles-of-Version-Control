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