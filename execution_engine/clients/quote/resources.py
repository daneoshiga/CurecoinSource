from simple_rest_client.resource import Resource


class RiskQuote(Resource):
    actions = {
        "create": {"method": "POST", "url": "quote/risks/"},
        "evaluate": {"method": "POST", "url": "quote/risks/{}/evaluate/"},
        "retrieve": {"method": "GET", "url": "quote/risks/{}/"},
        "update": {"method": "PUT", "url": "quote/risks/{}/"},
        "update_fields": {"method": "PATCH", "url": "quote/risks/{}/fields/"},
    }
