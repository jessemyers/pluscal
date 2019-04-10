from dataclasses import dataclass
from typing import Iterable, Sequence

from pluscal.ast.base import Expr, Line, Name
from pluscal.ast.statements.base import UnlabeledStmt


@dataclass(frozen=True)
class Call(UnlabeledStmt):
    """
    Call ::= call <MacroCall>

    MacroCall ::= <Name> ( [<Expr>, [, <Expr>]*]? ) ;

    """
    name: Name
    args: Sequence[Expr]

    def render(self, indent: int = 0) -> Iterable[Line]:
        args = ", ".join(str(arg) for arg in self.args)
        yield Line(f"call {str(self.name)}({args});", indent)

    def validate(self) -> None:
        self.name.validate()
        for arg in self.args:
            arg.validate()
