from pydantic import BaseModel


class DenavitHartenberg(BaseModel):
    a: float
    alpha: float
    d: float
    theta: float
