from pluscal.ast import DeclType, Return, Skip
from pluscal.builders import (
    AlgorithmBuilder as Algorithm,
    AssertBuilder as Assert,
    AssignBuilder as Assign,
    AwaitBuilder as Await,
    CallBuilder as Call,
    EitherBuilder as Either,
    GotoBuilder as Goto,
    IfBuilder as If,
    LHSBuilder as LHS,
    MacroBuilder as Macro,
    MacroCallBuilder as MacroCall,
    PrintBuilder as Print,
    ProcedureBuilder as Procedure,
    ProcessBuilder as Process,
    PVariableBuilder as PVariable,
    VariableBuilder as Variable,
    WhileBuilder as While,
    WithBuilder as With,
)


EQUALS = DeclType.EQUALS
IN = DeclType.IN


__all__ = [
    "EQUALS",
    "IN",
    "LHS",
    "Algorithm",
    "Assert",
    "Assign",
    "Call",
    "Await",
    "Either",
    "Goto",
    "If",
    "Macro",
    "MacroCall",
    "Print",
    "Procedure",
    "Process",
    "PVariable",
    "Return",
    "Skip",
    "Variable",
    "While",
    "With",
]
