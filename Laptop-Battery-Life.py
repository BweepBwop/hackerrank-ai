import math
import os
import random
import re
import sys


def load_training_data(filename):
    charge_times = []
    battery_lives = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                charge, battery = map(float, line.strip().split(','))
                charge_times.append(charge)
                battery_lives.append(battery)
    except FileNotFoundError:
        print("Error: trainingdata.txt not found.", file=sys.stderr)
        sys.exit(1)
    return charge_times, battery_lives

if __name__ == '__main__':
    # Load training data
    charge_times, battery_lives = load_training_data('trainingdata.txt')
    
    # Compute average ratio for points where charging time is <= 4.0 and non-zero
    ratios = [b/c for c, b in zip(charge_times, battery_lives) if c <= 4.0 and c > 0]
    slope = sum(ratios) / len(ratios) if ratios else 2.0  # Default to 2 if no valid ratios
    
    # Determine cap as maximum observed battery life
    cap = max(battery_lives) if battery_lives else 8.0  # Default to 8 if no data
    
    # Read input charging time
    try:
        timeCharged = float(input().strip())
    except ValueError:
        print("Invalid input", file=sys.stderr)
        sys.exit(1)
    
    # Predict battery life using data-driven slope and cap
    last_time = min(timeCharged * slope, cap)
    
    # Output prediction rounded to 2 decimal places
    print("{:.2f}".format(last_time))
