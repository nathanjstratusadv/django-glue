from dataclasses import dataclass

from django_glue.session.data import GlueSessionData


@dataclass
class GlueQuerySetSessionData(GlueSessionData):
    query_set_str: str
    fields: dict
    included_fields: list | tuple
    excluded_fields: list | tuple
    included_methods: list | tuple
