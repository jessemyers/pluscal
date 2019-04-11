from hamcrest import assert_that, equal_to, is_

from pluscal.builders.assign import AssignBuilder, LHSBuilder


class TestLHSBuilder:

    def test_name(self) -> None:
        builder = LHSBuilder("foo")

        assert_that(
            str(builder),
            is_(equal_to("foo")),
        )

    def test_args(self) -> None:
        builder = LHSBuilder("foo")["bar", "baz"]

        assert_that(
            str(builder),
            is_(equal_to("foo[bar, baz]")),
        )

    def test_field(self) -> None:
        builder = LHSBuilder("foo").bar

        assert_that(
            str(builder),
            is_(equal_to("foo.bar")),
        )

    def test_mixed(self) -> None:
        builder = LHSBuilder("foo")["bar"].baz["qux"]

        assert_that(
            str(builder),
            is_(equal_to("foo[bar].baz[qux]")),
        )


class TestAssignBuilder:

    def test_assign(self) -> None:
        builder = AssignBuilder("foo", "bar")

        assert_that(
            str(builder),
            is_(equal_to("foo := bar;")),
        )

    def test_assign_multiple(self) -> None:
        builder = AssignBuilder("foo", "bar").and_("this", "that")

        assert_that(
            str(builder),
            is_(equal_to("foo := bar || this := that;")),
        )
