from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr, Name, Variable
from pluscal.ast.macro import Macro
from pluscal.ast.statements import AlgorithmBody, Assert, Stmt


def test_macro() -> None:
    ast = Macro(
        name=Name("foo"),
        args=[
            Variable("bar"),
            Variable("baz"),
        ],
        body=AlgorithmBody(
            items=[
                Stmt(Assert(Expr("bar \\= baz"))),
            ],
        ),
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
        macro foo(bar, baz)
        begin
          assert bar \\= baz;
        end macro"""))),
    )
