import datetime

from pydantic import BaseModel, EmailStr, validator, constr
from datetime import date
from typing import Optional
from enum import Enum

from .models import ProfileCustomUser, CustomUser


class UserRoleEnum(str, Enum):
    DRIVER = 'driver'
    PASSENGER = 'passenger'
    BOTH = 'both'


class CustomUserValidator(BaseModel):
    last_name: str
    first_name: str
    email: EmailStr
    is_superuser: bool = False
    is_staff: bool = True
    is_active: bool = True
    date_joined: Optional[date] = None

    @validator('email')
    def email_must_be_unique(cls, v):
        if CustomUser.objects.filter(email=v).exists():
            raise ValueError('Email already exists')
        return v


class ProfileCustomUserValidator(BaseModel):
    user: int
    avatar: str = 'default.jpg'
    birth_date: Optional[date] = None
    genre: Optional[str] = None
    phone_number: str
    num_permis: str
    role: UserRoleEnum
    category: str
    date_delivrance: Optional[date] = None
    date_expiration: Optional[date] = None

    @validator('birth_date')
    def validate_birth_date(cls, v):
        today = date.today()
        age = today - v
        min_age = 18 * 365.25  # 18 années en jours (approximation)
        if age.days < min_age:
            raise ValueError("Vous devez avoir au moins 18 ans pour vous inscrire.")
        return v

    @validator('phone_number')
    def phone_number_must_be_unique(cls, v):
        if ProfileCustomUser.objects.filter(phone_number=v).exists():
            raise ValueError('Phone number already exists')
        return v

    @validator('num_permis')
    def num_permis_must_be_unique(cls, v):
        if ProfileCustomUser.objects.filter(num_permis=v).exists():
            raise ValueError('Num permis already exists')
        return v


class CarModelValidator(BaseModel):
    owner: int
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    color: Optional[str] = None
    licence_number: Optional[str] = None

    @validator('owner')
    def validate_owner_role(cls, v):
        owner = ProfileCustomUser.objects.get(pk=v)
        if owner.role not in [UserRoleEnum.DRIVER.value, UserRoleEnum.BOTH.value]:
            raise ValueError('Owner must be a driver or both to create a car')
        return v


class AddressValidator(BaseModel):
    position_name: Optional[str] = None
    number: Optional[int] = None
    street: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    google_maps: Optional[str] = None
    type_of_address: Optional[str] = None
    author: int  # L'ID de l'auteur de l'adresse

    @validator('author')
    def author_must_exist(cls, v):
        if not CustomUser.objects.filter(id=v).exists():
            raise ValueError('Author must exist')
        return v


class ReclaimValidator(BaseModel):
    owner: int
    date: Optional[datetime] = None
    reason: str

    @validator('owner')
    def owner_must_exist(cls, v):
        if not ProfileCustomUser.objects.filter(id=v).exists():
            raise ValueError('Owner must exist')
        return v

    @validator('date', pre=True, always=True)
    def set_date_now(cls, v):
        return v or datetime.now()


class NotificationValidator(BaseModel):
    sender: int
    receiver: int
    date: Optional[datetime] = None
    message: str
    status: Optional[str] = "unread"

    @validator('sender', 'receiver')
    def user_must_exist(cls, v):
        if not ProfileCustomUser.objects.filter(id=v).exists():
            raise ValueError('User must exist')
        return v

    @validator('date', pre=True, always=True)
    def set_date_now(cls, v):
        return v or datetime.now()
