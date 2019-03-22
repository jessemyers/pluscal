from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr
from pluscal.ast.statements import Await


def test_await() -> None:
    ast = Await(Expr("foo"))

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("await foo;")),
    )
