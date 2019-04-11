from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.api import Algorithm, Assert, Assign, If, Variable, While


ALGORITHM = dedent("""\
    --algorithm EuclidSedgewick
    variables m \\in 1..K, n \\in 1..K, u = m, v = n;

    begin
      while u \\= 0 do
        if u < v then
          u := v || v := u;
        end if;
        u := u - v;
      end while;
      assert IsGCD(v, m, n);
    end algorithm""")


def test_euclid() -> None:
    """
    Validate Euclid's algorithm.

    Adapted from section 2.1 of "The PlusCal Algorithm Language"

    """
    algorithm = Algorithm(
        "EuclidSedgewick",
    ).declare(
        Variable("m").in_range(1, "K"),
        Variable("n").in_range(1, "K"),
        Variable("u").eq_("m"),
        Variable("v").eq_("n"),
    ).do(
        While("u \\= 0").do(
            If("u < v").then(
                Assign("u", "v").and_("v", "u"),
            ),
            Assign("u", "u - v"),
        ),
        Assert("IsGCD(v, m, n)"),
    )

    assert_that(
        str(algorithm),
        is_(equal_to(ALGORITHM)),
    )
