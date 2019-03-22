from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Label
from pluscal.ast.statements import Goto


def test_goto() -> None:
    ast = Goto(Label("foo"))

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("goto foo;")),
    )
