from hamcrest import assert_that, equal_to, is_

from pluscal.builder.variable import VariableBuilder


def test_name():
    builder = VariableBuilder("foo")

    assert_that(
        str(builder),
        is_(equal_to("foo")),
    )


def test_in_range():
    builder = VariableBuilder("foo").in_range(1, 10)
    assert_that(
        str(builder),
        is_(equal_to("foo \\in 1..10")),
    )


def test_in_set():
    builder = VariableBuilder("foo").in_set("a", "b", "c")
    assert_that(
        str(builder),
        is_(equal_to("""foo \\in {"a", "b", "c"}""")),
    )


def test_eq():
    builder = VariableBuilder("foo").eq_("bar")
    assert_that(
        str(builder),
        is_(equal_to("foo = bar")),
    )
