from dataclasses import dataclass
from typing import Optional

from pluscal.ast import Assert, Expr, Label, Stmt


@dataclass
class AssertBuilder:
    value: str
    label: Optional[str] = None

    def __call__(self) -> Stmt:
        return Stmt(
            label=Label(self.label) if self.label is not None else None,
            value=Assert(Expr(self.value)),
        )
