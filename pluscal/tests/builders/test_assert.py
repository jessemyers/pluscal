from hamcrest import assert_that, equal_to, is_

from pluscal.builder.assert_ import AssertBuilder


class TestAssertBuilder:

    def test_assert(self) -> None:
        builder = AssertBuilder("foo")

        assert_that(
            str(builder),
            is_(equal_to("assert foo;")),
        )
