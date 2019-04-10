from dataclasses import dataclass, field
from typing import List

from pluscal.ast import Call, Expr, Name, Stmt
from pluscal.builder.base import Builder
from pluscal.builder.sources import LabelSource, to_label


@dataclass
class CallBuilder(Builder[Stmt]):
    name: str
    args: List[Expr] = field(default_factory=list)
    label: LabelSource = None

    def __call__(self, *args: str) -> "CallBuilder":
        return self.with_(*args)

    def with_(self, *args: str) -> "CallBuilder":
        self.args.extend(Expr(arg) for arg in args)
        return self

    def build(self) -> Stmt:
        return Stmt(
            label=to_label(self.label),
            value=Call(
                name=Name(self.name),
                args=self.args,
            ),
        )
