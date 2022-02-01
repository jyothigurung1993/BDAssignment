from enum import unique as unique_enum, Enum

@unique_enum
class ModelEnum(Enum):
    @classmethod
    def get_values(cls):
        return [(s.name, s.value) for s in cls]

    @classmethod
    def values(cls):
        return [s.value for s in cls]

