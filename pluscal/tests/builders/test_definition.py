from textwrap import dedent

from hamcrest import assert_that, equal_to, is_, none

from pluscal.builders.definition import DefinitionsBuilder


def test_definitions() -> None:
    builder = DefinitionsBuilder().define("foo")

    assert_that(
        str(builder),
        is_(equal_to(dedent("""\
        define
          foo
        end define""")))
    )


def test_no_definitions() -> None:
    builder = DefinitionsBuilder()

    assert_that(
        builder.ast,
        is_(none()),
    )
