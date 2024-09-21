from django.db.models import Model

from django_glue.entities.model_object.fields.entities import GlueModelField


def field_name_included(name: str, fields: list[str], exclude: list[str]) -> bool:
    included = False

    condition = (
        (name not in exclude or exclude[0] == '__none__') and
        (name in fields or fields[0] == '__all__')
    )

    if condition:
        included = True

    return included


def get_field_value_from_model_object(
    model_object: Model,
    field: GlueModelField
) -> str | int | None:
    relational = ['ForeignKey', 'BinaryField', 'OnetoOneField']

    if field._meta.type in relational:
        return getattr(model_object, f'{field.name}_id')

    return getattr(model_object, field.name)
