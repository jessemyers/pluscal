from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr, Name
from pluscal.ast.statements import Call


def test_call() -> None:
    ast = Call(
        Name("foo"),
        [
            Expr("bar"),
            Expr("baz"),
        ],
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("call foo(bar, baz);")),
    )
