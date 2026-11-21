import sqlite3

from supply_agent.paths import DATA_DIR

rows = [
    ("Steel beam 3m", 40, 100),
    ("M12 bolts", 800, 2000),
    ("Upright frame", 15, 50),
    ("Wire decking", 300, 100),
    ("Anchor bolts", 2500, 1000),
]

conn = sqlite3.connect(DATA_DIR / "inventory.db")
conn.execute("DROP TABLE IF EXISTS inventory")
conn.execute(
    "CREATE TABLE inventory (item TEXT PRIMARY KEY, on_hand INTEGER, reorder_point INTEGER)"
)
conn.executemany("INSERT INTO inventory VALUES (?, ?, ?)", rows)
conn.commit()
conn.close()
print("Created inventory.db")