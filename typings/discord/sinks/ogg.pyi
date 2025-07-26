from .core import CREATE_NO_WINDOW as CREATE_NO_WINDOW, Filters as Filters, Sink as Sink, default_filters as default_filters
from .errors import OGGSinkError as OGGSinkError
from _typeshed import Incomplete

class OGGSink(Sink):
    filters: Incomplete
    encoding: str
    vc: Incomplete
    audio_data: Incomplete
    def __init__(self, *, filters=None) -> None: ...
    def format_audio(self, audio) -> None: ...
