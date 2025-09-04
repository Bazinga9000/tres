from .argument import Argument, ArgumentBase
from util.decorators import decorates

from typing import Callable, Concatenate
from typeutils import F, Factory


class ArgFunc[S, *Ts, T]:
    type Inner[X] = Callable[[*Ts, T], None] | ArgFunc[S, *Ts, T, X]
    def __init__[X](self, inner: Inner[X], arg_factory: F[[S], Argument[T]]):
        self.__name__ = inner.__name__
        self.__doc__ = inner.__doc__
        self.__qualname__ = inner.__qualname__
        self.__module__ = inner.__module__
        self.__annotations__ = inner.__annotations__
        self.inner = inner
        self.arg_factory = arg_factory
        # i would like to make this a dataclass but i don't think you can capture the generic X -cap
    
    def call(self, seed: S, factory: Factory[str], args: Factory[tuple[*Ts]]):
        argument = self.arg_factory(seed)
        get_args = lambda: (*args(), argument.parse(factory()))
        
        inner = self.inner
        if callable(inner):
            return None, lambda: inner(*get_args())
        else:
            def callback(new_factory: Factory[str], /):
                return inner.call(seed, new_factory, get_args)
            return inner.arg_factory(seed), callback
    
    def compile(self, hooks: F[[ArgumentBase], Factory[str]], seed: S, *args: *Ts):
        argument = self.arg_factory(seed)
        ret = self.call(seed, hooks(argument), lambda: args)
        while ret[0] is not None:
            argument, callback = ret
            ret = callback(hooks(argument))
        return ret[1]
    
    type Creator[SS, *TTs, TT, X] = F[[ArgFunc[SS, *TTs, TT].Inner[X]], ArgFunc[SS, *TTs, TT]]
    @decorates
    @staticmethod
    def create[SS, *TTs, TT, X, **P](func: F[Concatenate[SS, P], Argument[TT]], *args: P.args, **kwargs: P.kwargs) -> Creator[SS, *TTs, TT, X]:
        return lambda inner: ArgFunc(inner, lambda seed: func(seed, *args, **kwargs))
