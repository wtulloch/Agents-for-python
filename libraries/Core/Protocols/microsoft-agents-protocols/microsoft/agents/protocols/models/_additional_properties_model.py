from typing import Any
from pydantic import BaseModel, model_validator


class AdditionalPropertiesModel(BaseModel):
    additional_properties: dict | None = None

    @model_validator(mode="before")
    @classmethod
    def set_additional_properties(cls, data: Any):
        if isinstance(data, dict):
            extra_fields = data.keys() - cls.model_fields.keys()
            if extra_fields:
                if "additional_properties" not in data:
                    data["additional_properties"] = {}
                data["additional_properties"].update(
                    {field_name: data[field_name] for field_name in extra_fields}
                )
        return data
