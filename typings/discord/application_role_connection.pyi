from .enums import ApplicationRoleConnectionMetadataType
from .types.application_role_connection import ApplicationRoleConnectionMetadata as ApplicationRoleConnectionMetadataPayload

__all__ = ['ApplicationRoleConnectionMetadata']

class ApplicationRoleConnectionMetadata:
    type: ApplicationRoleConnectionMetadataType
    key: str
    name: str
    name_localizations: dict[str, str]
    description: str
    description_localizations: dict[str, str]
    def __init__(self, *, type: ApplicationRoleConnectionMetadataType, key: str, name: str, description: str, name_localizations: dict[str, str] = ..., description_localizations: dict[str, str] = ...) -> None: ...
    @classmethod
    def from_dict(cls, data: ApplicationRoleConnectionMetadataPayload) -> ApplicationRoleConnectionMetadata: ...
    def to_dict(self) -> ApplicationRoleConnectionMetadataPayload: ...
