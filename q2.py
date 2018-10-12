from collections.abc import Iterable


data = [
    'one',
    ['one', 'two'],
    {'one': 1, 'two': 2},
    1
]


def to_list(args):
    if isinstance(args, str) or not isinstance(args, Iterable):
        args = [args]
    return [*args]


if __name__ == '__main__':
    for datum in data:
        print(str(to_list(datum)))
