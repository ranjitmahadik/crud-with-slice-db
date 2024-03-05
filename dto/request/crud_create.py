from pydantic import BaseModel, validator, Field
from exceptions import ApiException


class CrudCreate(BaseModel):
    key: str
    value: str
    ttl: int = Field(None)

    @validator("key")
    def validate_key(cls, key):
        if key is None or len(key) <= 0:
            raise ApiException("key must be present", 400)
        return key
    
    @validator("ttl")
    def validate_key(cls, ttl):
        if ttl <= 0:
            raise ApiException("ttl must be greater than 0", 400)
        return ttl