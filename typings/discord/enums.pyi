from enum import Enum as Enum
from typing import TypeVar

__all__ = ['Enum', 'ChannelType', 'MessageType', 'VoiceRegion', 'SpeakingState', 'VerificationLevel', 'ContentFilter', 'Status', 'AuditLogAction', 'AuditLogActionCategory', 'UserFlags', 'ActivityType', 'NotificationLevel', 'TeamMembershipState', 'WebhookType', 'ExpireBehaviour', 'ExpireBehavior', 'StickerType', 'StickerFormatType', 'InviteTarget', 'VideoQualityMode', 'ComponentType', 'ButtonStyle', 'StagePrivacyLevel', 'InteractionType', 'InteractionResponseType', 'NSFWLevel', 'EmbeddedActivity', 'ScheduledEventStatus', 'ScheduledEventPrivacyLevel', 'ScheduledEventLocationType', 'InputTextStyle', 'SlashCommandOptionType', 'AutoModTriggerType', 'AutoModEventType', 'AutoModActionType', 'AutoModKeywordPresetType', 'ApplicationRoleConnectionMetadataType', 'PromptType', 'OnboardingMode', 'ReactionType', 'SKUType', 'EntitlementType', 'EntitlementOwnerType', 'IntegrationType', 'InteractionContextType']

class EnumMeta(type):
    def __new__(cls, name, bases, attrs, *, comparable: bool = False): ...
    def __iter__(cls): ...
    def __reversed__(cls): ...
    def __len__(cls) -> int: ...
    @property
    def __members__(cls): ...
    def __call__(cls, value): ...
    def __getitem__(cls, key): ...
    def __setattr__(cls, name, value) -> None: ...
    def __delattr__(cls, attr) -> None: ...
    def __instancecheck__(self, instance): ...

class ChannelType(Enum):
    text = 0
    private = 1
    voice = 2
    group = 3
    category = 4
    news = 5
    news_thread = 10
    public_thread = 11
    private_thread = 12
    stage_voice = 13
    directory = 14
    forum = 15

class MessageType(Enum):
    default = 0
    recipient_add = 1
    recipient_remove = 2
    call = 3
    channel_name_change = 4
    channel_icon_change = 5
    pins_add = 6
    new_member = 7
    premium_guild_subscription = 8
    premium_guild_tier_1 = 9
    premium_guild_tier_2 = 10
    premium_guild_tier_3 = 11
    channel_follow_add = 12
    guild_stream = 13
    guild_discovery_disqualified = 14
    guild_discovery_requalified = 15
    guild_discovery_grace_period_initial_warning = 16
    guild_discovery_grace_period_final_warning = 17
    thread_created = 18
    reply = 19
    application_command = 20
    thread_starter_message = 21
    guild_invite_reminder = 22
    context_menu_command = 23
    auto_moderation_action = 24
    role_subscription_purchase = 25
    interaction_premium_upsell = 26
    stage_start = 27
    stage_end = 28
    stage_speaker = 29
    stage_raise_hand = 30
    stage_topic = 31
    guild_application_premium_subscription = 32

class VoiceRegion(Enum):
    us_west = 'us-west'
    us_east = 'us-east'
    us_south = 'us-south'
    us_central = 'us-central'
    eu_west = 'eu-west'
    eu_central = 'eu-central'
    singapore = 'singapore'
    london = 'london'
    sydney = 'sydney'
    amsterdam = 'amsterdam'
    frankfurt = 'frankfurt'
    brazil = 'brazil'
    hongkong = 'hongkong'
    russia = 'russia'
    japan = 'japan'
    southafrica = 'southafrica'
    south_korea = 'south-korea'
    india = 'india'
    europe = 'europe'
    dubai = 'dubai'
    vip_us_east = 'vip-us-east'
    vip_us_west = 'vip-us-west'
    vip_amsterdam = 'vip-amsterdam'

class SpeakingState(Enum):
    none = 0
    voice = 1
    soundshare = 2
    priority = 4
    def __int__(self) -> int: ...

class VerificationLevel(Enum, comparable=True):
    none = 0
    low = 1
    medium = 2
    high = 3
    highest = 4

class SortOrder(Enum):
    latest_activity = 0
    creation_date = 1

class ContentFilter(Enum, comparable=True):
    disabled = 0
    no_role = 1
    all_members = 2

class Status(Enum):
    online = 'online'
    offline = 'offline'
    idle = 'idle'
    dnd = 'dnd'
    do_not_disturb = 'dnd'
    invisible = 'invisible'
    streaming = 'streaming'

class NotificationLevel(Enum, comparable=True):
    all_messages = 0
    only_mentions = 1

class AuditLogActionCategory(Enum):
    create = 1
    delete = 2
    update = 3

