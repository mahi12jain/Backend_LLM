from pydantic import BaseModel, Field
from typing import Optional, List, Union

class QueryRequest(BaseModel):
    query: str
    session_id: str

class WeatherData(BaseModel):
    temperature: str
    city: str
    description: Optional[str] = None
    humidity: Optional[str] = None

class DealershipAddress(BaseModel):
    id: str
    name: str
    address: str
    city: str
    state: str
    zip_code: str

class AppointmentSlot(BaseModel):
    time: str
    available: bool

class AppointmentAvailability(BaseModel):
    dealership_id: str
    date: str
    slots: List[AppointmentSlot]

class AppointmentConfirmation(BaseModel):
    user_id: str
    dealership_id: str
    date: str
    time: str
    car_model: str
    confirmation_number: str

class ToolUseResponse(BaseModel):
    name: str
    output: Union[WeatherData, DealershipAddress, AppointmentAvailability, AppointmentConfirmation]