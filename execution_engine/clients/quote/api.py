from simple_rest_client.api import API

from execution_engine.settings import settings

from . import resources


def get_api_instance(timeout=None):
    api = API(api_root_url=settings.QUOTE_ROOT_URL, json_encode_body=True)

    api.add_resource(resource_name="risk_quote", resource_class=resources.RiskQuote)

    return api


quote_api = get_api_instance()
