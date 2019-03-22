from dataclasses import dataclass, field
from typing import Callable, Optional

from pluscal.ast import Expr, If, Label, Skip, Stmt


@dataclass
class IfBuilder:
    condition: str
    then_: Stmt = field(default_factory=lambda: Stmt(Skip()))
    # XXX elsif
    otherwise_: Optional[Stmt] = None
    label: Optional[str] = None

    def __call__(self) -> Stmt:
        return Stmt(
            label=Label(self.label) if self.label is not None else None,
            value=If(
                condition=Expr(self.condition),
                then=[
                    self.then_,
                ],
                else_=[
                    self.otherwise_,
                ] if self.otherwise_ else None,
            ),
        )

    def then(self, value: Callable[[], Stmt]) -> "IfBuilder":
        self.then_ = value()
        return self

    def else_(self, value: Callable[[], Stmt]) -> "IfBuilder":
        self.otherwise_ = value()
        return self
