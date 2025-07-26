from .._typed_dict import NotRequired as NotRequired
from .emoji import Emoji as Emoji
from _typeshed import Incomplete
from typing import TypedDict

PollLayoutType: Incomplete

class PollMedia(TypedDict):
    text: str
    emoji: NotRequired[Emoji]

class PollAnswer(TypedDict):
    answer_id: int
    poll_media: PollMedia

class PollResults(TypedDict):
    is_finalized: bool
    answer_counts: list[PollAnswerCount]

class PollAnswerCount(TypedDict):
    id: int
    count: int
    me_voted: bool

class Poll(TypedDict):
    question: PollMedia
    answers: list[PollAnswer]
    duration: NotRequired[int]
    expiry: NotRequired[str]
    allow_multiselect: bool
    layout_type: NotRequired[PollLayoutType]
    results: NotRequired[PollResults]
