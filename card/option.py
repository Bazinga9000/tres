from dataclasses import dataclass


@dataclass(frozen=True)
class OptionBase:
    name: str
    id: str

@dataclass(frozen=True)
class Option[T](OptionBase):
    value: T
