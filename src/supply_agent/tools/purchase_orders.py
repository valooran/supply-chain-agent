import csv

from supply_agent.paths import DATA_DIR


def read_purchase_orders(status: str | None = None) -> list[dict]:
    with open(DATA_DIR / "purchase_orders.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    if status:
        rows = [r for r in rows if r["status"] == status]
    return rows