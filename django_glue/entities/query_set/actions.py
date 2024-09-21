from django_glue.access.access import GlueAccess
from django_glue.access.actions import GlueAction


class GlueQuerySetAction(GlueAction):
    ALL = 'all'
    FILTER = 'filter'
    GET = 'get'
    UPDATE = 'update'
    DELETE = 'delete'
    METHOD = 'method'
    NULL_OBJECT = 'null_object'
    TO_CHOICES = 'to_choices'

    def required_access(self) -> GlueAccess:
        if self.value in ['get', 'all', 'filter', 'null_object', 'to_choices']:
            return GlueAccess.VIEW

        if self.value in ['update', 'method']:
            return GlueAccess.CHANGE

        if self.value == 'delete':
            return GlueAccess.DELETE

        message = 'That is not a valid action on a glue query set.'
        raise ValueError(message)
