from dataclasses import dataclass

from .option import Option, OptionBase


@dataclass(frozen=True)
class ArgumentBase:
    placeholder: str
    options: tuple[OptionBase, ...]


@dataclass(frozen=True)
class Argument[T](ArgumentBase):
    options: tuple[Option[T], ...]
    default: T | None = None
    
    def parse(self, id: str) -> T:
        for option in self.options:
            if option.id == id:
                return option.value
        if self.default is None:
            raise ValueError(f'Invalid argument: "{id}"')
        return self.default
    
    type Self[S] = Argument[S]
    @staticmethod
    def get_seed[S](seed: S) -> Self[S]:
        return Argument(placeholder='', options=(), default=seed)
