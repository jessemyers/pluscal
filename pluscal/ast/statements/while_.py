from dataclasses import dataclass
from typing import Iterable, Sequence

from pluscal.ast.base import Expr, Line
from pluscal.ast.statements.base import Stmt, UnlabeledStmt


@dataclass(frozen=True)
class While(UnlabeledStmt):
    """
    While ::= while <Expr> do <Stmt>+ end while;

    """
    condition: Expr
    statements: Sequence[Stmt]

    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line(f"while {str(self.condition)} do", indent)
        for statement in self.statements:
            yield from statement.render(indent + 2)
        yield Line("end while;", indent)

    def validate(self) -> None:
        self.condition.validate()
        assert self.statements
        for statement in self.statements:
            statement.validate()
