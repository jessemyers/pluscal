from dataclasses import dataclass, field
from typing import Iterable, Sequence, Union

from pluscal.ast.base import Expr, Field, Line, Variable
from pluscal.ast.statements.base import UnlabeledStmt


@dataclass(frozen=True)
class LHS:
    """
    LHS ::= Variable

    """
    name: Variable
    qualifier: Sequence[Union[Sequence[Expr], Field]] = field(default_factory=tuple)

    def validate(self) -> None:
        self.name.validate()

        for term in self.qualifier:
            if isinstance(term, Field):
                term.validate()
            else:
                expr: Expr
                for expr in term:
                    expr.validate()

    def wrap(self, item: Union[Sequence[Expr], Field]) -> str:
        if isinstance(item, Field):
            return f".{str(item)}"
        else:
            head, *tail = item
            rest = ", ".join(str(part) for part in tail)
            return f"[{str(head)}({rest})]"

    def __str__(self) -> str:
        qualifier = "".join(self.wrap(item) for item in self.qualifier)
        return f"{str(self.name)}{qualifier}"


@dataclass(frozen=True)
class Assignment:
    left: LHS
    right: Expr

    def validate(self) -> None:
        self.left.validate()
        self.right.validate()

    def __str__(self) -> str:
        return f"{str(self.left)} := {str(self.right)}"


@dataclass(frozen=True)
class Assign(UnlabeledStmt):
    """
    Assign ::= <LHS> := <Expr> [|| <LHS> := <Expr>]* ;

    """
    items: Sequence[Assignment]

    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line(" || ".join(str(item) for item in self.items) + ";", indent)

    def validate(self) -> None:
        assert self.items
        for item in self.items:
            item.validate()
