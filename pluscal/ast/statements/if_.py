from dataclasses import dataclass, field
from typing import Iterable, Optional, Sequence, Tuple

from pluscal.ast.base import Expr, Line
from pluscal.ast.statements.base import Stmt, UnlabeledStmt


@dataclass(frozen=True)
class If(UnlabeledStmt):
    """
    If ::= if <Expr> then <Stmt>+
                     [elsif <Expr> then <Stmt>+]*
                     [else <Stmt>+]?
            end if;

    """
    condition: Expr
    then: Sequence[Stmt]
    elsif: Sequence[Tuple[Expr, Sequence[Stmt]]] = field(default_factory=list)
    else_: Optional[Sequence[Stmt]] = None

    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line(f"if {str(self.condition)} then", indent)
        for statement in self.then:
            yield from statement.render(indent + 2)

        for condition, statements in self.elsif:
            yield Line(f"elsif {str(condition)} then", indent)
            for statement in statements:
                yield from statement.render(indent + 2)

        if self.else_:
            yield Line("else", indent)
            for statement in self.else_:
                yield from statement.render(indent + 2)

        yield Line(f"end if;", indent)

    def validate(self) -> None:
        self.condition.validate()

        assert self.then
        for statement in self.then:
            statement.validate()

        for _, statements in self.elsif:
            assert statements
            for statement in statements:
                statement.validate()

        if self.else_ is not None:
            assert self.else_
            for statement in self.else_:
                statement.validate()
