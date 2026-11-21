from supply_agent.tools import query_inventory, read_purchase_orders


def test_filter_open_pos():
    assert all(po["status"] == "open" for po in read_purchase_orders("open"))


def test_unknown_item_returns_error():
    assert "error" in query_inventory("Unicorn bolts")