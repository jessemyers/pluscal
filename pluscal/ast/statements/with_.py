from dataclasses import dataclass
from typing import Iterable, Sequence

from pluscal.ast.base import Line
from pluscal.ast.statements.base import Stmt, UnlabeledStmt
from pluscal.ast.variables import VarDecl


@dataclass(frozen=True)
class With(UnlabeledStmt):
    """
    With :: = with [<Variable> [=|\\in] <Expr> [;|,]]+
                do <Stmt>+
              end with;

    """
    declarations: Sequence[VarDecl]
    statements: Sequence[Stmt]

    def render(self, indent: int = 0) -> Iterable[Line]:
        declarations = ", ".join(str(declaration) for declaration in self.declarations)
        yield Line(f"with {declarations}", indent)

        yield Line("do", indent)
        for statement in self.statements:
            yield from statement.render(indent + 2)
        yield Line("end with;", indent)

    def validate(self) -> None:
        assert self.declarations
        assert self.statements

        for declaration in self.declarations:
            declaration.validate()

        for statement in self.statements:
            statement.validate()
