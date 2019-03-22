from textwrap import dedent

from hamcrest import assert_that, equal_to, has_length, is_

from pluscal.ast.base import Expr, Label
from pluscal.ast.statements import Print, Stmt, UnlabeledStmt


def test_unlabeled_stmt() -> None:
    # Assert, Assign, Await, Call, Either, Go, If, Print, Return, Skip, While, With
    assert_that(
        UnlabeledStmt.__subclasses__(),
        has_length(12),
    )


def test_stmt_without_label() -> None:
    ast = Stmt(
        value=Print(
            value=Expr("1"),
        ),
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
            print 1;"""))),
    )


def test_stmt_with_label() -> None:
    ast = Stmt(
        label=Label("foo"),
        value=Print(
            value=Expr("1"),
        ),
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
            foo:
              print 1;"""))),
    )
