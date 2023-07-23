from pydantic import BaseModel


class EmailModel(BaseModel):
    email_subject: str
    email_to: str
    email_content: str
    email_cc: str
