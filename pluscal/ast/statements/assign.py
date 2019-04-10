from dataclasses import dataclass, field
from typing import Iterable, Sequence, Union

from pluscal.ast.base import Expr, Field, Line, Node, Variable
from pluscal.ast.statements.base import UnlabeledStmt


@dataclass(frozen=True)
class LHS(Node):
    """
    LHS ::= <Variable> [ "[" <Expr> [, <Expr]* "]" | . <Field> ]*

    """
    name: Variable
    items: Sequence[Union[Sequence[Expr], Field]] = field(default_factory=tuple)

    def validate(self) -> None:
        self.name.validate()

        for item in self.items:
            if isinstance(item, Field):
                item.validate()
            else:
                expr: Expr
                for expr in item:
                    expr.validate()

    def wrap(self, item: Union[Sequence[Expr], Field]) -> str:
        if isinstance(item, Field):
            return f".{str(item)}"
        else:
            items = ", ".join(str(part) for part in item)
            return f"[{items}]"

    def __str__(self) -> str:
        items = "".join(self.wrap(item) for item in self.items)
        return f"{str(self.name)}{items}"


@dataclass(frozen=True)
class Assignment(Node):
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
