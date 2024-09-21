import uuid

from dataclasses import dataclass

from django_glue.entities.model_object.fields.entities import GlueModelField
from django_glue.session.data import GlueSessionData


@dataclass
class GlueModelObjectSessionData(GlueSessionData):
    app_label: str
    model_name: str
    object_pk: int | str | uuid.UUID
    fields: [GlueModelField]
    included_fields: list | tuple
    exclude_fields: list | tuple
    methods: list | tuple

    def __post_init__(self):
        if isinstance(self.object_pk, uuid.UUID):
            self.object_pk = str(self.object_pk)

