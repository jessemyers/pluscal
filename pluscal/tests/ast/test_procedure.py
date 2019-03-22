from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr, Label, Name, Variable
from pluscal.ast.procedure import Procedure, PVarDecl, PVarDecls
from pluscal.ast.statements import AlgorithmBody, Assert, Return, Stmt


def test_procedure() -> None:
    ast = Procedure(
        name=Name("foo"),
        args=[
            Variable("bar"),
        ],
        variables=PVarDecls(
            items=[
                PVarDecl(
                    name=Variable("baz"),
                    value=Expr("1"),
                ),
                PVarDecl(
                    name=Variable("qux"),
                ),
            ],
        ),
        body=AlgorithmBody(
            items=[
                Stmt(Assert(Expr("bar \\= baz")), label=Label("Foo")),
                Stmt(Return()),
            ],
        ),
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
        procedure foo(bar)
        variables baz = 1, qux;
        begin
          Foo:
            assert bar \\= baz;
          return;
        end procedure"""))),
    )
