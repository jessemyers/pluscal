from dataclasses import dataclass, field

from pluscal.ast import Algorithm, Name
from pluscal.builder.base import Builder
from pluscal.builder.body import BodyBuilder
from pluscal.builder.sources import StatementSource, VariableSource
from pluscal.builder.variable import VariablesBuilder


@dataclass
class AlgorithmBuilder(Builder[Algorithm]):
    name: str
    variables: VariablesBuilder = field(default_factory=VariablesBuilder)
    body: BodyBuilder = field(default_factory=BodyBuilder)

    def build(self) -> Algorithm:
        return Algorithm(
            name=Name(self.name),
            variables=self.variables.build(),
            body=self.body.build(),
        )

    def declare(self, *args: VariableSource) -> "AlgorithmBuilder":
        self.variables.declare(*args)
        return self

    def do(self, *args: StatementSource) -> "AlgorithmBuilder":
        self.body.do(*args)
        return self
