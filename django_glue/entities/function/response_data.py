from dataclasses import dataclass
from typing import Any

from django_glue.response.data import GlueJsonData


@dataclass
class GlueFunctionJsonData(GlueJsonData):
    function_return: Any

    def to_dict(self) -> dict[str, Any]:
        return {'function_return': self.function_return}
