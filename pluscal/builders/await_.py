from dataclasses import dataclass

from pluscal.ast import Await, Expr, Stmt
from pluscal.builders.base import Builder
from pluscal.builders.source import LabelSource, to_label


@dataclass
class AwaitBuilder(Builder[Stmt]):
    value: str
    label: LabelSource = None

    def build(self) -> Stmt:
        return Stmt(
            label=to_label(self.label),
            value=Await(Expr(self.value)),
        )