class AuditLogAction(Enum):
    guild_update = 1
    channel_create = 10
    channel_update = 11
    channel_delete = 12
    overwrite_create = 13
    overwrite_update = 14
    overwrite_delete = 15
    kick = 20
    member_prune = 21
    ban = 22
    unban = 23
    member_update = 24
    member_role_update = 25
    member_move = 26
    member_disconnect = 27
    bot_add = 28
    role_create = 30
    role_update = 31
    role_delete = 32
    invite_create = 40
    invite_update = 41
    invite_delete = 42
    webhook_create = 50
    webhook_update = 51
    webhook_delete = 52
    emoji_create = 60
    emoji_update = 61
    emoji_delete = 62
    message_delete = 72
    message_bulk_delete = 73
    message_pin = 74
    message_unpin = 75
    integration_create = 80
    integration_update = 81
    integration_delete = 82
    stage_instance_create = 83
    stage_instance_update = 84
    stage_instance_delete = 85
    sticker_create = 90
    sticker_update = 91
    sticker_delete = 92
    scheduled_event_create = 100
    scheduled_event_update = 101
    scheduled_event_delete = 102
    thread_create = 110
    thread_update = 111
    thread_delete = 112
    application_command_permission_update = 121
    auto_moderation_rule_create = 140
    auto_moderation_rule_update = 141
    auto_moderation_rule_delete = 142
    auto_moderation_block_message = 143
    auto_moderation_flag_to_channel = 144
    auto_moderation_user_communication_disabled = 145
    creator_monetization_request_created = 150
    creator_monetization_terms_accepted = 151
    onboarding_question_create = 163
    onboarding_question_update = 164
    onboarding_update = 167
    server_guide_create = 190
    server_guide_update = 191
    voice_channel_status_update = 192
    voice_channel_status_delete = 193
    @property
    def category(self) -> AuditLogActionCategory | None: ...
    @property
    def target_type(self) -> str | None: ...

class UserFlags(Enum):
    staff = 1
    partner = 2
    hypesquad = 4
    bug_hunter = 8
    mfa_sms = 16
    premium_promo_dismissed = 32
    hypesquad_bravery = 64
    hypesquad_brilliance = 128
    hypesquad_balance = 256
    early_supporter = 512
    team_user = 1024
    partner_or_verification_application = 2048
    system = 4096
    has_unread_urgent_messages = 8192
    bug_hunter_level_2 = 16384
    underage_deleted = 32768
    verified_bot = 65536
    verified_bot_developer = 131072
    discord_certified_moderator = 262144
    bot_http_interactions = 524288
    spammer = 1048576
    active_developer = 4194304

class ActivityType(Enum):
    unknown = -1
    playing = 0
    streaming = 1
    listening = 2
    watching = 3
    custom = 4
    competing = 5
    def __int__(self) -> int: ...

class TeamMembershipState(Enum):
    invited = 1
    accepted = 2

class WebhookType(Enum):
    incoming = 1
    channel_follower = 2
    application = 3

class ExpireBehaviour(Enum):
    remove_role = 0
    kick = 1
ExpireBehavior = ExpireBehaviour

class StickerType(Enum):
    standard = 1
    guild = 2

class StickerFormatType(Enum):
    png = 1
    apng = 2
    lottie = 3
    gif = 4
    @property
    def file_extension(self) -> str: ...

class InviteTarget(Enum):
    unknown = 0
    stream = 1
    embedded_application = 2

class InteractionType(Enum):
    ping = 1
    application_command = 2
    component = 3
    auto_complete = 4
    modal_submit = 5

class InteractionResponseType(Enum):
    pong = 1
    channel_message = 4
    deferred_channel_message = 5
    deferred_message_update = 6
    message_update = 7
    auto_complete_result = 8
    modal = 9
    premium_required = 10

class VideoQualityMode(Enum):
    auto = 1
    full = 2
    def __int__(self) -> int: ...

class ComponentType(Enum):
    action_row = 1
    button = 2
    string_select = 3
    select = string_select
    input_text = 4
    user_select = 5
    role_select = 6
    mentionable_select = 7
    channel_select = 8
    def __int__(self) -> int: ...

class ButtonStyle(Enum):
    primary = 1
    secondary = 2
    success = 3
    danger = 4
    link = 5
    premium = 6
    blurple = 1
    grey = 2
    gray = 2
    green = 3
    red = 4
    url = 5
    def __int__(self) -> int: ...

class InputTextStyle(Enum):
    short = 1
    singleline = 1
    paragraph = 2
    multiline = 2
    long = 2

class ApplicationType(Enum):
    game = 1
    music = 2
    ticketed_events = 3
    guild_role_subscriptions = 4

