"""
Charz GL
==========

Graphics library built upon `charz`

Includes
--------

- Annotations
  - `Self`  (from standard `typing` or from package `typing-extensions`)
- Math (from package `linflex`)
  - `lerp`
  - `sign`
  - `clamp`
  - `Vec2`
  - `Vec2i`
  - `Vec3`
- Framework
  - `Engine`
  - `Clock`
  - `DeltaClock`
  - `Scene`
- Decorators
  - `group`
- Enums
  - `CoreGroup`
- Components
  - `Transform`
- Nodes
  - `Camera`
  - `Node`
  - `Node2D`
"""

__all__ = [
    "Engine",
    "Clock",
    "DeltaClock",
    "Camera",
    "Scene",
    "group",
    "Group",
    "Self",
    "Node",
    "Node2D",
    "Sprite",
    "Transform",
    "Texture",
    "lerp",
    "sign",
    "clamp",
    "Vec2",
    "Vec2i",
    "Vec3",
]

# Init `pygame` without the support prompt
import os as _os

_os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame as _pygame

# NOTE: Initializing `pygame` is done before local imports that uses `pygame`
_pygame.init()

# Re-exports
from charz_core import (
    Engine,
    Clock,
    DeltaClock,
    Camera,
    Scene,
    group,
    Self,
    Node,
    Node2D,
    Transform,
    lerp,
    sign,
    clamp,
    Vec2,
    Vec2i,
    Vec3,
)

# Exports
from ._grouping import Group
from ._components._texture import Texture
from ._prefabs._sprite import Sprite
