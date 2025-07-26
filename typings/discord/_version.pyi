import datetime
from ._typed_dict import TypedDict
from _typeshed import Incomplete
from typing import Literal, NamedTuple

__all__ = ['__version__', 'VersionInfo', 'version_info']

__version__: Incomplete

class AdvancedVersionInfo(TypedDict):
    serial: int
    build: int | None
    commit: str | None
    date: datetime.date | None

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal['alpha', 'beta', 'candidate', 'final']
    @property
    def advanced(self) -> AdvancedVersionInfo: ...
    @advanced.setter
    def advanced(self, value: object) -> None: ...
    @property
    def release_level(self) -> Literal['alpha', 'beta', 'candidate', 'final']: ...
    @property
    def serial(self) -> int: ...
    @property
    def build(self) -> int | None: ...
    @property
    def commit(self) -> str | None: ...
    @property
    def date(self) -> datetime.date | None: ...

version_info: VersionInfo
