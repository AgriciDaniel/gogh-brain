from __future__ import annotations

import os
from datetime import date


def today() -> str:
    return os.environ.get("GOGH_TODAY") or date.today().isoformat()
