from dataclasses import dataclass, field

from pluscal.ast import Algorithm, Name
from pluscal.builders.base import Builder
from pluscal.builders.body import BodyBuilder
from pluscal.builders.definition import DefinitionsBuilder
from pluscal.builders.macro import MacrosBuilder
from pluscal.builders.procedure import ProceduresBuilder
from pluscal.builders.process import ProcessesBuilder
from pluscal.builders.source import MacroSource, ProcedureSource, ProcessSource, StatementSource, VariableSource
from pluscal.builders.variable import VariablesBuilder


@dataclass
class AlgorithmBuilder(Builder[Algorithm]):
    name: str
    body: BodyBuilder = field(default_factory=BodyBuilder)
    definitions: DefinitionsBuilder = field(default_factory=DefinitionsBuilder)
    fair_: bool = False
    macros_: MacrosBuilder = field(default_factory=MacrosBuilder)
    procedures_: ProceduresBuilder = field(default_factory=ProceduresBuilder)
    processes: ProcessesBuilder = field(default_factory=ProcessesBuilder)
    variables: VariablesBuilder = field(default_factory=VariablesBuilder)

    def build(self) -> Algorithm:
        return Algorithm(
            name=Name(self.name),
            body=self.body.build() if self.body else self.processes.build(),
            definitions=self.definitions.build(),
            fair=self.fair_,
            macros=self.macros_.build(),
            variables=self.variables.build(),
        )

    def declare(self, *args: VariableSource) -> "AlgorithmBuilder":
        self.variables.declare(*args)
        return self

    def define(self, *args: str) -> "AlgorithmBuilder":
        self.definitions.define(*args)
        return self

    def do(self, *args: StatementSource) -> "AlgorithmBuilder":
        assert not self.processes, "body and processes may not both be defined"

        self.body.do(*args)
        return self

    def do_in_parallel(self, *args: ProcessSource) -> "AlgorithmBuilder":
        assert not self.body, "body and processes may not both be defined"

        self.processes.do(*args)
        return self

    def fair(self) -> "AlgorithmBuilder":
        self.fair_ = True
        return self

    def macros(self, *args: MacroSource) -> "AlgorithmBuilder":
        self.macros_.define(*args)
        return self

    def procedures(self, *args: ProcedureSource) -> "AlgorithmBuilder":
        self.procedures_.define(*args)
        return self
