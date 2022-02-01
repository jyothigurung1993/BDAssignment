from enum import unique as unique_enum, Enum

@unique_enum
class ModelEnum(Enum):
    @classmethod
    def get_values(cls):
        return [(s.name, s.value) for s in cls]

    @classmethod
    def as_map(cls, default_value=None, key_to_lower=False, value_as_none=False):
        key = lambda s: s.name.lower() if key_to_lower else s.name
        value = lambda s: default_value if (default_value is not None or value_as_none) else s.value
        return {key(s): value(s) for s in cls}

    @classmethod
    def as_list(cls, key=None):
        return [s.name if not key else {key: s.name} for s in cls]

    @classmethod
    def values(cls):
        return [s.value for s in cls]

    @classmethod
    def get_member(cls, member_name, is_comparision_case_sensitive=False):
        try:
            if is_comparision_case_sensitive:
                return [s for s in cls if s.value == member_name][0]
            else:
                return [s for s in cls if s.value.lower() == member_name.lower()][0]
        except IndexError as ex:
            raise Exception('\"{0}\" is not a member of the ModelEnum: {1}.'.format(member_name, cls.__name__))    \
                    .with_traceback(ex.__traceback__)

CustomEnum = ModelEnum
