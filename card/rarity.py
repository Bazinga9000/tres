import enum

class Rarity(enum.Enum):
    BASIC = 0 # BASIC cards will appear in every randomly-generated deck (e.g numbers)
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5
