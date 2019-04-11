from dataclasses import dataclass, field
from typing import List

from pluscal.ast import AlgorithmBody, Stmt
from pluscal.builders.base import Builder
from pluscal.builders.source import StatementSource, to_statement


@dataclass
class BodyBuilder(Builder[AlgorithmBody]):
    items: List[Stmt] = field(default_factory=list)

    def __bool__(self) -> bool:
        return bool(self.items)

    def build(self) -> AlgorithmBody:
        return AlgorithmBody(
            items=self.items,
        )

    def do(self, *args: StatementSource) -> "BodyBuilder":
        self.items.extend(to_statement(arg) for arg in args)
        return self
