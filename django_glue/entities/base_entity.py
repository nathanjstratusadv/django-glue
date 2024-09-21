from abc import ABC, abstractmethod

from django_glue.access.access import GlueAccess
from django_glue.handler.enums import GlueConnection
from django_glue.session.data import GlueSessionData


class GlueEntity(ABC):
    def __init__(
        self,
        unique_name: str,
        connection: GlueConnection,
        access: GlueAccess | str = GlueAccess.VIEW
    ):

        self.unique_name = unique_name
        self.connection = connection

        if isinstance(access, str):
            self.access = GlueAccess(access)
        else:
            self.access = access

    @abstractmethod
    def to_session_data(self) -> GlueSessionData:
        pass
