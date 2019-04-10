from dataclasses import dataclass, field
from typing import List

from pluscal.ast import AlgorithmBody, Stmt
from pluscal.builder.base import Builder
from pluscal.builder.sources import StatementSource, to_statement


@dataclass
class BodyBuilder(Builder[AlgorithmBody]):
    items: List[Stmt] = field(default_factory=list)

    def build(self) -> AlgorithmBody:
        return AlgorithmBody(
            items=self.items,
        )

    def do(self, *args: StatementSource) -> "BodyBuilder":
        self.items.extend(to_statement(arg) for arg in args)
        return self
