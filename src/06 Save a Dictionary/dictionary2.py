import pickle

def save_dict(dictionary, file_path):
    """
    Saves a dictionary to a file using pickle.

    Args:
        dictionary: The dictionary to save.
        file_path: The path to the output file.
    """

    with open(file_path, 'wb') as f:
        pickle.dump(dictionary, f)

def load_dict(file_path):
    """
    Loads a dictionary from a file using pickle.

    Args:
        file_path: The path to the input file.

    Returns:
        The loaded dictionary.
    """

    with open(file_path, 'rb') as f:
        return pickle.load(f)

if __name__ == "__main__":
    save_dict({1: 'a', 2: 'b', 3: 'c'}, 'test.pickle')
    print(load_dict('test.pickle'))