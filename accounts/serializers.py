# serializers.py
from datetime import timezone, timedelta
from rest_framework import serializers
from .models import Address
from pydantic import BaseModel, Field, HttpUrl, ValidationError, validator
from typing import Optional
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'<PASSWORD>': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True},
        }


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')


class AddressSchema(BaseModel):
    number: Optional[str] = Field(None, max_length=10)
    street: Optional[str] = Field(None, max_length=255)
    city: str = Field(..., max_length=100)
    region: Optional[str] = Field(None, max_length=100)  # Région, état ou province
    country: str = Field(..., max_length=100)
    postal_code: Optional[str] = Field(None, max_length=20)  # Code postal
    google_maps: Optional[HttpUrl]
    type_of_address: Optional[str] = Field(None, max_length=1, pattern=r"^(O|H|T)$")

    @validator('city', 'country', pre=True, always=True)
    def not_empty(cls, v):
        if not v or v.strip() == '':
            raise ValueError('must not be empty')
        return v

"""
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def validate(self, data):
        try:
            # Validate data with Pydantic schema
            AddressSchema(**data)
        except ValidationError as e:
            raise serializers.ValidationError(e.errors())
        return data"""


from rest_framework import serializers
from .models import ProfileCustomUser, CarModel, Notification, Reclaim, Address


class ProfileCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCustomUser
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class ReclaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclaim
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
