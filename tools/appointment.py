from models import AppointmentAvailability, AppointmentConfirmation, AppointmentSlot
from datetime import datetime, timedelta
import uuid

def check_appointment_availability(dealership_id: str, date: str) -> AppointmentAvailability:
    """
    Mock appointment availability check
    In a real implementation, this would query a scheduling system
    """
    # Generate mock available slots
    slots = [
        AppointmentSlot(time="09:00", available=True),
        AppointmentSlot(time="10:00", available=True),
        AppointmentSlot(time="11:00", available=False),
        AppointmentSlot(time="14:00", available=True),
        AppointmentSlot(time="15:00", available=True)
    ]
    
    return AppointmentAvailability(
        dealership_id=dealership_id,
        date=date,
        slots=slots
    )

def schedule_appointment(
    user_id: str, 
    dealership_id: str, 
    date: str, 
    time: str, 
    car_model: str
) -> AppointmentConfirmation:
    """
    Mock appointment scheduling
    In a real implementation, this would interact with a booking system
    """
    return AppointmentConfirmation(
        user_id=user_id,
        dealership_id=dealership_id,
        date=date,
        time=time,
        car_model=car_model,
        confirmation_number=str(uuid.uuid4())
    )