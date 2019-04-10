"""
AST base classes.

"""
from dataclasses import dataclass
from typing import Iterable


class Node:
    """
    An AST node.

    """
    def validate(self) -> None:
        raise NotImplementedError("validate")

    def __str__(self) -> str:
        raise NotImplementedError("validate")


@dataclass(frozen=True)
class Expr(Node):
    """
    Expr ::= A TLA+ expression not containing a PlusCal reserved word or symbol.

    """
    value: str

    def validate(self) -> None:
        assert self.value

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class Field(Node):
    """
    Field ::= A TLA+ record-component label.

    """
    value: str

    def validate(self) -> None:
        assert self.value

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class Label(Node):
    """
    Label := A TLA+ identifier that is not a PlusCal reserved word and is not Done or Error.

    """
    value: str

    def validate(self) -> None:
        assert self.value
        assert self.value not in ("Done", "Error")

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class Name(Node):
    """
    Name := A TLA+ identifier that is not a PlusCal reserved word

    """
    value: str

    def validate(self) -> None:
        assert self.value

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class Variable(Node):
    """
    Name := A TLA+ identifier that is not a PlusCal reserved word and is not pc, stack, or self .

    """
    value: str

    def validate(self) -> None:
        assert self.value not in ("pc", "stack", "self")

    def __str__(self) -> str:
        return self.value


@dataclass
class Line:
    """
    A line of PlusCal output.

    """
    text: str
    indent: int = 0

    def __str__(self) -> str:
        return f"{' ' * self.indent}{self.text}"


class Base(Node):
    """
    A base class for something that is renderable as lines of PlusCal.

    """
    def render(self, indent: int = 0) -> Iterable[Line]:
        raise NotImplementedError("render")

    def __str__(self) -> str:
        return "\n".join(str(line) for line in self.render())
