from dataclasses import dataclass, field


@dataclass
class FilterGlueQuerySetPostData:
    filter_params: dict[str, str] = field(default_factory=dict)
    exclude_params: dict[str, str] = field(default_factory=dict)
