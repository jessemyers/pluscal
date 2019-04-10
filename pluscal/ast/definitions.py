from dataclasses import dataclass
from typing import Iterable, Sequence

from pluscal.ast.base import Base, Line


Def = str


@dataclass(frozen=True)
class Definitions(Base):
    """
    Definitions ::= define <Defs> end define [;]?

    Defs ::= A sequence of TLA+ definitions not containing a PlusCal reserved word or symbol

    """
    items: Sequence[Def]

    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line("define", indent)
        yield from (
            Line(line, indent + 2)
            for item in self.items
            for line in item.splitlines()
        )
        yield Line("end define", indent)

    def validate(self) -> None:
        assert self.items
