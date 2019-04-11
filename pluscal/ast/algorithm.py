from dataclasses import dataclass
from typing import Iterable, Optional, Union

from pluscal.ast.base import Base, Line, Name
from pluscal.ast.definition import Definitions
from pluscal.ast.macro import Macros
from pluscal.ast.procedure import Procedures
from pluscal.ast.process import Processes
from pluscal.ast.statements import AlgorithmBody
from pluscal.ast.variable import VarDecls


@dataclass(frozen=True)
class Algorithm(Base):
    """
    Algorithm ::= [ --algorithm | --fair algorithm ] <Name>
                  <VarDecls>?
                  <Definitions>?
                  <Macro>*
                  <Procedure>*
                  [<AlgorithmBody> | <Process>+]
                  end algorithm

    """
    name: Name
    body: Union[AlgorithmBody, Processes]
    fair: bool = False
    variables: Optional[VarDecls] = None
    definitions: Optional[Definitions] = None
    macros: Optional[Macros] = None
    procedures: Optional[Procedures] = None

    def render(self, indent: int = 0) -> Iterable[Line]:
        algorithm = "fair algorithm" if self.fair else "algorithm"
        yield Line(f"--{algorithm} {str(self.name)}", indent)

        if self.variables:
            yield from self.variables.render(indent)

        if self.definitions:
            yield from self.definitions.render(indent)

        if self.macros:
            yield from self.macros.render(indent)

        if self.procedures:
            yield from self.procedures.render(indent)

        yield from self.body.render(indent)

        yield Line("end algorithm", indent)

    def validate(self) -> None:
        self.name.validate()

        if self.variables:
            self.variables.validate()

        if self.definitions:
            self.definitions.validate()

        if self.macros:
            self.macros.validate()

        if self.procedures:
            self.procedures.validate()

        self.body.validate()
