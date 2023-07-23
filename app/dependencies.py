from typing_extensions import Annotated
from fastapi import Header, HTTPException


# async def get_token_header(x_token: Annotated[str, Header()]):
#     print(f'current x_token : {x_token}')
#     if x_token != "test-token":
#         raise HTTPException(status_code=400, detail='X-Toke heaver invalid')


# async def get_query_token(token: str):
#     print(f'current token : {token}')
#     if token != 'jssvs':
#         raise HTTPException(status_code=400, detail="No token provided")
