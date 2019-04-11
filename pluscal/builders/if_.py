from dataclasses import dataclass, field
from typing import List

from pluscal.ast import ElsifClause, Expr, If, IfClause, Stmt
from pluscal.builders.base import Builder
from pluscal.builders.source import LabelSource, StatementSource, to_label, to_statement


@dataclass
class ElsifBuilder(Builder[ElsifClause]):
    parent: "IfBuilder"
    condition: str
    statements: List[Stmt] = field(default_factory=list)

    def build(self) -> ElsifClause:
        return ElsifClause(
            Expr(self.condition),
            self.statements,
        )

    def then(self, *args: StatementSource) -> "IfBuilder":
        self.statements.extend(to_statement(arg) for arg in args)
        self.parent.elsif_clauses.append(self.build())
        return self.parent


@dataclass
class IfBuilder(Builder[Stmt]):
    condition: str
    statements: List[Stmt] = field(default_factory=list)
    elsif_clauses: List[ElsifClause] = field(default_factory=list)
    otherwise: List[Stmt] = field(default_factory=list)
    label: LabelSource = None

    def build(self) -> Stmt:
        return Stmt(
            label=to_label(self.label),
            value=If(
                IfClause(
                    Expr(self.condition),
                    self.statements,
                ),
                self.elsif_clauses,
                self.otherwise if self.otherwise else None,
            ),
        )

    def then(self, *args: StatementSource) -> "IfBuilder":
        self.statements.extend(to_statement(arg) for arg in args)
        return self

    def elsif(self, condition: str) -> ElsifBuilder:
        return ElsifBuilder(self, condition)

    def else_(self, *args: StatementSource) -> "IfBuilder":
        self.otherwise.extend(to_statement(arg) for arg in args)
        return self
