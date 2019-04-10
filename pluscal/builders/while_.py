from dataclasses import dataclass, field
from typing import List

from pluscal.ast import Expr, Stmt, While
from pluscal.builders.base import Builder
from pluscal.builders.source import LabelSource, StatementSource, to_label, to_statement


@dataclass
class WhileBuilder(Builder[Stmt]):
    condition: str
    statements: List[Stmt] = field(default_factory=list)
    label: LabelSource = None

    def build(self) -> Stmt:
        return Stmt(
            label=to_label(self.label),
            value=While(
                condition=Expr(self.condition),
                statements=self.statements,
            ),
        )

    def do(self, *args: StatementSource) -> "WhileBuilder":
        self.statements.extend(to_statement(arg) for arg in args)
        return self
