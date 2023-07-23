from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import APIKeyHeader

from src.models.email_model import EmailModel
from src.services.email_service import send_email
from src.auth.auth_lib import get_service_token

email_token_hader = APIKeyHeader(name='token')

router = APIRouter(
    prefix='/dataservice/v1',
    tags=['email', 'service'],
    responses={
        404: {"description": "Not found"}
    }
)


@router.get('/')
async def read_root():
    return {"message": "service root.."}


@router.post('/send_email')
async def dataservice_send_email(src_email: EmailModel, token=Depends(email_token_hader)):
    retern_message = {"message": "send_email success.."}

    if token != get_service_token(service_name='dataservice'):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='check the token value')

    # send email logic..

    return retern_message
