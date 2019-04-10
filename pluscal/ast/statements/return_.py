from typing import Iterable

from pluscal.ast.base import Line
from pluscal.ast.statements.base import UnlabeledStmt


class Return(UnlabeledStmt):
    """
    Return ::= return ;

    """
    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line("return;", indent)

    def validate(self) -> None:
        pass
