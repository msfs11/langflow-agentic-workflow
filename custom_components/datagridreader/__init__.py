from __future__ import annotations
from typing import TYPE_CHECKING
from lfx.components._importing import import_mod

if TYPE_CHECKING:
    from .datagridreader import DataGridReader

_dynamic_imports = {"DataGridReader": "datagridreader"}
__all__ = ["DataGridReader"]

def __getattr__(name: str) -> Any:
    if name not in _dynamic_imports:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
    result = import_mod(name, _dynamic_imports[name], __spec__.parent)
    globals()[name] = result
    return result
