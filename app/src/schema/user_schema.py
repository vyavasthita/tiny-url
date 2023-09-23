from typing import Annotated
from pydantic import BaseModel, validator, model_validator
from email_validator import validate_email, EmailNotValidError
from fastapi import HTTPException, status, Body
from ..errors.user_error import UserValidationException
from ..dependencies.config_dependency import Config


class UserBase(BaseModel):
    email: str = Body(title="Email Address")

    @validator("email")
    def validate_email(cls, email_address):
        try:
            email_info = validate_email(email_address, check_deliverability=True)
        except EmailNotValidError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

        return email_address


class UserName(BaseModel):
    first_name: Annotated[
        str,
        Body(
            title="First Name",
            description="First Name of the user",
            min_length=2,
            max_length=30,
        ),
    ]
    last_name: Annotated[
        str,
        Body(
            title="Last Name",
            description="Last Name of the user",
            min_length=2,
            max_length=30,
        ),
    ]


class UserCreate(UserBase, UserName):
    password: Annotated[
        str,
        Body(
            title="Password",
            description="Password of the user",
            min_length=Config().PASSWORD_LENGTH,
            max_length=25,
        ),
    ]
    confirm_password: Annotated[
        str,
        Body(
            title="Confirm Password",
            description="Confirm New Password",
            min_length=Config().PASSWORD_LENGTH,
            max_length=25,
        ),
    ]

    @model_validator(mode="after")
    def verify_password_match(self):
        password = self.password
        confirm_password = self.confirm_password

        if password != confirm_password:
            raise UserValidationException("The passwords did not match.")

        return self


class UserProfileUpdate(UserName):
    age: Annotated[int | None, Body(title="Age", description="Age of the user", ge=1)]


class UserPasswordUpdate(BaseModel):
    existing_password: Annotated[
        str, Body(title="Existing Password", description="Existing Password")
    ]
    new_password: Annotated[
        str,
        Body(
            title="New Password",
            description="New Password to be updated",
            min_length=Config().PASSWORD_LENGTH,
            max_length=25,
        ),
    ]
    confirm_password: Annotated[
        str,
        Body(
            title="Confirm New Password",
            description="Confirm New Password",
            min_length=Config().PASSWORD_LENGTH,
            max_length=25,
        ),
    ]

    @model_validator(mode="after")
    def verify_password_match(cls, values):
        password = values.get("new_password")
        confirm_password = values.get("confirm_password")

        if password != confirm_password:
            raise UserValidationException("The two passwords did not match.")

        return values


class UserRead(UserBase, UserName):
    pass


class UserProfileUpdateRead(UserBase, UserProfileUpdate):
    id: int

    class Config:
        from_attributes = True


class DBUser(UserRead):
    class Config:
        from_attributes = True
