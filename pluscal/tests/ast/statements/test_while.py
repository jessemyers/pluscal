from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr
from pluscal.ast.statements import Print, Stmt, While


def test_while() -> None:
    ast = While(
        condition=Expr("foo"),
        statements=[
            Stmt(Print(Expr("bar"))),
        ],
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
            while foo do
              print bar;
            end while;"""))),
    )
