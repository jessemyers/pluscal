from dataclasses import dataclass
from typing import List

from pluscal.ast import Either, Stmt
from pluscal.builders.base import Builder
from pluscal.builders.source import LabelSource, StatementSource, to_label, to_statement


@dataclass(init=False)
class EitherBuilder(Builder[Stmt]):
    items: List[List[Stmt]]
    label: LabelSource = None

    def __init__(self, *args: StatementSource, label: LabelSource = None):
        self.items = [[to_statement(arg) for arg in args]]
        self.label = label

    def build(self) -> Stmt:
        return Stmt(
            label=to_label(self.label),
            value=Either(self.items),
        )

    def or_(self, *args: StatementSource) -> "EitherBuilder":
        self.items.append([to_statement(arg) for arg in args])
        return self
