from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast import Skip
from pluscal.builder.if_ import IfBuilder


class TestIfBuilder:

    def test_if(self) -> None:
        builder = IfBuilder(
            "foo",
        ).then(
            Skip(),
        )

        assert_that(
            str(builder),
            is_(equal_to(dedent("""\
                if foo then
                  skip;
                end if;"""))),
        )

    def test_if_else(self) -> None:
        builder = IfBuilder(
            "foo",
        ).then(
            Skip(),
        ).else_(
            Skip(),
        )

        assert_that(
            str(builder),
            is_(equal_to(dedent("""\
                if foo then
                  skip;
                else
                  skip;
                end if;"""))),
        )

    def test_if_elsif(self) -> None:
        builder = IfBuilder(
            "foo",
        ).then(
            Skip(),
        ).elsif(
            "bar",
            Skip(),
        ).elsif(
            "baz",
            Skip(),
        )

        assert_that(
            str(builder),
            is_(equal_to(dedent("""\
                if foo then
                  skip;
                elsif bar then
                  skip;
                elsif baz then
                  skip;
                end if;"""))),
        )
