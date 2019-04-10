from typing import Optional, Union

from pluscal.ast import (
    LHS,
    Label,
    Macro,
    Procedure,
    Process,
    PVarDecl,
    Stmt,
    UnlabeledStmt,
    VarDecl,
    Variable,
)
from pluscal.builders.base import Builder


LabelSource = Optional[Union[Label, str]]
LHSSource = Union[Builder[LHS], LHS, str]
MacroSource = Union[Builder[Macro], Macro]
ProcedureSource = Union[Builder[Procedure], Procedure]
ProcessSource = Union[Builder[Process], Process]
PVariableSource = Union[Builder[PVarDecl], PVarDecl]
StatementSource = Union[Builder[Stmt], Stmt, UnlabeledStmt]
VariableSource = Union[Builder[VarDecl], VarDecl, Variable, str]


def to_label(value: LabelSource) -> Optional[Label]:
    if value is None:
        return None
    elif isinstance(value, Label):
        return value
    else:
        return Label(value)


def to_lhs(value: LHSSource) -> LHS:
    if isinstance(value, LHS):
        return value
    elif isinstance(value, Builder):
        return value.build()
    else:
        return LHS(Variable(value))


def to_macro(value: MacroSource) -> Macro:
    if isinstance(value, Builder):
        return value.build()
    else:
        return value


def to_procedure(value: ProcedureSource) -> Procedure:
    if isinstance(value, Builder):
        return value.build()
    else:
        return value


def to_process(value: ProcessSource) -> Process:
    if isinstance(value, Builder):
        return value.build()
    else:
        return value


def to_pvariable(value: PVariableSource) -> PVarDecl:
    if isinstance(value, Builder):
        return value.build()
    else:
        return value


def to_statement(value: StatementSource) -> Stmt:
    if isinstance(value, UnlabeledStmt):
        return Stmt(value)
    elif isinstance(value, Builder):
        return value.build()
    else:
        return value


def to_variable(value: VariableSource) -> VarDecl:
    if isinstance(value, VarDecl):
        return value
    elif isinstance(value, Builder):
        return value.build()
    elif isinstance(value, Variable):
        return VarDecl(name=value)
    else:
        return VarDecl(name=Variable(value))
