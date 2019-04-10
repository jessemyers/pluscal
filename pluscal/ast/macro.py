from dataclasses import dataclass, field
from typing import Iterable, Sequence

from pluscal.ast.base import Base, Line, Name, Variable
from pluscal.ast.statements import AlgorithmBody


@dataclass(frozen=True)
class Macro(Base):
    """
    Macro ::= macro <Name> ( <Variable> [, <Variable>]* )
              <AlgorithmBody>
              end macro

    """
    name: Name
    args: Sequence[Variable]
    body: AlgorithmBody

    def render(self, indent: int = 0) -> Iterable[Line]:
        args = ", ".join(str(arg) for arg in self.args)
        yield Line(f"macro {str(self.name)}({args})", indent)

        yield from self.body.render(indent)
        yield Line("end macro", indent)

    def validate(self) -> None:
        self.name.validate()

        for arg in self.args:
            arg.validate()

        self.body.validate()


@dataclass(frozen=True)
class Macros(Base):
    items: Sequence[Macro] = field(default_factory=tuple)

    def render(self, indent: int = 0) -> Iterable[Line]:
        for item in self.items:
            yield from item.render(indent)

    def validate(self) -> None:
        for item in self.items:
            item.validate()
