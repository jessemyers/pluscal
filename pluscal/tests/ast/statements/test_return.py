from hamcrest import assert_that, equal_to, is_

from pluscal.ast.statements import Return


def test_return() -> None:
    ast = Return()

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("return;")),
    )
