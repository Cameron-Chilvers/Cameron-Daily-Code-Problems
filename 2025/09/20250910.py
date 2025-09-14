## Failed, understood monte carlo, but confused on how to implement, still wonder if u can move the circle up to then try and simulate
# Moved the circle up and you can simulate based on that, just means you need to scale by r^2, as all the 4 quarters are counting
# Does this get more accurate with only half?, Same amount but its good to know that all three methods are roughly 3.14 which mean that even moving the circle gets the same outcome

# So the scale factor changes to what sections of the circle we are estimating



# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.

import random

def problem(samples):
    inside_circle = 0
    for _ in range(samples):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)

        if x**2 + y**2 <= 4:
            inside_circle += 1
    
    return round(4*inside_circle/samples, 3)

def problem_moved_circle(samples):
    inside_circle = 0
    for _ in range(samples):
        x = random.uniform(0, 4)
        y = random.uniform(0, 4)

        if (x-4)**2 + (y-4)**2 <= 4:
            inside_circle += 1
    
    return round(16*inside_circle/samples, 3)

def problem_half_circle(samples):
    inside_circle = 0
    for _ in range(samples):
        x = random.uniform(0, 4)
        y = random.uniform(-2, 2)

        if (x-4)**2 + (y)**2 <= 4:
            inside_circle += 1
    
    return round(8*inside_circle/samples, 3)

if __name__ == "__main__": 
    samples = 10000000
    # print(problem(samples))
    print(problem_moved_circle(samples))