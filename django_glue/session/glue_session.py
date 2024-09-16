import json
import threading

from django.core.serializers.json import DjangoJSONEncoder
from django_glue.conf import settings
from django_glue.session.data import GlueSessionData
from django_glue.session.session import Session


class GlueSession(Session):
    """
    Used to add models, query sets, and other objects to the session.
    """
    _lock = threading.Lock()

    def __init__(self, request):
        super().__init__(request)
        glue_session_name = settings.DJANGO_GLUE_SESSION_NAME
        self.request.session.setdefault(glue_session_name, {})
        self.session = self.request.session[glue_session_name]
        self.session.setdefault('rc', {})

    def __getitem__(self, key):
        return self.session[key]

    def __setitem__(self, key, value):
        self.session[key] = value

    def add_glue_entity(self, glue_entity: 'GlueEntity'):
        unique_name = glue_entity.unique_name

        with self._lock:
            if unique_name in self.session:
                self.increment_reference(unique_name)
            else:
                self.add_session_data(unique_name, glue_entity.to_session_data())
                self.session['rc'][unique_name] = 1

            self.set_modified()

    def remove_glue_entity(self, unique_name):
        with self._lock:
            self.decrement_reference(unique_name)

    def add_session_data(self, unique_name, session_data: GlueSessionData) -> None:
        self.session[unique_name] = session_data.to_dict()

    def clean(self, removable_unique_names):
        with self._lock:
            for unique_name in removable_unique_names:
                self.decrement_reference(unique_name)

            self.set_modified()

    def purge_unique_name(self, unique_name):
        self.session.pop(unique_name, None)
        self.session['rc'].pop(unique_name, None)

    def increment_reference(self, unique_name):
        reference = self.session['rc']
        reference[unique_name] = reference.get(unique_name, 0) + 1
        self.set_modified()

    def decrement_reference(self, unique_name):
        reference = self.session.get('rc', {})

        if unique_name in reference:
            reference[unique_name] -= 1

            if reference[unique_name] <= 0:
                self.purge_unique_name(unique_name)
                reference.pop(unique_name, None)

            self.set_modified()
        else:
            self.purge_unique_name(unique_name)

    def set_modified(self):
        self.request.session.modified = True

    def to_json(self):
        return json.dumps(self.session, cls=DjangoJSONEncoder)
