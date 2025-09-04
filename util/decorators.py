from functools import wraps
from inspect import iscoroutinefunction, markcoroutinefunction

from typing import Concatenate
from typeutils import F, AnyF


def copycoroutine[T: AnyF](source: AnyF) -> F[[T], T]:
    '''Copies the coroutine status of the input function to the decorated function.'''
    
    @wraps(source)
    def decorator(dest: T) -> T:
        return markcoroutinefunction(dest) if iscoroutinefunction(source) else dest
    return decorator


def decorates[T, R, **P, **Q](func: F[Concatenate[F[P, T], Q], R]) -> F[[F[P, T]], F[Q, R]]:
    '''Converts a function into a decorator.'''
    
    @wraps(func)
    def decorator(view: F[P, T]) -> F[Q, R]:
        @wraps(view)
        @copycoroutine(func)
        def wrapper(*args: Q.args, **kwargs: Q.kwargs) -> R:
            return func(view, *args, **kwargs)
        return wrapper
    return decorator
