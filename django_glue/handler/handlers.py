from abc import ABC, abstractmethod
from typing import Any

from django_glue.access.access import GlueAccess
from django_glue.access.actions import GlueAction
from django_glue.handler.body_data import GlueBodyData
from django_glue.response.data import GlueJsonResponseData
from django_glue.session.data import GlueSessionData
from django_glue.session.glue_session import GlueSession


class GlueRequestHandler(ABC):
    action: GlueAction = None
    _session_data_class: GlueSessionData = None
    _post_data_class: Any | None = None

    def __init__(self, glue_session: GlueSession, glue_body_data: GlueBodyData):
        if self._session_data_class is None:
            message = f'Please initialize class variable _session_data_class on {self.__class__.__name__}'
            raise ValueError(message)

        if self.action is None:
            message = f'Please initialize class variable action on {self.__class__.__name__}'
            raise ValueError(message)

        # Unique name maps what the user is requesting
        self.unique_name = glue_body_data.unique_name

        if self._post_data_class is None:
            self.post_data = glue_body_data.data
        else:
            # The data we are expecting in post
            self.post_data = self._post_data_class(**glue_body_data.data['data'])

        # data we stored in glue session.
        self.session_data = self._session_data_class(**glue_session[self.unique_name])

    def has_access(self) -> bool:
        glue_access = GlueAccess(self.session_data.access)
        return glue_access.has_access(self.action.required_access())

    @abstractmethod
    def process_response_data(self) -> GlueJsonResponseData:
        # Todo: Do we want to handle an error message here or let the system crash?
        pass
