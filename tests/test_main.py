from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_calculate_dh():
    response = client.post(
        "/calculate-dh/",
        headers={"Content-Type": "application/json"},
        json=[
            {"a": 2, "alpha": 0, "d": 4, "theta": 90},
            {"a": 1, "alpha": 180, "d": 0, "theta": 180},
            {"a": 0, "alpha": 0, "d": 2, "theta": 0},
            {"a": 0, "alpha": 0, "d": 0, "theta": 90}
        ]
    )
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            [
                -0.5352639122994977, -0.8328267254000491,
                0.14103967402566783, 0.37031406642550035
            ],
            [
                -0.44778377204093445, 0.42135061101509674,
                0.7886401943180406, 3.189227769365986
            ],
            [
                -0.7162277833808375, 0.3589753585646732,
                -0.5984600690578581, 2.803079861884284
            ],
            [0.0, 0.0, 0.0, 1.0]
        ],
        "coord": {
            "x": 0.37031406642550035,
            "y": 3.189227769365986,
            "z": 2.803079861884284
        }
    }
