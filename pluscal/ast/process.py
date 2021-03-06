from dataclasses import dataclass
from typing import Iterable, Optional, Sequence

from pluscal.ast.base import Base, Expr, Line, Name
from pluscal.ast.statements import AlgorithmBody
from pluscal.ast.variable import DeclType, VarDecls


@dataclass(frozen=True)
class Process(Base):
    """
    Process ::= [fair [+]?]? process <Name> [= | \\in] <Expr>
                <VarDecls>?
                <AlgorithmBody>
                end process [;]?

    """
    # XXX need to implement fairness/strong fairness
    name: Name
    type: DeclType
    value: Expr
    body: AlgorithmBody
    variables: Optional[VarDecls] = None

    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line(f"process {str(self.name)} {str(self.type)} {str(self.value)}", indent)

        if self.variables is not None:
            yield from self.variables.render(indent)

        yield from self.body.render(indent)
        yield Line("end process;", indent)

    def validate(self) -> None:
        self.name.validate()
        self.value.validate()

        if self.variables:
            self.variables.validate()

        self.body.validate()


@dataclass
class Processes(Base):
    items: Sequence[Process]

    def render(self, indent: int = 0) -> Iterable[Line]:
        for index, item in enumerate(self.items):
            yield Line()
            yield from item.render(indent)

    def validate(self) -> None:
        assert self.items
        for item in self.items:
            item.validate()
