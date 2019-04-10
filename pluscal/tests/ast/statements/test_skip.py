from hamcrest import assert_that, equal_to, is_

from pluscal.ast.statements import Skip


def test_skip() -> None:
    ast = Skip()

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("skip;")),
    )
