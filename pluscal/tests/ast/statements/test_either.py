from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr
from pluscal.ast.statements import Either, Print, Stmt


def test_either() -> None:
    ast = Either(
        Stmt(Print(Expr("foo"))),
        or_=[
            [
                Stmt(Print(Expr("bar"))),
            ],
            [
                Stmt(Print(Expr("baz"))),
            ],
        ],
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
            either
              print foo;
            or
              print bar;
            or
              print baz;
            end either;"""))),
    )
