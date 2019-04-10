from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr
from pluscal.ast.statements import Print


def test_print() -> None:
    ast = Print(Expr('"foo"'))

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("print \"foo\";")),
    )
