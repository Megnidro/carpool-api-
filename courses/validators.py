from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from typing import Optional


class TripValidator(BaseModel):
    driver_id: int
    car_id: int
    status: str = Field(..., max_length=10, description="Status of the trip")
    start_location: str = Field(..., max_length=100, description="Starting location")
    end_location: str = Field(..., max_length=100, description="Ending location")
    start_time: datetime
    end_time: datetime
    seats: int = Field(..., gt=0, description="Number of available seats")
    distance: float = Field(..., gt=0, description="Distance of the trip")

    class Config:
        orm_mode = True


class BookingValidator(BaseModel):
    trip_id: int
    passengers_id: int
    status: str = Field(..., max_length=10, description="Status of the booking")
    booked_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PaymentDriverBookingValidator(BaseModel):
    booking_id: int
    amount: Decimal
    payment_method: str = Field(..., max_length=10, description="Payment method")
    payment_status: str = Field(..., max_length=10, description="Payment status")
    payment_date: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class ReviewTripValidator(BaseModel):
    trip_id: int
    reviewer_id: int
    rating: Decimal
    comment: Optional[str]
    reviewed_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class RewardValidator(BaseModel):
    driver_id: int
    reward_type: str = Field(..., max_length=10, description="Type of reward")
    reward_date: datetime
    description: str

    class Config:
        orm_mode = True
