from hamcrest import assert_that, equal_to, is_

from pluscal.builders.call import CallBuilder, MacroCallBuilder


class TestCallBuilder:

    def test_call(self) -> None:
        builder = CallBuilder("foo")

        assert_that(
            str(builder),
            is_(equal_to("call foo();")),
        )

    def test_call_args(self) -> None:
        builder = CallBuilder("foo")("bar", "baz")

        assert_that(
            str(builder),
            is_(equal_to("call foo(bar, baz);")),
        )

    def test_call_args_with(self) -> None:
        builder = CallBuilder("foo").with_("bar", "baz")

        assert_that(
            str(builder),
            is_(equal_to("call foo(bar, baz);")),
        )


class TestMacroCallBuilder:

    def test_call(self) -> None:
        builder = MacroCallBuilder("foo")

        assert_that(
            str(builder),
            is_(equal_to("foo();")),
        )

    def test_call_args(self) -> None:
        builder = MacroCallBuilder("foo")("bar", "baz")

        assert_that(
            str(builder),
            is_(equal_to("foo(bar, baz);")),
        )

    def test_call_args_with(self) -> None:
        builder = MacroCallBuilder("foo").with_("bar", "baz")

        assert_that(
            str(builder),
            is_(equal_to("foo(bar, baz);")),
        )
