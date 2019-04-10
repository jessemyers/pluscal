from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr, Field, Variable
from pluscal.ast.statements.assign import LHS, Assign, Assignment


def test_assign() -> None:
    ast = Assign([
        Assignment(
            left=LHS(
                name=Variable("foo"),
            ),
            right=Expr(
                "bar",
            )
        ),
    ])

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("foo := bar;")),
    )


def test_assign_qualifier() -> None:
    ast = Assign([
        Assignment(
            left=LHS(
                name=Variable("foo"),
                items=[
                    Field("a"),
                    [
                        Expr("b"),
                        Expr("c"),
                        Expr("d"),
                    ],
                    Field("e"),
                ],
            ),
            right=Expr("bar"),
        ),
    ])

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("foo.a[b, c, d].e := bar;")),
    )


def test_assign_two() -> None:
    ast = Assign([
        Assignment(
            left=LHS(
                name=Variable("foo"),
            ),
            right=Expr("bar"),
        ),
        Assignment(
            left=LHS(
                name=Variable("this"),
            ),
            right=Expr("that"),
        ),
    ])

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to("foo := bar || this := that;")),
    )
