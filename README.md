# pluscal

[PlusCal][1] AST and builder in Python

 [1]: https://lamport.azurewebsites.net/tla/p-manual.pdf


## What Is This?

`PlusCal` is an algorithm language that compiles into a `TLA+` specification. This library defines
*Python types* that form an abstract syntax tree (AST) of the `PlusCal` P-Syntax grammar as well as
a *builder* API for fluently constructing algorithms. The implementation leans heavily on Python
`dataclasses` and type-hinting; a type checker (e.g. `mypy`) can be used to validate the grammar.

It is anticipated that this library will be used both by humans and by programs to construct grammatically
correct specifications and run them through the TLC model checker.


## Usage

Install from pip:

    pip install pluscal

Create an algorithm:

```python
>>> from pluscal.api import Algorithm, Print, Variable

>>> algorithm = Algorithm(
    "hello_world",
).declare(
    Variable("s").in_set("Hello", "World!"),
).do(
    Print("s", label="A"),
)

>>> print(algorithm)
--algorithm hello_world
variable s \in {"Hello", "World!"};
begin
  A:
    print s;
end algorithm
```


## Limitations

This library is not complete. Some known limitations include:

 1. The lower-level `TLA+` grammar used by the `Expr`, `Field`, `Label`, `Name`, and `Variable` types
    are neither modeled nor validated fully. These types are essentially strings at this time.

 2. The validation logic does not express the full nuances of `PlusCal`, especially as it relates to
    label placement.

 3. Some language features, especially as related to fairness, are not yet implemented.
