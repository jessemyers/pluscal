from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from pluscal.ast import LHS, Assign, Assignment, Expr, Label, Stmt, Variable


@dataclass
class AssignBuilder:
    left: str
    right: str
    extra: List[Tuple[str, str]] = field(default_factory=list)
    label: Optional[str] = None

    def __call__(self) -> Stmt:
        return Stmt(
            label=Label(self.label) if self.label is not None else None,
            value=Assign(
                items=[
                    Assignment(
                        LHS(
                            Variable(left),
                            # XXX
                        ),
                        Expr(right),
                    )
                    for left, right in [
                        (self.left, self.right),
                        *self.extra,
                    ]
                ],
            ),
        )

    def and_(self, left: str, right: str) -> "AssignBuilder":
        self.extra.append((left, right))
        return self
