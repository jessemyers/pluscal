from typing import Iterable

from pluscal.ast.base import Line
from pluscal.ast.statements.base import UnlabeledStmt


class Skip(UnlabeledStmt):
    """
    Skip ::= skip ;

    """
    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line("skip;", indent)

    def validate(self) -> None:
        pass
