from dataclasses import dataclass
from typing import Generic, TypeVar

from pluscal.ast.base import Node


T = TypeVar("T", bound=Node)


@dataclass
class Builder(Generic[T]):

    def build(self) -> T:
        """
        A builder is responsible for generating an instance of T.

        """
        raise NotImplementedError()

    @property
    def ast(self) -> T:
        ast = self.build()

        if ast:
            ast.validate()

        return ast

    def __str__(self) -> str:
        return str(self.ast)
