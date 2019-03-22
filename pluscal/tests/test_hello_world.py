from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast import Algorithm, Id, Print


def test_hello_world():
    ast = Algorithm(
        id=Id("HelloWorld"),
        statement=Print("Hello, world."),
    )
    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
            --algorithm HelloWorld
            begin print "Hello, world."
            end algorithm
        """))),
    )
