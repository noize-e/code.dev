"""
"""
import random

# Generate a list of n size with random numbers
numbers = random.sample(range(1, 100), 20)
target = random.randint(1, 100)


def get_pair_nums(target: int, numbers: list) -> list:
    """ worst-case: O(n) """
    numbers = sorted(numbers)
    input_size = len(numbers)
    total_steps =  0
    print(f"InputSize: {input_size}")
    # print(numbers)
    while bool(len(numbers)):
        max_number = numbers.pop()
        total_steps += 1
        if max_number < target:
            difference = abs(target - max_number)

            # print(f"Target: {target}, MaxNum:{max_number}, Diff: {difference}")
            
            try:
                numbers.index(difference)
                print(f"OutputSteps: {total_steps}")
                return (max_number, difference)
            except:
                continue
    print(f"OutputSteps: {total_steps}")
    return None


print(get_pair_nums(target, numbers))