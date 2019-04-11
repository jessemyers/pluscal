from dataclasses import dataclass
from typing import Iterable, Optional, Sequence

from pluscal.ast.base import Base, Label, Line


class UnlabeledStmt(Base):
    """
    UnlabeledStmt := <Assign> | <If> | <While> | <Either> | <With> |
                     <Await> | <Print> | <Assert> | <Skip> | <Return> |
                     <Goto> | <Call> | <MacroCall>

    Servces as a base class for unlabeled statements.

    """
    pass


@dataclass(frozen=True)
class Stmt(Base):
    """
    Stmt ::= [<Label> : [+|-]?]? <UnlabeledStmt>

    """
    # XXX label should be extended to allow fairness +/-
    value: UnlabeledStmt
    label: Optional[Label] = None

    def render(self, indent: int = 0) -> Iterable[Line]:
        if self.label is not None:
            yield Line(f"{str(self.label)}:", indent)
            extra_indent = 2
        else:
            extra_indent = 0

        yield from self.value.render(indent=indent + extra_indent)

    def validate(self) -> None:
        if self.label is not None:
            self.label.validate()
        self.value.validate()


@dataclass(frozen=True)
class AlgorithmBody(Base):
    """
    AlgorthmBody ::= begin <Stmt>+

    """
    items: Sequence[Stmt]

    def render(self, indent: int = 0) -> Iterable[Line]:
        yield Line("begin", indent)
        for item in self.items:
            yield from item.render(indent + 2)

    def validate(self) -> None:
        assert self.items
        for item in self.items:
            item.validate()
