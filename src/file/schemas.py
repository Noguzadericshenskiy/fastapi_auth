from pydantic import BaseModel, Field
from typing import Any


class FileInfo(BaseModel):
    file_name: str = Field(str)
    fields: list[str] = Field(list[Any])


class FileInfoOut(FileInfo):
    file_name: str
    fields: list[str]
