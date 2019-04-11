from dataclasses import dataclass, field
from typing import List, Tuple, Union

from pluscal.ast import LHS, Assign, Assignment, Expr, Field, Stmt, Variable
from pluscal.builders.base import Builder
from pluscal.builders.source import LabelSource, LHSSource, to_label, to_lhs


@dataclass
class LHSBuilder(Builder[LHS]):
    name: str
    items: List[Union[List[Expr], Field]] = field(default_factory=list)

    def build(self) -> LHS:
        return LHS(
            name=Variable(self.name),
            items=self.items,
        )

    def __getattr__(self, key: str) -> "LHSBuilder":
        self.items.append(Field(key))
        return self

    def __getitem__(self, key: Union[str, Tuple[str, ...]]) -> "LHSBuilder":
        if isinstance(key, tuple):
            self.items.append([Expr(arg) for arg in key])
        else:
            self.items.append([Expr(key)])
        return self


@dataclass
class AssignBuilder(Builder[Stmt]):
    left: LHSSource
    right: str
    items: List[Tuple[LHSSource, str]] = field(default_factory=list)
    label: LabelSource = None

    def build(self) -> Stmt:
        return Stmt(
            label=to_label(self.label),
            value=Assign(
                items=[
                    Assignment(
                        left=to_lhs(left),
                        right=Expr(right),
                    )
                    for left, right in [
                        (self.left, self.right)
                    ] + self.items
                ],
            ),
        )

    def and_(self, left: LHSSource, right: str) -> "AssignBuilder":
        self.items.append((left, right))
        return self
