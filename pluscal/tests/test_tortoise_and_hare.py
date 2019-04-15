from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.api import (
    Algorithm,
    Assert,
    Assign,
    Goto,
    If,
    Macro,
    MacroCall,
    Variable,
    While,
)


ALGORITHM = dedent("""\
    --fair algorithm tortoise_and_hare
    variables ll \\in LinkedLists(Nodes), tortoise = First(ll), hare = tortoise;

    macro advance(pointer)
    begin
      pointer := ll[pointer];
      if pointer = NULL then
        assert ~Cyclic(ll);
        goto Done;
      end if;
    end macro;

    begin
      while TRUE do
        advance(tortoise);
        advance(hare);
        advance(hare);
        if tortoise = hare then
          assert Cyclic(ll);
          goto Done;
        end if;
      end while;
    end algorithm""")


def test_tortoise_and_hare() -> None:
    """
    Validate tortoise and hare algorithm.

    Reproduced with permission from pp 135-136 of Pratical TLA+.

    """
    algorithm = Algorithm(
        "tortoise_and_hare",
    ).fair().declare(
        Variable("ll").in_("LinkedLists(Nodes)"),
        Variable("tortoise").eq_("First(ll)"),
        Variable("hare").eq_("tortoise"),
    ).macros(
        Macro("advance")("pointer").do(
            Assign("pointer", "ll[pointer]"),
            If("pointer = NULL").then(
                Assert("~Cyclic(ll)"),
                Goto("Done"),
            ),
        ),
    ).do(
        While("TRUE").do(
            MacroCall("advance")("tortoise"),
            MacroCall("advance")("hare"),
            MacroCall("advance")("hare"),
            If("tortoise = hare").then(
                Assert("Cyclic(ll)"),
                Goto("Done"),
            ),
        ),
    )

    assert_that(
        str(algorithm),
        is_(equal_to(ALGORITHM)),
    )
