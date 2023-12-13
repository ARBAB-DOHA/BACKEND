from typing import List
from fastapi import HTTPException, Depends,APIRouter
import httpx
from sqlalchemy.orm import Session
from .. schemas import Holiday
from .. database import get_db
from .. models import HolidayDB


router = APIRouter(
    prefix="/holidays",
    tags=['Holiday'])





@router.get("/holidays/{country}/{year}/{month}/{day}", response_model=List[Holiday])
async def get_holidays(country: str, year: int, month: int, day: int):
    api_key = "bb85ea9aa2cb45e59b189be7e4e24308"  # Replace with your actual API key
    api_url = f"https://holidays.abstractapi.com/v1/?api_key={api_key}&country={country}&year={year}&month={month}&day={day}"

    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)

    if response.status_code == 200:
        holidays_data = response.json()

        if not holidays_data:
            # No holidays found for the specified date and country
            return {"message": "No holidays found for the specified date and country"}

        # Process the holidays data as needed
        processed_holidays = process_holidays(holidays_data)
        
        return processed_holidays

    else:
        raise HTTPException(status_code=response.status_code, detail=f"Failed to fetch holidays. Status code: {response.status_code}")

def process_holidays(holidays_data: List[Holiday]):
    # Add any additional processing logic here
    # For example, you might want to format the data or filter out unnecessary information
    return holidays_data
