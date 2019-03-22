from dataclasses import dataclass
from textwrap import dedent

from pluscal.ast.id import Id
from pluscal.ast.print import Print


@dataclass(frozen=True)
class Algorithm:
    id: Id
    statement: Print

    def __str__(self) -> str:
        return dedent(f"""\
            --algorithm {str(self.id)}
            begin {str(self.statement)}
            end algorithm
        """)
