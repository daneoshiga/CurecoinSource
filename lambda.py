from engines.cover import execution_engine


def execution_handler(event, context):
    return execution_engine(event, context)
