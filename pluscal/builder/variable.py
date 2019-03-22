from dataclasses import dataclass
from typing import Sequence, Tuple, Union

from pluscal.ast import DeclType, Expr, VarDecl, Variable


def quote(s: str) -> str:
    return f'"{s}"'


@dataclass(frozen=True)
class VariableBuilder:
    name: str
    value: Union[Tuple[Union[int, str], Union[int, str]], Sequence[str], str]

    def __call__(self) -> VarDecl:
        # literal
        if isinstance(self.value, str):
            return VarDecl(
                name=Variable(self.name),
                value=(
                    DeclType.EQUALS,
                    Expr(self.value),
                ),
            )

        # range
        if isinstance(self.value, tuple):
            left, right = self.value

            return VarDecl(
                name=Variable(self.name),
                value=(
                    DeclType.IN,
                    Expr(f"{left}..{right}"),
                ),
            )

        # set
        if isinstance(self.value, Sequence):
            return VarDecl(
                name=Variable(self.name),
                value=(
                    DeclType.IN,
                    Expr(f"{{{', '.join(quote(item) for item in self.value)}}}"),
                ),
            )

        return VarDecl(
            name=Variable(self.name),
        )
