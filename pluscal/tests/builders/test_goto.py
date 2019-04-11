from hamcrest import assert_that, equal_to, is_

from pluscal.builders.goto import GotoBuilder


class TestGotoBuilder:

    def test_goto(self) -> None:
        builder = GotoBuilder("foo")

        assert_that(
            str(builder),
            is_(equal_to("goto foo;")),
        )
