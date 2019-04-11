from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.api import Algorithm, Print, Variable


ALGORITHM = dedent("""\
    --algorithm hello_world
    variable s \\in {"Hello", "World!"};

    begin
      A:
        print s;
    end algorithm""")


def test_hello_world() -> None:
    """
    Validate hello world algorithm.

    See: https://learntla.com/pluscal/a-simple-spec/

    """
    algorithm = Algorithm(
        "hello_world",
    ).declare(
        Variable("s").in_set("Hello", "World!"),
    ).do(
        Print("s", label="A"),
    )

    assert_that(
        str(algorithm),
        is_(equal_to(ALGORITHM)),
    )
