from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast import Skip
from pluscal.builder.either import EitherBuilder


class TestEitherBuilder:

    def test_either(self) -> None:
        builder = EitherBuilder(Skip(), Skip())

        assert_that(
            str(builder),
            is_(equal_to(dedent("""\
                either
                  skip;
                  skip;
                end either;"""))),
        )

    def test_either_or(self) -> None:
        builder = EitherBuilder(Skip(), Skip()).or_(Skip()).or_(Skip())

        assert_that(
            str(builder),
            is_(equal_to(dedent("""\
                either
                  skip;
                  skip;
                or
                  skip;
                or
                  skip;
                end either;"""))),
        )
