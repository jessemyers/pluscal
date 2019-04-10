from dataclasses import dataclass, field
from typing import Iterable, Optional, Sequence

from pluscal.ast.base import Base, Line, Name
from pluscal.ast.definitions import Definitions
from pluscal.ast.macro import Macro
from pluscal.ast.procedure import Procedure
from pluscal.ast.process import Process
from pluscal.ast.statements import AlgorithmBody
from pluscal.ast.variables import VarDecls


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
    body: AlgorithmBody
    fair: bool = False
    variables: Optional[VarDecls] = None
    definitions: Optional[Definitions] = None
    macros: Sequence[Macro] = field(default_factory=tuple)
    procedures: Sequence[Procedure] = field(default_factory=tuple)

    def render(self, indent: int = 0) -> Iterable[Line]:
        algorithm = "fair algorithm" if self.fair else "algorithm"
        yield Line(f"--{algorithm} {str(self.name)}", indent)

        if self.variables:
            yield from self.variables.render(indent)

        if self.definitions:
            yield from self.definitions.render(indent)

        yield from (
            line
            for macro in self.macros
            for line in macro.render(indent)
        )

        yield from (
            line
            for procedure in self.procedures
            for line in procedure.render(indent)
        )

        if isinstance(self.body, AlgorithmBody):
            yield from self.body.render(indent)
        else:
            process: Process
            yield from (
                line
                for process in self.body
                for line in process.render(indent)
            )

        yield Line("end algorithm", indent)

    def validate(self) -> None:
        self.name.validate()

        if self.variables:
            self.variables.validate()

        if self.definitions:
            self.definitions.validate()

        for macro in self.macros:
            macro.validate()

        for procedure in self.procedures:
            procedure.validate()

        if isinstance(self.body, AlgorithmBody):
            self.body.validate()
        else:
            process: Process
            for process in self.body:
                process.validate()
