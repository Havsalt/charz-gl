from enum import Enum, unique

import charz_core


# TODO: Use `StrEnum` for Python 3.11+
@unique
class Group(str, Enum):
    NODE = charz_core.CoreGroup.NODE
    TEXTURE = "texture"
    # Remove this in favour of sprite collision?
    COLLIDER = "collider"
