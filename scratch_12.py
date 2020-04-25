from functools import lru_cache
from typing import List

Vector = List[float]
height_weight_age = [170, 70, 40]

grades = [95, 80, 75, 65]

def add(v: Vector, w: Vector):
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def subtract(v: Vector, w: Vector):
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v,w)]


assert add([1,2,3], [1,2,3]) == [2,4,6]

assert subtract([1,2,3], [1,2,3]) == [0,0,0]

def vector_sum(vectors: List[Vector]):
    assert vectors , "no vectors"

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different lengths"

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

assert  vector_sum([[1,2], [3,4], [5,6], [7,8]]) == [16, 20]

def scalar_multiply(c: float, v: Vector):
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1,2,3]) == [2,4,6]

def vector_mean(vectors: List[Vector]):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w),  "differetn lengths"
    return sum(v_i * w_i for v_i, w_i  in zip(v, w))
assert dot([1,2,3], [4, 5, 6]) == 32

def sum_of_squares(v: Vector) -> float:
    return dot(v, v)

import math

def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))
assert magnitude([3,4]) == 5

def squared_distance(v: Vector, w: Vector):
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v, w))


from typing import Tuple
Matrix = List[List[float]]
def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows, num_cols

assert shape([[1,2,3], [4,5,6]]) == (2,3)

def get_row(A: Matrix, i: int) -> Vector:
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]

from typing import Callable
def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

def identitiy_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

for r in identitiy_matrix(5):
    print(r)

from collections import Counter
import matplotlib.pyplot as plt




