import numpy as np

from typing import List, Tuple
from app.model import DenavitHartenberg


def linalg_multi_dot(dh: List[np.ndarray]) -> np.ndarray:
    if len(dh) > 1:
        return np.linalg.multi_dot(dh)

    return dh[0]


def get_coord(dh: np.ndarray) -> Tuple:
    vector = np.array([[0], [0], [0], [1]])
    x, y, z, _ = dh.dot(vector).tolist()
    return x[0], y[0], z[0]


def generate_dh(dh: DenavitHartenberg) -> np.ndarray:
    return np.array([
        [
            np.cos(dh.theta), -np.cos(dh.alpha) * np.sin(dh.theta),
            np.sin(dh.alpha) * np.sin(dh.theta), dh.a * np.cos(dh.theta)
        ],
        [
            np.sin(dh.theta), np.cos(dh.theta) * np.cos(dh.alpha),
            -np.sin(dh.alpha) * np.cos(dh.theta), dh.a * np.sin(dh.theta)
        ],
        [0, np.sin(dh.alpha), np.cos(dh.alpha), dh.d],
        [0, 0, 0, 1],
    ])


def multiply_matrix(matrices: List) -> Tuple:
    try:
        dh_matrices = [generate_dh(dh=m) for m in matrices]
        dh_array = linalg_multi_dot(dh=dh_matrices)
        x, y, z = get_coord(dh=dh_array)
    except ValueError as e:
        return [], 0, 0, 0, str(e)

    return dh_array.tolist(), x, y, z, None
