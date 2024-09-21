from dataclasses import dataclass, field

from django_glue.form.field.attrs.entities import GlueFieldAttrs


@dataclass
class GlueFormField:
    name: str
    type: str
    attrs: GlueFieldAttrs
    label: str | None = None
    id: str | None = None
    help_text: str = ''
    choices: list | None = field(default_factory=list)

    def __post_init__(self):
        if self.id is None:
            self.id = f'id_{self.name}'

        if self.label is None:
            self.label = ' '.join(self.name.split('_')).title()

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'type': self.type,
            'attrs': self.attrs.to_dict(),
            'label': self.label,
            'help_text': self.help_text,
            'choices': self.choices
        }
