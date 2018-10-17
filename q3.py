"""
Objective: Given two lists (of same length):
    l1 = ['a', 'b', 'c', 'd']
    l2 = [1, 2, 3, 4]
Create a function that returns a dict where each element of l1 is the key and it's value is the corresponding element
from l2. Bonus points if you can explain how you'd deal with lists of different lengths.
"""

# Nonessential sample data used for both running main output and tests.
data = {
    'x': ['a', 'b', 'c', 'd'],
    'y': [1, 2, 3, 4]
}


# Turn keys and values into a single dictionary.
def create_dict(keys, values):
    # Create an empty return result to add to later.
    result = {}
    try:
        # Ensure every key is reached.
        for i in range(len(keys) + 1):
            # Add the relevant key and value to the dictionary.
            result[keys[i]] = values[i]
    # If either keys or values has been exhausted throw an error.
    except IndexError:
        pass
    return result


# Runs the example output if and only if the scripts is being executed directly. If it is imported do not run since
# such output might then be an inconvenience.
if __name__ == '__main__':
    print(str(create_dict(data['x'], data['y'])))
