from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast import Expr, Print, Stmt
from pluscal.builders.body import BodyBuilder
from pluscal.builders.print_ import PrintBuilder


def test_body_builder():
    builder = BodyBuilder().do(
        Print(Expr("a")),
        Stmt(Print(Expr("b"))),
        PrintBuilder("c", label="Foo"),
    )

    assert_that(
        str(builder),
        is_(equal_to(dedent("""\
            begin
              print a;
              print b;
              Foo:
                print c;"""))),
    )
