from typing_extensions import Self

from sympy.utilities import public

@public
class BasePolynomialError(Exception):
    def new(self, *args): ...

@public
class ExactQuotientFailed(BasePolynomialError):
    def __init__(self, f, g, dom=...) -> None: ...
    def __str__(self) -> str: ...
    def new(self, f, g) -> Self: ...

@public
class PolynomialDivisionFailed(BasePolynomialError):
    def __init__(self, f, g, domain) -> None: ...
    def __str__(self) -> str: ...

@public
class OperationNotSupported(BasePolynomialError):
    def __init__(self, poly, func) -> None: ...
    def __str__(self) -> str: ...

@public
class HeuristicGCDFailed(BasePolynomialError): ...

class ModularGCDFailed(BasePolynomialError): ...

@public
class HomomorphismFailed(BasePolynomialError): ...

@public
class IsomorphismFailed(BasePolynomialError): ...

@public
class ExtraneousFactors(BasePolynomialError): ...

@public
class EvaluationFailed(BasePolynomialError): ...

@public
class RefinementFailed(BasePolynomialError): ...

class CoercionFailed(BasePolynomialError): ...

@public
class NotInvertible(BasePolynomialError): ...

@public
class NotReversible(BasePolynomialError): ...

@public
class NotAlgebraic(BasePolynomialError): ...

@public
class DomainError(BasePolynomialError): ...

@public
class PolynomialError(BasePolynomialError): ...

@public
class UnificationFailed(BasePolynomialError): ...

@public
class UnsolvableFactorError(BasePolynomialError): ...

@public
class GeneratorsError(BasePolynomialError): ...

@public
class GeneratorsNeeded(GeneratorsError): ...

@public
class ComputationFailed(BasePolynomialError):
    def __init__(self, func, nargs, exc) -> None: ...
    def __str__(self) -> str: ...

@public
class UnivariatePolynomialError(PolynomialError): ...

@public
class MultivariatePolynomialError(PolynomialError): ...

@public
class PolificationFailed(PolynomialError):
    def __init__(self, opt, origs, exprs, seq=...) -> None: ...
    def __str__(self) -> str: ...

@public
class OptionError(BasePolynomialError): ...

@public
class FlagError(OptionError): ...
