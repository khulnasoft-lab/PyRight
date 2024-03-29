from collections.abc import Callable
from typing_extensions import Self

from gevent.hub import Hub

class AbstractLinkable:
    @property
    def hub(self) -> Hub | None: ...
    def __init__(self, hub: Hub | None = None) -> None: ...
    def linkcount(self) -> int: ...
    def rawlink(self, __callback: Callable[[Self], object]) -> None: ...
    def ready(self) -> bool: ...
    def unlink(self, __callback: Callable[[Self], object]) -> None: ...
