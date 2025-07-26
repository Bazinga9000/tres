from .core import CREATE_NO_WINDOW as CREATE_NO_WINDOW, Filters as Filters, Sink as Sink, default_filters as default_filters
from .errors import M4ASinkError as M4ASinkError
from _typeshed import Incomplete

class M4ASink(Sink):
    filters: Incomplete
    encoding: str
    vc: Incomplete
    audio_data: Incomplete
    def __init__(self, *, filters=None) -> None: ...
    def format_audio(self, audio) -> None: ...
