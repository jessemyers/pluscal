from dataclasses import dataclass, field
from typing import Callable, List, Optional

from pluscal.ast import Expr, Label, Stmt, While


@dataclass
class WhileBuilder:
    condition: str
    statements: List[Stmt] = field(default_factory=list)
    label: Optional[str] = None

    def __call__(self) -> Stmt:
        return Stmt(
            label=Label(self.label) if self.label is not None else None,
            value=While(
                condition=Expr(self.condition),
                statements=self.statements,
            ),
        )

    def do(self, head: Callable[[], Stmt], *tail: Callable[[], Stmt]) -> "WhileBuilder":
        self.statements.append(head())
        self.statements.extend(func() for func in tail)
        return self
