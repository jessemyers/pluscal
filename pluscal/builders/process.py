from dataclasses import dataclass, field
from typing import List

from pluscal.ast import DeclType, Expr, Name, Process, Processes
from pluscal.builders.base import Builder
from pluscal.builders.body import BodyBuilder
from pluscal.builders.source import ProcessSource, StatementSource, VariableSource, to_process
from pluscal.builders.variable import VariablesBuilder


@dataclass
class ProcessBuilder(Builder[Process]):
    name: str
    type: DeclType
    value: str
    variables: VariablesBuilder = field(default_factory=VariablesBuilder)
    body: BodyBuilder = field(default_factory=BodyBuilder)

    def build(self) -> Process:
        return Process(
            name=Name(self.name),
            type=self.type,
            value=Expr(self.value),
            variables=self.variables.build(),
            body=self.body.build(),
        )

    def declare(self, *args: VariableSource) -> "ProcessBuilder":
        self.variables.declare(*args)
        return self

    def do(self, *args: StatementSource) -> "ProcessBuilder":
        self.body.do(*args)
        return self


@dataclass
class ProcessesBuilder(Builder[Processes]):
    items: List[Process] = field(default_factory=list)

    def __bool__(self) -> bool:
        return bool(self.items)

    def build(self) -> Processes:
        return Processes(
            items=self.items,
        )

    def do(self, *args: ProcessSource) -> "ProcessesBuilder":
        self.items.extend(to_process(arg) for arg in args)
        return self
