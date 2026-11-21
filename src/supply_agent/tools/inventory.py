import sqlite3

from supply_agent.paths import DATA_DIR


def query_inventory(item: str) -> dict:
    db_path = DATA_DIR / "inventory.db"
    if not db_path.exists():
        raise FileNotFoundError(
            "inventory.db not found. Run: python scripts/create_inventory_db.py"
        )
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        "SELECT item, on_hand, reorder_point FROM inventory WHERE item = ?", (item,)
    ).fetchone()
    conn.close()
    if row is None:
        return {"error": f"No inventory record for '{item}'"}
    result = dict(row)
    result["below_reorder_point"] = row["on_hand"] < row["reorder_point"]
    return result