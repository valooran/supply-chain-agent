from supply_agent.tools.inventory import query_inventory
from supply_agent.tools.purchase_orders import read_purchase_orders

TOOL_SCHEMAS = [
    {
        "name": "read_purchase_orders",
        "description": (
            "Read purchase orders from the PO spreadsheet. Each PO has po_number, "
            "supplier, item, quantity, due_date (YYYY-MM-DD) and status. "
            "Optionally filter by status."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "status": {
                    "type": "string",
                    "enum": ["open", "delivered"],
                    "description": "Only return POs with this status.",
                }
            },
            "required": [],
        },
    },
    {
        "name": "query_inventory",
        "description": (
            "Look up current stock for one item. Returns on_hand, reorder_point and "
            "whether stock is below the reorder point. The item name must match "
            "exactly, e.g. 'M12 bolts'."
        ),
        "input_schema": {
            "type": "object",
            "properties": {"item": {"type": "string", "description": "Exact item name."}},
            "required": ["item"],
        },
    },
]

TOOL_FUNCTIONS = {
    "read_purchase_orders": read_purchase_orders,
    "query_inventory": query_inventory,
}