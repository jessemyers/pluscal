from hamcrest import assert_that, equal_to, is_

from pluscal.builders.print_ import PrintBuilder


class TestPrintBuilder:

    def test_print(self) -> None:
        builder = PrintBuilder("foo")

        assert_that(
            str(builder),
            is_(equal_to("print foo;")),
        )
