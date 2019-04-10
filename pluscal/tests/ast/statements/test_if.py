from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr
from pluscal.ast.statements import If, Print, Stmt


def test_if() -> None:
    ast = If(
        condition=Expr("foo"),
        then=[
            Stmt(Print(Expr("bar"))),
        ],
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
            if foo then
              print bar;
            end if;"""))),
    )


def test_if_else() -> None:
    ast = If(
        condition=Expr("foo"),
        then=[
            Stmt(Print(Expr("bar"))),
        ],
        else_=[
            Stmt(Print(Expr("baz"))),
        ],
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
            if foo then
              print bar;
            else
              print baz;
            end if;"""))),
    )


def test_if_elsif() -> None:
    ast = If(
        condition=Expr("foo"),
        then=[
            Stmt(Print(Expr("bar"))),
        ],
        elsif=[
            (
                Expr("baz"),
                [
                    Stmt(Print(Expr("baz"))),
                ],
            ),
        ],
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
            if foo then
              print bar;
            elsif baz then
              print baz;
            end if;"""))),
    )
