from typing import Any

import pygame
from charz_core import Self, group

from .._grouping import Group


@group(Group.TEXTURE)
class Texture:  # Component (mixin class)
    texture: pygame.Surface | None = None

    def with_texture(self, texture: pygame.Surface | None, /) -> Self:
        self.texture = texture
        return self
