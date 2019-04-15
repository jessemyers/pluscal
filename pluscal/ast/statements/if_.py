from dataclasses import dataclass, field
from typing import Iterable, Optional, Sequence

from pluscal.ast.base import Expr, Line, Node
from pluscal.ast.statements.base import Stmt, UnlabeledStmt


Statements = Sequence[Stmt]


@dataclass(frozen=True)
class Clause(Node):
    condition: Expr
    statements: Statements

    @property
    def clause_type(self) -> str:
        raise NotImplementedError()

    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line(f"{self.clause_type} {str(self.condition)} then", indent)
        for statement in self.statements:
            yield from statement.render(indent + 2)

    def validate(self) -> None:
        self.condition.validate()

        assert self.statements
        for statement in self.statements:
            statement.validate()


class IfClause(Clause):

    @property
    def clause_type(self) -> str:
        return "if"


class ElsifClause(Clause):

    @property
    def clause_type(self) -> str:
        return "elsif"


@dataclass(frozen=True)
class If(UnlabeledStmt):
    """
    If ::= if <Expr> then <Stmt>+
                     [elsif <Expr> then <Stmt>+]*
                     [else <Stmt>+]?
            end if;

    """
    if_clause: IfClause
    elsif_clauses: Sequence[ElsifClause] = field(default_factory=tuple)
    else_: Optional[Statements] = None

    def render(self, indent: int = 0) -> Iterable[Line]:
        yield from self.if_clause.render(indent)

        for elsif_clause in self.elsif_clauses:
            yield from elsif_clause.render(indent)

        if self.else_:
            yield Line("else", indent)
            for statement in self.else_:
                yield from statement.render(indent + 2)

        yield Line(f"end if;", indent)

    def validate(self) -> None:
        self.if_clause.validate()

        for elsif_clause in self.elsif_clauses:
            elsif_clause.validate()

        if self.else_ is not None:
            assert self.else_
            for statement in self.else_:
                statement.validate()
