from pydantic import BaseModel, validator, Field
from exceptions import ApiException


class CrudUpdate(BaseModel):
    key: str
    value: str
    ttl: int = Field(None)

    @validator("key")
    def validate_key(cls, key):
        if key is None or len(key) <= 0:
            raise ApiException("key must be present", 400)
        return key
    
    @validator("value")
    def validate_key(cls, value):
        if value is None or len(value)  <= 0:
            raise ApiException("value must be present", 400)
        return value