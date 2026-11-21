import runpy
from pathlib import Path

import pytest

@pytest.fixture(scope="session", autouse=True)
def inventory_db():
    script = Path(__file__).parents[1] / "scripts" / "create_inventory_db.py"
    runpy.run_path(str(script))