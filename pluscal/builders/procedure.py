from dataclasses import dataclass, field
from typing import List, Optional

from pluscal.ast import Expr, Name, Procedure, Procedures, PVarDecl, PVarDecls, Variable
from pluscal.builders.base import Builder
from pluscal.builders.body import BodyBuilder
from pluscal.builders.source import ProcedureSource, PVariableSource, StatementSource, to_procedure, to_pvariable


@dataclass
class PVariableBuilder(Builder[PVarDecl]):
    name: str
    value: Optional[str] = None

    def build(self) -> PVarDecl:
        return PVarDecl(
            name=Variable(self.name),
            value=Expr(self.value) if self.value else None,
        )


@dataclass
class ProcedureBuilder(Builder[Procedure]):
    name: str
    args_: List[Variable] = field(default_factory=list)
    variables_: List[PVarDecl] = field(default_factory=list)
    body: BodyBuilder = field(default_factory=BodyBuilder)

    def build(self) -> Procedure:
        return Procedure(
            name=Name(self.name),
            args=self.args_,
            body=self.body.build(),
            variables=PVarDecls(
                items=self.variables_
            ) if self.variables_ else None,
        )

    def args(self, *args: str) -> "ProcedureBuilder":
        self.args_.extend(Variable(arg) for arg in args)
        return self

    def vars(self, *args: PVariableSource) -> "ProcedureBuilder":
        self.variables_.extend(to_pvariable(arg) for arg in args)
        return self

    def do(self, *args: StatementSource) -> "ProcedureBuilder":
        self.body.do(*args)
        return self


@dataclass
class ProceduresBuilder(Builder[Optional[Procedures]]):
    items: List[Procedure] = field(default_factory=list)

    def __bool__(self) -> bool:
        return bool(self.items)

    def build(self) -> Optional[Procedures]:
        return Procedures(items=self.items) if self else None

    def define(self, *args: ProcedureSource) -> "ProceduresBuilder":
        self.items.extend(to_procedure(arg) for arg in args)
        return self
