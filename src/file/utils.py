import os
import shutil

import pandas as pd

from fastapi import HTTPException, status

from . import schemas
from config import CURRENT_PATH


def check_file_type(file) -> bool:
    "Проверка типа файла"
    if file.content_type == "text/csv":
        return True


def get_files_fields(files) -> list[schemas.FileInfo]:
    """Получение списка файлов с информацией о полях"""
    files_list = []
    for file in files:
        if check_file_type(file):
            file_info = schemas.FileInfo()
            file_info.file_name = file.filename
            data = pd.read_csv(file.file, encoding="utf-8")
            headers = list(data.columns)
            file_info.fields = headers
            files_list.append(file_info)
        else:
            raise HTTPException(detail=f"file: {file.filename}", status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    return files_list


def save_file(file):
    path = os.path.join(CURRENT_PATH,  "uploaded_files", file.filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)


def get_data_file(file, sorts, filters):
    try:
        df = pd.read_csv(file.file)
        if sorts:
            df = df.sort_values(by=sorts)
        if filters:
            df = df.filter(items=filters)
        return df.to_json(orient='columns')
    except:
        KeyError()
        ValueError()
