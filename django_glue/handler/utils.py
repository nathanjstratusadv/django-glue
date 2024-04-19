from django_glue.handler.enums import GlueConnection
from django_glue.response.data import GlueJsonResponseData

from django_glue.handler.maps import CONNECTION_TO_HANDLER_MAP


def process_glue_request(glue_session, glue_body_data) -> GlueJsonResponseData:
    unique_name = glue_body_data['unique_name']
    connection = GlueConnection(glue_session[unique_name]['connection'])
    handler_class = CONNECTION_TO_HANDLER_MAP[connection]
    return handler_class(
        unique_name=unique_name,
        glue_session=glue_session,
        glue_body_data=glue_body_data
    ).process_response()
