from types import EllipsisType
from typing import Any, Callable, Coroutine, Generator


type F[**P, T] = Callable[P, T]
'''Function. If you need to unpack TypeVarTuples in the argument list, use Callable instead'''

type G[YieldT, SendT=None, ReturnT=None] = Generator[YieldT, SendT, ReturnT]
'''Generator.'''

type C[ReturnT, YieldT=None, SendT=None] = Coroutine[YieldT, SendT, ReturnT]
'''Coroutine.'''

type AF[**P, T] = F[P, C[T]]
'''Async function.'''

type E = EllipsisType
'''Ellipsis.'''

type AnyF = F[..., Any]
'''Arbitrary function which takes any arguments and returns any value.'''

type NullF = F[[], None]
'''Function which takes no arguments and returns nothing.'''

type Factory[T] = F[[], T]
'''Function which takes no arguments and returns a value of type T.'''

type Action[**P] = F[P, None]
'''Function which returns nothing.'''