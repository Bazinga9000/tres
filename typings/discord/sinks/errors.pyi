from discord.errors import DiscordException as DiscordException

class SinkException(DiscordException): ...
class RecordingException(SinkException): ...
class MP3SinkError(SinkException): ...
class MP4SinkError(SinkException): ...
class OGGSinkError(SinkException): ...
class MKVSinkError(SinkException): ...
class WaveSinkError(SinkException): ...
class M4ASinkError(SinkException): ...
class MKASinkError(SinkException): ...
