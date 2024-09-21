from django_glue.access.access import GlueAccess
from django_glue.access.actions import GlueAction


class GlueModelObjectAction(GlueAction):
    GET = 'get'
    UPDATE = 'update'
    DELETE = 'delete'
    METHOD = 'method'

    def required_access(self) -> GlueAccess:
        if self.value in ['get', 'method']:
            return GlueAccess.VIEW

        if self.value in ['update']:
            return GlueAccess.CHANGE

        if self.value == 'delete':
            return GlueAccess.DELETE

        message = 'That is not a valid action on a glue model object.'
        raise ValueError(message)
