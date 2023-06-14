from typing import Any

from fastapi import File, Depends
from fastapi import APIRouter, HTTPException, UploadFile, status

from .utils import get_files_fields, check_file_type, save_file, get_data_file
from . import schemas

from auth.config_auth import fastapi_users
from auth.models import User


router = APIRouter(prefix="/file",
                   tags=['file'])


current_user = fastapi_users.current_user()


@router.post(
    "/upload_file/",
    status_code=status.HTTP_200_OK,
)
async def create_upload_file(user: User = Depends(current_user), file: UploadFile = File(...)):
    """Загрузка файла в формате csv"""
    if not check_file_type(file):
        raise HTTPException(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    else:
        save_file(file)
        return {"filename": file.filename}


@router.post("/upload_csv_files/", status_code=status.HTTP_200_OK,
             response_model=list[schemas.FileInfoOut]
             )
async def upload_csv_file(list_files: list[UploadFile] = File(...)) -> list[Any]:
    try:
        return get_files_fields(list_files)
    except:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)


@router.post("/get_data/", status_code=status.HTTP_200_OK)
async def get_data(sorts: list[str], filters: list[str], file: UploadFile = File(...)):
    try:
        return get_data_file(file, sorts, filters)
    except Exception as err:
        raise HTTPException(status_code=500,
                            detail={"details": err,
                                    "status": "error",
                                    "data": {"sorts": sorts,
                                             "filters": filters,
                                             "args": err.args}
                                    }
                            )
