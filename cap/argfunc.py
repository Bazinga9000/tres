from typing import Callable


type F[**P, T] = Callable[P, T]
type Factory[T] = F[[], T]

class ArgFunc[S, *Ts, T]:
    type Inner[X] = Callable[[*Ts, T], None] | ArgFunc[S, *Ts, T, X]
    def __init__[X](self, inner: Inner[X], options: F[[S], list[str]], converter: F[[S], F[[str], T]]):
        self.inner = inner
        self.options = options
        self.converter = converter
    
    def call(self, arg: S, factory: Factory[str], args: Factory[tuple[*Ts]]):
        converter = self.converter(arg)
        new_arg = converter(factory())
        get_args = lambda: (*args(), new_arg)
        
        inner = self.inner
        if callable(inner):
            return None, lambda: inner(*get_args())
        else:
            def callback(new_factory: Factory[str], /):
                return inner.call(arg, new_factory, get_args)
            return inner.options(arg), callback
    
    def compile(self, hooks: F[[list[str]], Factory[str]], arg: S, *args: *Ts):
        options = self.options(arg)
        ret = self.call(arg, hooks(options), lambda: args)
        while ret[0] is not None:
            options, callback = ret
            ret = callback(hooks(options))
        return ret[1]
    
    @staticmethod
    def create[SS, TT](func: F[[SS], tuple[list[str], F[[str], TT]]]):
        # TODO: combining opts and conv would make this much better
        # also the nested generics are pain
        def wrapper[*TTs, X](inner: ArgFunc[SS, *TTs, TT].Inner[X]) -> ArgFunc[SS, *TTs, TT]:
            def options(arg: SS) -> list[str]:
                opts, _ = func(arg)
                return opts
            def converter(arg: SS) -> F[[str], TT]:
                _, conv = func(arg)
                return conv
            return ArgFunc(inner, options, converter)
        return wrapper
