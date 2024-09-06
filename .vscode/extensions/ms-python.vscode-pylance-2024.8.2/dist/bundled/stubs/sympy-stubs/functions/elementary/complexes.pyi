from typing import Any, Literal
from typing_extensions import Self, Tuple as tTuple

from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import Function, UndefinedFunction
from sympy.core.relational import Equality, Ne, Relational
from sympy.core.symbol import Dummy, Symbol
from sympy.integrals.integrals import Integral
from sympy.series.order import Order

class re(Function):
    args: tTuple[Expr]
    is_extended_real = ...
    unbranched = ...
    _singularities = ...
    @classmethod
    def eval(cls, arg) -> type[UndefinedFunction] | None: ...
    def as_real_imag(self, deep=..., **hints) -> tuple[Self, Any]: ...

class im(Function):
    args: tTuple[Expr]
    is_extended_real = ...
    unbranched = ...
    _singularities = ...
    @classmethod
    def eval(cls, arg) -> None: ...
    def as_real_imag(self, deep=..., **hints) -> tuple[Self, Any]: ...

class sign(Function):
    is_complex = ...
    _singularities = ...
    def doit(self, **hints) -> Self: ...
    @classmethod
    def eval(cls, arg) -> sign | None: ...

class Abs(Function):
    args: tTuple[Expr]
    is_extended_real = ...
    is_extended_negative = ...
    is_extended_nonnegative = ...
    unbranched = ...
    _singularities = ...
    def fdiff(self, argindex=...) -> type[UndefinedFunction]: ...
    @classmethod
    def eval(cls, arg): ...

class arg(Function):
    is_extended_real = ...
    is_real = ...
    is_finite = ...
    _singularities = ...
    @classmethod
    def eval(cls, arg) -> type[UndefinedFunction] | Self | None: ...

class conjugate(Function):
    _singularities = ...
    @classmethod
    def eval(cls, arg) -> None: ...
    def inverse(self) -> type[conjugate]: ...

class transpose(Function):
    @classmethod
    def eval(cls, arg) -> None: ...

class adjoint(Function):
    @classmethod
    def eval(cls, arg) -> type[UndefinedFunction] | None: ...

class polar_lift(Function):
    is_polar = ...
    is_comparable = ...
    @classmethod
    def eval(cls, arg) -> Order | None: ...

class periodic_argument(Function):
    @classmethod
    def eval(cls, ar, period) -> type[UndefinedFunction] | Literal[0] | None: ...

def unbranched_argument(arg) -> type[UndefinedFunction]: ...

class principal_branch(Function):
    is_polar = ...
    is_comparable = ...
    @classmethod
    def eval(cls, x, period) -> type[UndefinedFunction] | None: ...

def polarify(
    eq, subs=..., lift=...
) -> (
    type[UndefinedFunction]
    | Symbol
    | Equality
    | Relational
    | Ne
    | Integral
    | tuple[Any | Symbol | Basic | Equality | Relational | Ne | Integral, dict[Dummy, Any | Symbol | Basic]]
): ...
def unpolarify(eq, subs=..., exponents_only=...) -> bool | Basic: ...
