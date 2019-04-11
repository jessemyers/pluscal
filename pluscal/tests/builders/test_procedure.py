from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast import Skip
from pluscal.builders.procedure import ProcedureBuilder, ProceduresBuilder, PVariableBuilder


def test_procedure() -> None:
    builder = ProcedureBuilder("foo").args(
        "bar",
    ).vars(
        PVariableBuilder("baz", "qox"),
    ).do(
        Skip(),
    )

    assert_that(
        str(builder),
        is_(equal_to(dedent("""\
        procedure foo(bar)
        variable baz = qox;
        begin
          skip;
        end procedure;""")))
    )


def test_procedures() -> None:
    builder = ProceduresBuilder().define(
        ProcedureBuilder("foo").do(
            Skip(),
        ),
    )

    assert_that(
        str(builder),
        is_(equal_to(dedent("""\

        procedure foo()
        begin
          skip;
        end procedure;""")))
    )
