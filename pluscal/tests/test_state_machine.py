from textwrap import dedent

from hamcrest import assert_that, equal_to, is_

from pluscal.api import (
    EQUALS,
    IN,
    LHS,
    Algorithm,
    Assert,
    Assign,
    Await,
    Either,
    If,
    Macro,
    MacroCall,
    Process,
    Skip,
    Variable,
    While,
    With,
)


ALGORITHM = dedent("""\
    --algorithm database
    variables query = [c \\in Clients |-> NULL], db_value \\in Data;

    define
      Exists(val) == val / NULL
      RequestingClients == {c \\in Clients: Exists(query[c]) /\\ query[c].type = "request"}
    end define;

    macro request(data)
    begin
      query[self] := [type |-> "request"] @@ data;
    end macro;

    macro wait_for_response()
    begin
      await query[self].type = "response";
    end macro;

    process clients \\in Clients
    variable result = NULL;
    begin
      Request:
        while TRUE do
          either
            request([request |-> "read"]);
            Confirm:
              wait_for_response();
            result := query[self].result();
            assert result = db_value;
          or
            with d \\in Data
            do
              request([request |-> "write", data |-> d]);
            end with;
            Wait:
              wait_for_response();
          end either;
        end while;
    end process;

    process database = "Database"
    begin
      DB:
        with client \\in RequestingClients, q = query[client]
        do
          if q.request = "write" then
            db_value := q.data;
          elsif q.request = "read" then
            skip;
          else
            assert FALSE;
          end if;
        end with;
    end process;
    end algorithm""")


def test_state_machine() -> None:
    """
    Validate state machine.

    Reproduced with permission from Chapter 9 of Pratical TLA+.

    """
    algorithm = Algorithm(
        "database",
    ).declare(
        Variable("query").eq_("[c \\in Clients |-> NULL]"),
        Variable("db_value").in_("Data"),
    ).define(
        "Exists(val) == val / NULL",
        "RequestingClients == {c \\in Clients: Exists(query[c]) /\\ query[c].type = \"request\"}"
    ).macros(
        Macro("request")("data").do(
            Assign(LHS("query")["self"], "[type |-> \"request\"] @@ data"),
        ),
        Macro("wait_for_response").do(
            Await("query[self].type = \"response\""),
        ),
    ).do_in_parallel(
        Process("clients", IN, "Clients").declare(
            Variable("result").eq_("NULL"),
        ).do(
            While("TRUE", label="Request").do(
                Either(
                    MacroCall("request")("[request |-> \"read\"]"),
                    MacroCall("wait_for_response", label="Confirm"),
                    Assign("result", "query[self].result()"),
                    Assert("result = db_value"),
                ).or_(
                    With(
                        Variable("d").in_("Data"),
                    ).do(
                        MacroCall("request")("[request |-> \"write\", data |-> d]"),
                    ),
                    MacroCall("wait_for_response", label="Wait"),
                ),
            ),
        ),
        Process("database", EQUALS, "\"Database\"").do(
            With(
                Variable("client").in_("RequestingClients"),
                Variable("q").eq_("query[client]"),
                label="DB",
            ).do(
                If("q.request = \"write\"").then(
                    Assign("db_value", "q.data"),
                ).elsif("q.request = \"read\"").then(
                    Skip(),
                ).else_(
                    Assert("FALSE"),
                ),
            ),
        ),
    )

    assert_that(
        str(algorithm),
        is_(equal_to(ALGORITHM)),
    )
