from dataclasses import dataclass
from typing import Iterable

from pluscal.ast.base import Label, Line
from pluscal.ast.statements.base import UnlabeledStmt


@dataclass(frozen=True)
class Goto(UnlabeledStmt):
    """
    Goto ::= goto <Label> ;

    """
    value: Label

    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line(f"goto {str(self.value)};", indent)

    def validate(self) -> None:
        self.value.validate()
