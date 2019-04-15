from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast import Skip
from pluscal.builders.macro import MacroBuilder, MacrosBuilder


def test_macro() -> None:
    builder = MacroBuilder("foo").args(
        "bar",
    ).do(
        Skip(),
    )

    assert_that(
        str(builder),
        is_(equal_to(dedent("""\
        macro foo(bar)
        begin
          skip;
        end macro;""")))
    )


def test_macros() -> None:
    builder = MacrosBuilder().define(
        MacroBuilder("foo").do(Skip()),
    )

    assert_that(
        str(builder),
        is_(equal_to(dedent("""\

        macro foo()
        begin
          skip;
        end macro;""")))
    )
