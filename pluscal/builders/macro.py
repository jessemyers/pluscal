from dataclasses import dataclass, field
from typing import List, Optional

from pluscal.ast import Macro, Macros, Name, Variable
from pluscal.builders.base import Builder
from pluscal.builders.body import BodyBuilder
from pluscal.builders.source import MacroSource, StatementSource, to_macro


@dataclass
class MacroBuilder(Builder[Macro]):
    name: str
    args_: List[Variable] = field(default_factory=list)
    body: BodyBuilder = field(default_factory=BodyBuilder)

    def build(self) -> Macro:
        return Macro(
            name=Name(self.name),
            args=self.args_,
            body=self.body.build(),
        )

    def args(self, *args: str) -> "MacroBuilder":
        self.args_.extend(Variable(arg) for arg in args)
        return self

    def do(self, *args: StatementSource) -> "MacroBuilder":
        self.body.do(*args)
        return self


@dataclass
class MacrosBuilder(Builder[Optional[Macros]]):
    items: List[Macro] = field(default_factory=list)

    def __bool__(self) -> bool:
        return bool(self.items)

    def build(self) -> Optional[Macros]:
        return Macros(items=self.items) if self else None

    def define(self, *args: MacroSource) -> "MacrosBuilder":
        self.items.extend(to_macro(arg) for arg in args)
        return self
