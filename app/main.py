from typing import List
from fastapi import FastAPI

from app.model import DenavitHartenberg
from app.utils import multiply_matrix

app = FastAPI()


@app.post("/calculate-dh/")
async def calculate_dh(dh_list: List[DenavitHartenberg]):
    dh_calc, x, y, z = multiply_matrix(dh_list)
    return {"result": dh_calc, "coord": {"x": x, "y": y, "z": z}}
