from .core import Filters as Filters, Sink as Sink, default_filters as default_filters
from _typeshed import Incomplete

class PCMSink(Sink):
    filters: Incomplete
    encoding: str
    vc: Incomplete
    audio_data: Incomplete
    def __init__(self, *, filters=None) -> None: ...
    def format_audio(self, audio) -> None: ...
