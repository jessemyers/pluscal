from dataclasses import dataclass
from typing import Iterable, Sequence

from pluscal.ast.base import Line
from pluscal.ast.statements import Stmt, UnlabeledStmt


@dataclass(frozen=True)
class Either(UnlabeledStmt):
    """
    Either ::= either <Stmt> [or <Stmt>+]+ end either ;

    """
    initial: Stmt
    or_: Sequence[Sequence[Stmt]]

    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line("either", indent)
        yield from self.initial.render(indent + 2)

        for item in self.or_:
            yield Line("or", indent)
            for statement in item:
                yield from statement.render(indent + 2)

        yield Line("end either;", indent)

    def validate(self) -> None:
        self.initial.validate()

        for item in self.or_:
            assert item
            for statement in item:
                statement.validate()
