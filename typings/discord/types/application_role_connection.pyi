from .._typed_dict import NotRequired as NotRequired, TypedDict as TypedDict
from _typeshed import Incomplete

ApplicationRoleConnectionMetadataType: Incomplete

class ApplicationRoleConnectionMetadata(TypedDict):
    type: ApplicationRoleConnectionMetadataType
    key: str
    name: str
    name_localizations: NotRequired[dict[str, str]]
    description: str
    description_localizations: NotRequired[dict[str, str]]
