"""
Objective: Create a function that receives one argument of any type and always returns a list of strings.
If the argument is a dict, return a list of the keys. If it's a number, return a string representation of it as a list,
etc. Bonus points if it can be done without explicitly checking the argument type inside the function body.

Sample output:

> to_list([1, 2, 3])
> ['1', '2', '3']
> to_list({'one': 1, 'two': 2})
> ['one', 'two']
> to_list('value')
> ['value']
"""

from collections.abc import Iterable

# Nonessential sample data used for both running main output and tests.
data = [
    'one',
    ['one', 'two'],
    {'one': 1, 'two': 2},
    1
]


# Convert any argument type into a list.
def to_list(args):
    # Checks if args is not an iterable data type in which case the return statement would otherwise fail.
    # Also checks if it is a string since Python's default behavior when iterating strings is to separate them by
    # character.
    if isinstance(args, str) or not isinstance(args, Iterable):
        # Wraps the existing data type in a list so that it is not unpacked in the next line.
        args = [args]
    # Unpacks args into a list and returns it. Because it is unpacked before being put in the list the preexisting
    # data type will no longer exist.
    return [*args]


# Runs the example output if and only if the scripts is being executed directly. If it is imported do not run since
# such output might then be an inconvenience.
if __name__ == '__main__':
    for datum in data:
        print(str(to_list(datum)))
