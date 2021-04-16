import logging

from bc_lambda import bc_lambda

from execution_engine.engines.cover import execution_engine


@bc_lambda(level=logging.DEBUG, service="ExecutionEngine", stage="sandbox")
def execution_handler(event, context):
    return execution_engine(event, context)
