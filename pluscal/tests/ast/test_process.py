from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast.base import Expr, Label, Name, Variable
from pluscal.ast.process import Process
from pluscal.ast.statements import AlgorithmBody, Skip, Stmt, While
from pluscal.ast.variable import DeclType, VarDecl, VarDecls


def test_process() -> None:
    ast = Process(
        name=Name("foo"),
        type=DeclType.EQUALS,
        value=Expr("\"bar\""),
        body=AlgorithmBody(
            items=[
                Stmt(
                    value=While(
                        condition=Expr("TRUE"),
                        statements=[
                            Stmt(Skip()),
                        ],
                    ),
                    label=Label("Foo"),
                ),
            ],
        ),
        variables=VarDecls(
            items=[
                VarDecl(
                    Variable("baz"),
                    (
                        DeclType.EQUALS,
                        Expr("1"),
                    ),
                ),
            ],
        ),
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
        process foo = "bar"
        variable baz = 1;
        begin
          Foo:
            while TRUE do
              skip;
            end while;
        end process;"""))),
    )
