from dataclasses import dataclass, field
from enum import Enum, unique
from typing import Iterable, Optional, Sequence, Tuple

from pluscal.ast.base import Base, Expr, Line, Variable


@unique
class DeclType(Enum):
    EQUALS = "="
    IN = "\\in"

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class VarDecl:
    """
    VarDecl ::= <Variable> [[= | \\in] <Expr>? [;|,]

    """
    name: Variable
    value: Optional[Tuple[DeclType, Expr]] = None

    def validate(self) -> None:
        self.name.validate()
        if self.value is not None:
            _, expr = self.value
            expr.validate()

    def __str__(self) -> str:
        if self.value is not None:
            return f"{str(self.name)} {str(self.value[0])} {str(self.value[1])}"
        else:
            return str(self.name)


@dataclass(frozen=True)
class VarDecls(Base):
    """
    VarDecls ::= [variable | variables] <VarDecl>+

    """
    items: Sequence[VarDecl] = field(default_factory=tuple)

    def render(self, indent: int = 0) -> Iterable[Line]:
        values = ", ".join(str(item) for item in self.items)
        variable = "variables" if len(self.items) > 1 else "variable"

        yield Line(f"{variable} {values};", indent)

    def validate(self) -> None:
        assert self.items
        for item in self.items:
            item.validate()
