from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django_glue.access.access import GlueAccess


class GlueAction(str, Enum):
    def __str__(self):
        return self.value

    def required_access(self) -> GlueAccess:
        message = 'You must override required access on Glue Actions'
        raise NotImplementedError(message)
