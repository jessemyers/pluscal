from dataclasses import dataclass
from typing import Iterable, Sequence

from pluscal.ast.base import Line
from pluscal.ast.statements import Stmt, UnlabeledStmt


@dataclass(frozen=True)
class Either(UnlabeledStmt):
    """
    Either ::= either <Stmt> [or <Stmt>+]+ end either ;

    """
    items: Sequence[Sequence[Stmt]]

    def render(self, indent: int = 0) -> Iterable[Line]:
        for index, statements in enumerate(self.items):
            yield Line("or" if index else "either", indent)
            for statement in statements:
                yield from statement.render(indent + 2)

        yield Line("end either;", indent)

    def validate(self) -> None:
        assert self.items
        for statements in self.items:
            assert statements
            for statement in statements:
                statement.validate()