class StagePrivacyLevel(Enum):
    closed = 2
    guild_only = 2

class NSFWLevel(Enum, comparable=True):
    default = 0
    explicit = 1
    safe = 2
    age_restricted = 3

class SlashCommandOptionType(Enum):
    sub_command = 1
    sub_command_group = 2
    string = 3
    integer = 4
    boolean = 5
    user = 6
    channel = 7
    role = 8
    mentionable = 9
    number = 10
    attachment = 11
    @classmethod
    def from_datatype(cls, datatype): ...

class EmbeddedActivity(Enum):
    ask_away = 976052223358406656
    awkword = 879863881349087252
    awkword_dev = 879863923543785532
    bash_out = 1006584476094177371
    betrayal = 773336526917861400
    blazing_8s = 832025144389533716
    blazing_8s_dev = 832013108234289153
    blazing_8s_qa = 832025114077298718
    blazing_8s_staging = 832025061657280566
    bobble_league = 947957217959759964
    checkers_in_the_park = 832013003968348200
    checkers_in_the_park_dev = 832012682520428625
    checkers_in_the_park_qa = 832012894068801636
    checkers_in_the_park_staging = 832012938398400562
    chess_in_the_park = 832012774040141894
    chess_in_the_park_dev = 832012586023256104
    chess_in_the_park_qa = 832012815819604009
    chess_in_the_park_staging = 832012730599735326
    decoders_dev = 891001866073296967
    doodle_crew = 878067389634314250
    doodle_crew_dev = 878067427668275241
    fishington = 814288819477020702
    gartic_phone = 1007373802981822582
    jamspace = 1070087967294631976
    know_what_i_meme = 950505761862189096
    land = 903769130790969345
    letter_league = 879863686565621790
    letter_league_dev = 879863753519292467
    poker_night = 755827207812677713
    poker_night_dev = 763133495793942528
    poker_night_qa = 801133024841957428
    poker_night_staging = 763116274876022855
    putt_party = 945737671223947305
    putt_party_dev = 910224161476083792
    putt_party_qa = 945748195256979606
    putt_party_staging = 945732077960188005
    putts = 832012854282158180
    sketch_heads = 902271654783242291
    sketch_heads_dev = 902271746701414431
    sketchy_artist = 879864070101172255
    sketchy_artist_dev = 879864104980979792
    spell_cast = 852509694341283871
    spell_cast_staging = 893449443918086174
    watch_together = 880218394199220334
    watch_together_dev = 880218832743055411
    word_snacks = 879863976006127627
    word_snacks_dev = 879864010126786570
    youtube_together = 755600276941176913

class ScheduledEventStatus(Enum):
    scheduled = 1
    active = 2
    completed = 3
    canceled = 4
    cancelled = 4
    def __int__(self) -> int: ...

class ScheduledEventPrivacyLevel(Enum):
    guild_only = 2
    def __int__(self) -> int: ...

class ScheduledEventLocationType(Enum):
    stage_instance = 1
    voice = 2
    external = 3

class AutoModTriggerType(Enum):
    keyword = 1
    harmful_link = 2
    spam = 3
    keyword_preset = 4
    mention_spam = 5

class AutoModEventType(Enum):
    message_send = 1

class AutoModActionType(Enum):
    block_message = 1
    send_alert_message = 2
    timeout = 3

class AutoModKeywordPresetType(Enum):
    profanity = 1
    sexual_content = 2
    slurs = 3

class ApplicationRoleConnectionMetadataType(Enum):
    integer_less_than_or_equal = 1
    integer_greater_than_or_equal = 2
    integer_equal = 3
    integer_not_equal = 4
    datetime_less_than_or_equal = 5
    datetime_greater_than_or_equal = 6
    boolean_equal = 7
    boolean_not_equal = 8

class PromptType(Enum):
    multiple_choice = 0
    dropdown = 1

class OnboardingMode(Enum):
    default = 0
    advanced = 1

class ReactionType(Enum):
    normal = 0
    burst = 1

class SKUType(Enum):
    durable = 2
    consumable = 3
    subscription = 5
    subscription_group = 6

class EntitlementType(Enum):
    purchase = 1
    premium_subscription = 2
    developer_gift = 3
    test_mode_purchase = 4
    free_purchase = 5
    user_gift = 6
    premium_purchase = 7
    application_subscription = 8

class EntitlementOwnerType(Enum):
    guild = 1
    user = 2

class IntegrationType(Enum):
    guild_install = 0
    user_install = 1

class InteractionContextType(Enum):
    guild = 0
    bot_dm = 1
    private_channel = 2

class PollLayoutType(Enum):
    default = 1
T = TypeVar('T')
