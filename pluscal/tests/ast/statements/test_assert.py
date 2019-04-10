from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr
from pluscal.ast.statements import Assert


def test_assert() -> None:
    ast = Assert(Expr("foo"))

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("assert foo;")),
    )
