from .api import quote_api


class RiskQuoteClient:
    quote_api = quote_api

    def retrieve(self, risk_id):
        response = self.quote_api.risk_quote.retrieve(risk_id)
        return response.body

    def create(self, quote, risk_type_name):
        payload = {
            "quote": quote["id"],
            "parent_risk_quote": quote["root_risk_quote_id"],
            "risk_type_name": risk_type_name,
        }
        response = self.quote_api.risk_quote.create(body=payload)
        return response.body

    def update(self, risk_id, payload):
        response = self.quote_api.risk_quote.update(risk_id, body=payload)
        return response.body

    def evaluate(self, risk_id):
        response = self.quote_api.risk_quote.evaluate(risk_id)
        return response.body

    def update_field(self, risk_id, field, answer):
        payload = {"field_answers": {field: answer}}

        response = self.quote_api.risk_quote.update_fields(risk_id, body=payload)
        return response.body
