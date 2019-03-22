from dataclasses import dataclass, field
from typing import Callable, List

from pluscal.ast import Algorithm, AlgorithmBody, Name, Stmt, VarDecl, VarDecls
from pluscal.builder.variable import VariableBuilder


@dataclass(frozen=True)
class AlgorithmBuilder:
    name: str
    statements: List[Stmt] = field(default_factory=list)
    variables: List[VarDecl] = field(default_factory=list)

    def __call__(self) -> Algorithm:
        return Algorithm(
            name=Name(self.name),
            variables=VarDecls(
                items=self.variables,
            ) if self.variables else None,
            body=AlgorithmBody(
                items=self.statements,
            ),
        )

    def __str__(self) -> str:
        ast = self()
        ast.validate()
        return str(ast)

    def do(self, *args: Callable[[], Stmt]) -> "AlgorithmBuilder":
        self.statements.extend(func() for func in args)
        return self

    def vars(self, *args: VariableBuilder) -> "AlgorithmBuilder":
        self.variables.extend(func() for func in args)
        return self
