from dataclasses import dataclass
from typing import Iterable, Sequence

from pluscal.ast.base import Expr, Line, Name
from pluscal.ast.statements.base import UnlabeledStmt


@dataclass(frozen=True)
class AbstractCall:
    name: Name
    args: Sequence[Expr]

    @property
    def value(self) -> str:
        args = ", ".join(str(arg) for arg in self.args)
        return f"{str(self.name)}({args});"

    def validate(self) -> None:
        self.name.validate()
        for arg in self.args:
            arg.validate()


class Call(AbstractCall, UnlabeledStmt):
    """
    Call ::= call <MacroCall>

    """
    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line(f"call {self.value}", indent)


class MacroCall(AbstractCall, UnlabeledStmt):
    """
    MacroCall ::= <Name> ( [<Expr>, [, <Expr>]*]? ) ;

    """
    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line(self.value, indent)
