from hamcrest import assert_that, calling, equal_to, is_, raises

from pluscal.ast.base import Base, Expr, Field, Line, Name, Variable


def test_base():
    ast = Base()

    assert_that(calling(ast.validate), raises(NotImplementedError))
    assert_that(calling(str).with_args(ast), raises(NotImplementedError))


def test_expr():
    ast = Expr("foo")

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("foo")),
    )


def test_field():
    ast = Field("foo")

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("foo")),
    )


def test_line():
    line = Line("foo", 2)

    assert_that(
        str(line),
        is_(equal_to("  foo")),
    )


def test_name():
    ast = Name("foo")

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("foo")),
    )


def test_variable():
    ast = Variable("foo")

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("foo")),
    )
