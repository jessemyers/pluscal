from dataclasses import dataclass
from typing import Optional

from pluscal.ast import Expr, Label, Print, Stmt


@dataclass
class PrintBuilder:
    value: str
    label: Optional[str] = None

    def __call__(self) -> Stmt:
        return Stmt(
            label=Label(self.label) if self.label is not None else None,
            value=Print(Expr(self.value)),
        )
