from hamcrest import assert_that, equal_to, is_

from pluscal.builders.await_ import AwaitBuilder


class TestAwaitBuilder:

    def test_await(self) -> None:
        builder = AwaitBuilder("foo")

        assert_that(
            str(builder),
            is_(equal_to("await foo;")),
        )
