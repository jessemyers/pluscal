from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr, Variable
from pluscal.ast.statements import Print, Stmt, With
from pluscal.ast.variable import DeclType, VarDecl


def test_with() -> None:
    ast = With(
        declarations=[
            VarDecl(
                Variable("foo"),
                (
                    DeclType.EQUALS,
                    Expr("1"),
                ),
            ),
            VarDecl(
                Variable("bar"),
                (
                    DeclType.IN,
                    Expr("1..10"),
                ),
            ),
        ],
        statements=[
            Stmt(Print(Expr("foo + bar"))),
        ],
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
        with foo = 1, bar \\in 1..10
        do
          print foo + bar;
        end with;"""))),
    )
