from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast import Skip
from pluscal.builders.while_ import WhileBuilder


class TestWhileBuilder:

    def test_while(self) -> None:
        builder = WhileBuilder(
            "TRUE",
        ).do(
            Skip(),
        )

        assert_that(
            str(builder),
            is_(equal_to(dedent("""\
                while TRUE do
                  skip;
                end while;"""))),
        )
