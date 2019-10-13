import os


def pytest_collection_modifyitems(items, config):
    return
    ci_node_total = int(os.getenv("CI_NODE_TOTAL", 1))
    ci_node_index = int(os.getenv("CI_NODE_INDEX", 0))
    items[:] = [
        item
        for index, item in enumerate(items)
        if index % ci_node_total == ci_node_index
    ]