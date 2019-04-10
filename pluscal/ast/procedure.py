from dataclasses import dataclass, field
from typing import Iterable, Optional, Sequence

from pluscal.ast.base import Base, Expr, Line, Name, Node, Variable
from pluscal.ast.statements import AlgorithmBody


@dataclass(frozen=True)
class PVarDecl(Node):
    """
    PVarDecl ::= <Variable> [= <Expr>]?

    """
    name: Variable
    value: Optional[Expr] = None

    def validate(self) -> None:
        self.name.validate()
        if self.value is not None:
            self.value.validate()

    def __str__(self) -> str:
        if self.value is not None:
            return f"{str(self.name)} = {str(self.value)}"
        else:
            return f"{str(self.name)}"


@dataclass(frozen=True)
class PVarDecls(Base):
    """
    PVarDecls ::= [variable | variables] [<PVarDecls> [;|,]]+

    """
    items: Sequence[PVarDecl] = field(default_factory=tuple)

    def render(self, indent: int = 0) -> Iterable[Line]:
        values = ", ".join(str(item) for item in self.items)
        variable = "variables" if len(self.items) > 1 else "variable"

        yield Line(f"{variable} {values};", indent)

    def validate(self) -> None:
        assert self.items
        for item in self.items:
            item.validate()


@dataclass(frozen=True)
class Procedure(Base):
    """
    Procedure ::= procedure <Name> ( [<Variable> [, <Variable>]*]?)
                  <PVarDecls>?
                  <AlgorithmBody>
                  end procedure

    """
    name: Name
    args: Sequence[Variable]
    variables: Optional[PVarDecls]
    body: AlgorithmBody

    def render(self, indent: int = 0) -> Iterable[Line]:
        args = ", ".join(str(arg) for arg in self.args)
        yield Line(f"procedure {str(self.name)}({args})", indent)

        if self.variables is not None:
            yield Line(str(self.variables), indent)

        yield from self.body.render(indent)
        yield Line("end procedure", indent)

    def validate(self) -> None:
        self.name.validate()

        for arg in self.args:
            arg.validate()

        if self.variables:
            self.variables.validate()

        self.body.validate()
