from datetime import date

from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional


class TripValidator(BaseModel):
    driver_id: int
    car_id: int
    status: str = Field(..., max_length=10, description="Status of the trip")
    start_location: str = Field(..., max_length=100, description="Starting location")
    end_location: str = Field(..., max_length=100, description="Ending location")
    start_time: date
    end_time: date
    seats: int = Field(..., gt=0, description="Number of available seats")
    distance: float = Field(..., gt=0, description="Distance of the trip")

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class BookingValidator(BaseModel):
    trip_id: int
    passengers_id: int
    status: str = Field(..., max_length=10, description="Status of the booking")
    booked_at: date
    updated_at: date

    class Config:
        from_attributes = True


class PaymentDriverBookingValidator(BaseModel):
    booking_id: int
    amount: Decimal
    payment_method: str = Field(..., max_length=10, description="Payment method")
    payment_status: str = Field(..., max_length=10, description="Payment status")
    payment_date: date
    created_at: date
    updated_at: date

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class ReviewTripValidator(BaseModel):
    trip_id: int
    reviewer_id: int
    rating: Decimal
    comment: Optional[str]
    reviewed_at: date
    updated_at: date

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class RewardValidator(BaseModel):
    driver_id: int
    reward_type: str = Field(..., max_length=10, description="Type of reward")
    reward_date: date
    description: str

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
