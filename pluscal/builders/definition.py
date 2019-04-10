from dataclasses import dataclass, field
from typing import List, Optional

from pluscal.ast import Def, Definitions
from pluscal.builders.base import Builder


@dataclass
class DefinitionsBuilder(Builder[Optional[Definitions]]):
    items: List[Def] = field(default_factory=list)

    def __bool__(self) -> bool:
        return bool(self.items)

    def build(self) -> Optional[Definitions]:
        return Definitions(items=self.items) if self else None

    def define(self, *args: str) -> "DefinitionsBuilder":
        self.items.extend(Def(arg) for arg in args)
        return self
