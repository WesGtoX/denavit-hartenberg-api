from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.model import DenavitHartenberg
from app.utils import multiply_matrix
from app.docs import RESPONSES_EXAMPLE

app = FastAPI()


origins = [
    'https://dh.wesleymendes.com.br',
    'https://www.dh.wesleymendes.com.br',
    'https://denavit-hartenberg.netlify.app',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', responses={200: RESPONSES_EXAMPLE.get('dh')})
def dh():
    return {'dh': 'Denavit-Hartenberg API'}


@app.post('/calculate-dh/', responses={200: RESPONSES_EXAMPLE.get('calculate_dh')})
async def calculate_dh(dh_list: List[DenavitHartenberg]):
    dh_calc, x, y, z, error = multiply_matrix(dh_list)

    if error:
        raise HTTPException(status_code=404, detail=error)

    return {'result': dh_calc, 'coord': {'x': x, 'y': y, 'z': z}}
