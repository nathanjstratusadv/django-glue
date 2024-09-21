from django_glue.access.access import GlueAccess
from django_glue.access.actions import GlueAction


class GlueTemplateAction(GlueAction):
    GET = 'get'

    def required_access(self) -> GlueAccess:
        if self.value == 'get':
            return GlueAccess.VIEW

        message = 'That is not a valid action on a glue query set.'
        raise ValueError(message)
