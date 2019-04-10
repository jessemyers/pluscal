from dataclasses import dataclass
from typing import List

from pluscal.ast import Stmt, VarDecl, With
from pluscal.builder.base import Builder
from pluscal.builder.sources import LabelSource, StatementSource, VariableSource, to_label, to_statement, to_variable


@dataclass(init=False)
class WithBuilder(Builder[Stmt]):
    declarations: List[VarDecl]
    statements: List[Stmt]
    label: LabelSource = None

    def __init__(self, *args: VariableSource, label: LabelSource = None):
        self.declarations = [to_variable(arg) for arg in args]
        self.statements = []
        self.label = label

    def build(self) -> Stmt:
        return Stmt(
            label=to_label(self.label),
            value=With(
                declarations=self.declarations,
                statements=self.statements,
            ),
        )

    def do(self, *args: StatementSource) -> "WithBuilder":
        self.statements.extend(to_statement(arg) for arg in args)
        return self
