import pytest
from nimbuspost.api.b2c import courier


def test_get_couriers(requests_mock):
    mock_response = {
        "couriers": [
            {"id": "dhl", "name": "DHL"},
            {"id": "fedex", "name": "FedEx"}
        ]
    }
    requests_mock.get(
        "https://api.yourshippingprovider.com/v1/couriers", json=mock_response)
    courier_instance = courier.Courier()
    result = courier_instance.serviceability()
    assert isinstance(result, dict)
    assert "couriers" in result
    assert len(result["couriers"]) == 2
    assert result["couriers"][0]["name"] == "DHL"
