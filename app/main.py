from typing import List
from fastapi import FastAPI, HTTPException

from app.model import DenavitHartenberg
from app.utils import multiply_matrix
from app.docs import RESPONSES_EXAMPLE

app = FastAPI()


@app.get('/', responses={200: RESPONSES_EXAMPLE.get('dh')})
def dh():
    return {'dh': 'Denavit-Hartenberg API'}


@app.post('/calculate-dh/', responses={200: RESPONSES_EXAMPLE.get('calculate_dh')})
async def calculate_dh(dh_list: List[DenavitHartenberg]):
    dh_calc, x, y, z, error = multiply_matrix(dh_list)

    if error:
        raise HTTPException(status_code=404, detail=error)

    return {'result': dh_calc, 'coord': {'x': x, 'y': y, 'z': z}}
