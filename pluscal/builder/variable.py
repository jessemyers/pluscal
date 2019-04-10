from dataclasses import dataclass, field
from typing import List, Optional, Union

from pluscal.ast import DeclType, Expr, VarDecl, VarDecls, Variable
from pluscal.builder.base import Builder
from pluscal.builder.sources import VariableSource, to_variable


def quote(s: str) -> str:
    return f'"{s}"'


@dataclass
class VariableBuilder(Builder[VarDecl]):
    name: str
    type: Optional[DeclType] = None
    value: Optional[Expr] = None

    def build(self) -> VarDecl:
        return VarDecl(
            name=Variable(self.name),
            value=(
                self.type,
                self.value,
            ) if self.type is not None and self.value is not None else None
        )

    def in_(self, value: str) -> "VariableBuilder":
        self.type = DeclType.IN
        self.value = Expr(value)
        return self

    def in_range(self, left: Union[int, str], right: Union[int, str]) -> "VariableBuilder":
        self.type = DeclType.IN
        self.value = Expr(f"{left}..{right}")
        return self

    def in_set(self, *args: str) -> "VariableBuilder":
        self.type = DeclType.IN
        self.value = Expr(f"{{{', '.join(quote(item) for item in args)}}}")
        return self

    def eq_(self, value: str) -> "VariableBuilder":
        self.type = DeclType.EQUALS
        self.value = Expr(value)
        return self


@dataclass
class VariablesBuilder:
    items: List[VarDecl] = field(default_factory=list)

    def build(self) -> Optional[VarDecls]:
        return VarDecls(self.items) if self.items else None

    def declare(self, *args: VariableSource) -> "VariablesBuilder":
        self.items.extend(to_variable(arg) for arg in args)
        return self
