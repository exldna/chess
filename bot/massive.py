import numpy as np

advantage_map = np.array([
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ], [
        [0, 4, 6, 6, 8, 15, 25, 20],
        [0, 4, 8, 8, 12, 18, 25, 20],
        [0, 4, 8, 12, 16, 25, 28, 28],
        [0, 6, 12, 16, 24, 32, 32, 35],
        [0, 6, 12, 16, 24, 32, 32, 35],
        [0, 4, 8, 12, 16, 25, 28, 28],
        [0, 4, 8, 8, 12, 18, 25, 20],
        [0, 4, 6, 6, 8, 15, 25, 20]
    ], [
        [14, 14, 14, 14, 14, 14, 14, 14],
        [14, 22, 18, 18, 18, 18, 22, 14],
        [14, 18, 22, 22, 22, 22, 18, 14],
        [14, 18, 22, 25, 25, 22, 18, 14],
        [14, 18, 22, 25, 25, 22, 18, 14],
        [14, 18, 22, 22, 22, 22, 18, 14],
        [14, 22, 18, 18, 18, 18, 22, 14],
        [14, 14, 14, 14, 14, 14, 14, 14]
    ], [
        [0, 4, 8, 10, 10, 8, 4, 0],
        [4, 8, 16, 20, 20, 16, 8, 4],
        [8, 16, 24, 28, 28, 24, 16, 8],
        [10, 20, 28, 32, 32, 28, 20, 10],
        [10, 20, 28, 32, 32, 28, 20, 10],
        [8, 16, 24, 28, 28, 24, 16, 8],
        [4, 8, 16, 20, 20, 16, 8, 4],
        [0, 4, 8, 10, 10, 8, 4, 0]
    ], [
        [7, 8, 10, 11, 12, 15, 17, 20],
        [10, 12, 15, 15, 15, 18, 20, 25],
        [15, 15, 17, 19, 19, 20, 25, 25],
        [20, 15, 19, 21, 21, 25, 27, 30],
        [20, 15, 19, 21, 21, 25, 27, 30],
        [15, 15, 17, 19, 19, 20, 25, 25],
        [10, 12, 15, 15, 15, 18, 20, 25],
        [7, 8, 10, 11, 12, 15, 17, 20]
    ], [
        [7, 8, 10, 11, 12, 15, 17, 20],
        [10, 12, 15, 15, 15, 18, 20, 25],
        [15, 15, 17, 19, 19, 20, 25, 25],
        [20, 15, 19, 21, 21, 25, 27, 30],
        [20, 15, 19, 21, 21, 25, 27, 30],
        [15, 15, 17, 19, 19, 20, 25, 25],
        [10, 12, 15, 15, 15, 18, 20, 25],
        [7, 8, 10, 11, 12, 15, 17, 20]
    ], [
        [25, 21, 23, 9, 9, 23, 21, 25],
        [25, 21, 13, 5, 5, 13, 21, 25],
        [21, 17, 5, 0, 0, 5, 17, 21],
        [15, 13, 5, 0, 0, 5, 13, 15],
        [15, 13, 5, 0, 0, 5, 13, 15],
        [21, 17, 5, 0, 0, 5, 17, 21],
        [25, 21, 13, 5, 5, 13, 21, 25],
        [25, 21, 13, 9, 9, 13, 21, 25]
    ],
])

pieces_cost = [0, 100, 300, 300, 500, 900, 100000]
