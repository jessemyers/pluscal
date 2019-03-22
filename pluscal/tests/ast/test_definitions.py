from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.ast.definitions import Def, Definitions


def test_definitions() -> None:
    ast = Definitions(
        items=[
            Def("Foo == bar >= 0")
        ],
    )

    ast.validate()

    assert_that(
        str(ast),
        is_(equal_to(dedent("""\
        define
          Foo == bar >= 0
        end define"""))),
    )
