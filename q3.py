data = {
    'x': ['a', 'b', 'c', 'd'],
    'y': [1, 2, 3, 4]
}


def create_dict(keys, values):
    result = {}
    try:
        for i in range(len(keys) + 1):
            result[keys[i]] = values[i]
    except IndexError:
        pass
    return result


if __name__ == '__main__':
    print(str(create_dict(data['x'], data['y'])))
