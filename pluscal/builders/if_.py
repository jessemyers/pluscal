from dataclasses import dataclass, field
from typing import List, Tuple

from pluscal.ast import Expr, If, Stmt
from pluscal.builders.base import Builder
from pluscal.builders.source import LabelSource, StatementSource, to_label, to_statement


@dataclass
class IfBuilder(Builder[Stmt]):
    condition: str
    statements: List[Stmt] = field(default_factory=list)
    elsif_: List[Tuple[str, List[Stmt]]] = field(default_factory=list)
    otherwise: List[Stmt] = field(default_factory=list)
    label: LabelSource = None

    def build(self) -> Stmt:
        return Stmt(
            label=to_label(self.label),
            value=If(
                condition=Expr(self.condition),
                then=self.statements,
                elsif=[
                    (
                        Expr(condition),
                        statements,
                    )
                    for condition, statements in self.elsif_
                ],
                else_=self.otherwise if self.otherwise else None,
            ),
        )

    def then(self, *args: StatementSource) -> "IfBuilder":
        self.statements.extend(to_statement(arg) for arg in args)
        return self

    def elsif(self, condition: str, *args: StatementSource) -> "IfBuilder":
        self.elsif_.append((condition, [to_statement(arg) for arg in args]))
        return self

    def else_(self, *args: StatementSource) -> "IfBuilder":
        self.otherwise.extend(to_statement(arg) for arg in args)
        return self
