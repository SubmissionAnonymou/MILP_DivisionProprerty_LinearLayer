Matrix = [
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
]



ShiftRowIndex_all = {
16:[0, 1, 2, 3, 12, 13, 14, 15, 8, 9, 10, 11, 4, 5, 6, 7],
32:[0, 1, 26, 27, 20, 21, 14, 15, 8, 9, 2, 3, 28, 29, 22, 23, 16, 17, 10, 11, 4, 5, 30, 31, 24, 25, 18, 19, 12, 13, 6, 7],
64:[0, 57, 50, 43, 36, 29, 22, 15, 8, 1, 58, 51, 44, 37, 30, 23, 16, 9, 2, 59, 52, 45, 38, 31, 24, 17, 10, 3, 60, 53, 46, 39, 32, 25, 18, 11, 4, 61, 54, 47, 40, 33, 26, 19, 12, 5, 62, 55, 48, 41, 34, 27, 20, 13, 6, 63, 56, 49, 42, 35, 28, 21, 14, 7]
}

ShiftRowIndex = ShiftRowIndex_all[16]

#[a0, a1, ... , a7, b0, ..., b7, c] where a -> b and a7, b7 are LSB
SboxInqs = [
#Sbox0 = [
    [
        [1, 1, 41, 1, 1, 1, 1, 1, -7, -7, -7, -7, -7, -6, -7, -6, 6],
        [0, 0, 0, 0, 0, 0, 7, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1],
        [1, 1, 1, 40, 1, 1, 1, 1, -6, -7, -7, -7, -6, -6, -7, -7, 6],
        [1, 1, 1, 1, 1, 45, 1, 1, -6, -8, -8, -7, -8, -6, -8, -8, 7],
        [35, 1, 1, 1, 1, 1, 1, 1, -5, -6, -6, -6, -6, -6, -6, -6, 5],
        [1, 1, 1, 1, 50, 1, 1, 1, -6, -6, -11, -6, -11, -5, -11, -11, 10],
        [-3, 0, -3, -4, -4, -3, -1, -3, -3, -2, -6, 19, -2, -2, -3, -4, 24],
        [-4, 5, -4, -4, 0, -4, -4, 5, -1, -1, 0, -5, -1, -1, -1, -1, 21],
        [-4, -6, -4, -4, -2, -1, -6, -1, 23, 26, 27, 24, 27, 22, 27, 27, 0],
        [-17, -20, -17, -17, -17, -17, -20, -16, 4, 2, 3, 4, 2, -1, 2, 3, 122],
        [1, 2, 0, 2, -5, 0, 0, -1, -6, -5, -6, -6, -3, -4, -6, 25, 12],
        [0, -2, -2, -5, -1, -4, -1, -5, -5, -2, -4, -2, -3, 3, -3, 13, 23],
        [-2, -2, 0, -1, -1, -3, -2, -7, 3, -2, 8, -2, -3, -5, -3, 1, 21],
        [1, -5, 1, -1, 0, 0, 0, 2, -2, 18, -5, -4, -5, -3, -3, -5, 11],
        [-3, -2, -6, -5, -6, -8, -8, -8, 5, 5, 2, 4, 4, 5, 5, -1, 39],
        [-1, -4, -4, -2, -2, -3, -4, 0, -2, 1, 2, 4, 4, 4, 4, 2, 18],
        [0, 2, 0, 1, 1, -1, 0, -1, -4, 16, -5, 1, -4, -5, -5, -3, 7],
        [-4, -6, -2, -4, -2, -1, -6, -3, 4, 2, 4, 3, 4, -1, 4, 4, 23],
        [-2, 1, -2, -2, 0, 1, -2, -2, -1, 0, 1, -4, 1, 1, -2, 0, 12],
        [-2, -2, 0, -1, -1, -2, -2, 6, 2, -5, -5, 2, 7, -7, 0, -5, 15],
        [-3, -3, -3, -2, -3, -3, -3, 0, 3, 2, 4, 3, 1, 1, 2, 4, 16],
        [-1, -2, 0, -3, -1, -2, -2, -2, 1, 2, -1, 1, -1, 1, -1, -3, 14],
        [0, 1, 0, 0, -1, 1, 0, -1, -3, -1, -1, -1, 8, -2, -3, -2, 5],
        [-1, -6, -2, -2, -2, -1, 0, -3, -2, -2, -4, -2, 15, -1, -4, -3, 20],
        [-2, -2, 0, -1, -1, 0, -2, -2, 2, -1, -1, 1, 1, -3, -1, 1, 11],
        [-1, -1, -1, 2, 0, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -2, 7],
        [-1, -3, -2, -2, -2, -1, -3, 0, 12, 13, 14, 13, 13, 11, 13, 14, 0],
        [-1, 0, -1, -1, 1, -1, -1, 1, 1, 0, -1, -2, -1, 1, 0, 0, 6],
    ]
#Sbox1 = [
    ,[
        [1, 1, 36, 1, 1, 1, 1, 1, -6, -6, -6, -6, -6, -6, -6, -6, 5],
        [0, 0, 0, 0, 0, 7, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1],
        [0, 0, 0, 7, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1],
        [7, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1],
        [1, 1, 1, 1, 1, 1, 1, 35, -6, -6, -6, -6, -5, -6, -6, -6, 5],
        [0, 0, 0, 0, 9, 0, 0, 0, 0, -2, -2, -2, -1, -1, -2, -1, 2],
        [0, 9, 0, 0, 0, 0, 0, 0, -2, -2, -2, 1, -2, -1, -2, -1, 2],
        [-23, -23, -23, -20, -19, -23, -18, -20, 2, 4, 3, 4, -1, 5, 3, 2, 147],
        [-1, -2, 0, -2, -1, -2, -1, -2, 9, 10, 11, 11, 11, 11, 10, 10, 0],
        [0, 0, 0, 0, -1, 0, 14, 0, -1, -4, -1, -4, -2, -2, -1, -3, 5],
        [0, 0, 0, 0, -1, 0, -1, 1, -4, -2, -3, -5, -2, -5, 16, -1, 7],
        [0, -5, 0, 0, 2, 0, 0, 1, -4, -3, -4, -5, 1, 15, -5, -3, 10],
        [0, -1, -2, -2, -1, -2, -4, -2, 8, -3, -2, -3, -3, 1, 4, -5, 17],
        [-3, 1, -3, -3, 1, -3, 0, -3, -5, -6, 6, 7, 2, -9, -5, 2, 21],
        [-1, 0, 0, -1, -1, -1, -3, -1, -1, 1, -1, -1, -1, 2, -2, 2, 9],
        [-3, -3, -3, -2, -3, -1, -2, -1, 17, 16, 15, 17, 17, 17, 17, 17, 0],
        [-2, -2, -2, -1, -1, -2, 0, -1, -2, -1, 1, -1, -3, 2, 4, 3, 12],
        [-1, -1, 0, -1, -1, -1, -1, -1, 1, -1, 0, 0, 0, 0, 1, -1, 7],
        [0, 0, 0, 0, 0, 0, 0, 2, -1, -1, 4, -1, -1, -1, -1, -1, 1],
        [-1, 0, -1, -1, -1, -1, -1, -1, 1, -1, 0, -2, -1, 1, 3, -2, 8],
        [-1, -1, -1, -1, 1, -1, 0, -1, 0, -1, 0, -1, 1, 1, 0, -2, 7],
        [-3, -3, -3, -2, -2, -3, 0, -1, 3, 4, 2, 4, 1, 3, 3, 3, 13],
    ]
    #Sbox2 = [
    ,[
        [1, 1, 1, 35, 1, 1, 1, 1, -6, -6, -5, -6, -6, -6, -6, -6, 5],
        [0, 0, 0, 0, 0, 0, 7, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1],
        [1, 1, 39, 1, 1, 1, 1, 1, -6, -6, -7, -7, -7, -6, -6, -7, 6],
        [39, 1, 1, 1, 1, 1, 1, 1, -6, -6, -7, -6, -7, -7, -6, -7, 6],
        [-1, 16, -1, 0, 1, 0, 0, 0, -2, -3, -3, -2, -3, -1, -3, -3, 5],
        [0, 0, 0, 0, 0, 6, 0, 0, -1, -1, -1, -1, -1, -1, 0, -1, 1],
        [-2, 0, -3, 1, 2, 0, 0, -2, -5, -6, -6, -5, -7, -3, -7, 29, 14],
        [1, 0, 4, 5, 5, 2, 0, 2, -17, -17, 82, -18, -14, -17, -18, -20, 20],
        [-2, -3, -2, -4, -4, -3, -4, -1, 22, 20, 21, 21, 22, 21, 19, 21, 0],
        [0, 0, -1, -5, 0, 0, 0, -1, -1, -1, -7, 5, -1, -1, 5, -6, 14],
        [9, 1, 2, 1, 1, 2, 1, 1, 82, -23, -15, -16, -23, -23, -14, -8, 22],
        [-4, -3, -3, -3, -3, -1, 0, -1, -4, 12, 1, -2, -3, -2, -2, -3, 21],
        [1, 2, 1, 1, 1, 1, 1, 9, -14, -14, -7, -7, 39, -13, -7, -7, 13],
        [-2, 0, -1, -2, -1, -2, -2, -2, 10, 12, 12, 11, 12, 10, 11, 12, 0],
        [-1, -1, -2, 0, -1, -1, -1, -1, -1, 0, -2, -1, -2, 5, -1, 1, 9],
        [-2, -2, -2, 0, -2, -1, -2, 0, 1, 1, 2, 2, 1, -1, 1, 0, 10],
        [-1, 0, -2, -3, -3, -2, -3, -3, 2, 4, 4, 2, 4, 3, 1, 4, 13],
        [-3, -1, -3, -3, 0, -1, -3, -3, 3, 2, 2, 2, 1, -1, 2, 1, 15],
        [-1, -2, 0, -3, -3, -3, -3, -3, 1, 2, 3, 4, 4, 3, 3, 4, 14],
        [0, 0, -1, -1, -1, -1, -1, 0, 5, 5, 5, 4, 5, 5, 5, 5, 0],
        [2, 0, 0, 0, 1, 1, 0, 1, -4, -3, -4, -3, 13, -4, -3, -1, 4],
        [-5, -2, -1, -3, -2, -3, -2, -3, -3, -2, 2, 1, -1, 2, 2, -1, 21],
        [-4, -4, -2, -1, -4, -4, -4, -2, 2, 2, -1, 2, 1, 3, 2, 1, 22],
        [-2, -1, -2, -1, -1, 0, -1, 0, -1, 0, 2, 1, -1, 1, -2, -1, 9],
        [-2, -3, -3, -3, -1, -3, -3, -3, 1, 1, -1, 1, 2, -2, 1, -3, 21],
        [-1, 0, -1, -1, -1, -1, 0, -1, 5, 6, 6, 6, 6, 6, 6, 6, 0],
        [0, 1, 0, 6, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1],
    ]
    #Sbox3 = [
    ,[
        [1, 1, 1, 1, 1, 1, 36, 1, -6, -6, -6, -6, -6, -6, -6, -6, 5],
        [0, 0, 0, 0, 0, 7, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1],
        [1, 1, 39, 1, 1, 1, 1, 1, -7, -7, -7, -6, -7, -6, -6, -6, 6],
        [7, 63, 1, 1, 1, 1, 1, 1, -6, -13, -13, -6, -13, -13, -12, -12, 12],
        [1, 1, 1, 1, 1, 1, 1, 34, -6, -7, -1, -7, -7, -6, -7, -6, 6],
        [0, 0, 0, 0, 5, 0, 0, 0, -1, -1, -1, -1, 0, -1, -1, 0, 1],
        [8, 0, 0, 0, 0, 0, 0, 0, -1, -2, -2, -1, -1, 0, -1, -2, 2],
        [-22, -25, -19, -21, -25, -22, -22, -20, 5, 3, 4, 5, 4, -2, 3, 1, 153],
        [-4, -3, -4, -1, -1, -3, -3, -2, 20, 20, 17, 19, 19, 20, 20, 18, 0],
        [0, 0, 0, 14, 0, 0, 0, -1, -2, -4, -1, -1, -1, -3, -4, -2, 5],
        [2, 4, 1, 1, 1, 1, 4, 1, 1, -15, -14, -12, -15, -13, -11, 50, 14],
        [1, -2, 0, -2, 5, 0, 0, -4, -10, -8, -1, -8, 5, -11, 25, -9, 19],
        [1, 2, 1, 1, 1, 1, 1, 1, -8, -9, 1, 1, -10, 22, -7, -8, 9],
        [2, -1, -3, 0, 2, 0, 0, 3, -6, -10, -7, -5, -2, 31, -10, -8, 14],
        [-4, 1, 0, 0, -6, 0, 2, 0, -4, 16, 1, -5, -6, -3, -4, -4, 16],
        [-2, -1, -5, -4, -5, -5, -5, -3, 1, 5, 4, 2, 5, 5, 4, 4, 24],
        [-2, -1, 0, -5, -1, 0, -3, -3, 13, -2, -3, -2, -4, -5, -2, 1, 19],
        [-5, -3, -1, -1, -4, -5, -5, -3, 4, 4, 2, 4, 2, 0, 4, -2, 24],
        [-2, 5, -2, -2, -2, -1, -1, -3, -6, -5, -7, 8, 1, -5, 2, 2, 18],
        [-1, -3, -4, -2, -3, -5, -5, -4, 3, 5, 5, 1, 4, 3, 4, 5, 21],
        [-2, -1, 0, -2, -2, -2, -1, -2, 1, 2, 1, 2, 1, 1, -1, 2, 11],
        [3, 3, 6, 4, 5, 3, 5, 10, 86, -30, -31, -30, -5, 1, -31, -27, 28],
        [-2, -3, -3, 0, -3, -3, -3, -1, 1, 4, 2, 3, 3, 2, 4, 3, 14],
        [-2, -2, -2, -1, -2, -1, 3, -2, 3, -1, -2, -1, -1, -3, 2, -1, 13],
        [0, -1, -1, -3, -1, -1, -2, 0, 3, -1, 4, 1, -2, -4, -1, -3, 12],
        [-2, -1, 2, 0, -1, -1, -1, -1, -1, 1, -1, -4, -3, 1, 1, 1, 10],
        [-1, 1, 0, 0, -1, -1, -1, -1, 1, 0, 1, 0, -1, -2, 1, -3, 7],
        [-1, -2, -1, 0, -1, 0, -2, -2, -1, -1, -2, 1, 2, 1, -1, 0, 10],
        [3, -1, -2, -2, -2, -2, -2, -2, 5, -2, -2, 2, 2, -3, -4, -2, 15],
        [1, 1, 1, 25, 1, 1, 1, 1, -5, -5, -5, -5, -1, -5, -5, -5, 4],
    ]
]


# SboxDP = {

# }