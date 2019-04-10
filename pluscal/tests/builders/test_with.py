from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast import Skip
from pluscal.builder.variable import VariableBuilder
from pluscal.builder.with_ import WithBuilder


class TestWithBuilder:

    def test_with(self) -> None:
        builder = WithBuilder(
            "foo",
        ).do(
            Skip(),
            Skip(),
        )

        assert_that(
            str(builder),
            is_(equal_to(dedent("""\
                with foo
                do
                  skip;
                  skip;
                end with;"""))),
        )

    def test_with_variables(self) -> None:
        builder = WithBuilder(
            VariableBuilder("foo"),
            VariableBuilder("bar").in_("baz"),
        ).do(
            Skip(),
            Skip(),
        )

        assert_that(
            str(builder),
            is_(equal_to(dedent("""\
                with foo, bar \\in baz
                do
                  skip;
                  skip;
                end with;"""))),
        )
