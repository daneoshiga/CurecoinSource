import logging

from execution_engine.clients.quote import RiskQuoteClient

logger = logging.getLogger(__name__)


risk_quote_client = RiskQuoteClient()


def execution_engine(event, context):
    root_risk_id = event["root_risk_quote_id"]
    root_risk = risk_quote_client.retrieve(root_risk_id)
    risk_quote_client.update(root_risk_id, root_risk)
    return {"result": "execution engine success"}
