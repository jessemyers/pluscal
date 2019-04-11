from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast import DeclType, Skip
from pluscal.builders.process import ProcessBuilder, ProcessesBuilder
from pluscal.builders.variable import VariableBuilder


def test_process_builder():
    builder = ProcessBuilder("foo", DeclType.EQUALS, "bar").declare(
        VariableBuilder("baz"),
    ).do(
        Skip(),
    )

    assert_that(
        str(builder),
        is_(equal_to(dedent("""\
            process foo = bar
            variable baz;
            begin
              skip;
            end process;"""))),
    )


def test_processes_builder():
    builder = ProcessesBuilder().do(
        ProcessBuilder("foo", DeclType.EQUALS, "foo").do(
            Skip(),
        ),
        ProcessBuilder("bar", DeclType.EQUALS, "bar").do(
            Skip(),
        ),
    )

    assert_that(
        str(builder),
        is_(equal_to(dedent("""\

            process foo = foo
            begin
              skip;
            end process;

            process bar = bar
            begin
              skip;
            end process;"""))),
    )
