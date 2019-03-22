from dataclasses import dataclass
from typing import Iterable

from pluscal.ast.base import Expr, Line
from pluscal.ast.statements.base import UnlabeledStmt


@dataclass(frozen=True)
class Print(UnlabeledStmt):
    """
    Print ::= print <Expr> ;

    """
    value: Expr

    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line(f"print {str(self.value)};", indent)

    def validate(self) -> None:
        self.value.validate()
