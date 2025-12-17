import json
import pytest
from app.model_deployment import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_api_predict_success(client):
    """Tes apakah endpoint /predict merespon dengan benar."""
    payload = {
        "location": "New York",
        "amount": 500000,
        # "jam_transaksi": 10,
        # "kategori_transaksi": 1
    }

    response = client.post(
        "/api/prediction", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code == 200
    data = response.get_json()
    assert "prediction" in data


def test_api_missing_fields(client):
    """Tes API harus memunculkan error jika input kurang."""
    payload = {
        "amount": 500000
        # field lain tidak diisi
    }

    response = client.post(
        "/api/prediction", data=json.dumps(payload), content_type="application/json"
    )

    assert response.status_code in (400, 422)
