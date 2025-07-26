import io
import os

__all__ = ['File']

class File:
    fp: io.BufferedIOBase
    filename: str | None
    description: str | None
    spoiler: bool
    def __init__(self, fp: str | bytes | os.PathLike | io.BufferedIOBase, filename: str | None = None, *, description: str | None = None, spoiler: bool = False) -> None: ...
    def reset(self, *, seek: int | bool = True) -> None: ...
    def close(self) -> None: ...
