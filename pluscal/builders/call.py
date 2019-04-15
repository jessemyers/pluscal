from dataclasses import dataclass, field
from typing import List, Type, Union

from pluscal.ast import Call, Expr, MacroCall, Name, Stmt
from pluscal.builders.base import Builder
from pluscal.builders.source import LabelSource, to_label


@dataclass
class AbstractCallBuilder(Builder[Stmt]):
    name: str
    args: List[Expr] = field(default_factory=list)
    label: LabelSource = None

    @property
    def call_type(self) -> Union[Type[Call], Type[MacroCall]]:
        raise NotImplementedError()

    def __call__(self, *args: str) -> "AbstractCallBuilder":
        return self.with_(*args)

    def with_(self, *args: str) -> "AbstractCallBuilder":
        self.args.extend(Expr(arg) for arg in args)
        return self

    def build(self) -> Stmt:
        return Stmt(
            label=to_label(self.label),
            value=self.call_type(
                name=Name(self.name),
                args=self.args,
            ),
        )


class CallBuilder(AbstractCallBuilder):

    @property
    def call_type(self) -> Type[Call]:
        return Call


class MacroCallBuilder(AbstractCallBuilder, Builder[Stmt]):

    @property
    def call_type(self) -> Type[MacroCall]:
        return MacroCall
