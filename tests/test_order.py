import pytest
from nimbuspost.api.b2c import shipment


def test_create_order(requests_mock):
    payload = {
        "receiver": {"name": "John", "address": "123 Main St"},
        "items": [{"name": "Shoes", "quantity": 1}]
    }
    mock_response = {"order_id": "ORD123", "status": "created"}

    requests_mock.post(
        "https://api.yourshippingprovider.com/v1/orders",
        json=mock_response,
        status_code=201
    )

    shipment_obj=shipment.Shipment()
    result = shipment_obj.create(payload)
    assert result["order_id"] == "ORD123"
    assert result["status"] == "created"
